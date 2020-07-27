import yfinance as yf
import sys
from gpiozero import LEDBoard
from time import sleep
from datetime import datetime

leds = LEDBoard(4, 17, 27, 22, 12, 16, 13, 19, 26)

stock_map = {}

OPEN_KEY = 'previousClose'
ASK_KEY = 'ask'
BID_KEY = 'bid'
INTERVAL = 300

def reset_leds():
	leds.off()


def render_movement(movement):
	print(datetime.now(), 'Movement:', movement)
	leds.off()

	green1 = 1 if movement > 0.0 else 0
	green2 = 1 if movement >= 1 else 0
	green3 = 1 if movement >= 1.5 else 0
	green4 = 1 if movement >= 2 else 0

	blue = 1 if movement < 0.5 and movement > -0.5 else 0

	red1 = 1 if movement < 0.0 else 0
	red2 = 1 if movement <= -1 else 0
	red3 = 1 if movement <= -1.5 else 0
	red4 = 1 if movement <= -2 else 0

	leds.value = (green4, green3, green2, green1, blue, red1, red2, red3, red4)


def get_open(stock):
	if stock not in stock_map:
		stock_map[stock] = yf.Ticker(stock).info

	return stock_map[stock][OPEN_KEY]


def get_current_price(stock):
	if stock not in stock_map:
		stock_map[stock] = yf.Ticker(stock).info

	stock = stock_map[stock]
	ask = stock[ASK_KEY]
	bid = stock[BID_KEY]

	return (ask + bid) / 2


def run(stock):
	while True:
		try:
			open_val = get_open(stock)
			current_price = get_current_price(stock)

			diff = current_price - open_val
			movement = (diff / open_val) * 100
			render_movement(movement)

			stock_map.clear()
		except (KeyboardInterrupt, SystemExit) as _:
			raise
		except:
			print("Error occurred")
		sleep(INTERVAL)

if __name__ == "__main__":
	run(sys.argv[1].upper())

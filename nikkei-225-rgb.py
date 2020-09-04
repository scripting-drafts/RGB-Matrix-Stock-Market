# NIKKEI 225
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
from threading import Thread, Event
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

event = Event()

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.investing.com/indices/major-indices")

def get_values(shared_data):
    while True:
        shared_data.stockValue = shared_data.driver.find_element_by_css_selector('.pid-178-last').text
        try:
            red = shared_data.driver.find_element_by_css_selector('.bold.redFont.pid-178-pc')
            shared_data.color = "red"
        except NoSuchElementException:
            pass
        try:
            green = shared_data.driver.find_element_by_css_selector('.bold.greenFont.pid-178-pc')
            shared_data.color = "green"
        except NoSuchElementException:
            pass

        if event.is_set():
            break

    print('Rendering Stop')

options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)
offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/6x13.bdf")
pos = offscreen_canvas.width

color = "green"
stockValue = 0

shared_data = {
    "driver": driver,
    "stockValue": stockValue,
    "color": color
}

t = Thread(target=get_values, args=(shared_data,))
t.start()

while True:
    try:
        textColor = graphics.Color(255, 0, 0) if color == "red" else graphics.Color(51, 255, 51)
        pos -=1
        time.sleep(0.05)
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 14, textColor, str(stockValue))
        if (pos + len < 0):
            pos = offscreen_canvas.width
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    except KeyboardInterrupt:
        event.set()
        break

t.join()

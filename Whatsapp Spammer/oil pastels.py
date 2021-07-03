import pyautogui as pg
from time import sleep

while True:
    posXY= pg.position()
    print(posXY, pg.pixel(posXY[0], posXY[1]))
    sleep(1)
    if posXY[0] | posXY[1]==0:
        break


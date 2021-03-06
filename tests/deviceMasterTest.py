#!/usr/bin/python
# -*- coding: utf-8 -*-

# socat -d -d pty,raw,echo=0 pty,raw,echo=0
# socat PTY,link=./ptyp1,b9600 PTY,link=./ptyp2,b9600

from ..devicemaster import DeviceMaster
# from ..devicemaster import DeviceMaster
from time import sleep

import os

RED = [0xfff, 0x0, 0x0]
GREEN = [0x0, 0xfff, 0x0]
BLUE = [0x0, 0x0, 0xfff]


def setLedValue(leds, id, color):
    leds[id * 3 + 0] = color[0]
    leds[id * 3 + 1] = color[1]
    leds[id * 3 + 2] = color[2]


def testSmartLeds(slave):
    smartLeds = slave.getSmartLeds().get()
    print("Change ALL")
    for index in range(32):
        setLedValue(smartLeds, index, RED)
    slave.setSmartLeds(smartLeds)
    raw_input("Press Enter to continue...")
    print("Change ONE")
    for index in [4]:
        setLedValue(smartLeds, index, GREEN)
    slave.setSmartLeds(smartLeds)

    raw_input("Press Enter to continue...")

    # print("Change 2")
    # for index in range(2):
    #     setLedValue(smartLeds, index, BLUE)
    # slave.setSmartLeds(smartLeds)

    print("Change 4 Blue")
    for index in range(4):
        setLedValue(smartLeds, index, BLUE)
    slave.setSmartLeds(smartLeds)

    raw_input("Press Enter to continue...")

    print("Change 6")
    for index in range(6):
        setLedValue(smartLeds, index, [0x00, 0x00, 0x00])
    slave.setSmartLeds(smartLeds)
    raw_input("Press Enter to continue...")


def printAllStates(master, slave):
    print("Buttons: ", master.getButtons(slave).get())
    print("Adc: ", master.getAdc(slave).get())
    print("Encoders: ", master.getEncoders(slave).get())
    print("Lcd: ", master.getLcd(slave).get())
    print("Relays: ", master.getRelays(slave).get())
    print("Sensors: ", master.getSensors(slave).get())
    print("SimpleLeds: ", master.getSimpleLeds(slave).get())
    print("SmartLeds: ", master.getSmartLeds(slave).get())


if __name__ == "__main__":
    pass
    master = DeviceMaster()

    # portDestination = os.path.expanduser('~') + '/ptyp2'
    #portDestination = "/dev/ttyUSB0"
    #portDestination = "/dev/ttyUSB0"
    port_CB_SLAVE_1 = "COM5"
    port_CB_SLAVE_2 = "COM4"
    CB_SLAVE_2 = master.addSlave("CB_SLAVE_2", port_CB_SLAVE_2, 1, boudrate=5)
    CB_SLAVE_1 = master.addSlave("CB_SLAVE_1", port_CB_SLAVE_1, 2, boudrate=5)
    master.start()
    while True:
    	print("CB_SLAVE_1: ")
        master.getButtons(CB_SLAVE_1).printResource()
        master.getAdc(CB_SLAVE_1).printResource()
        # printAllStates(master, slave)
        # raw_input("Press Enter to continue...")
	print("\n\nCB_SLAVE_2: ")
        master.getButtons(CB_SLAVE_2).printResource()
        master.getAdc(CB_SLAVE_2).printResource()
	master.getRelays(CB_SLAVE_2).printResource()
        sleep(0.1)
        os.system('clear')

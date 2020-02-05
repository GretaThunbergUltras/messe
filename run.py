#!/usr/bin/python3

from botlib.bot import Bot

import time

class HannoverMesse:
    def __init__(self):
        self._bot = Bot()
        self._bot.calibrate()

        self._linetracker = self._bot.linetracker()
        #self._objdetector = self._bot.objectdetector()

    def start(self):

        input('press key to start')

        self._bot.drive_power(20)
        self._linetracker.autopilot(True)

        try:
            for i in range(60):
                #objs = self._objdetector.detect('../classifiers/palette.xml')
                #print(objs)
                time.sleep(1)
        except KeyboardInterrupt:
            pass

        self._linetracker.autopilot(False)
        self._bot.drive_power(0)

    def run():
        HannoverMesse().start()

if __name__ == '__main__':
    HannoverMesse.run()

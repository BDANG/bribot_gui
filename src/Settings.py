from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

DEFAULT_MIN_REFRESH = 0.35
DEFAULT_MAX_REFRESH = 0.75
DEFAULT_CHECKOUT_DELAY = 1.25
class Settings:
    def __init__(self, MIN_REFRESH=DEFAULT_MIN_REFRESH, MAX_REFRESH=DEFAULT_MAX_REFRESH, CHECKOUT_DELAY=DEFAULT_CHECKOUT_DELAY):
        self.MIN_REFRESH = MIN_REFRESH
        self.MAX_REFRESH = MAX_REFRESH
        self.CHECKOUT_DELAY = CHECKOUT_DELAY

    def reset_to_default(self, filePath, minRefreshEntry, maxRefreshEntry, checkoutDelayEntry):
        # reset the Entry to the default values
        minRefreshEntry.delete(0, END)
        minRefreshEntry.insert(0, DEFAULT_MIN_REFRESH)

        maxRefreshEntry.delete(0, END)
        maxRefreshEntry.insert(0, DEFAULT_MAX_REFRESH)

        checkoutDelayEntry.delete(0, END)
        checkoutDelayEntry.insert(0, DEFAULT_CHECKOUT_DELAY)

        # save the default values
        self.save_to_file(filePath, "", "", "")


    def load_from_file(self, filePath):
        minrefresh = DEFAULT_MIN_REFRESH
        maxrefresh = DEFAULT_MAX_REFRESH
        checkoutdelay = DEFAULT_CHECKOUT_DELAY

        settingsFilePath = Path(filePath)
        if settingsFilePath.is_file():
            with settingsFilePath.open() as f:
                try:
                    # wip: cursory/haphazard
                    minrefresh = float(f.readline())
                    maxrefresh = float(f.readline())
                    checkoutdelay = float(f.readline())
                except:
                    None


        return Settings(minrefresh, maxrefresh, checkoutdelay)

    def save_to_file(self, filePath, minrefresh, maxrefresh, checkoutdelay):
        settingsFilePath = Path(filePath)
        with settingsFilePath.open(mode="w") as f:
            if minrefresh == "":
                f.write(str(DEFAULT_MIN_REFRESH)+"\n")
            else:
                f.write(minrefresh+"\n")

            if maxrefresh == "":
                f.write(str(DEFAULT_MAX_REFRESH)+"\n")
            else:
                f.write(maxrefresh+"\n")
            if checkoutdelay == "":
                f.write(str(DEFAULT_CHECKOUT_DELAY)+"\n")
            else:
                f.write(checkoutdelay+"\n")

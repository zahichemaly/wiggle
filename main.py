import pyautogui
import threading
import datetime as dt
import sys
import argparse

screenSize = pyautogui.size()

parser = argparse.ArgumentParser()
parser.add_argument('--delay', '-D', help="Delay of wiggling in seconds", type= int, default=60)
parser.add_argument('--hour', '-H', help="Hour threshold to stop the wiggling", type= int, default= 18)

args = parser.parse_args()

delay = args.delay
maxHour = args.hour

def log(message):
    current_time = dt.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print("[" + formatted_time + "]: " + message)

def moveMouse():
    log("Moved mouse")
    pyautogui.moveTo(5, screenSize[1], duration = 1)
    #pyautogui.click()
    main()

def main():
    hour = dt.datetime.now().hour
    if hour == maxHour:
        log("End of day reached. Exiting...")
        sys.exit()
    else:
        threading.Timer(delay, moveMouse).start()
        
log("Started wiggling...")
main()

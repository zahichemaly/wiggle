import pyautogui
import threading
import datetime as dt
import sys

screenSize = pyautogui.size()

# delay in seconds
delay = 60.0

def log(message):
    current_time = dt.datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    print("[" + formatted_time + "]: " + message)

def moveMouse():
    pyautogui.moveTo(5, screenSize[1], duration = 1)
    #pyautogui.click()
    log("Moved mouse")
    main()

def main():
    hour = dt.datetime.now().hour
    if hour == 17 or hour == 12:
        log("End of day reached. Exiting...")
        sys.exit()
    else:
        threading.Timer(delay, moveMouse).start()
        
log("Started wiggling...")
main()

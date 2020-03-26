import time
import pyautogui

DELAY_BETWEEN_COMMANDS = 1.00

def main():
    countdownTimer()
    initializePyAutoGUI()
    goToMerchant()
    tradeWithMerchant()
    returnToShip()
    # reportMousePosition()
    flyToEarthStation()
    print("Done")

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True, moving the mouse to the upper-left
    # corner will abort your program.
    pyautogui.FAILSAFE = True

def countdownTimer():
    # Countdown timer
    print("Starting", end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print("Go")

def holdKey(key, seconds = 1.00):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def goToMerchant():
    print("Goind to merchant")
    print("Back away from Louden MacEwen")
    holdKey('s', 6.00)
    print("Face the entrance")
    holdKey('a', 0.10)
    print("Go through the entrance into the main lobby")
    holdKey('w', 7.00)
    print("Turn to the bazaar lobby")
    holdKey('d', 0.65)
    print("Go through the entrance into the bazaar lobby")
    holdKey('w', 5.60)
    print("Turn to the trade merchant")
    holdKey('d', 1.16)
    print("Walk up to the trade merchant")
    holdKey('w', 1.50)
    print("Arrived merchant")

def reportMousePosition(seconds = 10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

def tradeWithMerchant():
    print("Hover the mouse over merchant")
    pyautogui.moveTo(1207, 508, 0.25)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    print("click the merchant to start our chat")
    pyautogui.click()
    print("Allow time for the chat to begin")
    time.sleep(3.00)

    print("Click the trade button")
    pyautogui.click(537, 797, duration=0.25)
    # Allow time for the inventory to load
    time.sleep(1.00)

    print("Move to the item. Was having trouble when I combined the movement with click() on this step")
    pyautogui.moveTo(1172, 395, 0.25)
    time.sleep(1.0)
    # Now click on it to select it
    pyautogui.click()
    time.sleep(1.00)

    print("Buy the item")
    numToBuy = 10
    pyautogui.keyDown('shiftleft')
    for i in range(0, numToBuy):
        pyautogui.click()
        time.sleep(0.5)
    pyautogui.keyUp('shiftleft')

    print("close window")
    pyautogui.click(1585, 320, duration=0.5)

    print("Click the done button and wait for zoom out animation to finish")
    pyautogui.click(498, 757, duration=0.5)
    time.sleep(2.00)

def returnToShip():
    print("return to ship")
    # Change our body angle
    holdKey('a', 0.20)
    # Backup to center of the bazaar
    holdKey('s', 2.65)
    # Turn to the exit
    holdKey('d', 0.08)
    # Go through the exit back into the main lobby
    holdKey('w', 5.76)
    # Turn to the hangar
    holdKey('a', 0.68)
    # Go through the exit into the hangar
    holdKey('w', 6.20)
    # Turn towards our ship
    holdKey('a', 0.30)
    # Click our ship to exit the station
    pyautogui.click(438, 285, duration=0.25)
    # Allow time for the outside world to load
    time.sleep(10.00)

def flyToEarthStation():
    print("FlyToEarthStation")
    print("Open the navigation map")
    pyautogui.click(160, 840, duration=0.5)
    print("Select the sector gate to Earth")
    pyautogui.click(856, 457, duration=0.5)
    # Wait for warp path to be calculated
    time.sleep(1.5)
    # Initiate warp
    holdKey('z', 0.10)
    # Wait for warp to finish
    time.sleep(36)
    # Enter the gate
    pyautogui.click(1544, 627, duration=0.5)
    # Wait for the sector change to load
    time.sleep(15)
    # Open the navigation map
    pyautogui.click(160, 840, duration=0.5)
    # Select Earth Station
    pyautogui.click(351, 397, duration=0.5)
    # Wait for warp path to be calculated
    time.sleep(1.0)
    # Initiate warp
    holdKey('z', 0.10)
    # Wait for warp to finish
    time.sleep(17)
    # Dock at the station
    pyautogui.click(1544, 627, duration=0.5)



if __name__ == "__main__":
    main()    
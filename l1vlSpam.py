import pyautogui, time
import pyfiglet
print(pyfiglet.figlet_format("l1vlSpam"))
time.sleep(2);
print("To enable spam, go to any messenger and select a chat with your enemy")
time.sleep(2);
input('Press ENTER to start');
print("Program has been started!")
time.sleep(1); f = open("spamTXT.txt", "r")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
input('Press ENTER to exit');
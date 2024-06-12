from program.screen_rec import ScreenRecording

from threading import Thread

screen_rec = ScreenRecording

if __name__ == '__main__':
    Thread(target = screen_rec()).start()
    Thread(target = pass).start()
    Thread(target = pass).start()
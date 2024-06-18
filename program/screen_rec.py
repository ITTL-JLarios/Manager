from program.service import Service, threaded

from datetime import datetime, timedelta
import numpy as np
import imageio
import os
import cv2
import mss
import time

class ScreenRecording( Service ):
    def __init__(self, base_dir='rec', fps=30, time_lapse=1, elderness=7):
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


    def get_combined_screenshot():
        # Get information about all monitors
        pass

            

    def record(self):
        '''
            Screen Recording as service
        '''
        init_time = datetime.now()
        end_time = init_time + timedelta(minutes=self.time_lapsus)
        with mss.mss() as sct:
            monitor = sct.monitors[1]  # Capture the primary monitor
            fourcc = cv2.VideoWriter_fourcc(*'VP80')  # VP8 codec for .webm format
            out = cv2.VideoWriter(
                os.path.join(self.base_path,f'{init_time.date()}_{init_time.hour}_{init_time.minute}.mkv'), 
                fourcc, 
                self.fps, 
                (monitor['width'], monitor['height']))

       
            while datetime.now() < end_time:
                img = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                out.write(frame)

            out.release()


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
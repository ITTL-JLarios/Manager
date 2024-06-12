from program.service import Service

class ScreenRecording( Service ):
    def __init__(self, base_dir, fps=10):
        super().__init__(base_dir, fps)
import os
from threading import Thread

class Service:
    def __init__(
                self,
                base_dir,
                fps=None,
                fernet=None,
                file_name=None):
        
        '''
        args:
            base_dir: Directory where the service will store or get files
            files_name: Name of output or input file
            fps: Frames per second for service (video)
            key: Secret Key for encryption 
        '''
        self.base_path = os.path.join('', base_dir) if base_dir else base_dir
        self.file_name = ( os.path.join(self.base_path, file_name) 
                            if file_name else file_name )
        self.fps = fps
        self.fernet = fernet


def threaded(fn):
    '''
    args:
        fn: Function to pass through a decorator
    return:
        thread: Thread for the CPU
        wraper: Wraps the function in another function
    '''
    def wraper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs).start()
        # Return thread
        return thread
    # Return wraper
    return wraper
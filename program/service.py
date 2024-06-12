import os

class Service:
    def __init__(
                self,
                base_dir,
                fps=None,
                key=None,
                file_name=None):
        
        # Service Variables
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
        self.key = key


    def get_path(self):
        '''
        return:
            base_path: The base path for the service out put or input files
        '''
        return self.base_path
    

    def get_file_name(self):
        '''
        return:
            base_path: The Name for the file service out put or input
        '''
        return self.file_name
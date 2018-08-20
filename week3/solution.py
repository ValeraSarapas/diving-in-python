class FileReader:
    ''' This class convert file to string '''

    def __init__(self,path):
        self._path = path
        
    def read(self):
        try:
            with open(self._path, 'r', encoding = 'UTF-8' ) as f:
                data = f.read()
        except IOError:
            print("File {} is not exist".format(self._path))
            return None
        return str(data)
    

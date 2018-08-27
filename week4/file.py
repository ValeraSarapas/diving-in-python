import tempfile
import os
import sys

class File:
    def __init__(self, path):
        self.path=path
        os.makedirs(os.path.dirname(path), exist_ok=True)

        self.current_line = 0
        self.temp_dir = tempfile.gettempdir()
      
    def write(self, string):
        with open(self.path, "w+") as f:
            f.write(string)

    def read(self):
        with open(self.path, "r+") as f:
            return f.read()
           
            
    def __add__(self,obj):
        new_path = os.path.join(self.temp_dir,'tmp')
        new = File(new_path)
        new.write(self.read()+obj.read())
        return new

    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path) as f:
            f.seek(self.current_line)
            line = f.readline()
 
            if not line:
                raise StopIteration
            self.current_line = f.tell()
        return line
    
    def __str__(self):
        return '{}'.format(self.path)
    
if __name__ == "__main__":
    obj = File('/tmp/file.txt')
    print(obj)

    obj.write('line\n')
    print("Read file:\n", obj.read())

    for line in File('/tmp/file.txt'):
        print("String:",line.strip())

    first = File('/tmp/file.txt')
    second = File('/tmp/file2.txt')

    new_obj = first + second

    print("Read new file:\n",new_obj.read())
    

    

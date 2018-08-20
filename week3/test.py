import sys
from solution import FileReader

def _main():
    file = sys.argv[1]

    reader = FileReader("example.txt")
    print(reader.read())
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[2] =="--v":
        print(sys.argv)
    _main()

import sys
if __name__ == '__main__':
    num_steps =  int(sys.argv[1])
    for line in range(1,num_steps+1):
        print((num_steps-line)*' '+line*r'#')

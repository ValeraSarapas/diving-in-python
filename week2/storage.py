import sys
import argparse
import os
import tempfile
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Key-value storage parser')
    
    parser.add_argument('--key', action='store', dest='key', help='Key')
    parser.add_argument('--val', action='store', dest='value', help='Value')

    args = parser.parse_args()
    print("Args:", args)
    print("Arguments: Key: {}, Value: {}".format(args.key,args.value))

    data = list()
    
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    print("Path", storage_path)
    try:
        with open(storage_path, 'r') as f:
            try:
                data = json.load(f)
            except ValueError:
                print("Storage file is empty")
                data = None
    except FileNotFoundError:
        print("File is not created yet")
        f = open(storage_path, 'w+')
        f.close()
        data = None

    print("Data: ", data)
     
    def get_values(i_key,storage = data):
        key_list = []
        value_list = []
        for record in data:
            for key, value in record.items():
                if key == i_key:
                    value_list.append(value)
                key_list.append(key)

        unique_keys = set(key_list)
        print("Keys:",unique_keys)
        print("Values:",value_list)

        key_found = False
        if i_key in unique_keys:
            key_found = True
            
        
        return key_found, value_list
    
    if args.key is not None:     
        if args.value is not None:
            # Add new key:value
            if data is None:
                data = [{args.key:args.value}]
            else:
                data.append({args.key:args.value})
            with open(storage_path, 'w') as f:
                json.dump(data,f)
            print("Data ", data, " saved in ",storage_path)
        else:
            # Print values
            key_found, value_list = get_values(args.key)
            if key_found:
                print(", ".join(value_list))
            else:
                print("Key : {} is not found ".format(args.key))
    else:
        print('Please run with --key and --value arguments')
        exit()

    
 

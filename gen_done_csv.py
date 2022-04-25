import os
from common import (
    path_join,
    file_exist,
    size_file,
    file_name,
    create_csv
)

#tick = 'ICBP INDF JSMR MYOR PTBA TLKM UNVR'.split(' ')
tick = 'TLKM UNVR'.split(' ')
year = '2022'
month = '04'
date = '11 12 13 14 18 19 20 21 22'.split(' ')

if __name__ == "__main__":
    root = os.getcwd()
    done_dir = os.path.join(root,'done_detail')
    
    file_path = ''
    print(file_path)
    
    for t in tick :
        for d in date:
            file_path = path_join([done_dir, t, file_name(t, year, month, d)])
            if not file_exist(file_path):
                print('create file : '+ file_path)
                create_csv(file_path)
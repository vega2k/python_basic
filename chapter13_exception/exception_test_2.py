def exception_2(file_path):
    try:
        f = open(file_path,'r')
    except IOError as err:
        print('cannot open',file_path)
        print(err.args)
    else:
        print('File has',len(f.readlines()),'lines')
        f.close()
    finally:
        print("I just tried to read this file",file_path)

exception_2("readme1.txt")
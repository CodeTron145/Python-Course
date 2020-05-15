import os
import sys
import hashlib

BUF_SIZE = 65536


def duplicates(dir):

    stat_files = []
    for direct in os.walk(dir):
        for file in direct[2]:

            stat_file = []
            name = direct[0] + "/" + file
            md5 = hashlib.md5()

            stat_file.append(name)
            stat_file.append(os.path.getsize(name))

            with open(name, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)

            stat_file.append(md5.hexdigest())
            stat_file.append(False)
            stat_files.append(stat_file)

    for file_act in stat_files:
        for file in stat_files:
            if file_act[0] == file[0] or file[3] is True:
                continue
            if file_act[1] == file[1] and file_act[2] == file[2]:
                if file_act[3] is False:
                    print("----------------------------------")
                    print(file_act[0])
                    file_act[3] = True
                print(file[0])
                file[3] = True
    pass


duplicate(sys.argv[1])
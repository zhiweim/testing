import os

for filename in os.listdir(r"/Users/zhiweima/Desktop/tianocore/edk2-edkrepo/edkrepo/commands"):
    if '.py' in filename:
        line_num = 0
        with open(os.path.join(r"/Users/zhiweima/Desktop/tianocore/edk2-edkrepo/edkrepo/commands", filename), 'r') as f:
            with open('needs_fixing.txt', 'a') as output:
                for line in f:
                    line_num += 1
                    if len(line) > 120:
                        output.write(filename + ' ' + str(line_num) + '\n')

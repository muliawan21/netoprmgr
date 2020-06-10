import os
'''
current_dir=os.getcwd()
files = os.listdir(current_dir)
count_file = 0
for file in files:
    if 'check_script' in file:
        pass
    else:
        try:
            read_file = open(file, 'r')
            read_file_list = read_file.readlines()
            for line in read_file_list:
                if "if re.findall('.*PID\s+TTY\s+Allocated\s+Freed\s+Holding\s+Getbufs\s+Retbufs\s+Process',line):" in line:
                    print(file)
                    count_file+=1
                    break
        except:
            pass
print('Total File : '+str(count_file))
'''

current_dir=os.getcwd()
files = os.listdir(current_dir)
count_file = 0
for file in files:
    if '__pycache__' in file:
        pass
    elif 'check_script.py' in file:
        pass
    elif '__init__.py' in file:
        pass
    elif 'cisco_None.py' in file:
        pass
    else:
        print(file)
    count_file+=1
print('Total File : '+str(count_file))

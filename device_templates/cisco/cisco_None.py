import sqlite3
import re



class cisco_None:
    def __init__(self,file):
        #variable constructor
        self.file = file
        #read all things in file
        read_file = open(self.file,'r')
        read_file_list = read_file.readlines()
        for line in read_file_list:
            #SOFTWARE TABLE
            #get device name
            if re.findall('^hostname (.*)',line):
                devicename = re.findall('^hostname (.*)',line)
                devicename = devicename[0]
                break
                #print(devicename)
        for line in read_file_list:
            #get device model
            if re.findall('^.isco\s+(\S+).*with.*bytes',line):
                model = re.findall('^.isco\s+(\S+).*with.*bytes',line)
                model = model[0]
                break           
        #open db connection
        db = sqlite3.connect('pmdb')
        cursor = db.cursor()
        #LOG Checking
        try:
            cursor.execute('''INSERT INTO logtable(devicename, model, script)
                    VALUES(?,?,?)''', (devicename+'(template not found)', model+'(template not found)',self.__class__.__name__+'(template not found)',))
        except:
            cursor.execute('''INSERT INTO logtable(devicename, model, script)
                    VALUES(?,?,?)''', (self.file+'-'+'error'+'(template not found)', self.file+'-'+'error'+'(template not found)',self.file+'-'+'error'+'(template not found)',))
        db.commit()             
        db.close()

        
        
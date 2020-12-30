import json
import time
class Error(Exception):
    pass
class KeyExists(Error):
    pass
class TimeExceeded(Error):
    pass
class KeyNotFound(Error):
    pass
class FileSystem:
    
    def __init__(self,path):
        self.path=path
        f=open(path,w)
        s={"":""}
        s=json.dumps(s)
        for x in s:
            f.write(x)
    def __init__(self):
        self.path="D://myfile.json"
        s={"":""}
        s=json.dumps(s)
        for x in s:
            f.write(x)
    def addEntry(self,k,value,time):
        with open(self.path) as f:
            d=json.load(f)
        f.close()
        try:
            if(k in d):
                raise KeyExists
            else:
                d[k]=[]
                d[k].append(value)
                d[k].append(time)
                d=json.dumps(d)
                with open(self.path) as f:
                    f.write(d)
        except:
            print("Key Doesn't Exist")
    def addEntry(self,key,value):
        with open(self.path) as f:
            d=json.load(f)
        f.close()
        if(k in d):
            raise KeyExists
        else:
            d[k]=[]
            d[k].append(value)
            d[k].append(2**31)
            d=json.dumps(d)
            with open(self.path) as f:
                f.write(d)
    def entryRead(self,key):
        with open(self.path) as f:
            d=json.load(f)
        try:
            if(key in d):
                times=int(time.time()*1000.0)
                if(times-d[key][1]<d[key][0]):
                    return d[key][0]
                else:
                    raise timeExceeded
            else:
                raise KeyNotFound
        except timeExceeded:
            print("Time is Exceeded")
        except KeyNotFound:
            print("Key is Not Found")
    def entryDeletion(self,key):
        with open(self.path) as f:
            d=json.load(f)
        try:
            if(key in d):
                times=int(time.time()*1000.0)
                if(times-d[key][1]<d[key][0]):
                    del d[key]
                else:
                    raise timeExceeded
            else:
                raise KeyNotFound
        except timeExceeded:
            print("Time is Exceeded")
        except KeyNotFound:
            print("Key is Not Found")
    
            

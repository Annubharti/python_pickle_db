import json
import random



def load(filename='hello.db', true = False):
    meraDB = Mydb(filename , true)
    meraDB.load_file()
    return meraDB


class Mydb():
    filename = ""
    jsonobject={}
    true=False

    def __init__(self, filename, true):
        self.filename = filename
        self.true= true

    def load_file(self):
        print ("loading")
        try:
            data = open(self.filename, 'r+')
        except:
            data = open(self.filename, "w+")
            
        content = data.read()
        if content == "":
            content = json.dumps({})
        self.jsonobject = json.loads(content)
        return self.jsonobject

        

    def dump(self):
        file1 = open(self.filename, 'w')
        content = json.dumps(self.jsonobject) 
        print ("dumping")
        file1.write(content)
        return content

    def set(self, key, value):
        
        self.jsonobject[key]=value
        if self.true == True:
            self.dump()
        print (self.jsonobject)
        return self.jsonobject



    def get(self,key):
        try:
            print (self.jsonobject[key])
            return self.jsonobject[key]
        except:
            print ("This key doesn't exits.")
            return "This key doesn't exits."

    def get_all(self):
        list_of_all_keys = []
        file1=open(self.filename,"r")
        content=file1.read()
        
        if content != "":
            jsonobject = json.loads(content)
            for keys in self.jsonobject:
                list_of_all_keys.append(keys)
            if list_of_all_keys==[]:
                print ("There is no key present in database.")
                return "ok"
        print (list_of_all_keys)
        return list_of_all_keys

    def rem(self,key):
        
        if key in self.jsonobject:
            del self.jsonobject[key]
        else:
            print ("This key don't exist.")
            return ("This key don't exist.")
        if self.true == True:
            self.dump()
        print (self.jsonobject)
        return self.jsonobject

    def exist(self,key):
        if key in self.jsonobject:
            return True
        else:
            return False
    
    def total_keys(self):
        count = 0
        for keys in self.jsonobject:
            count = count+1
        print (count)
        return count

    def del_db(self):
        self.jsonobject.clear()
        if self.true==True:
            self.dump()
        print (self.jsonobject)
        return self.jsonobject

    def random_insert(self,number):
        
        file1=open(self.filename,"r")
        content=file1.read()
        count = 0
        while count < number:
            key = random.randint(1,1000)
            value = random.randint(1,1000)
            self.jsonobject[key] = value
            count = count+1
        if self.true == True:
            self.dump() 
        print (self.jsonobject)
        
        return self.jsonobject


    def demerge(self,some_other_db):
        second_db = Mydb(some_other_db, True)
        self.jsonobject = second_db.load_file()
        return second_db








        


            
        
        
        

        



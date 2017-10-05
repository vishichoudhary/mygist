import requests,json,datetime,time,getpass
#import global_vars as gv
class Create_gist:
    "Class for gist creation"
    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd
    def create(self):
        self.des=input("Enter the description for gist ")
        self.public=input("Make this gist public (y/n) ")
        if self.public=='y' or self.public=='Y':
            self.public=True
        else:
            self.public=False
        self.file_name=input("Enter the file name with extension ")
        with open(self.file_name,"r") as myfile:
            self.info=myfile.read()
        self.file_name = self.file_name.split('/')[-1]
        self.send_dict={"description":self.des,
                "public":self.public,
                "files":{
                    self.file_name:{
                        "content":self.info
                        }
                    }
                }
        re=requests.post('https://api.github.com/gists',auth=(self.user,self.passwd),data=json.dumps(self.send_dict))
        print("Gist id of new gist is ",re.json()['id'])

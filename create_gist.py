import requests,json
import global_vars as gv
class Create_gist:
    "Class for gist creation"
    def __init__(self,url):
        self.url=url
        self.headers=gv.headers
    def create(self):
        self.des=input("Enter the description for gist")
        self.public=input("Make this gist public (y/n)")
        if self.public=='y' or self.public=='Y':
            self.public='true'
        else:
            self.public='false'
        self.file_name=input("Enter the file name with extension ")
        with open(self.file_name,'r') as myfile:
            self.data=myfile.read().replace('\n','')
        self.send_dict={"description":self.des,
                "public":self.public,
                "files":{
                    self.file_name:{
                        "content":self.data
                        }
                    }
                }
        re=requests.post(self.url,headers=self.headers,files=self.send_dict)
        print(re.status_code)

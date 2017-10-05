import requests,json,datetime,time
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
            self.fdata=myfile.read()
        print(self.fdata)
        self.info="try after a long time"
        self.date=datetime.date.today()
        self.c_time=time.strftime("%H:%M:%S")
        self.send_dict="""{"description":"%s",
                "public":"%s",
                "files":{
                    "%s":{
                        "content":"%s"
                        }
                    }
                }"""
        self.send_dict=self.send_dict%(self.des,self.public,self.file_name,self.info)
        re=requests.post('https://api.github.com/gists',headers=self.headers,data=json.dumps(self.send_dict))
        print(re.status_code)

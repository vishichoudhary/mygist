import json
import requests
class fetch_gist:
    "Simple fetch command class"
    def __init__(self,url,pas='',user_name=''):
        self.url=url
        self.pas=pas
        self.user_name=user_name
    def fetch(self):
        req=requests.get(self.url)
        res_ans=req.json()
        if req.status_code==200:
            print("Total no of public gists are "+str(len(res_ans)))
            for i in range(len(res_ans)):
                l=list(res_ans[i]['files'].keys())
                print(l[0])
        else:
            print(req.status_code)
            print("unsuccessful")
    def fetch_auth(self):
        req=requests.get(self.url,auth=(self.user_name,self.pas))
        res_ans=req.json()
        if req.status_code==200:
            print("Total no of public gists are "+str(len(res_ans)))
            for i in range(len(res_ans)):
                l=list(res_ans[i]['files'].keys())
                print(l[0])
        else:
            print(req.status_code)
            print("unsuccessful")


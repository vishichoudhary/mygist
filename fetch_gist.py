import json
import requests
class fetch_gist:
    "Simple fetch command class"
    def __init__(self,url):
        self.url=url
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


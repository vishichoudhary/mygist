import json
import requests
import global_vars as gv
class fetch_gist:
    "Simple fetch command class"
    def __init__(self,url,token,pas='',user_name=''):
        self.url=url
        #self.pas=pas
        #self.user_name=user_name
        self.token=token
    def fetch(self):
        req=requests.get(self.url)
        res_ans=req.json()
        if req.status_code==200:
            print("Total no of public gists are "+str(len(res_ans)))
            for i in range(len(res_ans)):
                l=list(res_ans[i]['files'].keys())
                print(str(i)+l[0])
                new_dict={l[0]:res_ans[i]['files'][l[0]]['raw_url']}
                gv.link_dict.update(new_dict)
                gv.no_dict.update({str(i):l[0]})
        else:
            print(req.status_code)
            print("unsuccessful")
    def fetch_auth(self):
        self.headers = {'Authorization': 'token %s' % self.token}
        req=requests.get(self.url,headers=self.headers)
        #req=requests.get(self.url,auth=(self.user_name,self.pas))
        res_ans=req.json()
        if req.status_code==200:
            print("Total no of public gists are "+str(len(res_ans)))
            for i in range(len(res_ans)):
                l=list(res_ans[i]['files'].keys())
                print(str(i)+l[0])
                new_dict={l[0]:res_ans[i]['files'][l[0]]['raw_url']}
                gv.link_dict.update(new_dict)
                gv.no_dict.update({str(i):l[0]})
        else:
            print(req.status_code)
            print("unsuccessful")

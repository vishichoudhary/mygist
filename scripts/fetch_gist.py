import json,requests,getpass
#import global_vars as gv
class fetch_gist:
    """Simple fetch command class"""
    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd
    def fetch_auth(self):
        url='https://api.github.com/users/'+self.user+'/gists'
        req=requests.get(url,auth=(self.user,self.passwd))
        res_ans=req.json()
        if req.status_code==200:
            print("Total no of gists are "+str(len(res_ans)))
            for i in range(len(res_ans)):
                l=list(res_ans[i]['files'].keys())
                new_dict={l[0]:res_ans[i]['files'][l[0]]['raw_url']}
                id_temp={l[0]:res_ans[i]['id']}
                print(str(i+1)+" "+l[0])
                print("Gist id is " + res_ans[i]['id']+"\n")
                #print(id_temp)
                #gv.link_dict.update(new_dict)
                #gv.no_dict.update({str(i+1):l[0]})
                #gv.id_no.update(id_temp)
        else:
            print(req.status_code)
            print("unsuccessful")

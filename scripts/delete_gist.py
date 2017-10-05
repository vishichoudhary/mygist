import json,requests,getpass
#import global_vars as gv
class delete_gist :
    def __init__(self,user,passwd):
        self.user=user
        self.passwd=passwd
    def del_gist(self,gist_id):
        self.url='https://api.github.com/gists/'+gist_id
        req=requests.delete(self.url,auth=(self.user,self.passwd))
        if(req.status_code==204):
            print("succesfully deleted")
        else:
            print("unsuccessful error code is ")
            print(req.status_code)


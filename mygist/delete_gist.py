import json,requests
import global_vars as gv
class delete_gist :
    def __init__(self):
        self.headers=gv.headers
    def del_gist(self,gist_id):
        self.url='https://api.github.com/gists/'+gist_id
        req=requests.delete(self.url,headers=self.headers)
        if(req.status_code==204):
            print("succesfully deleted")
        else:
            print("unsuccessful error code is ")
            print(req.status_code)


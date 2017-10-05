import requests,json,datetime,time,getpass
#import global_vars as gv

class Gist:
	"Class for gist creation"
	def __init__(self, user = None, passwd = None):
		self.user = user
		self.passwd = passwd
		self.gists_number = 0
		
	def list(self):
		url='https://api.github.com/users/'+self.user+'/gists'
		req=requests.get(url,auth=(self.user,self.passwd))
		res_ans=req.json()
		
		if req.status_code==200:
			self.gists_number = len(res_ans)
            #print("Total no of gists are "+str(len(res_ans)))
			for i in range(len(res_ans)):
				l=list(res_ans[i]['files'].keys())
				new_dict={l[0]:res_ans[i]['files'][l[0]]['raw_url']}
				id_temp={l[0]:res_ans[i]['id']}
				print("\n"+str(i+1)+" "+l[0])
				print("Gist id is " + res_ans[i]['id'])
		else:
			raise Exception("Login failed.")
		
	def create(self, description, files, public = True):
        
		files_dic = {}

		for file_name, file_cont in files:
			files_dic[file_name] = {"content": file_cont}
		
		self.send_dict={"description":description,
						"public": public,
						"files": files_dic
						}
						
		req=requests.post('https://api.github.com/gists',auth=(self.user,self.passwd),data=json.dumps(self.send_dict))
		return None if req.status_code != 201 else json.loads(req.text)["id"]
		
	def delete(self, gist_id):
		self.url='https://api.github.com/gists/' + gist_id
		req=requests.delete(self.url, auth = (self.user,self.passwd))
		#print(req.status_code)
		return req.status_code == 204
		

import datetime, re, requests, json, time
#import global_vars as gv

class GistFile:
	def __init__(self, json_data):
		self.filename = json_data["filename"]
		self.content = json_data["content"]
		self.language = json_data["language"]
		self.size = json_data["size"]
		self.type = json_data["type"]
		self.truncated = json_data["truncated"]


class Gist:
	def __init__(self, json_data):
		self.url = json_data["url"]
		self.forks_url = json_data["forks_url"]
		self.commits_url = json_data["commits_url"]
		self.id = json_data["id"]
		self.description = json_data["description"]
		self.public = json_data["public"]
		self.owner = json_data["owner"]["login"]
		self.truncated = json_data["truncated"]
		self.comments = json_data["comments"]
		self.created_at = json_data["created_at"]
		self.updated_at = json_data["updated_at"]
		
		# Store also the created and updated datetimes as timestamps
		dt_pattern = r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z"
		created_groups = map(int, re.match(dt_pattern, self.created_at).groups())
		self.created_at_ts = int(time.mktime(datetime.datetime(*created_groups).timetuple()))
		updated_groups = map(int, re.match(dt_pattern, self.updated_at).groups())
		self.updated_at_ts = int(time.mktime(datetime.datetime(*updated_groups).timetuple()))

		self.files = []

		for file_name in json_data["files"]:
			self.files.append(GistFile(json_data["files"][file_name]))


class GistHandler:
	"Class for gist creation"
	def __init__(self, user = None, passwd = None):
		self.user = user
		self.passwd = passwd
		self.gists_number = 0
	
	def auth(user, passwd):
		self.user = user
		self.passwd = passwd

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

	def retrieve(self, gist_id):
		self.url='https://api.github.com/gists/' + gist_id
		#req=requests.get(self.url, auth = (self.user,self.passwd))
		req=requests.get(self.url)
		return Gist(json.loads(req.text)) if req.status_code == 200 else None

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
		return req.status_code == 204
		
	def star(self, gist_id):
		url = 'https://api.github.com/gists/%s/star' % gist_id
		req = requests.put(url, auth = (self.user,self.passwd))
		return req.status_code == 204

	def unstar(self, gist_id):
		url = 'https://api.github.com/gists/%s/star' % gist_id
		req = requests.delete(url, auth = (self.user,self.passwd))
		return req.status_code == 204



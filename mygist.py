import requests,json
import global_vars as gv
import create_gist as cg
#user_name=input("Enter user name ")
user_name='vishichoudhary'
url='https://api.github.com/users/'+user_name+'/gists?per_page=30000'
gv.init()
obj=cg.Create_gist(url)
obj.create()

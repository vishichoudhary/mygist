import requests, getpass,json
import global_vars as gv
from fetch_gist import fetch_gist as fg
user_name=input("Enter user name ")
#passwd=getpass.getpass("Enter your robust password ")
url='https://api.github.com/users/'+user_name+'/gists?per_page=30000'
token=input('Enter your api_token ')
gv.init()
ob=fg(url,token)
ob.fetch_auth()
choice=input("Enter the no. of file you want to download ")
choice=gv.no_dict[choice]
fe=requests.get(gv.link_dict[choice])
output=open(choice,'w')
output.write(fe.text)

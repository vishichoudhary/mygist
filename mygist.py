import requests
import getpass
import json
from fetch_gist import fetch_gist as fg
user_name=input("Enter user name ")
passwd=getpass.getpass("Enter your robust password ")
url='https://api.github.com/users/'+user_name+'/gists?per_page=30000'
ob=fg(url,passwd,user_name)
ob.fetch_auth()

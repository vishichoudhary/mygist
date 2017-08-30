import requests
import getpass
import json
from fetch_gist import fetch_gist as fg
user_name=input("Enter user name ")
url='https://api.github.com/users/'+user_name+'/gists?per_page=30000'
ob=fg(url)
ob.fetch()


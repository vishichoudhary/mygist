import requests,json
import global_vars as gv
import create_gist as cg
import fetch_gist as fg
import delete_gist as dg
#user_name=input("Enter user name ")
user_name='vishichoudhary'
url='https://api.github.com/users/vishichoudhary/gists'
gv.init()
ob=fg.fetch_gist(url)
ob.fetch_auth()
ob1=dg.delete_gist();
ch=input("enter the id to be deleted ")
ob1.del_gist(ch)

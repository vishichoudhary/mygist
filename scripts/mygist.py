import requests,json,getpass
import create_gist as cg
import fetch_gist as fg
import delete_gist as dg
user_name=input("Enter your github user name ")
passwd=getpass.getpass("Enter your github password ")
ob=fg.fetch_gist(user_name,passwd)
ob.fetch_auth()
ob=cg.Create_gist(user_name,passwd)
ob.create()
ob=dg.delete_gist(user_name,passwd)
id_no=input("Enter the id no to be deleted ")
ob.del_gist(id_no)

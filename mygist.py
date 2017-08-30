import requests
import getpass
user_name=input("Enter user name ")
passwd=getpass.getpass("Enter password ")
url='https://api.github.com/users/'+user_name+'/gists'
re=requests.get(url,auth=(user_name,passwd))
if re.status_code==200:
    print("Succesful")
else:
    print(re.status_code)
    print("Unsuccessful")

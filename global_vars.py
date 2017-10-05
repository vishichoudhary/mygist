def init():
    global link_dict
    link_dict={}
    global no_dict
    no_dict={}
    global id_no
    id_no={}
    global token
    token=input("Enter your token ")
    global headers
    headers={'X-Github-Username':'vishichoudhary',
            'Content-Type':'application/json',
            'Authorization':'token %s' %token
            }
    #headers={'X-Github-Username':'vishichoudhary','Content-Type':'application/json','Autorization':'token %s' %token}
    #headers={'Autorization':'token %s' %token}

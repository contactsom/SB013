import getpass

try:
    p=getpass.getpass()
except Exception as error:
    print("Error",error)
else:
    print("Password entred",p)
'''
How to create the Custome Exception
'''

class IdCardNotFoundException(Exception):
    def __init__(self,arg):
        self.msg=arg

#swap="Failed"
swap="Success"

if swap=="Failed":
    raise IdCardNotFoundException("Please wait we will bring temproary ID card for you")
else:
    print("Enter to office")



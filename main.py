import os
import hashlib
import json

def hash_password():
    json = {}
    user_password = 'ham' #password (replace with request.form)
    hashed_password = hashlib.md5(user_password.encode())  #create a new variable, with the value being an encoded user_password variable
    json['hashed_password'] = hashed_password.hexdigest() #hexdigest converts the hash file into a readable value
    print(json) #print the hashed password as a string
    return None


hash_password()

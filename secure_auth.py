import bcrypt 
import json
import os 
import re 
import time 


class SecureAuth:
    def __init__(self,db_file='users.json'):
        self.db_file=db_file
        self.failed_attempts={}
        self.users=self.load_users()

    def load_users(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {}
        
    def save_users(self):
        with open(self.db_file,'w') as f:
            json.dump(self.users, f, indent=4)
    
    def validate_password_strenght(self, password):
        """ __Enforce Strong Passoword__"""
        if len(password)<8:
            return False,"Password must be 8 characters long "
        if not re.search(r"[A-Z]", password):
            return False , "Password must include at least 1 character in uppercase "
        if not re.search(r"[a-z]", password):
            return False, "Passowrd must include at least 1 lowercase character "
        if not re.search(r"[0-9]", password):
            return False , "Password must contain at least 1 number "
        if not re.search(r"[!@#$%^&*()~|<>,.:;?'_-]", password):
            return False, "Password must contain at least 1 special character "
        return True ,"Strong Password "
    
    def register(self, username,password):
        if username in self.users:
            return "Error!! Username already exists ..."
        
        is_strong, msg=self.validate_password_strenght(password)
        if not is_strong:
            return f"Registraction Faild: {msg}"
        
        hashed=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users[username]=hashed.decode()
        self.save_users()
        return "Regristration successfull !!"

    def login(self,username,password):
        if self.failed_attempts.get(username, 0) >=3:
            return "Account locked due to many failed attempts Try again later "

        if username not in self.users:
            return "Invalid credententials!! "

        stored_hash=self.users[username].encode()
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            self.failed_attempts[username]=0
            return "Login Successfull "
        else:
            self.failed_attempts[username]=self.failed_attempts.get(username, 0) +1
            remaining=3 - self.failed_attempts[username]
            return f"Invalid credentials ! Remaining attempys : {remaining}"


if __name__=="__main__":
    auth =SecureAuth()
    print("---Testing Registration System ---")
    print(auth.register("hammad", "1234567")) #weak pass 
    print(auth.register("hammad", "hAmmad123$@")) #storng pass

    print("\n ---Testing Brute Force Defense---")
    print(auth.login("hammad", "11Aq2233"))
    print(auth.login("hammad", "54554885"))
    print(auth.login("hammad", "hAmmad123$@"))
       


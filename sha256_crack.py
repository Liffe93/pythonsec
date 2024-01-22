from pwn import * 
import sys 


# pass shah hash arguments from command line 
# correct user if they do not enter right argu
if len(sys.argv) != 2:
	print("Nah that's not right")
	print(">> {} <shah256sum".format(sys.argv[0]))
	exit()

# otherwise crack that hash bb
wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0 

with log.progress("Lets Crack: {}!\n".format(wanted_hash)) as p:
	#open rockyou.txt to read and specify encoding within file
	with open(password_file, "r", encoding='latin-1') as password_list:
		#iterate over each password in file 
		for password in password_list:
			password = password.strip("\n").encode("latin-1")
			password_hash = sha256sumhex(password)
			#print attempts, password, and password hash 
			p.status("[{}] {} == {}".format(attempts, password.decode("latin-1"), password_hash))
			#if we found the plain text that matches
			if password_hash == wanted_hash:
				p.success("We found the password hash! After {} attempts and {} hashes to {}".format(attempts, password.decode('latin-1'), password_hash))
				exit()
			# if we didnt find the password then iterate back thru the loop 	
			attempts += 1 		
		# nothing found 
		p.failure("Dude this password hash was not found")


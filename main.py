import requests
import time
from colorama import Fore


    

header = '''
 __      ___  _  ___ ___ ___    ___ _  _ ___ ___ _  _____ ___  __   __  ___ 
 \ \    / / || |/ _ \_ _/ __|  / __| || | __/ __| |/ / __| _ \ \ \ / / |_  )
  \ \/\/ /| __ | (_) | |\__ \ | (__| __ | _| (__| ' <| _||   /  \ V /   / / 
   \_/\_/ |_||_|\___/___|___/  \___|_||_|___\___|_|\_\___|_|_\   \_/   /___|
    BY NIZAR BAMIDA v 2.0.5     SEONJ.NET
   '''
try:
	print(Fore.GREEN + header)
	input_list = input("THe list you want me to scan ?? : ")
	save_as = input("save results as what ? : ")
	file1 = open(input_list, 'r') 
	domains = file1.readlines()
	count = 0
	counter = 0
	start  = time.time()
	for domain in domains:
		counter += 1
	print("STARTING  "+ str(counter) +" of domains loaded")
	f= open("./output/available_domains"+str(save_as)+".csv","w+")
	f.close()
	rez = open("./output/available_domains"+str(save_as)+".csv","a")
	for domain in domains :
		count +=1
		start = time.time()
		session = requests.session()

		reqq_url = "https://domains.revved.com:443/v1/whois?domains=" + domain.rstrip("\n")
		reqq_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-GB,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.namecheap.com", "Connection": "close", "Referer": "https://www.namecheap.com/domains/registration/results/?domain=&type=beast"}
		if count == 225 or  count == 10000 or count == 2544  :
			print(Fore.BLUE + "sleeping at"+ str(count) +"for 12 sec")
			time.sleep(12)
		else:
			
			resp = session.get(reqq_url, headers=reqq_headers).json()
			
			if str(resp) == "{'results': []}" :
				rez.write(domain.rstrip("\n")  + '\n')
				
				print(Fore.GREEN +"["+str(count)+"]  "+domain.rstrip("\n") +"   is available  logged [+]")
			else:
				print(Fore.RED + "["+str(count)+"]  "+"Sorry "+domain.rstrip("\n") +" is registred")
	rez.close()           
			
	end = time.time()
	print(f"Runtime of the program is {end - start}")
except:
	pass

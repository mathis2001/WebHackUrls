#!/usr/bin/env python3

import requests
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import re

print('''

 ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ 
||w ||||e ||||b ||||h ||||a ||||c ||||k ||||u ||||r ||||l ||||s ||
||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
						   by S1rN3tZ
''')

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="target domain (exp: target.com)", type=str)
parser.add_argument("-k", "--keyword", help="search for a specific extension or keyword (js, xml, json, pdf... or admin, login, dashboard...)", type=str)
parser.add_argument("-l", "--limit", help="limit (number of links you want)", type=str)
parser.add_argument("-s", "--screenshot", help="take screenshot of each url", action="store_true")
parser.add_argument("-r", "--rate-limit", help="time between two screens", type=float)
parser.add_argument("-o", "--output", help="Output file name", type=str)
parser.add_argument("-oD", "--outdomains", help="Output domain names", type=str)
args = parser.parse_args()
	
def screenshot(urls):
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Firefox(options=options)
	driver.set_page_load_timeout(30)    
	driver.maximize_window()
	
	lines=urls.split()
	i=0
	print(bcolors.OK+"[+] "+bcolors.RESET+"Screening urls...")
	for url in lines:
		i=i+1
		cut=url.split('/')
		driver.get(url)
		if args.rate_limit:
			sleep(args.rate_limit)
		else:
			sleep(1)
		driver.save_screenshot("screens/screen-"+str(cut[3])+"-"+str(i)+".png")
		print('.')
	driver.quit()
	print(bcolors.OK+"[+] "+bcolors.RESET+"done!")

def MatchDomains(urls):
    	regex = r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)/?"
    	matches = re.finditer(regex, urls, re.MULTILINE)
    	domainList = []

    	for match in matches:
    		domainList.append(match.group(1))
    	
    	NoDuplicate = []
    	print(bcolors.INFO+"[*] "+bcolors.RESET+"Domains found for "+bcolors.INFO+args.domain+bcolors.RESET)
    	for domain in domainList:
    		if domain not in NoDuplicate:
    			NoDuplicate.append(domain)
    			print(domain)
    	return NoDuplicate 


def main():
	url="https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"

	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./webhackurls -d target.com [-k keyword] [-l limit] [-o output] [-oD Domain names output]")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"help: ./webhackurls -h")
		exit(0)
	else:
		if args.domain:
			domain = args.domain
			url = url+"&url="+domain+"/"
			if args.keyword:
				keyword=args.keyword
				url=url+"&filter=urlkey:.*"+keyword
			if args.limit:
				limit=args.limit
				url=url+"&limit="+limit
		else:
			print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")

	print(bcolors.INFO+"[*] "+bcolors.RESET+"Processing your request... It can take few seconds.")
	rq=requests.get(url)
	print(rq.text)

	if args.screenshot:
		screenshot(rq.text)
	if args.output:
		file = args.output
		log = open(file, "w")
		log.write(rq.text)
		log.close()
	if args.outdomains:
		file = args.outdomains
		log = open(file, "w")
		domains = MatchDomains(rq.text)
		for domain in domains:
			log.write(domain+'\n')
		log.close()
try:
        main()
except Exception as e:
        print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")



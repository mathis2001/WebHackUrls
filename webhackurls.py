#!/usr/bin/env python3

import requests
import sys
import argparse

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
parser.add_argument("-o", "--output", help="Output file name", type=str)
args = parser.parse_args()
	


def main():
	url="https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"

	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./webhackurls -d target.com [-k keyword] [-l limit] [-o output]")
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
	
	if args.output:
		file = args.output
		log = open(file, "w")
		log.write(rq.text)
		log.close()
try:
        main()
except Exception as e:
        print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")



#!/usr/bin/env python3

import requests
import sys
from sys import argv
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

def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", action='store_true', help="target domain (exp: target.com)")
	parser.add_argument("-k", action='store_true', help="search for a specific extension or keyword (js, xml, json, pdf... or admin, login, dashboard...)")
	parser.add_argument("-l", action='store_true', help="limit (number of links you want)")
	parser.add_argument("-o", action='store_true', help="Output file name")
	args = parser.parse_args()
	print(args)

def getopts(argv):
	opts = {}  
	while argv:
		if argv[0][0] == '-':
			try:
				opts[argv[0]] = argv[1]  
			except Exception:
				parser()
		argv = argv[1:] 
	return opts

def main():
	myargs = getopts(argv)
	url="https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"

	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./webhackurls -d target.com [-k keyword] [-l limit] [-o output]")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"help: ./webhackurls -h")
	else:
		if '-d' in myargs:
			url = url+"&url="+myargs['-d']+"/"
		if '-k' in myargs:
			url=url+"&filter=urlkey:.*"+myargs['-k']
		if '-l' in myargs:
			url=url+"&limit="+myargs['-l']

	rq=requests.get(url)
	print(rq.text)
	
	if '-o' in myargs:
		log = open(myargs['-o'], "w")
		log.write(rq.text)
		log.close()
try:
        main()
except Exception as e:
        print(e)
except KeyboardInterrupt:
        print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")



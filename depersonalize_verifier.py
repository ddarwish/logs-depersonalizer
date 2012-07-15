import sys
import re

fh = open('logcat_pr.log')
for line in fh.readlines():
	if re.search(r'(?i)your.surname', line):
		print line
	if re.search(r'(?i)your.nickname', line):
		print line
	if re.search(r'your.phone.number', line):
		print line
	if re.search(r'(?i)your.login', line):
		print line
	if re.search(r'(?i)sms', line):
		print line
	if re.search(r'(?i)mms', line):
		print line		
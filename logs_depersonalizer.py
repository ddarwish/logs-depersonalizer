import sys
import re

os.rename("logcat.log", "logcat.log.bak")
fh = open('logcat.log.bak')
fo = open('logcat.log','w')
for line in fh.readlines():
	line = re.sub(r'\+7\d{10,10}(\D)', r'+7xXxXxXxXxX\1', line)
	line = re.sub(r'\D7\d{10,10}(\D)', r'7xXxXxXxXxX\1', line)
	line = re.sub(r'(\s)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}(\s)', r'\1zzzy@zzzz.com\2', line)
	if re.search(r'(?i)userid', line):
		line = re.sub(r'([\d-]{5}\x20[\d:]*.[\d]*\x20[\w/()]*:)[^\n]*', r'\1 ---------- line clr ----------', line)
	if re.search(r'(?i)your.surname', line):
		line = re.sub(r'([\d-]{5}\x20[\d:]*.[\d]*\x20[\w/()]*:)[^\n]*', r'\1 ---------- line clr ----------', line)
	fo.writelines(line)	
fo.close()
fh.close()

os.rename("logcat_radio.log", "logcat_radio.log.bak")
fh = open('logcat_radio.log.bak')
fo = open('logcat_radio.log','w')
for line in fh.readlines():
	line = re.sub(r'\+7\d{10,10}(\D)', r'+7xXxXxXxXxX\1', line)
	line = re.sub(r'\D7\d{10,10}(\D)', r'7xXxXxXxXxX\1', line)
	line = re.sub(r'(\s)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}(\s)', r'\1zzzy@zzzz.com\2', line)
	if re.search(r'(?i)userid', line):
		line = re.sub(r'([\d-]{5}\x20[\d:]*.[\d]*\x20[\w/()]*:)[^\n]*', r'\1 ---------- line clr ----------', line)
	if re.search(r'(?i)your.surname', line):
		line = re.sub(r'([\d-]{5}\x20[\d:]*.[\d]*\x20[\w/()]*:)[^\n]*', r'\1 ---------- line clr ----------', line)
	fo.writelines(line)	
fo.close()
fh.close()
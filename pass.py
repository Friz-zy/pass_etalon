#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sha512(sha512("salt" XOR "nick : site") XOR "pass")[:32]

# python -c 'import hashlib; print hashlib.sha512("test\n").hexdigest()'
#http://news.ycombinator.com/item?id=4374888
#https://gist.github.com/3334991

# python -c "import hashlib, getpass;from itertools import cycle, izip;f = open('pass.py');salt = f.read();f.close();print hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(salt, cycle(raw_input('nick:') + ' : ' + raw_input('site:'))))).hexdigest(), cycle(getpass.getpass())))).hexdigest()[:32]"

# use this code as salt and check the unique
with open('pass.py') as f:
	salt = f.readlines()
# if salt isn't unique: add some unique string to it
if "#" in salt[-1][1]:
	import os
	try:
		# only linux way
		os.popen("(dmesg;env;head -c16 /dev/random)|sha512sum >> ./pass.py")
		with open('pass.py', "r") as f:
			salt = f.readlines()
		salt[-1]="#" + salt[-1]
		with open('pass.py', "w") as f:
			f.writelines(salt)
		os.popen("chmod 400 ./pass.py") # only your user can read this file
	except IOError, OSError:
		# it is works in all OS, but clock() is most efficient in Windows
		from time import clock
		with open('pass.py', "a") as f:
			f.writeline("#" + hashlib.sha512(clock()).hexdigest())

import hashlib, getpass

from itertools import cycle, izip

# XOR function, thk The Internet
def xor(ss, key):
	key = cycle(key)
	return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))

# use this code as salt
with open('pass.py') as f:
	salt = f.read()

nick = raw_input("nick:") + " : " + raw_input("site:")
firstXor = xor(salt, nick)
firstSha = hashlib.sha512(firstXor).hexdigest()
print hashlib.sha512(xor(firstSha, getpass.getpass())).hexdigest()[:32]
##

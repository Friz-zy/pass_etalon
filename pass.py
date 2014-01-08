#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sha512(sha512("salt" XOR "nick : site") XOR "pass")[:32]

# python -c 'import hashlib; print hashlib.sha512("test\n").hexdigest()'
#http://news.ycombinator.com/item?id=4374888
#https://gist.github.com/3334991

# python2 -c "import hashlib, getpass;from itertools import cycle, izip;f = open('pass.py');salt = f.read();f.close();print hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(salt, cycle(raw_input('nick:') + ' : ' + raw_input('site:'))))).hexdigest(), cycle(getpass.getpass())))).hexdigest()[:32]"

# use this code as salt and check the unique
import six
import hashlib, getpass

if six.PY3:
    from itertools import cycle
    izip = zip
    raw_input = input
else:
    from itertools import cycle, izip

file = "./pass.py"
with open(file, "r") as f:
    salt = f.readlines()
# if salt isn't unique: add some unique string to it
if "#" in salt[-1][1]:
    import os
    import subprocess
    try:
        subprocess.call("(dmesg;env;head -c16 /dev/random)|sha512sum >> " + file, shell=True)
        with open(file, "r") as f:
            salt = f.readlines()
        salt[-1]="#" + salt[-1]
        with open(file, "w") as f:
            f.writelines(salt)
        os.chmod(file, 256) # only your user can read this file
    except (IOError, OSError):
        # it is works in all OS, but clock() is most efficient in Windows
        with open(file, "a") as f:
            f.writeline("#" + hashlib.sha512(clock()).hexdigest())
        try:
            os.chmod(file, 256) # only your user can read this file
        except OSError:
            pass

# XOR function, thk The Internet
def xor(ss, key):
    key = cycle(key)
    if six.PY3:
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key)).encode()
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))

# use this code as salt
with open('pass.py') as f:
    salt = f.read()

nick = raw_input("nick:") + " : " + raw_input("site:")
firstXor = xor(salt, nick)
firstSha = hashlib.sha512(firstXor).hexdigest()
secondXor = xor(firstSha, getpass.getpass())
six.print_((hashlib.sha512(secondXor).hexdigest()[:32]))
##

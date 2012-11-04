Implementation of the algorithm and the generation of the password, as described http://news.ycombinator.com/item?id=4374888 + https://gist.github.com/3334991

# sha512(sha512("salt" XOR "nick : site") XOR "pass")[:32]

For quick use in bash:
# python -c "import hashlib, getpass;from itertools import cycle, izip;f = open('pass.py');salt = f.read();f.close();print hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(salt, cycle(raw_input('nick:') + ' : ' + raw_input('site:'))))).hexdigest(), cycle(getpass.getpass())))).hexdigest()[:32]"

Written on python2.8 by Filipp Frizzy aka filipp.s.frizzy@gmail.com

MIT license

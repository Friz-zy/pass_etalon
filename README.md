# Pass - «associate password so simple»

Implementation of an algorithm generating and storing a passwords like this: "cf83e1357eefb8bdf1542850d66d8007". Written on python 2.7.
Used `sha512(sha512("salt" XOR "nick : site") XOR "pass")[:32]` algorithm, created by [Gist](https://gist.github.com/3334991) and modified [here](http://news.ycombinator.com/item?id=4374888).
It's an etalone and salt file for other programs.

**How to:**
This script helps you generate unique passwords for sites, programs, etc...
At first start python will record unique salt in pass.py and run generating password. You need to enter nick, url of site and master password. New password will be displayed in console (or standart stdout). Just copy it.

Src on [Github](http://friz-zy.github.com)
Code under **MIT license**

For quick use copy to bash:
`python -c "import hashlib, getpass;from itertools import cycle, izip;f = open('pass.py');salt = f.read();f.close();print hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(salt, cycle(raw_input('nick:') + ' : ' + raw_input('site:'))))).hexdigest(), cycle(getpass.getpass())))).hexdigest()[:32]"`

*Filipp Frizzy aka filipp.s.frizzy@gmail.com*
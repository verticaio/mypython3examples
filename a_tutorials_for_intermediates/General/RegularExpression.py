import re


# Compiling Expressions

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),

    if regex.search(text):
        print('found a match!')
    else:
        print('no match')

# Search pattern, store it any variable and find position from store variable
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "%s" in "%s" from %d to %d ("%s")' % \
    (match.re.pattern, match.string, s, e, text[s:e]))



# Search and print
patterns = ['this','that']
text = 'Does this text match the pattern?'

for pattern  in patterns:
	print('Looking for "%s" in "%s" ->' % (pattern, text))

	if re.search(pattern,text):
		print('Found')
	else:
		print('Not Found')



### Match only email and entered email
str1="[a-z]+@[a-z]+\.[a-z]+"
str2="[a-z0-9]+@[a-z]+\.[a-z]+"
str3="[a-z0-9A-Z]+@[a-z]+\.[a-z]+"
str4="[a-z0-9A-Z]+@[a-z]+\.(net|com|az|)"

# Email Match 
email_re="^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
#URL
url='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
# Phone Number
phone = '(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'



s1='sssA23.mammadov9A@gmail.com'
s2='liran#devarea.com'

c = re.match(str4, email_re)
if c:
    print (f"{s1} : yeah, it is email address")
else:
    print (f"{s1} : no, it is not email address")

print("\n")

### Search in text based on regular expression. For example if we want to find a sentence starting with ‘hello’ or ‘bye’ and ending with ‘day’ or ‘month’
str = 'welcome and hello all, have a good day'
 
m = re.search(r"(hello|bye).*(day|month)", str)
if m:
    print('Matched',m.groups())
    print('Start index', m.start())
    print('End index', m.end())


### Regular expression substitution, For example  we want to find all the numbers in the text and replace it with *
str = 'string with456 some111 888 numbers'
txt = re.sub('[0-9]+', '*', str)
print(txt)



### Splitting a string, yeni stringdeki reqemleri gosterme

str = 'string with456 some111 888 numbers'
txt = re.split('[0-9]+',str)
print(txt)

# yeni kvadrat moterizeler icherisinde gosterilenleri gosterme
str = 'str,in;g wi,th*456 so#me1;11 88$8 numbers'
txt = re.split('[,;*#$]',str)
print(txt)



### Shorcuts, Also you can use specific shotcuts for processing
# \d - digit
# \D - Not digit
# \w – word
# \W – not word
# \s – white space
# \S – not white space


str = 'string with456 some111 888 numbers'
txt = re.split('\d+',str)
print(txt)

### Find all regular on text 
str = 'string with456 some111 888 numbers'
txt = re.findall('[0-9]+', str)
print(txt)
# output:
# ['456', '111', '888']


# Read text and iterate findable objects 	
str = 'string with456 some111 888 numbers'
for m in re.finditer('[0-9]+', str):
    print(m)

###Compiling a regular expression, If you are using a regular expression in a loop , for example while reading lines from a file it is better to compile it for performance :
reobj = re.compile (r"[0-9]+")
for line in myfile:
    m = reobj.match(line)
    if m:
        print(m.string[m.start():m.end()])

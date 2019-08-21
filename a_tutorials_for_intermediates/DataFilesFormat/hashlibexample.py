import hashlib

print(hashlib.algorithms_available)
print('\n')
print(hashlib.algorithms_guaranteed)

print(b'Hello World')
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())


### OR from input

mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())
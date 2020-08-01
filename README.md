## File Encryptor 

Encrypt-Decrypt <i>**any file**</i>

### Working

The program takes all the bits of the file in an array, and then applies a XOR operation with a key.

<b>Example of XOR operation and how this works<b>
```
a = 10 	# a represents the bits of the file you wanna encrypt
key = 27 	# Any positive integer between 0 to 255
a = a ^ key 	#Applying XOR operation between a and the key, this encrypts the file
print(a) 	#a = 17
a = a ^ key 	#Applying XOR operation between a and the key again decrypts the file
print(a) 	#a = 10

```
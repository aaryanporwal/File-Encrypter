## File Encryptor 🔐

Encrypt-Decrypt <i>**any file**</i>.

### Working

The program takes all the bits of the file in an array, and then applies a XOR operation with a key to encrypt it.
To decrypt it, it applies the XOR operation with the same key to get back the file.

<b>Example of XOR operation and how this works</b>b>

```python
a = 10 # a represents the bits of the file you wanna encrypt
key = 27 # Any positive integer between 0 to 255
a = a ^ key #Applying XOR operation between a and the key, this encrypts the file
print(a) #a = 17
a = a ^ key #Applying XOR operation between a and the key again decrypts the file
print(a) #a = 10
```

### How to encrypt🔒?
1.  Clone the repo in your system, head over to cryptocode.py and replace "subject.png" with name of any file you want (keep it in the same folder) in quotes.

2.  Replace "encrypted_subject.png" with any name. (This will be your encrypted file)

3.  Now run the code in your IDE or run in terminal/cmd:
```bash
cd File-Encrypter
python3 cryptocode.py
```
4. In your file browser you can now see the encrypted file!

### How to decrypt🔓?
1.  Open the cryptocode.py file and in the first line replace "subject.png" with the encrypted file name.

2.  Replace name of your encrypted file in the 7th line to any name. (this will be your decrypted file)

3.  That's it! Just run cryptocode.py and you'll see the decrypted file in your folder! 🥳

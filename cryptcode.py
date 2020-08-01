fo = open("subject.png","rb") #rb reads binary
image = fo.read()
image = bytearray(image)
key = 48 # Valuws accepted bw 0 - 255
for index, value in enumerate(image): 
	image[index] = value ^ key # ^ is a XOR operator
fo = open("encrypted_subject.png","wb")
fo.write(image)
fo.close()
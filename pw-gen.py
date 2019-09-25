import random
 
strng = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlength = 10
pw =  "".join(random.sample(strng,passlength ))
print(pw)

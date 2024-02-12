import random
znaki=int(input("Z ile znaków ma się składać towje hasło?"))
p=''
x=('+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
for i in range(znaki):
    p+=random.choice(x)
print (p)

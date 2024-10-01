import random
import string

length = 3
chars = string.ascii_letters

rs1 = ''.join(random.choice(chars) for i in range(length))
rs2 = ''.join(random.choice(chars) for i in range(length))

message = input("Your Message Please: ")
c_d = input("Coding or Decoding: ")
words = message.split(" ")

if c_d == "1":
    coding = True
else:
    coding = False

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            newmess = rs1 + word[1:] + word[0] + rs2
            nwords.append(newmess)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            newmess = word[-4] + word[3:-4]
            nwords.append(newmess)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

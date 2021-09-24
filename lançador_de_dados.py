import random
dado = input("Qual dado? (d4, d6, d8, d10, d12, d20 ou d100)  ")
quantidade = int(input("quantos dados?   "))
randomlist = []
if dado == "d4":
    for i in range (0,quantidade):
        n = random.randint(1,4)
        randomlist.append(n)
    print (randomlist)
elif dado == "d6": 
    for i in range (0,quantidade):
        n = random.randint(1,6)
        randomlist.append(n)
    print (randomlist)
elif dado == "d8": 
    for i in range (0,quantidade):
        n = random.randint(1,8)
        randomlist.append(n)
    print (randomlist)
elif dado == "d10": 
    for i in range (0,quantidade):
        n = random.randint(1,10)
        randomlist.append(n)
    print (randomlist)
elif dado == "d12": 
    for i in range (0,quantidade):
        n = random.randint(1,12)
        randomlist.append(n)
    print (randomlist)
elif dado == "d20": 
    for i in range (0,quantidade):
        n = random.randint(1,20)
        randomlist.append(n)
    print (randomlist)
elif dado == "d100": 
    for i in range (0,quantidade):
        n = random.randint(1,100)
        randomlist.append(n)
    print (randomlist)
else:
    print ("digite um dado valido")
#medidas com precisão o bastante pra um rpg
vi = input("qual a medida inicial m-metros q-quadrados f-feats ")
mi = float(input("quantos? "))
va = input("pra qual? (m, q ou f) ")
if vi == "m":
    if va == "q":
        vf = mi / 1.5
        print ("são {} {}".format(vf,va))
    elif va == "f":
        vm = mi / 1.5
        vf = vm * 5
        print ("são {} {}".format(vf,va)) 
    else:
        print("digite corretamente")
elif vi == "q":
    if va == "m":
        vf = mi * 1.5
        print ("são {} {}".format(vf,va))
    elif va == "f":
        vf = mi * 5
        print ("são {} {}".format(vf,va)) 
    else:
        print("digite corretamente")
elif vi == "f":
    if va == "m":
        vm = mi / 5
        vf = vm * 1.5
        print ("são {} {}".format(vf,va)) 
    elif va == "q":
        vf = mi / 5
        print ("são {} {}".format(vf,va)) 
    else:
        print("digite corretamente")
else:
        print("digite corretamente")
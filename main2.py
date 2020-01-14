name = input("What is your name? ")
flavor = input("What is your favorite flavor of ice cream? ")
th = int(input("What is the tub Height? "))
td = float(input("What is the tub Diamater? "))
sd = int(input("What is the scoop Diameter? "))


tr = (td/2) #tubRadius 

tv = (th*(tr*tr)*3.14159265359) #tubVolume

sr = (sd/2) #scoopRadius

scoop = (4/3*3.14159265359*sr*sr*sr)

ss = (tv/scoop) #servingSize


print ("Name:",name,)
print ("Flavor:",flavor,)
print("Tub Volume",tv,)
print("Scoop Volume:",scoop,)
print("Serving Size:",ss,)
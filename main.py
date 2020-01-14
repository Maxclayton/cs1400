name = input("What is your name? ")
flavor = input("What is your favorite flavor of ice cream? ")

th = 11 #tubHeight
tr = 4.75 #tubRadius 

tv = (th*(tr*tr)*3.14159265359) #tubVolume


sv = 4.18879 #scoopVolume

ss = (tv/sv) #servingSize



print ("Name:",name,)
print ("Flavor:",flavor,)
print("Tub Volume",tv,)
print("Scoop Volume:",sv,)
print("Serving Size:",ss,)
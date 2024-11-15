



ask=str(input("Hello,What do you wanna calculate today:  ?"))


if ask == "Resistance"  :
    ask2=int(input("Specify current: "))
    ask3=int(input("Specify vltage: "))
    resist=(ask3/ask2)



    print(resist)

if ask == "voltage" :
    ask3=int(input("Specify resistance: "))
    ask4=int(input("Specify current: "))

    voltify=(ask4*ask3)
    
    print(voltify)


if ask == "Current"  :
    ask5=int(input("Specify voltage:  "))
    ask6=int(input("Specify Resistance: "))
    current=(ask5/ask6)

    print(current)



if ask == "Series Resistance":
    ask7=int(input("R1 ? : "))
    ask8=int(input("R2 ?: "))
    SR=(ask7 + ask8)
    
    print(SR)


if ask == "Parallel Resistance":
    ask9=int(input("R1?: "))
    ask10=int(input("R2?: "))
    PR=(1/ask9 + 1/ask10)


    print(PR)
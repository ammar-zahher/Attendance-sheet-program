#system for staff attendance
print("names of the participating members_in_the journey:")
for members in ["Ammar","Muhammed","Yasser","Hesham","Raghad","Khadija"]:
    print(".",members)
print("THAT IS ALL NAMES")
while True:
    nam0e=input("what is your name?")
    name1=nam0e.strip()
    name=name1.lower()
    if name=="ammar":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==50397:
                    print("greeat,you are ammar.")
                    print("this is your code:(3864)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
    if name=="muhammed":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==36904:
                    print("greeat,you are muhammed.")
                    print("this is your code:(4682)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
                        
    if name=="yasser":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==4725:
                    print("greeat,you are yasser.")
                    print("this is your code:(29737)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
    if name=="hesham":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==8735:
                    print("greeat,you are hesham.")
                    print("this is your code:(4358)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
    if name=="raghad":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==8346:
                    print("greeat,you are raghad.")
                    print("this is your code:(2579)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
    elif name=="khadija":
        while True:
            try:
                pin=input("what is your code")
                pin=pin.strip()
                pin=int(pin)
                if pin==1679:
                    print("greeat,you are khadija.")
                    print("this is your code:(3047)")
                    print("the journey stats sfter 20 days")
                    break
                else:
                    print("wrong pin..try agin")
                    continue
            except:
                print("you can`t add letter.")
                print("try agin:")
    else:
        print("your name are not in the lest.")
        continue
print("I hope you will enjoy")

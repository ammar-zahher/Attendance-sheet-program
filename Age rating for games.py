print("hello,how are you")
try:
    age=int(input("how old are you: "))
    print("if you want to play fifa enter 1 .")
    print("if you want to play grand 5 enter 2 .")
    print("if you want to play call of duty enter 3 .")
    try:
        disire=int(input("which game you want to play"))
        if age <18 :
            if disire==1 :
                print("yes,you can play fifa.")
            if disire==2 :
                print("you can`t play grand 5.")
            elif disire==3 :
                print("you can`t play call of duty.")
            else :
                print("we don`t know about games aren`t_in the options.")
        if age <21 :
             if disire==1:
                print("yes,you can play fifa.")
             if disire==2:
                print("you can play grand 5.")
             elif disire==3:
                print("you can play call of duty.")
             else :
                print("we don`t know about games aren`t_in the options.")
        if age>21:
             if disire==1:
                print("yes,you can play fifa.")
             if disire==2:
                print("you can play grand 5.")
             elif disire==3:
                print("you can play call of duty.")
             else :
                print("we don`t know about games aren`t_in the options.")
    except:
        print("we told you.enter the number of the game you want to play")
except:
    print("you can`t enter letters")
 

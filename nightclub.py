name=input("please enter you name:")

age=input("please enter your age:")
#print("data type is", type(age))
if age.isdigit():
    print("Thank you!")
    if int(age) < 21:
        print("Sorry", name + "!""your too young!!Better luck next time")
    else:
        print("welcome abroad", name + "!!!")
else:
    print("enter your age in numerical values!!!!")
    age = input("please enter your age:")
    if int(age) < 21:
        print("Sorry", name + "!""your too young!!Better luck next time")
    else:
        print("welcome abroad", name + "!!!")
#else:

        #break

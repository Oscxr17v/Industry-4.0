name=input("What is your name?")   
majo=input("What´s your career?")
print("Hi!!", name, "from the career of ",majo)
print("What is your average?")
ave = float(input())
if ave>=8:
    print("You have ",ave, "average.You are a genius.")    
    print("So, ", name)
    answer=input("Do you want to have a job right now?(Y/N)")
    if answer == 'y':
        print("Let's start. Show up tomorrow in building number 2.")
    if answer == 'n':
        print("Well, maybe for the next time :(")
else:
    print("You HAVE ",ave, "average. You can do it better")
    print("So, ",name)
    print("You can´t start a job")
    
        
age=int(input("enter you are age"))
if age<18:
    print("you are a minor")
elif age>=18 and age<=60:
    print("you are an adult")    
elif age>60 and age<=100:
    print("you are a senior")
else:
    print("sorry, you are death")    

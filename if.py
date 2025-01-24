#nested if
num=int(input("Enter a Number:"))
if (num>20)and(num<100):
    print("This Block Is Executed Successfully")
    if(num==60)or(num==100):
        print("This block Is Almost successfully Correct")
    else:
        print("Second block is not  correct!")
#sample task in nested if
name=(input("Enter your name:"))
print("welcome to voting section",name)
age=int(input("Enter your age:"))
rule=(input("do you have a voter id:"))
if age>18:
    print("you can eligible for voting!")
    if (rule=="yes")or(rule=="Yes")or(rule=="YES"):
        print("you go to voting section")
    else:
        print("if you can eligible!but you don't have voter id")
else:
 print("if you not eligible for  voting,thank you!")

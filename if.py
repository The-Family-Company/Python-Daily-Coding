#nested if
num=int(input("Enter a Number:"))
if (num>50)and(num<80):
    print("This Block Is Executed Successfully")
    if(num==60)or(num==100):
        print("This block Is Almost successfully Correct")
    else:
        print("Second block is not  correct!")
#sample task in nested if
        print("Voting section,welcome")
name=(input("Enter your name:"))
age=int(input("Enter your age:"))
rule=(input("do you have a voter id:"))
if age>18:
    print("you can eligible for voting!")
    if rule=="yes"and rule=="no":
        print("you go to voting section")
    else:
        print("if you can eligible!but you don't have voter id")
else:
 print("if you not eligible for  voting,thank you!")
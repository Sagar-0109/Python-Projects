print('''
      +ADD
      -Subtract
      *Multiply
      /Divide
      ''')


num1=int(input("Enter the value 1 : "))
num2=int(input("Enter the value 2 : "))
opr=input("Enter the opr...")
if opr =="+":
    print(num1+num2)

elif opr=="-":
    print(num1-num2)

elif opr=="*":
    print(num1*num2)        


elif opr=="/":
    print(num1/num2)

elif opr=="%":
    print(num1%num2)    


else:
    print("Please Enter an Valid Input")    

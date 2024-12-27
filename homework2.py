balance=1000
print("welcome to my ATM")

choice=input("choose an option\n 1.check balance\n 2.deposit\n 3.withdraw\n 4.exit")

if choice == '1':
    print(f"your balance is:(balance)")
elif choice =='2':
    amount= input("enter the amount to deposit")
    balance= balance + int(amount)
    print("your new balance is ",balance)
elif choice =='3':
    amount= int(input("enter the amount to withdraw"))
    if balance< amount:
      print("not enough balance")
    else:
     print(f"(amount)is withdrawn from you account")
    balance= balance-amount
    print("your neew balance is ",balance)
    
elif choice =='4':
    print("thank you for visiting")
else:
    print("invalid choise! please enter the choice from 1-4")
        
    
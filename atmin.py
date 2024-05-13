import time
user_Id=input("Enter the user_Id:")

pin = int(input("Enter 4 digit pin number :"))
amount=10000.34
if pin==1234 :
    time.sleep(0.5)
while True:
    print("**********MENU**********")
    print("1.TRANSACTIN HISTORY")
    print("2.DEPOSIT")
    print("3.WITHDRAWY")
    print("4.TRANSFER")
    print("5.QUIT")
    time.sleep(0.5)

    try :
       option =int(input("Select an Option to be performed :"))
    except:
        print("please choose the valid option :")


    if option==1:
        print("view transcation history")
        customer_details1=["Aisha",76834798922,"13.09.2023",1500]
        customer_details2=["Stella",67809833209,"19.12.2023",20000]
        customer_details3=["Mani",756342878423,"29.01.2024",100]
        customer_details4=["krishna",5667382788932,"20.05.2024",10000]
        print(customer_details1 )
        print(customer_details2 )
        print(customer_details3 )
        print(customer_details4 )
        
        

        
    elif option ==2:

     deposit_amount=int(input("Enter the Deposit Amount :"))
     amount=amount+deposit_amount
     time.sleep(0.5)
     print("Your Amount is successfully deposited") 
     time.sleep(0.5)
     print("YOUR BALANCE AMOUNT IS AFTER DEPOSITED",amount)
    
     
    elif option==3:
        withdraw_amount=int(input("Enter the Withdrawl Amount :"))
        time.sleep(0.5)
        if amount < withdraw_amount :
          print("SORRY! YOU HAVE INSUFFICIENT FUND")
          time.sleep(0.5)
      
        
        else :   
         amount=amount-withdraw_amount   
         print("YOUR BALANCE AMOUNT IS AFTER WITHDRAWL",amount)
         time.sleep(0.5)
        
    elif option==4:
     account_no =int(input("Enter the  Account number :"))
     customer_name=input("Enter the name :")
     ifcs_code=int(input("Enter your IFCS code :"))
     mobile_number=int(input("Enter the mobile number :"))
     pin=int(input("enter your pin :"))
     transfer_amt=int(input("Enter the transfer amount :"))
     time.sleep(1)
     print("YOUR AMOUNT WILL BE TRANSFER!!!!")

     
    elif option==5:
     print("THANK YOU FOR USING THE ATM.GoodBye!")
    else:
     print("Invalid choice.Please try again")
     time.sleep(0.5)
else:
     print("you entered the wrong pin number!...try again")


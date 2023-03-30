#Take two number from user to compare  
while True:                   
 num1 = int(input("Enter first number: "))      
 num2 = int(input("Enter second number: ")) 
 #Compare both the number 
 if num1 >= num2:   
     pass
     if num1 == num2:    
         print("Both numbers are equal.") 
         pass      
     else:  
         print("First number is greater than the second number.")
         pass
 else:   
   print("Second number is greater than the First number.")
   pass
    
 conti= input("Would you like to continue? (yes/no): ")
 pass
 if conti == "yes":
  continue
 if conti == "no":
        break
 else:
        print("Invalid Input, please try again.")
        continue
     
 
     

#Start Code
print ("What is your name?") 
username= input ("Username: ")
print ("Alright, Sir/Maam", username )
#About
while True:
 print ("This is a code/program made by MD Affan, a senior python developer, to find the hypotenuse of a right-angled triangle, also known as the Pythagorean Theorem") 
 print ("Please do not add anything else other than numbers in the calculation!")
 start= input ("Would you like to start? (yes/no) : ")
 if start == "yes":
    pass
 elif start == "no":
    break
 else:
    pass
    print('Invalid Input, please try again!')
    continue

 a= float(input ("Give a: "))
 b= float(input ("Give b: "))
 ab= a ** 2 
 abi= 5
 abii= 6
 c= (ab-5*b+abii)
 print (a, "** 2 - 5 X", b, "+ 6= ", c )
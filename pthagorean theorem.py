#Start Code
print ("What is your name?") 
username= input ("Username: ")
print ("Alright, Sir/Maam", username )
#About
print ("This is a code/program made by MD Affan, a senior python developer, to find the hypotenuse of a right-angled triangle, also known as the Pythagorean Theorem") 
print ("Please do not add anything else other than numbers in the calculation!")
input ("Would you like to continue? : ")
Yes= True
No= False
a = float(input("Give side a: "))
b = float(input("Give side b: "))
c = (a ** 2 + b ** 2) 
hypo= c ** (1/2)
print (f"The length of the hypotenuse c is {hypo}")
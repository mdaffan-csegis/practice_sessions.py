while True:
    ai= input ("Are you a bot? (yes/no): ")
    if ai == "yes":
       aichat= input ("That's so cool, robot! Would you like to eat now? ")
       if aichat == "yes":
        break
       if aichat == "no":
        pass
        print ("right")
        break
    if ai == "no": 
      print ("Humans deny")
    else: 
      print("Invalid Input", ai) 





     
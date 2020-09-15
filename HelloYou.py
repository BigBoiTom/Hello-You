while True:

 import sys

 print ("Hello You! Ik ben Tomas")
 print ("Wie ben jij?")

 name = input("Voer hier je naam in: ")
 print ("Hello " + name)

 import datetime

 x = datetime.datetime.now()

 print("De datum en tijd is ") 
 print(x)

 while True:

  restart = input(name + " wil jij dit programma nog een keer doen?" + "Type Y/N: ")


  if restart == "Y" or restart == "y":
    break
    continue
 
 
  elif restart == "N" or restart == "n":
   print ("Script Ending. Goodbye.")
   quit()
  

  else:
   print ("Invalid input.")
   continue
 
 

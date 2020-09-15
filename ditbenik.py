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
  print("Weet jij waar ik woon?")
  print("A: Alkmaar")
  print("B: Den Helder")
  print("C: Amsterdam")
 
  questionone = input("Type A/B/C: ")

  if questionone == "A" or questionone == "a":
   print("Dit is niet correct!")
   break
   continue

  elif questionone == "B" or questionone == "b":
   print("Dit is juist!")
   break 
   continue

  elif questionone == "C" or questionone == "c":
   print("Fout! Maar ik zit hier wel in Amsterdam op school!")
   break
   continue
  
  else:
   print("Dit is geen A/B of C!")
   continue


 while True:

  print("Weet jij hoe oud ik ben?")
  print("A: 18 jaar")
  print("B: 20 jaar")
  print("C: 16 jaar")

  questiontwo = input("Type A/B/C: ")

  if questiontwo == "A" or questiontwo == "a":
   print("Dat klopt!")
   break 
   continue

  elif questiontwo == "B" or questiontwo == "b":
   print("Nee dat is niet correct!")
   break
   continue

  elif questiontwo == "C" or questiontwo == "c":
   print("Niet juist!")
   break
   continue

  else:
   print("Typ alsjeblieft een A, B of een C!")
   continue

 while True:

  print("Wat is mijn hobby?")
  print("A: Gamen")
  print("B: Muziek")
  print("C: Sport")

  questionthree = input("Type A/B/C: ")

  if questionthree == "A" or questionthree == "a":
   print("Correct en tevens juist!")
   break
   continue

  elif questionthree == "B" or questionthree == "b":
   print("Dit is ook een hobby maar niet het juiste antwoord!")
   break
   continue

  elif questionthree == "C" or questionthree == "c":
   print("Nee, gewoon Nee!")
   break
   continue
 
  else:
   print("Wat begrijp je niet aan A, B of C?")
   continue

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

  
 
 

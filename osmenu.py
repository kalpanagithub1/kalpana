import os 
import pttsx3
print("welcome :)")
print()
pyttsx3.speak("welcome")
print()
print("to go to menu bar : enter 1")
print("to go wiyh your own choice : enter 2")
print("to close the menu : enter 3")
print()
print("type", end=":")
u = input()
while True:
 if (("exit in x") or("terminate in x") or ("not in x") or ("dont in x")):
       print("good day")
       break
 elif("1" in u):
     print("menu bar for user: ")
     print()
     print("to terminate this : enter 0 ")
     print()
     print("to open chrome browser: enter 1")
     print("to open texteditor: enter 2") 
     print("to open media player: enter 3")
     print("to open calculator: enter 4")
     print("to create folder: enter 5")
     print("to open whatsapp: enter 6")
 m = input()
 if("0" m):
 print("good day")
 break
 elif("1" in m):
   print("for chrome browser type chrome")
   print("Type", end:"=")
   b = input()
   os.system(b)
  elif("2 in m"):
   print("for notepad type notepad")
   print("Type",end:"=")
   n = input()
   os.system(n)
   elif("3 in m"):
   print("for windows mediaplayer type wmp")
   print("Type", end:"=")
   w = input()
   os.system(w)
   elif("4 in m"):
   print("for calculator type calc")
   print("Type",end:"=")
   c = input()
   os.system(c)
   elif("5 in m"):
   print("name that u wuold like to give to new folder")
   f=input()
   os.system("mkdir " +f)
   print("folder created")
   elif("6 in m")
   os.system("Whatsapp")
elif("3 in u"):
   print("good day")
   pyttsx3.spaek("good day")
   break
elif("2" in u)
  while True:
   print("welcome")
   print()
   pyttsx3.speak("what can i do for u")
   print()
   print("if u want to terminate type exit")
   print()
   print("Type yr requirements",end=":")
   x = input()
   pyttsx3.speak(x)
   if((("run" in x) or ("execute" in x) or ("open" in x)) and (("notepad" in x) or ("texteditor" in x))):
     os.system("notepad")
    if((("run" in x) or ("execute" in x) or ("open" in x)) and (("calculator" in x) or ("calc" in x))):
     os.system("calc") 
   elif((("run" in x) or ("execute" in x) or ("open" in x)) and (("chrome" in x) or ("chromebrowser" in x))):
     os.system("chrome")
   elif((("run" in x) or ("execute" in x) or ("open" in x)) and (("vlc" in x) or ("windows media player" in x)):
     os.system("vlc")
   elif((("run" in x) or ("execute" in x) or ("open" in x)) and ("perform" in x) and (("chrome" in x) or ("browser" in x))):
     print("which site u wanna open in chrome", end=":")
     site = input()
     os.system("chrome www."+site".com")
   elif((("make" in x) or ("create" in x) or ("mkdir" in x)) and (("directory" in x) or ("dir" in x) or ("make directory" in x) or ("make a folder" in x))):
     print("name that u would like to give to the folder", end=":")
     fname = input()
     os.system("mkdir "+fname)
   elif(("exit in x") or ("terminate" in x) or ("quite" in x) or ("close" in x)):
     break
   else:
     print("the os couldn't find the file specified")
     os.system("vlc")  
   

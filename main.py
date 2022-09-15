import random
import itertools
import threading
import time
import sys
import os
from time import sleep

#saved

                        #Introductions



  #creater: real-life name = (KHAIRULLAH BIN HAROON HASSAN) mostly called kHALULAH 
  
  #this quiz application was made with the help of Mr Zubair with his hard work I appreciate it


  
                      #about myself

# I am Khairallah bin Haroon Hassan u can call me khairu I am 12 years old going to be 13 this quiz is made by me it took 2 months I hope u love it once again thank your to Mr Zubair and to all my teachers and PROFECCER UGAIL thank your for providing with my biggest life opportunities I will never forget this day I hope I get a chance to learn more about  python programming language in thecircle programming class




                         #Quizz 

    #content
#in line [3] there is the count which will count how many questions it will start with 0 and if u get any question right it will add one to it 

#in line [14] it is unused questions

#In line 66 #the greeting used in line [99] to print a greeting for the user

#line 117 is the colour function with gives the typing colour 

#in 121 will ask for your name note: it will not be seen by the creator

#127 will start a while loop

#in 131 it will use a random sentence from the greetings and add it with the name u gave the system and ask if u want to start the quiz 

#in 136 it will make a clear() command 

#in 139 it will clear the console 

#in forme lines 142  to 147 it will print "Quiz" in rainbow colour 

#in line 148 it will print a line from 1 side to the end 

#in line 151 it will show the first question 

#in 153 it will show the program the answer for the first question if u get the answer right it will print a show an animation if wrong it won’t count as a correct question and it will print that the answer is wrong in red colour and it will continue with the quiz

# and all the other questions are the same up to q10: 

#after question 10 is done it will give the user  1 extra question if they want in line 557 and on line 558 

#in line 573 it will give your the extra question 

#lastly in line 622 it will show you a calculating  screen and in line 628 it will print how many answers the user got correct 

                                      

  
#dont add quotes in the endding 
count = 0 #refer to line 8

width = os.get_terminal_size().columns#get the center co
questions = ['Is the economy doing well?','Does your family really love you?','Why is there hatred in the world?','Is the Mona Lisa beautiful?','What is the purpose of life?','Who is the best football player ever?','Are you having a good day?','Does this dress make me look fat?']#these cuestyions arent used 


#FONT COLORS
#color or outher's are in #python color in files 
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

#--------------------------------------------
#BACKGROUND COLORS

Background_Black = "\u001b[40m"
Background_Red = "\u001b[41m"
Background_Green = "\u001b[42m"
Background_Yellow = "\u001b[43m"
Background_Blue = "\u001b[44m"
Background_Magenta = "\u001b[45m"
Background_Cyan = "\u001b[46m"
Background_White = "\u001b[47m"
Background_Bright_Black = "\u001b[40;1m"
Background_Bright_Red = "\u001b[41;1m"
Background_Bright_Green = "\u001b[42;1m"
Background_Bright_Yellow = "\u001b[43;1m"
Background_Bright_Blue = "\u001b[44;1m"
Background_Bright_Magenta = "\u001b[45;1m"
Background_Bright_Cyan = "\u001b[46;1m"
Background_Bright_White = "\u001b[47;1m"
##CORRECTIONS

Bold = "\u001b[1m"#Bold
Underline = "\u001b[4m"#Underline
Reversed = "\u001b[7m"#rivers
#--------------------------------------
#THINGS


greetings = [ "Hi nice to meet your " , "Welcome " , "Nice to meat your " , "Good afternoon "] #the greeting used in line [127]

endings = ["Have an nice day","It was nice to see your here"]


#print(Reversed)
done = False  
#LOding screen if u dont want loding screen  deleat forme line-72 to line-86

#this is the firs this u will see wehn u run the code the animation
def animate():
    for c in itertools.cycle(['⚪⚪⚪⚪⚪', '⚫⚪⚪⚪⚪', '⚫⚫⚪⚪⚪', '⚫⚫⚫⚪⚪', '⚫⚫⚫⚫⚪', '⚫⚫⚫⚫⚫']):
        if done:
            break
        sys.stdout.write('\rWe are loding up your questions. ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r""')

t = threading.Thread(target = animate)
t.start()

#long process here
time.sleep(5)#used to be 10
done = True

sleep(0)




def color (question):
  return input(white + question + bright_green)



  
sleep(1)

name = input("Hi we would like to know your name please : ")
print("")


while True:

  start = color(random.choice(greetings) + name + ' do you wish to start the quiz?\n [yes or No]\n = ')
  print("")
  
  if start == 'Yes' or start == 'yes' or start == ' yes' or start == ' Yes':
    width = os.get_terminal_size().columns
    clear = lambda: os.system("clear")
    clear()
    print(red + "                            Q", end = '')
    print(yellow + "U", end = '')
    print(green + "I", end = '')
    print(blue + "Z", end = '')
    print(magenta + "Z")    
    print(Reversed + "")
    print(white + Bold +  '─'*60)
    print("")
    print("")
    Answer1 = color(blue + 'Q1: How many teaths dose an human have  \n' + magenta + 'Answer: ')
    
    if Answer1 == "32" or Answer1 == "32 teaths" or Answer1 == "32 Teaths":
      bar = [#-------------#
      " Correct      ",
      "  Correct     ",
      "   Correct    ",
      "    Correct   ",
      "     Correct  ",
      "      Correct ",
      "     Correct  ",
      "    Correct   ",
      "   Correct    ",
      "  Correct     ",
      " Correct   \n ",
      ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end ="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      count = count + 1
    
      print("")
      
    else:
      print(red + 'wrong answer ')
      print(green + ",32 is the correct answer,")
      print("") 

      
    Answer2 = color(blue + 'Q2: What tissues connect the muscels to the bones?\n '+ magenta + 'Answer: ')
    Answer2 = Answer2.lower()
    if Answer2 == "Tendons" or Answer2 == "tendons":
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ')
      
      
      print(green + ",Tendons is the correct answer,")
      print("")
      
  #wrong
    Answer3 = color(blue + 'Q3: wich year was very first model of iphone released? \n ' + magenta + "Answer: ")
    Answer3 = Answer3.lower()
    if Answer3 == "2007" or Answer3 == " 2007" or Answer3 == "YEAR 2007" or Answer3 == "YEAR2007":
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      count = count + 1
      
      print("")
    else:
      print(red + 'worng asnwer')
      
      
      print(green + ",2007 is the correct answer,")
      print("")
  
    Answer4 = color(blue + 'Q4: Who is soften Called the Father of the computers\n'+ magenta +  'Answer: ')
    Answer4 = Answer4.lower()
    if Answer4 == "CHARLES BABBAGE" or Answer4 == "CHARLESBABBAGE"  or Answer4 == "CHARLES BABBGE " or Answer4 == "charles BABBAGE" or Answer4 == "charlesBABBAGE" or Answer4 == "charles babbage":
  
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      count = count + 1
      
      print("")
    else:
      print(red + 'worng asnwer')
      
      
      print(green + ",CHARLES BABBAGE is the correct answer,")
      print("")
      
    Answer5 = color(blue + 'Q5: What is the name of the perosn who launched "ebay" in back in the 1995\n'+ magenta + 'Answer: ')
    Answer5 = Answer5.lower()
    if Answer5 == "PIERRE OMIDYAR" or Answer5 == "PIERREOMIDYAR" or Answer5 == "PIERREomidyar" or Answer5 == "PIERREomidyar" or Answer5 == "pierre omidyar":
  
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1      
      
      print("")
    else:
      print(red + 'wrong answer ') 
      
      
      print(green + ",PIERRE OMIDYAR is the correct answer,")
      print("")

      
    Answer6 = color(blue + 'Q6: Google, chrome, safari, Fire fox, and explorers are diffrent typys of what?\n'+ magenta + 'Answer: ')
    Answer6 = Answer6.lower()
    if Answer6 == "WEB BROWSERS" or Answer6 == "WEBBROWSERS" or Answer6 == "WEB BROWSERS " or Answer6 == "WEBBROWSERS " or Answer6 == "browser" or Answer6 == "webrowser":
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ') 
      
      
      print(green + ",web browser is the correct answer,")
      print("")
      
    Answer7 = color(blue + 'Q7: what was twitters original name? \n'+ magenta + 'Answer: ')
    Answer7 = Answer7.lower() 
    if Answer7 == "twttr" or Answer7 == " TWTTR" or Answer7 == "TWTTR " or Answer7 == " TWTTR " or Answer7 == " twttr" or Answer7 == "twttr " or Answer7 == " twttr " :
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ') 
        
      print(green + ",Twttr is the correct answer,")
      print("")

    
    Answer8 = color(blue + 'Q8: What part of the atom has no electric charge? \n'+ magenta + 'Answer: ')
    Answer8 = Answer8.lower() 
    if Answer8 == "Neutron " or Answer8 == "NEUTRON" or Answer8 == "Neutron" or Answer8 == " Neutron" or Answer8 == " neutron " or Answer8 == "newtron":
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ') 
        
      print(green + ",Neutron is the correct answer,")
      print("")


    
    Answer9 = color(blue + 'Q9: What is the symbol for potassium?\n '+ magenta + 'Answer: ')
    if Answer9 == "k" or Answer9 == "K" or Answer9 == " k" or Answer9 == " K" or Answer9 == " K " or Answer9 ==  " k ":
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ') 
        
      print(green + ",k is the correct answer,") 
      print("")
      
    Answer10 = color(blue + 'Q10: How many eyes do caterpillars have\n'+ magenta + 'Answer: ')
    if Answer10 == "12" or Answer10 == " 12" or Answer10 == "12 " or Answer10 == " 12 " or Answer10 == "12legs" or Answer10 == "12 LEGS " or Answer10 == " 12 legs": 
      
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
  
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
      
      
  
    else:
      print(red + 'wrong answer ') 
      
      print(green + ",12 is the correct answer,")
      print("")
    
    exstra = input(bright_green + 'Do u want' + magenta + ' 1 ' + bright_green + 'more exstra question ')
    if exstra == "Yes" or exstra == " yes" or exstra == "Yes" or exstra == "yes":
      
      
      
      print(white + "")
    
      
  
    else:
      print('')
      break
        
    
    
    
      print(blue + "Here is your question \n ^-^")
    mcq_answer11 = color(blue + 'Whats the full form of "HTTP" \n \n' + magenta + 'A.'+ blue + ' Hyper Text \n' + magenta + 'B.' + blue + ' Hyper Text transfer Protocol \n' + magenta + 'C. ' + blue + 'HTTs:/ \n\n Answer: ')
    mcq_answer11 = mcq_answer11.lower()
    if mcq_answer11 == 'HyperText transfer Protocol' or mcq_answer11 == ' HyperText transfer Protocol' or mcq_answer11 == 'HyperText transferProtocol' or mcq_answer11 == 'HyperTexttransfer Protocol' or mcq_answer11 == 'HyperTexttransferProtocol' or mcq_answer11 == 'B':
      print(bright_green)
  
      bar = [#-------------#
        " Correct      ",
        "  Correct     ",
        "   Correct    ",
        "    Correct   ",
        "     Correct  ",
        "      Correct ",
        "     Correct  ",
        "    Correct   ",
        "   Correct    ",
        "  Correct     ",
        " Correct   \n ",
        ]
      i = 0
  
      timeout = 2.2   # [seconds]
  
      timeout_start = time.time()
      
      while time.time() < timeout_start + timeout:
          test = 0
          print(bar[i % len(bar)], end="\r")
          time.sleep(.2)
          i += 1
          if test == 5:
            sleep(1)
            break
            test -= 1
      #print(green + Bold +  '─'*20)
      count = count + 1
      
      print("")
    else:
      print(red + 'wrong answer ') 
      break
      print("")
      
  elif start == "No" or start == "no":
    print ("your have chosen not to start the quizz")
    break
  
  else:
    print("invalid answer")
    
  
print(cyan + "Getting your score")

N=12
while True:
  for i in range(N):
     sleep(0.5)
     print(f"{i/N*100:.1f} %", end="\r")
     break
  print("")
  print(bright_magenta + "your score is ".center(width))
  print(cyan + str(count).center(width))
  print(bright_magenta + "──".center(width))
  print(cyan + "11".center(width))
  print("")
  clear = lambda: os.system("clear")
  clear()
  if start == 'No' or start == 'no' or start == ' No' or start == ' no':
    break

  for x in ("Your have finished the quizz succesfully and  your got Total\n " + str(count) +" correct forme all 11 questiosn u did.\n " ):
  	sys.stdout.write(x)
  	sys.stdout.flush()
  	time.sleep(0.02)
  print("")
  break
  if count >= 11:
     print('your got all the questiosn right :)')  
  elif count == 10:
     print('Amazing! Your score is equal to ' + str(count))
  
  elif count <= 2: 
     print('Not so good. That\s ok though! Your score was ' + str(count))
  continue
while True:
    ask = color(blue + 'Do u want info about the creator? \n' )
   
    if ask == "yes" or ask == "Yes":
      print(green + "\n I am khairallah bin haroon hassan u can call me khairu i am 12 years elderly going to be 13 this quiz is made by me it took 2 months i hope u love it once again thank your to mr zubair and to all my teachers and profeccer ugail thank your for providing with my biggest life opportunities i will never forget this day i hope i assist, obtain a chance to learn more about  python programming language in thecircle programming class \n")
      break#last 
      print("")
    else:
      print(red + '')
      clear()
      break
      print("")

#The end 
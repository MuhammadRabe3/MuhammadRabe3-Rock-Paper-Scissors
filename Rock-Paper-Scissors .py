#ask the user to enter his value.
#ask the computer to enter its random value.
#check if the user value == r or p or s and the pc == s or r or p relatevely
# if yes ..user won
# if no the pc won 
# if pc==user ===> it will be tie 
# mohammad Rabea 

import random

values=['r', 's', 'p']


while True:
     uservalue=input("it is your turn, Enter Your value (r=> rock, p=> paper, s=> scisor) \n").lower()
     if uservalue in values:
          computervalue=random.choice(values)
          print (f"the user entered value is :{uservalue}")
          print(f"the pc entered value is : {computervalue}" )
          if uservalue==computervalue:
               print("it is tie! ")

          elif (uservalue=='r' and computervalue=='s') or (uservalue=='p' and computervalue=='r') or (uservalue=='s' and computervalue=='p'):
               print("you Won, That is great!!")
          else:
               print("ohh, you lost") 
          
     else:
          print("please enter valid value!")
   
 
 #end

import random

values=['r', 's', 'p']


while True:
     uservalue=input("it is your turn, Enter Your value (r=> rock, p=> paper, s=> Scissors) \n").lower()
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
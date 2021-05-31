import random

def shuffle(string):   #Function to shuffle the obtained password
  tempList = list(string)
  random.shuffle(tempList)  #random.shuffle shuffles the lust randomly
  return ''.join(tempList)

u_case1=chr(random.randint(65,90))    #Generating a random uppercase ASCII value using chr and randint method
u_case2=chr(random.randint(65,90))
l_case1=chr(random.randint(97,122))
l_case2=chr(random.randint(97,122))
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))
symb1=chr(random.randint(33,47))
symb2=chr(random.randint(33,47))
password = u_case1+u_case2+l_case1+l_case2+num1+num2+symb1+symb2 #adding every generated character
password = shuffle(password)

print(f"The password generated is {password}")

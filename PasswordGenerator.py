import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

u_case1=chr(random.randint(65,90))
u_case2=chr(random.randint(65,90))
l_case1=chr(random.randint(97,122))
l_case2=chr(random.randint(97,122))
num1=chr(random.randint(48,57))
num2=chr(random.randint(48,57))
symb1=chr(random.randint(33,47))
symb2=chr(random.randint(33,47))
password = u_case1+u_case2+l_case1+l_case2+num1+num2+symb1+symb2
password = shuffle(password)

print(password)

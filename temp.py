import random
choice1 = ('R', 'P', 'S')

def get_key(val, u, p):
    dict1 = {"you": u, "PC": p}
    for key, value in dict1.items():
        if val == value:
            print(f"Pc's choice is {p}. So, the Winner is {key}")

def rps(u, p):
    dict2={"RS":"SR","SP":"PS","PR":"RP"}
    up = u + p
    for key,value in dict2.items():
        if up == key or up == value:
            get_key(key[0], u, p)

while True:
    PcChoice = choice1[random.randint(0, 2)]
    UserChoice = (input("Enter Your Choice (R/P/S)")).upper()
    if PcChoice == UserChoice:
        print("Tie")
    else:
        rps(UserChoice, PcChoice)
    choice = input("Do you want to play again(Y/N)").upper()
    if choice != "Y":
        break

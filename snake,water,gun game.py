import random

def gamewin(comp,you):
    if comp == you:
        return None#if both chooses the same it will bw a tie
    
    #check all possibilities when computer choose s
    if comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    #check all possibilities when computer choose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #check all possibilities when computer choose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# randNo=random.randint(1,2)
# print(randNo)

print("Comp Turn: Snake(s) water(w) or gun(g)?")

randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("your Turn: Snake(s) water(w) or gun(g)?")

a=gamewin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")
if a== None:
    print ("the game is a tie")
elif a:
    print("you win")
else:
    print("you lose")
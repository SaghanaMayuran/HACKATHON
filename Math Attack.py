import random

user_name = ""
computer_health = 100
computer_action = 0
user_health = 100
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
answer = 0
user_answer = 0
user_action = ""
user_heal = 0
damage_to_attack = 0
amount_to_heal = 0

MAXIMUM_DAMAGE= 15
MINIMUM_DAMAGE = 5

MINIMUM_HEAL= 5
MAXIMUM_HEAL = 15

def computer_attack_hard():
    global user_health
    global damage_to_attack
    damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
    user_health = user_health - damage_to_attack
def computer_heal_hard():
     global computer_health
     global amount_to_heal
     amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
     computer_health = computer_health + amount_to_heal
    
def battle_hard():
    global user_action
    global user_health
    global computer_health
    global computer_action
    global damage_to_attack
    global amount_to_heal
    while True:
        user_action = ""
        while user_action != "attack" and user_action != "heal" and user_health >=0 and computer_health >= 0:
            user_action = input("Would you like to attack or heal: ")
            if user_action == "attack" :
                damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
                computer_health = computer_health - damage_to_attack
                print("Now the computer has" , computer_health , "health")
            elif user_action == "heal":
                amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
                user_health = user_health + amount_to_heal
                print("Now you have" , user_health , "amount of health")
        computer_action = random.randint (0, 1)
        if computer_action == 0:
            computer_attack_hard()
        elif computer_action == 1:
            computer_heal_hard()
        if user_health <= 0:
            print("You lost!")
            exit()
        elif computer_health <= 0:
            print("You won!")
            exit()





def hard():
    global num_1,num_2,num_3,num_4,num_5,num_6
    global answer
    global user_answer
    global user_health
    global user_action
    global computer_health
    while True:
        num_1 = random.randint(1,5)
        num_2 = random.randint(1,5)
        num_3 = random.randint(1,5)
        num_4 = random.randint(1,5)
        equation = random.randint(1,7)
        if equation == 1:
            num_5 = num_1+num_2
            num_6 = num_3*num_4
            answer = num_5 + num_6
            user_answer = int(input("What is " + str(num_1)+" + "+str(num_2)+" + "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    print("The computer gained health and now has " + str(computer_health) + " health.")
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
            
        elif equation == 2:
            num_5 = num_1-num_2
            num_6 = num_3*num_4
            answer = num_5 + num_6
            user_answer = int(input("What is " + str(num_1)+" - "+str(num_2)+" + "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
            
        elif equation == 3:
            num_5 = num_1*num_2
            num_6 = num_3*num_4
            answer = num_5 + num_6
            user_answer = int(input("What is " + str(num_1)+" x "+str(num_2)+" + "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                user_action = ""
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
        elif equation == 4:
            num_5 = num_1 + num_2
            num_6 = num_3*num_4
            answer = num_5 - num_6
            user_answer = int(input("What is " + str(num_1)+" + "+str(num_2)+" - "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
                        
        elif equation == 5:
            num_5 = num_1 - num_2
            num_6 = num_3*num_4
            answer = num_5 - num_6
            user_answer = int(input("What is " + str(num_1)+" - "+str(num_2)+" - "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
        elif equation == 6:
            num_5 = num_1 * num_2
            num_6 = num_3*num_4
            answer = num_5 - num_6
            user_answer = int(input("What is " + str(num_1)+" x "+str(num_2)+" - "+str(num_3)+" x "+str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()
        elif equation == 7:
            num_5 = num_1 * num_2
            num_6 = num_3*num_4
            answer = num_5 * num_6
            user_answer = int(input("What is "+ str(num_1)+" x "+ str(num_2)+" x " + str(num_3)+" x "+ str(num_4)+" ? "))
            if user_answer == answer:
                user_health = user_health + random.randint(11, 15)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    
                    elif user_action == "go to the battle":
                        battle_hard()
            else:
                computer_health = computer_health + random.randint(11, 15)
                while user_action != "try again" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the battle":
                        battle_hard()


def computer_attack_medium():
    global user_health
    global damage_to_attack
    damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
    user_health = user_health - damage_to_attack
def computer_heal_medium():
     global computer_health
     global amount_to_heal
     amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
     computer_health = computer_health + amount_to_heal
    
def battle_medium():
    global user_action
    global user_health
    global computer_health
    global computer_action
    global damage_to_attack
    global amount_to_heal
    while True:
        user_action = ""
        while user_action != "attack" and user_action != "heal":
            user_action = input("Would you like to attack or heal: ")
            if user_action == "attack" :
                damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
                computer_health = computer_health - damage_to_attack
                print("Now the computer has" , computer_health , "health")
            elif user_action == "heal":
                amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
                user_health = user_health + amount_to_heal
                print("Now you have" , user_health , "amount of health")
        computer_action = random.randint (0, 1)
        if computer_action == 0:
            computer_attack_medium()
        elif computer_action == 1:
            computer_heal_medium()
        if user_health <= 0:
            print("You lost!")
            exit()
        elif computer_health <= 0:
            print("You won!")
            exit()



def medium():
    global num_1
    global num_2
    global num_3
    global answer
    global user_answer
    global user_health
    global user_action
    global computer_health
    while True:
        num_1 = random.randint(1,5)
        num_2 = random.randint(1,5)
        num_3 = random.randint(1,5)
        equation = random.randint(1,4)
        if equation == 1:
            answer = num_1 - num_2 - num_3
            user_answer = int(input("What is " + str(num_1) + " - " + str(num_2) + " - " + str(num_3) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                user_action = ""
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
            else:
                computer_health = computer_health + random.randint(1, 5)
                print("The computer gained health and now has" , computer_health , "health.")
                user_action = ""
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again, go to the next level, or go to the battle? ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
            
        elif equation == 2:
            answer = num_1 + num_2 + num_3
            user_answer = int(input("What is  " + str(num_1) + " + " + str(num_2) + " + " + str(num_3) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                user_action = ""
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium ()
                
            else:
                computer_health = computer_health + random.randint(1, 5)
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
            
        elif equation == 3:
            answer = num_1 * num_2
            user_answer = int(input("What is " + str(num_1) + " x " + str(num_2) + " x " + str(num_3) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
                        
            else:
                computer_health = computer_health + random.randint(1, 5)
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
                        
        elif equation == 4:
            answer = num_1 * num_2 + num_3
            user_answer = int(input("What is " + str(num_1) + " x " + str(num_2) + " + " + str(num_3) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()
                            
            else:
                computer_health = computer_health + random.randint(1, 5)
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("The computer gained health and now has " + str(computer_health) + " health. Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        hard()
                    elif user_action == "go to the battle":
                        battle_medium()


def computer_attack_easy():
    global user_health
    global damage_to_attack
    damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
    user_health = user_health - damage_to_attack
def computer_heal_easy():
     global computer_health
     global amount_to_heal
     amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
     computer_health = computer_health + amount_to_heal
    
def battle_easy():
    global user_action
    global user_health
    global computer_health
    global computer_action
    global damage_to_attack
    while True:
        user_action = ""
        while user_action != "attack" and user_action != "heal":
            user_action = input("Would you like to attack or heal: ")
            if user_action == "attack" :
                damage_to_attack = random.randint(MINIMUM_DAMAGE,MAXIMUM_DAMAGE)
                computer_health = computer_health - damage_to_attack
                print("Now the computer has" , computer_health , "health")
            elif user_action == "heal":
                amount_to_heal = random.randint(MINIMUM_HEAL, MAXIMUM_HEAL)
                user_health = user_health + amount_to_heal
                print("Now you have" , user_health , "amount of health")
        computer_action = random.randint (0, 1)
        if computer_action == 0:
            computer_attack_easy()
        elif computer_action == 1:
            computer_heal_easy()
        if user_health <= 0:
            print("You lost!")
            exit()
        elif computer_health <= 0:
            print("You won!")
            exit()

        


def easy():
    global num_1
    global num_2
    global answer
    global user_answer
    global user_action
    global user_health
    global computer_health
    while True:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        equation = random.randint(1,3)
        if equation == 1:
            answer = num_1 - num_2
            user_answer = int(input("What is " + str(num_1) + " - " + str(num_2) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
            else:
                computer_health = computer_health + random.randint(1, 5)
                print("The computer gained health and now has" , computer_health , "health.")
                user_action = ""
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
            
                        
        elif equation == 2:
            answer = num_1 + num_2
            user_answer = int(input("What is " + str(num_1) + " + " + str(num_2) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like to try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
                
            else:
                computer_health = computer_health + random.randint(1, 5)
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    print("The computer gained health and now has" , computer_health , "health.")
                    user_action = input("Would you like try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
            
        elif equation == 3:
            answer = num_1 * num_2
            user_answer = int(input("What is " + str(num_1) + " x " + str(num_2) + " equal to: "))
            if user_answer == answer:
                user_health = user_health + random.randint(1, 5)
                print("You are right, now you have" , user_health , "health")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
                            
            else:
                computer_health = computer_health + random.randint(1, 5)
                print("The computer gained health and now has" , computer_health , "health.")
                while user_action != "try again" and user_action != "go to the next level" and user_action != "go to the battle":
                    user_action = input("Would you like try again, go to the next level, or go to the battle: ")
                    if user_action == "try again":
                        print("Okay, answer more questions.")
                    elif user_action == "go to the next level":
                        medium()
                    elif user_action == "go to the battle":
                        battle_easy()
        

            
    
        

print("Welcome to Math Attack! In this game, there are three levels: easy, medium, and hard. You can choose which level, and if you answer correctly you can gain health. Using the health you can attack the computer or heal yourself. You have to defeat the computer by getting the computer's health to zero before your health gets to zero.")
user_action = ""
while user_action != "easy" and user_action != "medium" and user_action != "hard":
    user_action = input("Would you like an easy, medium or hard level: ")
    if user_action == "easy":
        easy()
    elif user_action == "medium":
        medium()
    elif user_action == "hard":
        hard()
    
    
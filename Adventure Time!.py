# Importing Library

import random
from time import sleep

# welcome the player and get their name
print("Welcome to the adventure time game!")
sleep (.2)
print("1.0v")
sleep (1)

name = input("What is your name? ")

# set the initial values
location = "forest"
gold = 50
health = 100
armor = 0


while True:
  # show the player their current status
  print("\n" + name + ", you are in the " + location)
  sleep (.2)
  print("Gold: " + str(gold) + " | Health: " + str(health))
  sleep (.2)

  # get the player's input
  action = input("What would you like to do? [shop/adventure/exit] ")
  sleep (.2)

  # handle the player's input
  if action == "shop":
    # show the player their current gold and health
    print("\nYou have " + str(gold) + " gold.")
    sleep (.2)
    print("Your health is " + str(health) + ".")
    sleep (.2)

    # let the player buy items
    print("\nWhat would you like to buy?")
    sleep (.2)
    print("1. health potion (+25 health) [60 gold]")
    sleep (.2)
    print("2. armor upgrade (+10 armor) [80 gold]")
    sleep (.2)
    print("3. diamond armor upgrade (+25 armor) [100 gold]")
    sleep (.2)
    print("any number = cancel")
    item = input("Enter the number of the item you want to buy: ")
    sleep (.2)

    # handle the player's purchase
    if item == "1":
      if gold >= 60:
        gold -= 60
        health += 25
        print("You bought a health potion. Your health is now " + str(health) + ".")
        sleep (.2)
      else:
        print("You don't have enough gold to buy that.")
        sleep (.2)
    elif item == "2":
      if gold >= 80:
        gold -= 80
        armor += 10
        print("You bought armor. Your armor is now " + str(armor) + ".")
        sleep (.2)
      else:
        print("You don't have enough gold to buy that.")
        sleep (.2)
    elif item == "3":
        if gold >= 100:
          gold -= 100
          armor += 25
          print("You bought diamond armor. Your armor is now " + str(armor) + ".")
          sleep (.2)
        else:
            print("You don't have enough gold to buy that.")
            sleep (.2)
    else:
        print("chose to exit shop")
        sleep (.2)
  elif action == "adventure":
    direction_adv = input("\nIn which direction you want to go? [east/west/nort/south] ")
    sleep (.2)
    if direction_adv == "east":
        print("You chose to go towards east.")
        sleep (.3)

        # "Outcome = 1" is in comment... Remove it from comment to activate cheat and comment outcome = random.radint(1, 2) to Enable cheats!

        # Cheat code enabled
        # outcome = 1

        # No cheat code
        outcome = random.randint(1, 2)

        if outcome == 1:
            print("You successfully completed the adventure.")
            sleep (.2)
            print("You have been awarded with 10 gold.")
            gold += 10
            print(gold)
            if health == 100:
                health = 100
            elif health <= 100:
                health = 100
            elif health <= 90:
                health += 10
            else:
                print("lol")


        else:
            outcome == 2
            print("You were unsuccessful on the adventure.")
            sleep (.2)
            print("You have lost 10 health and 5 gold")
            gold -= 5
            print(gold)
            health -= 5
    elif direction_adv == "west":
      print("You chose to go towards east.")
      sleep (.15)
      outcome = random.randint(1, 2)

      if outcome == 1:
            print("You successfully completed the adventure.")
            sleep (.2)
            print("You have been awarded with 10 gold.")
            gold += 10
            print(gold)
            if health == 100:
                health = 100
            elif health <= 100:
                health = 100
            elif health <= 90:
                health += 10
            else:
                print("lol")
      else:
            outcome == 2
            print("You were unsuccessful on the adventure.")
            sleep (.2)
            print("You have lost 10 health and 5 gold")
            gold -= 5
            print(gold)
            health -= 5

    elif direction_adv == "north":
      print("You chose to go towards north.")
      sleep (.15)
      outcome = random.randint(1, 2)

      if outcome == 1:
            print("You successfully completed the adventure.")
            sleep (.2)
            print("You have been awarded with 10 gold.")
            gold += 10
            print(gold)
            if health == 100:
                health = 100
            elif health <= 100:
                health = 100
            elif health <= 90:
                health += 10
            else:
                print("lol")
      else:
            outcome == 2
            print("You were unsuccessful on the adventure.")
            sleep (.2)
            print("You have lost 10 health and 5 gold")
            gold -= 5
            print(gold)
            health -= 5

    else:
      print("You chose to go towards north.")
      sleep (.15)
      outcome = random.randint(1, 2)

      if outcome == 1:
            print("You successfully completed the adventure.")
            sleep (.2)
            print("You have been awarded with 10 gold.")
            gold += 10
            print(gold)
            if health == 100:
                health = 100
            elif health <= 100:
                health = 100
            elif health <= 90:
                health += 10
            else:
                print("lol")
      else:
            outcome == 2
            print("You were unsuccessful on the adventure.")
            sleep (.2)
            print("You have lost 10 health and 5 gold")
            gold -= 5
            print(gold)
            health -= 5

  elif action == "exit":
    print("Bye bye")
    exit()
    
  else:
    print("Invalid Input")



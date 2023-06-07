import random



def intro():
  print("----------------------------------------------------------\nWelcome to the Super Awesome Number Guessing Game!\n----------------------------------------------------------\n\nThe rules are very complicated, so listen up!\n\nYou will be asked to guess a number between 1 and 10. Type your guess and hit \"Enter\".\nRULE #1: You are expected to enter a whole number. Do not enter a decimal or we shall say \"Ni!\" to you.\nRULE #2: Only use numbers. Do not spell out your guess or we shall say \"Ni!\" to you.\nRULE #3: Guess a number between 1 and 10 or we shall say \"Ni!\" to you.\n\n\n\nLet us begin!\n")
  
def game():
  solution = random.randrange(1,10)
  tries = 1
  ni_count = 0
  high_score = 0
  if high_score == 0:
    print("The score to beat is:\nThere are no scores yet!\nGood luck!\n")
  else:  
    print("The score to beat is:\n{}\nGood luck!\n".format(high_score))
  guess = input("What is your guess?    ")
  while guess != solution:
    try:
      guess = int(guess)
    except ValueError:
      ni_count += 1
      print("Ni!")
      guess = input("Try again. But THIS time, type a whole number - no decimals, and no spelling out the number!\nWhat is your guess?    ")
    else:
      if guess < 1 or guess > 10:
        ni_count += 1
        print("Ni!")
        guess = input("Try again. But THIS time, guess a number that is between 1 and 10!\nWhat is your guess?    ")
      elif guess > solution:
        print("That's too high! Try again.")
        tries += 1
        guess = input("What is your next guess?    ")
      elif guess < solution:
        print("That's too low! Try again.")
        tries += 1
        guess = input("What is your next guess?    ")
      else:
        tries += 0
        if high_score == 0:
          high_score = tries
        elif tries < high_score:
          high_score = tries
        print("\n\nYou got it! It only took you {} guess(es), and we only had to say \"Ni!\" to you {} times!\n\n\n Nice job!".format(tries,ni_count))

  
def start_game():
  play = "y"
  tries = 1
  intro()
  while play == "y":
    game()
    play = input("Would you like to play? Y/N    ").lower()
  else: 
    print("Thanks for playing!")
  
  
start_game()

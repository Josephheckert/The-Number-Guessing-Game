import random

solution = random.randrange(1,10)
high_score = "No scores yet!"
tries = 1

def set_high_score(tries):
  if tries < high_score:
    high_score = tries
    return high_score
  else:
    return high_score
  
def intro(high_score):
  print("----------------------------------------------------------\nWelcome to the Super Awesome Number Guessing Game!\n----------------------------------------------------------\n\nThe rules are very complicated, so listen up!\n\nYou will be asked to guess a number between 1 and 10. Type your guess and hit \"Enter\".\nRULE #1: You are expected to enter a whole number. Do not enter a decimal or we shall say \"Ni!\" to you.\nRULE #2: Only use numbers. Do not spell out your guess or we shall say \"Ni!\" to you.\nRULE #3: Guess a number between 1 and 10 or we shall say \"Ni!\" to you.\n\n\nThe high score to beat is: \n{}. Good luck!\n\n\nLet us begin!".format(high_score))
  

def start_game(solution):
  ni_count = 0
  tries = 1
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
        print("\n\nYou got it! It only took you {} guess(es), and we only had to say \"Ni!\" to you {} times!\n\n\n Nice job!".format(tries,ni_count))
        return tries
        if high_score == "No scores yet!":
          high_score = tries
          return high_score
        else:
          if tries < high_score:
            high_score = tries
            return high_score
          else:
            return high_score

intro(high_score)
start_game(solution)
play_again = input("Would you like to play again? Y/N    ")
if play_again.lower() != "y":
  print("Thanks for playing!")
else:
  intro(high_score)
  start_game(solution)

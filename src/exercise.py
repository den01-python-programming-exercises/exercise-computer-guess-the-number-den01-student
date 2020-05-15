from random import randint

def main():

    lower_bound = 1
    upper_bound = 10

    print("I'm going to guess a number between " + str(lower_bound) + " and " + str(upper_bound) + ".")
    guess = randint(lower_bound,upper_bound)

    while True:

      print("I guessed " + str(guess) + ".")
      
      correct = input("Was I correct? ")
      if correct == "You got it right":
        print("Woo!")
        return
      elif correct == "Too high!":
        guess = randint(lower_bound,guess)
      elif correct == "Too low!":
        guess = randint(guess,upper_bound)
      else:
        print("Sorry I didn't quite catch that!")

    # note - this is not a very clever solution. There are lots of ways that this could be improved!


if __name__ == '__main__':
    main()

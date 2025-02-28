[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=2777159&assignment_repo_type=AssignmentRepo)
# Exercise - Computer guess the number

Implement a program in Python which guesses a random number that the computer has chosen.

**Hints:**

- Use the string `"I guessed " + str(guess) + "."` when outputting the user's guess.
- Input the string `You got it right!` when the answer is right.
- Input the string `Too high!` when the guess is too high.
- Input the string `Too low!` when the guess is too low.

You might find the following helpful:

```plaintext
user thinks of random number (no coding here!)

loop until the computer gets it right
    computer guesses random number

    if the guess is right
        user inputs yes
    otherwise
        if the number is too low
            user inputs higher
        if the number is too high
            user inputs lower
```

Implement the program so that the following issues are fixed:

- Tell the computer what *higher* and *lower* means.
- Don't let the computer guess the same answer twice.

**Note:** *There is no automatic testing for this exercise - you are responsible for writing and running your own tests!*

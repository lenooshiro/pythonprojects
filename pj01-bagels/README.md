## Bagel, a deductive logic game

Let's play a game. I'll think of a number and you need to guess it based on some clues.

Here's the rules:

1) It's a 3 digit number
2) You have a maximun of 10 guesses
3) I'll give you a clue based on how close you got from my number. The clues are:
- Pico: One digit is correct but in the wrong position.
- Fermi: One digit is correct and in the right position.
- Bagels: No digit is correct.

For example:

Number: 248
Guess: 843

My clues will be: Fermi Pico. This means that one number is in the right place and is a correct value (Fermi, 4), and there's another digit that is in the incorrect place, but it's one correct value (Pico, 8).

***

The output will look like this:

```
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
Guess #1:

> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
```
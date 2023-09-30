## Blackjack

Blackjack, also known as 21, is a card game where players try to get as close to 21 points as possible without going over. This program uses images drawn with text characters, called ASCII art. American Standard Code for Information Interchange (ASCII) is a mapping of text characters to numeric codes that computers used before Unicode replaced it. The playing cards in this program are an example of ASCII art:

 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|

When you run blackjack.py, the output will look like this:

```
Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
Money: 5000
How much do you bet? (1-5000, or QUIT)
> 400
Bet: 400

DEALER: ???
 ___   ___
|## | |2  |
|###| | ♥ |
|_##| |__2|

PLAYER: 17
 ___   ___
|K  | |7  |
| ♠ | | ♦ |
|__K| |__7|


(H)it, (S)tand, (D)ouble down
> h
You drew a 4 of ♦.
--snip--
DEALER: 18
 ___   ___   ___
|K  | |2  | |6  |
| ♦ | | ♥ | | ♠ |
|__K| |__2| |__6|

PLAYER: 21
 ___   ___   ___
|K  | |7  | |4  |
| ♠ | | ♦ | | ♦ |
|__K| |__7| |__4|

You won $400!
```
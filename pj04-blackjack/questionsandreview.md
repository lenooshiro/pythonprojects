# Questions

1. <b>How can you make the player start with a different amount of money?</b>

By changing the initial value of the var "money"

2. <b>How does the program prevent the player from betting more money than they have?</b>

By including an if statement to check if the value of the bet is higher than 1 and lower or equal than the amount of money the player has

3. <b>How does the program represent a single card?</b>

Using a tuple with the suit and the value/rank


4. <b>How does the program represent a hand of cards?</b>

With a list of tuples

5. <b>What do each of the strings in the rows list (created on line 197) represent?</b>

It represents the text of each row that the card drawing is composed by. The card drawing is made by 4 rows and one extra line to separate it from the following text.

Its values are not really used besides rows[4] since it will be replaced by the actual card values later. But still it needs to be initiated, or else it will occur an error of index out of range.

6. <b>What happens if you delete or comment out random.shuffle(deck) on line 148?</b>

The deck will always be ordered by how it is created. This means every game will have the same order of cards, so it's really predictable.

7. <b>What happens if you change money -= bet on line 112 to money += bet?</b>

The player will lose money rather than earn.

8. <b>What happens when showDealerHand in the displayHands() function is set to True? What happens when it is False?</b>

The program will print the value of the dealer's cards in hand. This is against the rules of the game, where it will only show when the player stops betting.

# Review

This challenge is a bit more difficult than the others. You need to have a good understanding of all the BlackJack rules, divide all the stages and locate the loops. Also, we need to use common sense to extract some functions into separate methods so they can be called again in other places.

I didn't understand at first how to draw the card, so that part I basically copied from the book's solution. That aside, the challenge is not really difficult, but it takes a lot of work and patience.
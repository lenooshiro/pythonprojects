## Questions:


1. <b>What happens when you change the NUM_DIGITS constant?</b>

You are increasing the length of the secret number, which makes more difficult to guess.

2. <b>What happens when you change the MAX_GUESSES constant?</b>

<p>The player will have more tries to guess, making the game a little bit easier

3. <b>What happens if you set NUM_DIGITS to a number larger than 10?</b>

It will exit with an error "Index Out of Bounds" since we created a list with 10 digits (from 0 to 9) and we are trying to access the 11th value, which does not exist. 

4. <b>What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?</b>

The function "getSecretNum()" will never get called, instead we are fixing a number to be the secret number, so it'll always be the same.

5. <b>What error message do you get if you delete or comment out numGuesses = 1 on line 34?</b>

Since we never declared the variable and associated it with any int value, the next line will throw an error because it's trying to make a comparison between and int and 'nothing'. 

6. <b>What happens if you delete or comment out random.shuffle(numbers) on line 62?</b>

It will always get the same X initial digits. If we keep the number of digits 3, then the secret number will always be the first 3 numbers of the 'numbers' list, meaning will always be '012'.

7. <b>What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?</b>

It will run a block of code which would have skipped otherwise, and will not show the congratulatory message informing that the player won. The game will still work as normal, although not as performatic or intuitive as before, but it will not have any problem since there's another victory check just before the number of guesses increment.

8. <b>What happens if you comment out numGuesses += 1 on line 44?</b>

The code will not increment the guesses counter, it will act like it's always the player's first guess, meaning he/she will have infinite chances to get the right answer.

# Review

// TODO
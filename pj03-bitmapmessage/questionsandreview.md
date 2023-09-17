# Questions:

1. <b>What happens if the player enters a blank string for the message?</b>

The program exits

2. <b>Does it matter what the nonspace characters are in the bitmap variable’s string?</b>

No. The code only checks for space characters in the string. Anything that's different will go through the same action, which is
entering the 'else' code and calculating the message's index to know which character to print.

3. <b>What does the i variable created on line 45 represent?</b>

*(In my code, it's line 38)*

It's a counter for how many characters the 'line' has. The 'enumerate' function returns a pair of a counter and the value in that position, which it's named 'bit' in the code.

Example: Let's say that 'line' = 'abcdefg'. This means that the loop in enumerate will go from i = 0 to 6, and bit will go from a to g. But they will always return in pairs, so in the first loop i = 0 and bit = a, the second loop will return i = 1 and bit = b, and so on.

4. <b>What bug happens if you delete or comment out print() on line 52?</b>

*(In my code, it's line 54)*

Since it's an image, the characters position is very important, or else the image will become really confusing and will not make sense.

The 'print()' is there to break the line when it reaches the end of the inner loop. If we don't put one in there, the first loop will continue printing in the same line, and in the end we'll just have a giant string that won't form an image at all.

The bitmap image is a multiline string, and it's important to keep their structure when executing the code, hence why it's important to put a 'print()' there.

# Review

This challenge is interesting because it has a fairly simple solution, which at first I didn't realize that and wrote a more amateur code.

Let's say that we needed to implement the same program, but we couldn't use the same approach.

To be more specific, I'm talking about this line:
> print(message[i % len(message)], end='')

The first method that I've tried is to declare a counter variable to keep track of which characters of the message I've already used. When it reaches the last one, It'll just reset. Something like this:

```
mgCounter = 0
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if mgCounter >= len(message):
            mgCounter = 0
        if (bit == ' '):
            print(' ', end='')
        else:
            print(message[mgCounter], end='')
        mgCounter += 1
    print()
```

And it works fine, but I believe the book's code is cleaner and it shows the importance of math in programming.
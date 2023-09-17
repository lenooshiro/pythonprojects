# Questions:

1. <b>How are birthdays represented in this program? (Hint: look at line 16.)</b>

*(In my code, it's line 60)*

The 'date' function is constructed by passing the year, month and day as arguments, in that order. After that we'll just add a random amount of days an it will calculate the birth date for us.

After that, we formatted the output by having our own list of months name and returned the correct one using the 'getMonth' function we wrote.

2. <b>How could you remove the maximum limit of 100 birthdays the program generates?</b>

Just remove the if check when checking the value given by the user. We can change the value 100 to another one or just remove that statement (although we need to keep checking if it's more than 0).

The problem with that is that you could increase the amount of processing needed to run the simulations by a large amount, potentially crashing the machine you're running this program on. So it's always best to put a limit in order to avoid such errors.

3. <b>What error message do you get if you delete or comment out numBDays = int(response) on line 57?</b>

*(In my code, it's line 20)*

That line converts a string into an integer. If we don't do that, any place in the code that expects an integer will receive a string and it'll throw an error saying that it can't interpret it.  

4. <b>How can you make the program display full month names, such as 'January' instead of 'Jan'?</b>

Just change the values inside our 'MONTHS' list.

5. <b>How could you make 'X simulations run...' appear every 1,000 simulations instead of every 10,000?</b>

In line 41, we have an if statement that prints a message every 10.000 runs (the remainder of the divisions is 0). We can just change to 1.000 and do the same check.

# Review

// TODO
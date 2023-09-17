## The Birthday Paradox

The Birthday Paradox, also called The Birthday Problem, is the probability that two people will have the same birthday even in a small group.

In a group of 70 people, there's 99.9% chance of two people have a matching birthday.

In a group of 23 people, there's 50% of chance of two people have a matching birthday.

**Write a program to perform several probability experiments to determine the percentage for groups of different sizes.**

We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.

***

The output will look like this:


```
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--snip--
How many birthdays shall I generate? (Max 100)
> 23

Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18

In this simulation, multiple people have a birthday on Jul 29

Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!
```
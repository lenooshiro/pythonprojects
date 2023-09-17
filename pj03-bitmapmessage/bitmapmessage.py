"""
The Big Book of Small Python Projects
Project #03 - Bitmap Message
"""

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Welcome to the Bitmap Message')
print('Please type a message to be transformed into a World Map:')
message = input('> ')
if message == '':
    sys.exit

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        # If there's a space, it will print a space
        if (bit == ' '):
            print(' ', end='')
        else:
            # The idea here is that I'm iterating through 2 variables at the same time. When dividing
            # the 'i' by len(message), the remainder will never go out of bounds, since it'll restart
            # once it goes over the message's length
            #
            # Ex: message = 'cat'
            # If i = 0, message[i % len(message)] = 0 % 3 = message[0] = c
            # If i = 1, message[i % len(message)] = 1 % 3 = message[1] = a
            # If i = 2, message[i % len(message)] = 2 % 3 = message[2] = t
            # If i = 3, message[i % len(message)] = 0 % 3 = message[0] = c
            # If i = 4, message[i % len(message)] = 1 % 3 = message[1] = a
            print(message[i % len(message)], end='')
    print()
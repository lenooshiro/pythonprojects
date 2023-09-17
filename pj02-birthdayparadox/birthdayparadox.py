"""
The Big Book of Small Python Projects
Project #02 - The Birthday Paradox (which is not a paradox)
"""

import datetime
import random

def main():

    print('''
            The Birthday Paradox, by Al Sweigart
            Program written by Leno Oshiro
          ''')
    
    while True:
        print('How many birthdays shall I generate? (Max 100)')
        groupSize = input('> ')
        if groupSize.isdecimal() and (0 < int(groupSize) <= 100):
            #groupSize = int(groupSize)
            break

    birthdays = getBirthdays(groupSize)
    print('Here are {} birthdays:'.format(groupSize))
    for i in range (len(birthdays)):
        print('{} {}'.format(getMonth(birthdays[i]), birthdays[i].day))

    match = getMatch(birthdays)
    if match != None:
        print('In this simulation, multiple people have birthday on {} {}'.format(getMonth(match), match.day))
    else:
        print('In this simulation, there\'s no matching birthday')

    print('')
    print('Generating', groupSize, 'random birthdays 100.000 times')
    input('Press ENTER to begin')
    print('')

    simMatches = 0
    for i in range (100000):
        if i % 10000 == 0:
            print('Ran {} simulations'.format(i))

        birthdays = getBirthdays(groupSize)
        if getMatch(birthdays) != None:
            simMatches += 1
        
    probability = round(simMatches / 100000 * 100, 2)
    print('')
    print('Finished 100.000 simulations.')
    print('Out of 100.000 simulations of {} people, there was a matching birthday'.format(groupSize))
    print('in that group {} times. This means that {} people have a {}% chance of'.format(simMatches, groupSize, probability))
    print('having a match birthday in their group.')


def getBirthdays(groupSize):
    birthdays = []
    for i in range (groupSize):
        # For this simulation, the year doesn't matter
        startOfYear = datetime.date(2000, 1, 1)

        # Get a random day in the year
        randomDay = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomDay
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays):
    # Set does not allow duplicated values, so if the length is different, it must
    # have matching birthdays
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA
            

def getMonth(birthday):
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    
    return MONTHS[birthday.month - 1]


if __name__ == '__main__':
    main()
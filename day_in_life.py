def day_in_life():
    energy= 600
    output_score= 0

    print('Good morning! Hope you slept well')
    print('How do you want to start the morning:')
    print('1. Coffee and shower')
    print('2. Go for a run and make breakfast after')
    print('3. Skip work and sleep in')

    morn= int(input('What do you want to do 1/2/3?'))
    if morn == 1 : 
        print('Great! Enjoy the shower')
        energy += 50
        output_score += 120
    elif morn ==2:
        print('Great! Dont forget to grab your towel')
        energy -= 110
        output_score += 100
    elif morn == 3:
        print('Ah doesnt seem like you slept well last night, take your time now')
        energy -= 150
        output_score -= 80
    else : print('Invalid response')
    
    print('\n Its almost 1pm')
    print('1. Call up a friend and make plans')
    print('2. Make lunch and watch a movie')
    afn= int(input('What would you like to do:'))
    if afn == 1:
        print('Have fun! dont forget to take your wallet')
        energy -= 150
        output_score += 150
    elif afn == 2:
        print('Good choice! Do you want any suggestions in which movie or cuisine')
        
        mov= input('Y/N')
        if mov == 'Y' : 
            print('How about Pasta, Dumplings, Sushi and Murder mystery, Knives out for a movie')
            energy += 180
            output_score += 150
        elif mov == 'N' : 
            print('Alright, have a good time!')
            energy += 180
            output_score += 150
        else: print('invalid')
    else : print('Invalid response')

    print('Its 4pm, lets review your points')
    print(f' \nEnergy = {energy}')
    print(f'\n Output score = {output_score} ')
    if energy >= 400:
        print('Weather seems to be good today, care for walk?')
        q1= input('Y/N')
        if q1 == 'Y': 
            print('Have fun and maybe you should try a sandwich on the way back')
            output_score += 60
            energy -= 100
        elif q1== 'N': 
            print('Alright')
            output_score += 20
            energy -= 20
    elif energy<400 :
        print('You can catch up on leftover work or go for grocery shopping')
        q2= int(input('1/2'))
        if q2 == 1: 
            print('Okay lets set the system up')
            energy -= 180
            output_score += 150
        elif q2 == 2: 
            print('Sure! Dont forget to grab your list')
            energy -= 180
            output_score += 140
        else : 
            print('Alright')
            energy -= 25

    print('Its the end of the day')
    print(f' \nEnergy = {energy}')
    print(f'\n Output score = {output_score} ')


day_in_life()

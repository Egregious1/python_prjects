wins = 0
loses = 0
count = 0

while True:
    track = input('Enter "win" or "lose". Enter "done" when finished. ')
    if count != 'done':
        count += 1
    if track == 'win':
        wins += 1
    elif track == 'lose':
        loses += 1
    elif track == 'done':
        print('You won ', wins, 'times')
        print('You lost ', loses, 'times')

        def average(wins, loses):
            return (wins + loses) / 2

        avg = average(wins, loses)
        print('your average today was: ', avg, "in", count - 1, 'games!')
        if input('Do you want to start again y/n: ') != 'y':
            break
#  need to find a way to restart entire program in order to begin on fresh slate.


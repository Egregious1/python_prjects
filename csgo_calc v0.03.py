wins = 0
loses = 0
count = 0
ovr_wins = []
ovr_loses = []
print('     |========== CS:GO Calculator ==========|') # made for simple tracking for overall win/lose ratios.
print('')
user_name = input('Please enter a username: ') # gets printed when entering done
while True:
    track = input('Enter "win" or "lose". Enter "done" when finished. ')
    if track not in {'win', 'lose', 'done'}:
      print('!===== Not a valid entry =====!')
      print('')
    if track == 'win':
        wins += 1
        count += 1
        ovr_wins.append(track)
    elif track == 'lose':
        loses += 1
        count += 1
        ovr_loses.append(track)
    elif track == 'done': # wrap up returns games won/lost and an overall average
        print('')
        print(user_name + ' this time:')
        print('You won ', wins, 'games')
        print('You lost ', loses, 'games')
        wins = 0
        loses = 0

        def average(ovr_wins, ovr_loses): # used to find average between both counts
            return (ovr_loses + ovr_wins) / 2

        avg = average(wins, loses)
        print('your average was: ', avg, "in", count, 'games!')
        print('')
        if input('Do you want to start again y/n: ') != 'y': # anything other than y stops program.
          print('')
          print('     |========== Restart Program ===========|')
          break

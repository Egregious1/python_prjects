wins = 0
loses = 0
count = 0
print('     |========== CS:GO Calculator ==========|')
print('')
while True:
    track = input('Enter "win" or "lose". Enter "done" when finished. ')
    if track not in {'win', 'lose', 'done'}:
      print('!===== Not a valid entry =====!')
      print('')
    if track == 'win':
        wins += 1
        count += 1
    elif track == 'lose':
        loses += 1
        count += 1
    elif track == 'done':
        print('You won ', wins, 'games')
        print('You lost ', loses, 'games')

        def average(wins, loses):
            return (wins + loses) / 2

        avg = average(wins, loses)
        print('your average today was: ', avg, "in", count, 'games!')
        if input('Do you want to start again y/n: ') != 'y':
          print('')
          print('     |========== Restart Program ===========|')
          break

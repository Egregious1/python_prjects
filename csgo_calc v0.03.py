wins = 0
loses = 0
count = 0
ovr_wins = []
ovr_loses = []
maps = ['dust2', 'inferno', 'train', 'mirage', 'nuke', 'overpass', 'vertigo']

# made for simple tracking for overall win/lose ratios.
print('|========== CS:GO Calculator ==========|')
print('')
# gets printed when entering done
user_name = input('Please enter a username: ')
while True:
    map_name = str(input('What map are you playing? '))
    if map_name in maps:
        print('Thank you!')
        break
    elif map_name not in maps:
        print('Please enter valid map!')

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

    elif track == 'done':  # wrap up returns games won/lost and an overall average
        print('')
        print(user_name + ' this time on ' + map_name + ':')
        print('You won ', wins, 'games')
        print('You lost ', loses, 'games')
        wins = 0
        loses = 0

        # used to find average between both counts it stopped working......what the flying fuck!
        def average(ovr_wins, ovr_loses):
            return (loses + wins) / 2

        avg = average(wins, loses)
        print('your average was: ', avg, "in", count, 'games!')
        print('')
        # anything other than y stops program.
        if input('Do you want to start again y/n: ') != 'y':
            print('')
            print('|========== Restart Program ===========|')
            break

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:04:40 2021

@author: saira

"""

# Date:              12 November 2021
#video game file
#read coin file
# when coin in text file - add coin
# when jump in text file - jump to line as specified by number

               #break
with open('coins.txt', 'w') as coin_file:
    coin_file.write('')

with open('game.txt', 'r') as video_games:
    video = []
    for x in video_games:
        video.append(x.strip())
        
    coins = 0
    spot = 0
    coin_list = []
   # with open('coins.txt', 'w') as coin_file:
    while spot < 624:
        #video.split(' ')
        if 'coin' == video[spot][:4]:
            coin = video[spot].split(' ')
            coins += int(coin[1])
            spot += 1
            coin_list.append(coins)
        elif 'none' == video[spot][:4]:
            spot += 1
        elif 'jump' == video[spot][:4]:
            jump = video[spot].split(' ')
            jump_to = int(jump[1])
            spot += jump_to
        if spot > 624:
            break
       # with open('coins.txt', '')
        with open('coins.txt', 'w') as coin_file:
            coin_file.write(str(int(coin[1])) + '\n')
           # for coins in coin_list:
            #    coin_file.write(str(coins) + '\n')
    print("Total coins: {}".format(coins))
        
#print(coins)            
      # print(jump)
  # print(Game[int(jump)])
   #print(jump)
  # print(video_split)
#print(video_games[0])
#print("Total coins:",coins)

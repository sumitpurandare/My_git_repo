player = {'name':'Manuel','attack':10,'heal':16,'health':100}
monster = {'name':'Max','attack':12,'health':100}
game_running = True

while game_running == True:
    print('Select Action :')
    print("1) Attack")
    print("2) Heal")

    player_choice = input()

    if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <= 0 : 
            pass 
        else:
            player['health'] = player['health'] - monster['attack']
            if player['health '] <=0:
                pass

        print(monster['health'])
        print(player['health'])
    elif player_choice == '2':
        player['heal']
        print('Heal Player')
    else:
        print ('Invalid Input')

    

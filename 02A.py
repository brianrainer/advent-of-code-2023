cube_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    with open('input02A.txt', 'r') as f1:
        line = f1.readline()
        ans = 0
        while line:
            game, content = line.split(':')
            
            game_id = int(game.split(' ')[1])
            ball_combi = content.strip().split(';')

            is_possible = True
            for bc in ball_combi:
                balls = bc.strip().split(' ')
                
                for i in range(0, len(balls), 2):
                    count = int(balls[i].strip())
                    color = balls[i+1].strip(',')

                    if cube_dict[color] < count:
                        is_possible = False
                        break

            if is_possible:
                ans += game_id

            line = f1.readline()
        print(ans)

main()
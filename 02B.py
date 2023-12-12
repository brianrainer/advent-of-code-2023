from collections import defaultdict

def main():
    with open('input02A.txt', 'r') as f1:
        line = f1.readline()
        ans = 0
        while line:
            game, content = line.split(':')
            
            game_id = int(game.split(' ')[1])
            ball_combi = content.strip().split(';')

            min_cube_dict = defaultdict(int)
            for bc in ball_combi:
                balls = bc.strip().split(' ')
                
                for i in range(0, len(balls), 2):
                    count = int(balls[i].strip())
                    color = balls[i+1].strip(',')
                    min_cube_dict[color] = max(min_cube_dict[color], count)
                
            res = 1
            for count in min_cube_dict.values():
                res *= count
            ans += res

            line = f1.readline()
        print(ans)

main()
def main():
    with open('input06A.txt', 'r') as f1:
        l1 = f1.readline().split(':')[-1]
        l2 = f1.readline().split(':')[-1]

        time = [int(x.strip()) for x in l1.split(' ') if x]
        dist = [int(x.strip()) for x in l2.split(' ') if x]

        ans = 1

        for t, d in zip(time, dist):
            cnt = 0
            for i in range(1, t):
                res = (t-i) * i
                if res > d:
                    cnt += 1
            if cnt > 0:
                ans *= cnt
        
        print(ans)

main()
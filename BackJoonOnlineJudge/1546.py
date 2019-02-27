n = float(input())
score = list(map(float,input().split()))
total = 0
for i in score:
    total = i + total
O_mean = total/n

score.sort()
N_mean = (O_mean/(score[-1]))*100
print(format(N_mean,".6f"))
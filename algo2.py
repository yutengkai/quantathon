import part2
'''
all_l = []
for i in range(24):
    all_l.append([0]*12)
    
for i in range(12):
    all_l[i][i] = 100
    all_l[i+12][i] = -100
    
accu = 0.000001
speed = 9
result_l = []
for i in range(24):
    result_l.append(part2.s_r(all_l[i]))
maxi = max(result_l)
mini = min(result_l)
print(maxi, mini)

while (maxi - mini > accu):
    big = result_l.index(maxi)
    small = result_l.index(mini)
    for i in range(12):
        all_l[small][i] = (all_l[small][i] + speed*all_l[big][i])/(speed+1)
    lsum = sum(all_l[small])
    for i in range(12):
        all_l[small][i] = (all_l[small][i]/abs(lsum)) * 100
    result_l = []
    print("\n\n------------------------------\n\n")
    for i in range(24):
        print(all_l[i])
    for i in range(24):
        result_l.append(1000 * part2.s_r(all_l[i]))
    maxi = max(result_l)
    mini = min(result_l)
    print("\n")
    print(maxi, mini)    
    
result = [0.0, 0.0, 95.6298828125, 0.0, 4.3701171875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
'''
def f(sl):
    l = [[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[]]
    for i in l:
        for j in sl:
            i.append(j)
    return l

new = [-1, -1, 5, -22, 1, 1, -2, -2, -1, -1, 1, 3]
'''
for i in range(0, 12, 2):
    new[i] *= -1
'''

l = f(new)
accu = 0.00000001

for i in range(12):
    l[i][i] = l[i][i] + 10
    l[i+12][i] = l[i+12][i] - 10

for i in range(24):
    print(l[i])
rl = []
for i in range(24):
    rl.append(part2.s_r(l[i]))
    
maxi = max(rl)
ori = part2.s_r([1]*24)

while (maxi - ori > accu):
    new = l[rl.index(maxi)]
    l = f(new)
    for i in range(12):
        l[i][i] = l[i][i] + 10
        l[i+12][i] = l[i+12][i] - 10
        
    
    print("\n\n---------------------------------------------------\n\n")    
    
    for i in range(24):
        print(l[i])    
    rl = []
    for i in range(24):
        rl.append(part2.s_r(l[i]))   
    maxi = max(rl)
    print("\n\n-------------------------\n\n")
    print(new)
    print(maxi)
    ori = part2.s_r(new)
    
print(new)
print(ori)

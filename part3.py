import math
import part2
import team37

stocks = team37.stock_list

def fill3(a_l):
    
    fill3_list = []
    w3 = part2.w2_list(a_l)
    
    for i in range(len(w3)):
        line = [w3[i][0]]
        for j in range(100):
            if w3[i][j+1] * stocks[j][i+2][6] >= 0:
                line.append(1)
            else:
                line.append(0)
        fill3_list.append(line)
    return fill3_list

'''
for i in range(20):
    print(fill3_list[i][:11])
'''

rocs = part2.roc_list

def rp3(a_l):
    sum1 = 0
    sum2 = 0
    w = part2.w2_list(a_l)
    fill = fill3(a_l)
    result = []
    for day in range(len(w)):
        rp = [w[day][0]]
        for i in range(100):
            sum1 += fill[day][i+1] * w[day][i+1] * rocs[i][day+2][1]
            sum2 += abs(fill[day][i+1] * w[day][i+1])
        if sum2 == 0:
            rp.append(0)
        else:
            rp.append(sum1/sum2)
        result.append(rp)
    return result

def s_r(a_l):
    r3 = rp3(a_l)
    rp = []
    for i in r3:
        rp.append(i[1])
    #print(sum(rp))
    #print(len(rp))
    mean = sum(rp) / len(rp)
    s = 0
    for i in rp:
        s += (i - mean)**2
    de = math.sqrt(s/100)
    
    return mean/de

def f(sl):
    l = [[],[],[],[],[],[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],[],[],[],[],[]]
    for i in l:
        for j in sl:
            i.append(j)
    return l

def algo(accu, speed):
    new = [1,-1]*6   
    l = f(new) 
    for i in range(12):
        l[i][i] = l[i][i] + speed
        l[i+12][i] = l[i+12][i] - speed
    
    for i in range(24):
        print(l[i])
    rl = []
    for i in range(24):
        rl.append(s_r(l[i]))
        
    maxi = max(rl)
    ori = s_r([1]*24)
    
    while (maxi - ori > accu):
        new = l[rl.index(maxi)]
        l = f(new)
        for i in range(12):
            l[i][i] = l[i][i] + speed
            l[i+12][i] = l[i+12][i] - speed
            
        
        print("\n\n---------------------------------------------------\n\n")    
        
        for i in range(24):
            print(l[i])    
        rl = []
        for i in range(24):
            rl.append(s_r(l[i]))   
        maxi = max(rl)
        print("\n\n-------------------------\n\n")
        print(new)
        print(maxi)
        ori = part2.s_r(new)
        
    print(new)
    print(ori)
    
a_l = [1, -1, 1, -1, 1, -1, 0, -1, 1, -1, 1, -1]
w3 = part2.w2_list(a_l)
r3 = rp3(a_l)

cumr_list = []
for day in range(len(r3)):
    product = 1
    for i in range(day + 1):
        product *= (1 + r3[i][1])
    cumr_list.append([r3[day][0], math.log(product)])
    
q4 = []
for day in w3:
    s = 0
    for i in day[1:]:
        s += abs(i)
    q4.append([day[0], s/100])
    
q5 = []
for i in range(len(q4)):
    q5.append([q4[i][0], sum(w3[i][1:]) / q4[i][1]])


result_list = []
result_list.append([20000104] + [0]*105)
result_list.append([20000105] + [0]*105)

for day in range(len(w3)):
    sublist = [w3[day][0]]
    sublist.append(r3[day][1])
    sublist.append(cumr_list[day][1])
    sublist.append(q4[day][1])
    if r3[day][1] >= 0:
        sublist.append(1)
    else:
        sublist.append(-1)
    sublist += w3[day][1 :]
    sublist.append(q5[day][1])
    result_list.append(sublist)



fin = open("data_part2.team_037.csv", "r")
fout = open("part3.csv", "w")

fout.write(fin.readline().strip() + ", Question 5\n")

for l in result_list:
    fout.write(team37.l_to_csv(l))

fin.close()
fout.close()
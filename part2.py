import math
import team37

rco_list = []
for stock in team37.stock_list:
    rco_of_stock = []
    for day in range(len(stock) - 1):
        rco = (stock[day + 1][1]/stock[day][4]) - 1
        rco_of_stock.append([stock[day + 1][0], rco])
    rco_list.append(rco_of_stock)

roc_list = []
for stock in team37.stock_list:
    roc_of_stock = []
    for day in range(len(stock)):
        roc = (stock[day][4]/stock[day][1]) - 1
        roc_of_stock.append([stock[day][0], roc])
    roc_list.append(roc_of_stock)
    
'''
beverly = []
for i in range(len(team37.rcc_list[0])):
    s = 0
    for j in range(100):
        s += team37.rcc_list[j][i][1]
    beverly.append([team37.rcc_list[0][i][0], s/100])

b_file = open("beverly.csv", "w")
for i in beverly:
    s = str(i[0]) + ", " + str(i[1]) + "\n"
    b_file.write(s)
b_file.close()
'''

roo_list = []
for stock in team37.stock_list:
    roo_of_stock = []
    for day in range(len(stock) - 1):
        roo = (stock[day + 1][1]/stock[day][1]) - 1
        roo_of_stock.append([stock[day + 1][0], roo])
    roo_list.append(roo_of_stock)
    
rvp_list = []
for stock in team37.stock_list:
    rvp_of_stock = []
    for day in range(len(stock) - 1):
        rvp = (1/(4*math.log(2)))*((math.log(stock[day][2])
                                    - math.log(stock[day][3]))**2)
        rvp_of_stock.append([stock[day][0], rvp])
    rvp_list.append(rvp_of_stock)
    
avg_rco_list = []
avg_roc_list = []
avg_roo_list = []
avg_rvp_list = []
avg_tvl_list = []
avg_rcc_list = []
rcc_list = team37.rcc_list

for day in range(len(rco_list[0])):
    s = 0
    for stock in rco_list:
        s += stock[day][1]
    avg_rco_list.append([rco_list[0][day][0], s/100])
    
for day in range(len(roc_list[0])):
    s = 0
    for stock in roc_list:
        s += stock[day][1]
    avg_roc_list.append([roc_list[0][day][0], s/100])
    
for day in range(len(roo_list[0])):
    s = 0
    for stock in roo_list:
        s += stock[day][1]
    avg_roo_list.append([roo_list[0][day][0], s/100])

# avg rvp    
for day in range(len(rvp_list[0])):
    avg_of_day = [rvp_list[0][day][0]]
    for i in range(100):
        r_list = []
        j = max(0, day - 199)
        while (j <= day):
            r_list.append(rvp_list[i][j][1])
            j += 1
        avg_of_day.append(sum(r_list)/len(r_list))
    avg_rvp_list.append(avg_of_day)
'''
print(avg_rvp_list[0])
for i in range(10):
    print((rvp_list[i][0][1] + rvp_list[i][0][1])/2)
print(avg_rvp_list[1])
for i in range(10):
    print((rvp_list[i][0][1] + rvp_list[i][1][1])/2)
'''

# avg tvl
for day in range(len(team37.stock_list[0])):
    avg_of_day = [team37.stock_list[0][day][0]]
    for i in range(100):
        t_list = []
        j = max(0, day - 199)
        while (j <= day):
            t_list.append(team37.stock_list[i][j][5])
            j += 1
        avg_of_day.append(sum(t_list)/len(t_list))
    avg_tvl_list.append(avg_of_day)

'''
print(avg_tvl_list[0][1:12])
for i in range(10):
    print(team37.stock_list[i][0][5])
    
print(avg_tvl_list[1][1:12])
for i in range(10):
    print((team37.stock_list[i][0][5] + team37.stock_list[i][1][5])/2)
'''

for i in range(len(team37.stock_list[0]) - 1):
    avg_rcc_list.append([team37.stock_list[0][i+1][0], 
                         team37.avg_rcc_dict[team37.stock_list[0][i+1][0]]])

def w2_list(a_l):
    result = []
    for day in range(len(avg_tvl_list) - 2):
        day_list = [avg_tvl_list[day+2][0]]
        for i in range(100):
            w2 = 0
            # variables needed by today's w2
            rcc = rcc_list[i][day][1]
            arcc = avg_rcc_list[day][1]
            rco = rco_list[i][day+1][1]
            arco = avg_rco_list[day+1][1]
            roc = roc_list[i][day+1][1]
            aroc = avg_roc_list[day+1][1]
            roo = roo_list[i][day+1][1]
            aroo = avg_roo_list[day+1][1]
            rvp = rvp_list[i][day+1][1]
            arvp = avg_rvp_list[day+1][i + 1]
            tvl = team37.stock_list[i][day+1][5]
            atvl = avg_tvl_list[day+1][i + 1]
            cc = rcc - arcc
            co = rco - arco
            oc = roc - aroc
            oo = roo - aroo
            t = tvl / atvl
            r = rvp / arvp
            # formula
            w2 += a_l[0] * cc
            w2 += a_l[1] * oo
            w2 += a_l[2] * oc
            w2 += a_l[3] * co
            w2 += a_l[4] * t * cc
            w2 += a_l[5] * t * oo
            w2 += a_l[6] * t * oc
            w2 += a_l[7] * t * co
            w2 += a_l[8] * r * cc
            w2 += a_l[9] * r * oo
            w2 += a_l[10] * r * oc
            w2 += a_l[11] * r * co
            day_list.append(w2/100)
        result.append(day_list)
    return result



'''
print(avg_rcc_list[0])
print(avg_rco_list[0])
print(avg_roc_list[0])
print(avg_roo_list[0])
print(avg_rvp_list[0])
print(avg_tvl_list[0])

i = 0
day = 1
rcc = rcc_list[i][day]
arcc = avg_rcc_list[day]
rco = rco_list[i][day+1]
arco = avg_rco_list[day+1]
roc = roc_list[i][day+1]
aroc = avg_roc_list[day+1]
roo = roo_list[i][day+1]
aroo = avg_roo_list[day+1]
rvp = rvp_list[i][day+1]
arvp = avg_rvp_list[day+1][0]
tvl = team37.stock_list[i][day+1][0]
atvl = avg_tvl_list[day+1][0]
print("----------------------------------------")
print(rcc)
print(arcc)
print(rco)
print(arco)
print(roc)
print(aroc)
print(roo)
print(aroo)
print(rvp)
print(arvp)
print(tvl)
print(atvl)
'''

def rp2_list(a_l):
    w2 = w2_list(a_l)
    result = []
    for day in range(len(w2)):
        sublist = [w2[day][0]]
        sum_1 = 0
        sum_2 = 0
        for i in range(100):
            sum_1 += w2[day][i+1] * roc_list[i][day + 2][1]
            sum_2 += abs(w2[day][i+1])
        sublist.append(sum_1/sum_2)
        result.append(sublist)
    return result
'''
a_l = [1] + [0]*11
rp2 = rp2_list(a_l)
for i in range(20):
    print(rp2[i])
'''

def s_r(a_l):
    rp2 = rp2_list(a_l)
    rp = []
    for i in rp2:
        rp.append(i[1])
    #print(sum(rp))
    #print(len(rp))
    mean = sum(rp) / len(rp)
    s = 0
    for i in rp:
        s += (i - mean)**2
    de = math.sqrt(s/100)
    
    return mean/de

'''
a_l = [1] + [0]*11
print(s_r(a_l))
'''

a_l = [-1, -1, 5, -22, 1, 1, -2, -2, -1, -1, 1, 3]

w2 = w2_list(a_l)

'''
rp2 = rp2_list(a_l)

cumr_list = []
for day in range(len(rp2)):
    product = 1
    for i in range(day + 1):
        product *= (1 + rp2[i][1])
    cumr_list.append([rp2[day][0], math.log(product)])
    
q4 = []
for day in w2:
    s = 0
    for i in day[1:]:
        s += abs(i)
    q4.append([day[0], s/100])
    
q5 = []
for i in range(len(q4)):
    q5.append([q4[i][0], sum(w2[i][1:]) / q4[i][1]])


result_list = []
result_list.append([20000104] + [0]*105)
result_list.append([20000105] + [0]*105)

for day in range(len(w2)):
    sublist = [w2[day][0]]
    sublist.append(rp2[day][1])
    sublist.append(cumr_list[day][1])
    sublist.append(q4[day][1])
    if rp2[day][1] >= 0:
        sublist.append(1)
    else:
        sublist.append(-1)
    sublist += w2[day][1 :]
    sublist.append(q5[day][1])
    result_list.append(sublist)



fin = open("data_part2.team_037.csv", "r")
fout = open("part2.csv", "w")

fout.write(fin.readline().strip() + ", Question 5\n")

for l in result_list:
    fout.write(team37.l_to_csv(l))

fin.close()
fout.close()
'''
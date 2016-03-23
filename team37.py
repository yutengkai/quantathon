import math

def l_to_csv(l):
    result = ""
    for i in l:
        result += " ," + str(i)
    return result[2:] + "\n"

data_file = open("in_sample_data.txt","r")
line_list = data_file.readlines()

# construct our list of numbers
day_list = []
for line in line_list:
    str_list = line.strip().split(",")
    float_list = []
    for i in str_list:
        try:
            float_list.append(int(i))
        except:
            float_list.append(float(i))
    day_list.append(float_list)

'''
x = " 32423.24234 "
try:
    y = int(x)
except:
    y = float(x)
'''

# [[day_number, [[s], [s], ...]] , [d], [d], ...]
day_list_of_stock = []
for line in day_list:
    day_line = []
    day_line.append(line[0])
    day_line.append([])
    for i in range(100):
        day_line[1].append(line[6*i+1: 6*i+7])
    day_list_of_stock.append(day_line)

# list of stock of days
stock_list = []

for i in range(100):
    stock = []
    for line in day_list_of_stock:
        stock_of_day = []
        stock_of_day.append(line[0])
        stock_of_day += line[1][i]
        stock.append(stock_of_day)
    stock_list.append(stock)
   


#part 1

# list of stock of rcc 
rcc_list = []
for i in range(100):
    stock_rcc = []
    for day in range(len(stock_list[0]) - 1):
        pair = [stock_list[i][day+1][0]]
        rcc = (stock_list[i][day+1][4] / stock_list[i][day][4]) - 1
        pair.append(rcc)
        stock_rcc.append(pair)
    rcc_list.append(stock_rcc)

# list of average rcc    
avg_rcc_dict = {}
for day in range(len(rcc_list[0])):
    avg_rcc = 0
    for stock in rcc_list:
        avg_rcc += stock[day][1]
    avg_rcc /= 100
    avg_rcc_dict[rcc_list[0][day][0]] = avg_rcc

'''   
x = 0
for i in rcc_list:
    x += i[678][1]
x /= 100
'''

w1_list = []
for day in range(len(avg_rcc_dict) - 1):
    day_list = []
    day_list.append(rcc_list[0][day+1][0])
    for stock in rcc_list:
        diff = stock[day][1] - avg_rcc_dict[stock[day][0]]
        diff /= -100
        day_list.append(diff)
    w1_list.append(day_list)
   
rp1_list = []
for day in range(len(w1_list)):
    sum1 = 0
    sum2 = 0
    for w1 in w1_list[day][1:]:
        sum2 += abs(w1)
    for stock_number in range(100):
        sum1 += (w1_list[day][stock_number + 1] 
                 * rcc_list[stock_number][day+1][1])
    rp1_list.append([w1_list[day][0], sum1/sum2])

cumr_list = []
for day in range(len(rp1_list)):
    product = 1
    for i in range(day + 1):
        product *= (1 + rp1_list[i][1])
    cumr_list.append([rp1_list[day][0], math.log(product)])
    
q4 = []
for day in w1_list:
    s = 0
    for i in day[1:]:
        s += abs(i)
    q4.append([day[0], s/100])
    
q5 = []
for i in range(len(q4)):
    q5.append([q4[i][0], sum(w1_list[i][1:]) / q4[i][1]])

result_list = []
result_list.append([20000104] + [0]*104)
result_list.append([20000105] + [0]*104)
for day in range(len(w1_list)):
    sublist = [w1_list[day][0]]
    sublist.append(rp1_list[day][1])
    sublist.append(cumr_list[day][1])
    sublist.append(q4[day][1])
    if rp1_list[day][1] >= 0:
        sublist.append(1)
    else:
        sublist.append(-1)
    sublist += w1_list[day][1 :]
    result_list.append(sublist)
infile1 = open("data_part1.team_037.csv", "r")
outfile1 = open("data_part1.team_0371.csv", "w")

outfile1.write(infile1.readline())
for l in result_list:
    outfile1.write(l_to_csv(l))
infile1.close()
outfile1.close()



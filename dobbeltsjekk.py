data = "individer1000.txt"
sum1 = 0
sum2 = 0
fil = open(data)
for line in fil: 
    datas = line.strip().split(",")
    if datas[9] == "vil betale": 
        sum1 += 1
    else: 
        sum2 += 1

print(sum1)
print(sum2)

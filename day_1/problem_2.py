input=open('input.txt','r').readlines()

elfs_cal=[]
cal_sum=0

for line in input:
    if line == '\n': 
        elfs_cal.append(cal_sum)
        cal_sum=0
    else: 
        cal_sum=cal_sum+int(line)

K=3
elfs_cal.sort()
res = sum(elfs_cal[-K:])

print(res)

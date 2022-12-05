input=open('input.txt','r').readlines()

elfs_cal=[]
sum=0

for line in input:
    if line == '\n': 
        elfs_cal.append(sum)
        sum=0
    else: 
        sum=sum+int(line)

print(max(elfs_cal))

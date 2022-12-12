import re

input = open("input.txt", 'r').readlines()

path_dict = {} # Dictionary that will store the path and the size of each file
tmp_dir = [] # Directory names will be stored here temporarly

for line in input:
    line=line.strip()
    # WHY TF putting "is" doesn't work BUT == works???
    # Anyways if the line is a "go back" then go back by removing the last dir from the tmp_dir array
    if line == "$ cd ..":
        tmp_dir.pop(-1)
        continue
    # IF it's a change of dir
    if line.startswith("$ cd"):
        tmp_dir.append(line[5:]) # Append the directory name, so skip the command
        # IF it's not in the path_dict yet then create it with size 0
        if ''.join(tmp_dir) not in path_dict.keys():
            path_dict.update({ ''.join(tmp_dir): 0 })
        continue
    # IF we find a numeric value
    if re.search("^\d+ ", line):
        size = line.split(' ') # Clean the input
        dir_name = []
        # FOR each dir in the TMP array assign the size to the dir name
        for directory in tmp_dir:
            dir_name.append(directory)
            path_dict.update({ ''.join(dir_name): path_dict[''.join(dir_name)] + int(size[0]) })    
        continue

# Find the sum of all folders < 100000
sum=0
for size in path_dict.values():
    if size < 100000:
        sum=sum+size
        
print(sum)
# Find a list of possible folders to delete
tot_size=0
# Look: i just wanted to get the ROOT size at index 0 and idk nor care to search how to do it so i'm doing like this
for size in path_dict.values():
    tot_size=tot_size+size
    break
candidates=[]
for size in path_dict.values():
    if 70000000 - tot_size + size >= 30000000:
        candidates.append(size)
# Print the smallest possible folder, as the array is now sorted
candidates.sort()
print(candidates[0])

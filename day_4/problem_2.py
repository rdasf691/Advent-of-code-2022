input=open("input.txt",'r').readlines()
contained_total=0 # The total number of pairs that contain the other
# FOR each line of the input
for line in input:
    line=line.strip() # Clean it from newline etc...
    first_group,second_group=line.split(',') # Divide the two groups 
    # Find the start and end of each group
    range_start_first_group,range_end_first_group=first_group.split('-')
    range_start_second_group,range_end_second_group=second_group.split('-')
    # Put them both into an array
    first_group = [i for i in range(int(range_start_first_group),int(range_end_first_group)+1)] 
    second_group = [i for i in range(int(range_start_second_group),int(range_end_second_group)+1)]
    # Remove all possible duplicates from each group
    first_group = set(first_group)
    second_group= set(second_group)
    # Check if the two groups have at least one intersection
    if len(first_group.intersection(second_group)) > 0:
        contained_total=contained_total+1

print(contained_total)

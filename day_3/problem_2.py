input = open("input.txt",'r').readlines()
# ALL the possible characters (we'll take index+1 as their value)
values=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total=0
N=3
# FOR each line in the file in groups of N
for index in range(0,len(input),N):
    # Store the index+N-1 lines in separate variables and strip them
    line_1=input[index].strip()
    line_2=input[index+1].strip()
    line_3=input[index+2].strip()
    # Find the common element between all N lines
    common_element=set(line_1).intersection(line_2, line_3)
    # Convert the set into a character
    common_element = ''.join(common_element)
    # Find the value of that character and accumulate it
    value=values.index(common_element)+1
    total=total+value

print(total)

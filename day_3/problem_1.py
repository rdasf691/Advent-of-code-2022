input = open("input.txt",'r').readlines()
# ALL the possible characters (we'll take index+1 as their value)
values=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total=0
# FOR each line in the file
for line in input:
    line=line.strip() # Remove newline and trailing spaces
    length = len(line) # How long is that line?
    middle_len = length//2 # How much is half of that lenght? 
    compartment_1 = line[:middle_len] # The first half of the line (in the first compartment)
    compartment_2 = line[middle_len:] # The second half of the line (in the second compartment)
    # Scroll each character in the first compartment and print the common element with the second
    for character in compartment_1:
        if character in compartment_2:
            value=values.index(character)+1
            total=total+value
            break
print(total)

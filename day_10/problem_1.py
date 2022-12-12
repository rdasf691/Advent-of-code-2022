input = open("input.txt", 'r').read().splitlines()

tot_cycles=0
register_value=1  # The initial value of the register
escape_conditions=[20,60,100,140,180,220] # List of points where we want to stop and check the strenght
strenghts=0
for command in input:
    # Find how many ctcles are needed for each instruction
    cycles=0
    if command.startswith("noop"): 
        cycles=1
    if command.startswith("addx"):
        cycles=2
    # Run those instruction with the needed "delay" (cycle)
    for _ in range(1,cycles+1):
        tot_cycles=tot_cycles+1
        if tot_cycles in escape_conditions:
            strenght=register_value*tot_cycles
            print(strenght) # Print the strenght if an escape condition is detected
            strenghts=strenghts+strenght
        # IF it's an addx command run it
        if _ > 1:
            value=command.split(' ')
            value=int(value[1])
            register_value=register_value+value

print("Total: ",strenghts)

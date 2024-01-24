print("Iteration Calculator")

initialValue = int(input("Enter Initial Value: "))
print("---------------------------")
print("Process [sum, sub, mul, div]")
process = input("Enter Process: ")
print("---------------------------")
change = int(input("Enter Change Value: "))
print("---------------------------")
iterations = int(input("Enter Itterations: "))
print()

value = initialValue    
    
for _ in range(iterations):
    if(process == "sum"):
        value += change
    
    if(process == "sub"):
        value -= change
        
    if(process == "mul"):
        value *= change
        
    if(process == "div"):
        value /= change
    
    print("{} {}".format(i, value))

print("---------------------------")
endstr = "Total change in {} iteration(s): {} to {}".format(iterations, initialValue, value)
print(endstr)

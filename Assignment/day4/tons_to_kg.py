calculate = [
    lambda tons: tons * 1000,
    lambda kg: kg * 1000,
    lambda gram: gram * 1000,                 
    lambda mg: mg * 0.00000220462  #mg to pound
    ] 
tons=float(input("enter weight in tons:"))

kg = calculate[0](tons)
gram = calculate[1](kg)
mg = calculate[2](gram)
lbs = calculate[3](mg)

print("weight in kg",kg)
print("weight in gram",gram)
print("weight in miligram",mg)
print("weight in poumds",lbs)




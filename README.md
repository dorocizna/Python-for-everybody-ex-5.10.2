# Write program that prompts for a list of numbers and at the end prints out total, count, maximum and minimum of the numbers.
count = 0
total = 0
biggest = None
smallest = None

while True :
    value = input('Enter a number: ')
    if value == 'done' :
        break
    try :
        value = float(value)
    except :
        print('Enter valid number')
        continue
    total = total + value
    count = count + 1

for val in value :
    if smallest is None or val < smallest :
        smallest = val
for val in value :
    if smallest is None or val < smallest :
        smallest = val
print(total,count,biggest,smallest)

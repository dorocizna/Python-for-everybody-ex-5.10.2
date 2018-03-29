# printing total, count, minimum and maximum with error messages
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

    total = total + value
    count = count + 1
    if smallest is None or value < smallest :
        smallest = value
    if biggest is None or value > biggest :
        biggest = value
print(total,count,smallest,biggest)

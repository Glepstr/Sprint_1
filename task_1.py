list1 = '1h 45m,360s,25m,30m 120s,2h 60s'

minutes = 0
hours = 0
seconds = 0
total_minutes = 0

items = list1.replace(' ', ',').split(',')

for i in items:
    if 'h' in i:
        total_minutes += int(i.replace('h', '')) * 60

    elif 'm' in i:
        total_minutes += int(i.replace('m', ''))

    elif 's' in i:
        total_minutes += int(i.replace('s', '')) / 60

#print(int(minutes + hours*60 + seconds*(1/60)))
print(total_minutes)
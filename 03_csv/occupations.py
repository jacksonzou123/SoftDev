#Jackson Zou
#Softdev pd1
#K06 -- Divine your destiny
#2019-09-15

file = open("occupations.csv", 'r')
words = file.readlines()
words.pop(0)
index = 0
rolls = {}
for each in words:
    each = each.strip()
    each = each.split(',')
    job = each[0]
    print(each)
    percent = float(each[1])
    while percent > 0:
        rolls[index] = job
        percent -= 0.1
        index += 0.1
print(rolls)

    

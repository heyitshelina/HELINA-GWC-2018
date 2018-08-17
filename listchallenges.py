#option 1
aList = [5, 4, 3, 2, 5]
x = 4

for i in range(len(aList)):
    if aList[i] == x:
        print(i)
print(-1)


# option 2
list = [5, 4, 3, 2, 5]
y = 2
frequency=0

for i in range(len(list)):
    if (list[i] == y):
        frequency += 1
print (frequency)


#option 3
data = [1, 2, 3, 4, 5]
first = 0

for i in range(len(data)):
    first += data[i]
    mean = first / len(data)
print (mean)

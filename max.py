a = [1, 2, 7, 8, 9, 5]
max1 = a[0]
for i in range(len(a)):
    if a[i] > max1:
        max1 = a[i]
print("first max:", max1)
max2 = 0
for i in range(len(a)):
    if a[i] != max1:
        if max2 is 0 or a[i] > max2:
            max2 = a[i]
print("Second max:", max2)

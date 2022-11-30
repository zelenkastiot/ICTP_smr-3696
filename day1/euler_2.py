
a = list()
a.append(1)
a.append(2)

for i in range(2, 10**3):
    a.append(a[i-1] + a[i-2])
    if a[-1] > 10**6:
        break

    

my_sum = 0
for i in a:
    if i % 2 ==0:
        my_sum+=i

print(my_sum)
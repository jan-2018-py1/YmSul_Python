# Multiples Section, Part I: printing odd numbers
for i in range(1,1000):
    if (i % 2 != 0):
        print i

# Multples Section, Part II: printing multiples of 5
for i in range(5,1000000):
    if (i % 5 == 0):
        print i

# Sum List Section:
a = [1, 2, 5, 10, 255, 3]
asum = sum(a)
print asum

# Average list Section:
a = [1, 2, 5, 10, 255, 3]
asum = sum(a)
alen = len(a)
aavg = asum / alen
print aavg

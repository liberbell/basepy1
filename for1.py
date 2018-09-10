# words = ['cat', 'window', 'defenestrate']
#
# for w in words:
#     print(w,len(w))
for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            # break roop
            break
    else:
        print(n, 'is a prime number')

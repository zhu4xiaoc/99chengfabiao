# # n*m, m确定行数，在外层循环定义
# m = 1
# while m <= 9:
#     n = 1  # n确定列数，每次都从1开始循环，在内层循环定义
#     while n <= m:
#         print("%i x %i = %i" % (n, m, n * m), end='\t')
#         n += 1  # 当n<m时，继续执行第二个while循环
#     print()
#     m += 1

for x in range(1, 10):
    for y in range(1, x+1):
        print('%i * %i = %i' % (y, x, y * x), end='\t')
        y += 1
    print()

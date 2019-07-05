import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('Result is %d digits long!\n' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

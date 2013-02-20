
cols = 5

dimensions = [
    (1,1),
    (2,2),
    (2,4),
    # (4,1),
]

dimensions_b = [
]

for w, h in dimensions:
    result = []
    for i in range(h):
        for j in range(w):
            result.append('1')
        result += ['0'] * (cols-w)
    
    print ''.join(reversed(result))
    dimensions_b.append(int(''.join(reversed(result)), 2))

for i, d in enumerate(dimensions):
    print d, dimensions_b[i]

from random import choice

grid = 0

print 
for r in range(200):
    r = choice(range(len(dimensions)))
    d, db = dimensions[r], dimensions_b[r]

    i = 0
    while True:
        _, m = divmod(i, cols)
        if (m+d[0])>cols or db&grid:
            i += 1
            db = db<<1
        else:
            print i, d
            print '{0:032b}'.format(db)
            print '{0:032b}'.format(grid)
            grid = db|grid
            print '{0:032b}'.format(grid)
            print 
            break



    # print (w,h), '{0:08b}'.format(wb)
    # print (w,h), result
    # break

# print '{0:08b}'.format(1<<4)

# print int('1111', 2)

# print '{0:08b}'.format(2)
# print '{0:08b}'.format(4)


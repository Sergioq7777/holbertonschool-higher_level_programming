def generator(*args):
    for valor in args
    yield valor * 10, True

for v_1, v2 in generator(1,2,3,4,5,6,7,8,9):
    print(v_1, v2)
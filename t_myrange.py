
def myrange(start, stop, step):
    mylist = []
    i = start
    while i < stop:
        mylist.append(i)
        i += step
    return mylist

def myxrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4

mygen = mygenerator()
for i in mygen:
    print(i)
# print(next(mygen))
# print(next(mygen))
# print(next(mygen))
# print(next(mygen))
# print(next(mygen))

'''
print(myrange(1, 10, 2))
mygen = myxrange(1, 10, 2)
print(mygen)
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
'''


def allTrue(elements):
    return all(elements)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(allTrue(tuple1))
print(allTrue(tuple2))

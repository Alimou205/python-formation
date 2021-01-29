var = [32, 5, 12, 8, 3, 75, 2, 15]
pairs = []
impairs = []
i = 0
while i < len(var):
 if var[i] % 2 == 0:
    pairs.append(var[i])
 else:
    impairs.append(var[i])
 i = i + 1
print("nombres pairs :", pairs)
print("nombres impairs :", impairs)

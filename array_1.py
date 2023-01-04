array = [(1,11),(2,22),(3,33),(4,44),(5,55)]

answer = []
answer2 = []

num = 0
for (a,b) in array:
    answer.append(a*2)
    answer2.insert(num,b*2)
    num += 1

print(answer)
print(answer2)

answer3 = answer + answer2
print(answer3)
answer3 += [15]
print(answer3)
answer3.extend([17,18,4])
print(answer3)

del answer3[0]
print(answer3)

answer3.remove(4)
answer3.remove(4)
print(answer3)
answer3.sort()
print(answer3.__len__())
print(len(answer3))
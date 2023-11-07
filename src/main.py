""" from itertools import combinations

print(list(combinations('231',2)))
print("=========================")

print(list(combinations('231',3)))
print("=========================")

A = [1, 1, 3, 3, 3]
print(list(combinations(A,4))) """

""" print(list(combinations(S, 1)))
print("======================")
print(list(combinations(S, 2))) """

from itertools import combinations

S = 'HACK'
k = 2
S = sorted(S)
combinationsResult = []

for i in range (1, k + 1):
    combinationsResult = list(combinations(S, i))
    for j in combinationsResult:
        print("".join(j))

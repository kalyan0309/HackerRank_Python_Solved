# Enter your code here. Read input from STDIN. Print output to STDOUTfrom itertools import product

from itertools import product
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))

import sys
input = sys.stdin.readline

n = int(input())
books = dict()
for _ in range(n):
    book = input().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

books = sorted(books.items(), key = lambda x : (-x[1], x[0]))

print(books[0][0])

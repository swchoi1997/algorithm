import sys
input = sys.stdin.readline

def cut_tree(m, tree, start, end):
    result = 0 
    while start <= end:
        mid = (start + end) // 2
        cutlen = 0

        for i in tree:
            cut_tree_length = i - mid
            if cut_tree_length <= 0:
                cut_tree_length = 0
            cutlen += cut_tree_length

        if cutlen == m:
            return mid
        elif cutlen > m:
            start = mid + 1
            result = max(result, mid)
        else:
            end = mid - 1 
    return result


n, m = map(int, input().split())
tree = list(map(int,input().split()))

c_tree = cut_tree(m, tree, 0, max(tree))

print(c_tree)
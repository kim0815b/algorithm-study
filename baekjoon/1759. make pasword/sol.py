def dfs(path=[],idx=0):
    if l - len(path) > c - idx:   #4 - 0 > 6 - 3
        return
    if len(path) == l:
        if sum(path.count(vowel) for vowel in vowels) >= 1 and sum(path.count(con) for con in cons) >= 2:
            print(''.join(path))
        return

    dfs(path + [arr[idx]], idx + 1)
    dfs(path, idx + 1)

l, c = map(int, input().split())
arr = input().split()
arr.sort()
vowels = ['a','e','i','o','u']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

dfs()
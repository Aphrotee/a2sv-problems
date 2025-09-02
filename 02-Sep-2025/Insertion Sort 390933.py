# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    cur = n - 2
    misplaced = arr[-1]
    while cur >= 0:
        if arr[cur] >= misplaced:
            arr[cur + 1] = arr[cur]
            print(' '.join(map(str, arr)))
        else:
            arr[cur + 1] = misplaced
            print(' '.join(map(str, arr)))
            return
        cur -= 1
    arr[cur + 1] = misplaced
    print(' '.join(map(str, arr)))
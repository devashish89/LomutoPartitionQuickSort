# Lomuto Partition
# https://www.youtube.com/watch?v=PgBzjlCcFvc

def lomutoPartition(l, left, right):
    i = left - 1
    # last element is the pivot
    pivot = l[right]

    for j in range(left, right):
        if l[j] <= pivot:
            i = i + 1
            l[i], l[j] = l[j], l[i]

    l[i + 1], l[right] = l[right], l[i + 1]
    return i + 1


def quickSort(arr, left, right):
    if left < right:
        p = lomutoPartition(arr, left, right)
        quickSort(arr, left, p - 1)
        quickSort(arr, p + 1, right)


if __name__ == '__main__':
    lst = [10, 80, 30, 90, 40, 50, 70]
    # p = lomutoPartition(lst, 0, len(lst) - 1)
    # print("index of pivot", p)
    # print(lst)
    print("--" * 30)
    quickSort(lst, 0, len(lst) - 1)
    print("After quick sort")
    print(lst)


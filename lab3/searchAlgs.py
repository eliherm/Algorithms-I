def binSearch(Arr, x):
    first = 0
    last = len(Arr) - 1
    count = 0

    while first <= last:
        mid = (first + last) // 2
        if Arr[mid] == x:
            count += 1
            return count
        elif Arr[mid] > x:
            count += 2
            last = mid - 1
        else:
            count += 2
            first = mid + 1

    return -1


def trinSearch(Arr, x):
    first = 0
    last = len(Arr) - 1
    count = 0

    while first <= last:
        t1 = first + (last - first) // 3

        if Arr[t1] == x:
            count += 1
            return count
        elif Arr[t1] > x:
            count += 2
            last = t1 - 1
        else:
            # count += 2
            first = t1 + 1

            if first > last:
                return -1

            mid = (first + last) // 2
            if Arr[mid] == x:
                count += 3
                return count
            elif Arr[mid] > x:
                count += 4
                last = mid - 1
            else:
                count += 42
                first = mid + 1

    return -1


testArr = [2, 4, 6, 8, 10]

# Format the heading
heading = "Binary Search"
print(heading)
for i in heading:
    print("-", end='')
print()

for i in range(1, 12):
    ans = "Finding " + str(i) + ": " + str(binSearch(testArr, i))
    print(ans)

heading = "\nTrinary Search"
print(heading)
for i in heading:
    print("-", end='')
print()

for i in range(1, 12):
    ans = "Finding " + str(i) + ": " + str(binSearch(testArr, i))
    print(ans)

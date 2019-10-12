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


def avgIterations(Arr):
    binSearchCounts = []
    trinSearchCounts = []

    for i in range(1, Arr[len(Arr) - 1] + 1):
        binSearchCounts.append(binSearch(Arr, i))
        trinSearchCounts.append(trinSearch(Arr, i))

    results = {
                'binSearch': sum(binSearchCounts) / len(binSearchCounts),
                'trinSearch': sum(trinSearchCounts) / len(trinSearchCounts)
               }

    return results


# Test Examples
test1k = [i*2 for i in range(1, 1001)]
test2k = [i*2 for i in range(1, 2001)]
test4k = [i*2 for i in range(1, 4001)]
test8k = [i*2 for i in range(1, 8001)]
test16k = [i*2 for i in range(1, 16001)]

avg1k = avgIterations(test1k)
print("Average for 1,000 values:")
print("Binary Search: " + str(avg1k['binSearch']))
print("Trinary Search: " + str(avg1k['trinSearch']))
print()

avg2k = avgIterations(test2k)
print("Average for 2,000 values:")
print("Binary Search: " + str(avg2k['binSearch']))
print("Trinary Search: " + str(avg2k['trinSearch']))
print()

avg4k = avgIterations(test4k)
print("Average for 4,000 values:")
print("Binary Search: " + str(avg4k['binSearch']))
print("Trinary Search: " + str(avg4k['trinSearch']))
print()

avg8k = avgIterations(test8k)
print("Average for 8,000 values:")
print("Binary Search: " + str(avg8k['binSearch']))
print("Trinary Search: " + str(avg8k['trinSearch']))
print()

avg16k = avgIterations(test16k)
print("Average for 16,000 values:")
print("Binary Search: " + str(avg8k['binSearch']))
print("Trinary Search: " + str(avg8k['trinSearch']))

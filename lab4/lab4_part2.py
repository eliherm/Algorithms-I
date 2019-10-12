"""
Name: Elikem Hermon
Student Number: 20075527
I certify that this submission contains my own work, except as noted.
"""

import math
import random
import matplotlib.pyplot as plt


def bfi_subset_count(input_set, target):
    """Returns the number of operations taken to find a subset that sums to the target"""
    count = 0   # Count of operations

    subsets = [{'elements': [], 'sum': 0}]
    count += 1

    # Iterate through the input set
    for idx, value in enumerate(input_set):
        new_subsets = []

        # Iterate through existing subsets
        for old_sub in subsets:
            new_elements = old_sub['elements'].copy()
            new_elements.append(value)
            count += 2

            # Create a new subset with the current value in input_set
            new_sub = {
                'elements': new_elements,
                'sum': old_sub['sum'] + value
            }
            count += 2

            if new_sub['sum'] == target:
                count += 1
                return count
            else:
                new_subsets.append(old_sub)
                new_subsets.append(new_sub)
                count += 3
        subsets = new_subsets[:]
        count += 1

    return count


def bfi_find_count(input_set):
    """Returns all subsets in a given set and the number of operations taken"""
    count = 0   # Count of operations

    subsets = [{'elements': [], 'sum': 0}]
    count += 1

    # Iterate through the input set
    for idx, value in enumerate(input_set):
        new_subsets = []

        # Iterate through existing subsets
        for old_sub in subsets:
            new_elements = old_sub['elements'].copy()
            new_elements.append(value)
            count += 2

            # Create a new subset with the current value in input_set
            new_sub = {
                'elements': new_elements,
                'sum': old_sub['sum'] + value
            }
            count += 2

            new_subsets.append(old_sub)
            new_subsets.append(new_sub)
            count += 2
        subsets = new_subsets[:]
        count += 1

    return [subsets, count]


def hs_subset_count(input_set, target):
    """Returns the number of operations taken to find a subset that sums to the target"""
    count = 0   # Count of operations
    mid = (len(input_set) - 1) // 2     # Find the midpoint of the set

    # Divide the set into two parts
    input_l = input_set[0: mid + 1]
    input_r = input_set[mid + 1: len(input_set)]
    count += 2

    # Find all subsets
    subs_l = bfi_find_count(input_l)[0]
    subs_r = bfi_find_count(input_r)[0]

    # Update count with operations from finding subsets
    count += bfi_find_count(input_l)[1] + bfi_find_count(input_r)[1]

    # Check if the target is in one of these subsets
    for subset in subs_l:
        count += 1
        if subset['sum'] == target:
            return count

    for subset in subs_r:
        count += 1
        if subset['sum'] == target:
            return count

    # Sort the subset list based on sums
    subs_l.sort(key=lambda x: x['sum'])
    subs_r.sort(key=lambda x: x['sum'])

    # Update count with operations from sorting
    count += 3 * len(subs_l) * math.log(len(subs_l), 2)
    count += 3 * len(subs_r) * math.log(len(subs_r), 2)

    # Use pair sum to find a subset from the left and right
    sum_idx = pair_sum_count(sum_list(subs_l), sum_list(subs_r), target)
    count += sum_idx[2]     # Operations from pair sum

    if (sum_idx[0] == -1) and (sum_idx[1] == -1):
        count += 1
        return count
    else:
        count += 1
        return count


def sum_list(subsets):
    """Returns a list of sums from a list of subset dictionaries along with the number of operations taken"""
    count = 0   # Count of operations
    sums = []
    for i in subsets:
        sums.append(i['sum'])
        count += 1

    return [sums, count]


def pair_sum_count(lset, rset, target):
    """Checks if a pair of values from two sets sum to the target"""
    count = lset[1] + rset[1]   # Update count with operations taken to extract the list of sums
    lset = lset[0]
    rset = rset[0]

    l_ptr = 0   # Left pointer
    r_ptr = len(rset) - 1   # Right pointer

    while (l_ptr <= len(lset) - 1) and (r_ptr >= 0):
        cur_sum = lset[l_ptr] + rset[r_ptr]
        count += 2
        if cur_sum == target:
            count += 1
            return [l_ptr, r_ptr, count]
        elif cur_sum < target:
            count += 2
            l_ptr += 1
        else:
            count += 2
            r_ptr -= 1
    return [-1, -1, count]


results = []    # Store test results
for test_size in range(4, 16):
    # Store averages for tests
    bfi_avg = []
    hs_avg = []

    for num_test in range(1, 21):
        test_set = [random.randint(0, 1000) for _ in range(0, test_size)]

        # Randomly generate at least 10 targets
        num_targets = random.randint(10, 20)
        targets = [random.randint(500, 1500) for _ in range(0, num_targets)]

        # Count of operations
        bfi_counts = []
        hs_counts = []
        for targ in targets:
            bfi_num_ops = bfi_subset_count(test_set, targ)
            hs_num_ops = hs_subset_count(test_set, targ)

            bfi_counts.append(bfi_num_ops)
            hs_counts.append(hs_num_ops)

        bfi_avg.append(sum(bfi_counts) / len(bfi_counts))
        hs_avg.append(sum(hs_counts) / len(hs_counts))

    test_result = {
        'size': test_size,
        'bfi': sum(bfi_avg) / len(bfi_avg),
        'hs': sum(hs_avg) / len(hs_avg)
    }
    results.append(test_result)

# Print the table headings
for heading in ["Size", "BFI Avg", "HS Avg"]:
    print("{: ^20}".format(heading), end="")
print()

# Print the table data
for res in results:
    print("{: ^20} {: <20} {: <20}".format(res['size'], res['bfi'], res['hs']))

# Plot of the data
plt.plot(list(range(4, 16)), [res['bfi'] for res in results], label="BFI")
plt.plot(list(range(4, 16)), [res['hs'] for res in results], label="Horowitz & Sahni")

# Plot models for comparison
plt.plot(list(range(4, 16)), [6*2**val for val in range(4, 16)], label="6 * 2^n")
plt.plot(list(range(4, 16)), [6*val * (2 ** (val / 2)) for val in range(4, 16)], label="6 * n * 2^(n/2)")

# Labels for axes
plt.xlabel("Set size")
plt.ylabel("Operations")
plt.legend()  # Show the legend
plt.title("Comparing BFI vs Horowitz & Sahni")
plt.show()

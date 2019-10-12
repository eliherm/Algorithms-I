"""
Name: Elikem Hermon
Student Number: 20075527
I certify that this submission contains my own work, except as noted.
"""


def bfi_subset_sum(input_set, target):
    """Checks if a subset sums to the target"""
    subsets = [{'elements': [], 'sum': 0}]  # List of subsets

    # Iterate through the input set
    for idx, value in enumerate(input_set):
        new_subsets = []    # Store new subsets for each value in the input set

        # Iterate through existing subsets
        for old_sub in subsets:
            new_elements = old_sub['elements'].copy()
            new_elements.append(value)

            # Create a new subset with the current value in input_set
            new_sub = {
                'elements': new_elements,
                'sum': old_sub['sum'] + value
            }

            if new_sub['sum'] == target:
                print(f"{new_sub['elements']} sums to {target}")
                return
            else:
                new_subsets.append(old_sub)
                new_subsets.append(new_sub)
        subsets = new_subsets[:]

    # No solution found
    print(f"No subset sums to {target}")


def bfi_find_subsets(input_set):
    """Returns all subsets in the input set"""
    subsets = [{'elements': [], 'sum': 0}]  # List of subsets

    # Iterate through the input set
    for idx, value in enumerate(input_set):
        new_subsets = []

        # Iterate through existing subsets
        for old_sub in subsets:
            new_elements = old_sub['elements'].copy()
            new_elements.append(value)

            # Create a new subset with the current value in input_set
            new_sub = {
                'elements': new_elements,
                'sum': old_sub['sum'] + value
            }

            new_subsets.append(old_sub)
            new_subsets.append(new_sub)
        subsets = new_subsets[:]

    return subsets


def hs_subset_sum(input_set, target):
    """Checks if a subset sums to the target"""
    mid = (len(input_set) - 1) // 2  # Find the midpoint of the set

    # Divide the set into two parts
    input_l = input_set[0: mid + 1]
    input_r = input_set[mid + 1: len(input_set)]

    # Find all subsets
    subs_l = bfi_find_subsets(input_l)
    subs_r = bfi_find_subsets(input_r)

    # Check if the target is in one of these subsets
    for subset in subs_l:
        if subset['sum'] == target:
            print(f"{subset['elements']} sums to {target}")
            return

    for subset in subs_r:
        if subset['sum'] == target:
            print(f"{subset['elements']} sums to {target}")
            return

    # Sort the subset list based on sums
    subs_l.sort(key=lambda x: x['sum'])
    subs_r.sort(key=lambda x: x['sum'])

    # Use pair sum to find a subset from the left and right
    sum_idx = pair_sum(sum_list(subs_l), sum_list(subs_r), target)
    if (sum_idx[0] == -1) and (sum_idx[1] == -1):
        print(f"No subset sums to {target}")
    else:
        print(f"{subs_l[sum_idx[0]]['elements'] + subs_r[sum_idx[1]]['elements']} sums to {target}")


def sum_list(subsets):
    """Returns a list of sums from a list of subset dictionaries"""
    sums = []
    for i in subsets:
        sums.append(i['sum'])

    return sums


def pair_sum(lset, rset, target):
    """Checks if a pair of values from two sets sum to the target"""
    l_ptr = 0   # Left pointer
    r_ptr = len(rset) - 1   # Right pointer

    while (l_ptr <= len(lset) - 1) and (r_ptr >= 0):
        cur_sum = lset[l_ptr] + rset[r_ptr]
        if cur_sum == target:
            return [l_ptr, r_ptr]
        elif cur_sum < target:
            l_ptr += 1
        else:
            r_ptr -= 1

    # Target was not found
    return [-1, -1]


test_set = [3, 5, 3, 9, 18, 4, 5, 6]    # Set for testing
print(f"Test Set: {test_set}\n")

# Testing bfi_subset_sum
heading = "BFI Subset Sum"
print(heading)
for k in heading:
    print("-", end="")

print("\n\nCase 1: Target value (5) is in the set")
bfi_subset_sum(test_set, 5)

print("\nCase 2: The sum of the set is the target value (53)")
bfi_subset_sum(test_set, 53)

print("\nCase 3: No subset sums to the target value (52)")
bfi_subset_sum(test_set, 52)

# Testing hs_subset_sum
heading = "\nHS Subset Sum"
print(heading)
for j in heading:
    print("-", end="")

print("\n\nCase 1: Target value (5) is in the set")
hs_subset_sum(test_set, 5)

print("\nCase 2: The sum of the set is the target value (53)")
hs_subset_sum(test_set, 53)

print("\nCase 3: No subset sums to the target value (52)")
hs_subset_sum(test_set, 52)

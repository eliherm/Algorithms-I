import sys


def f1(s):
    s_sum = 0
    for c in s:
        s_sum += ord(c)
    return s_sum


def f2(s):
    result = 0
    for c in s:
        result = 2 * result + ord(c)
    return result


def f2mod(s):
    result = 7
    for c in s:
        result = (31 * result + ord(c)) % sys.maxsize
    return result


with open("TheSunderingFloodASCII.txt") as input_file:
    hashtable1 = {}
    hashtable2 = {}
    word_count = 0

    for line in input_file:
        word_count += 1
        string_hash1 = f2mod(line[:-1])
        string_hash2 = f2mod(line[:-1])

        if string_hash1 in hashtable1:
            hashtable1[string_hash1].append(line[:-1])
        else:
            hashtable1[string_hash1] = [line[:-1]]

        """
        if string_hash2 in hashtable2:
            hashtable2[string_hash2].append(line[:-1])
        else:
            hashtable1[string_hash2] = [line[:-1]]
        """

    false_count = 0
    for hash_val in hashtable1.items():
        if len(hash_val[1]) > 1:
            for idx in range(1, len(hash_val[1])):
                if hash_val[1][idx] != hash_val[1][idx - 1]:
                    false_count += 1

    print(false_count / word_count)

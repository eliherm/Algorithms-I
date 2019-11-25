"""
Name: Elikem Hermon
Student Number: 20075527
I certify that this submission contains my own work, except as noted.
"""
import sys


def hash_string(s):
    """Returns the hash for a given string using a method shown in lab9"""
    hash_result = 0
    for char in s:
        hash_result = (31 * hash_result + ord(char)) % sys.maxsize
    return hash_result


def compare_lines(line1, line2):
    """Checks two lines for equality"""
    if hash_string(line1) != hash_string(line2):
        return False
    else:
        return line1 == line2


def lcs(lines1, lines2):
    """Uses the longest common subsequence algorithm to find the largest match between two files"""
    # Stores the length of the subsequence and the corresponding lines in each cell
    # table[x][y][0] -> Length of the lcs
    # table[x][y][1] -> Line numbers for file 1 corresponding to the lcs
    # table[x][y][2] -> Line numbers for file 2 corresponding to the lcs
    table = [[[0, '', ''] for x in range(len(lines2))] for x in range(len(lines1))]

    # Iterate through all lines for both files
    for i in range(len(lines1)):
        for j in range(len(lines2)):
            if compare_lines(lines1[i][0], lines2[j][0]):
                # The lines match
                if i == 0 or j == 0:
                    table[i][j][0] = 1  # Increment the length of the subsequence
                    table[i][j][1] = str(lines1[i][1]) + "\t"  # Add to the matched lines for file 1
                    table[i][j][2] = str(lines2[j][1]) + "\t"  # Add to the matched lines for file 2
                else:
                    table[i][j][0] = 1 + table[i - 1][j - 1][0]  # Increment the length of the subsequence
                    table[i][j][1] = table[i - 1][j - 1][1] + str(lines1[i][1]) + "\t"
                    table[i][j][2] = table[i - 1][j - 1][2] + str(lines2[j][1]) + "\t"
            else:
                # The lines do not match
                if i == 0 and j == 0:
                    table[i][j][0] = 0
                elif i == 0:
                    table[i][j][0] = int(table[0][j - 1][0] == 1)
                    table[i][j][1] = table[0][j - 1][1]
                    table[i][j][2] = table[0][j - 1][2]
                elif j == 0:
                    table[i][j][0] = int(table[i - 1][0][0] == 1)
                    table[i][j][1] = table[i - 1][0][1]
                    table[i][j][2] = table[i - 1][0][2]
                else:
                    # Select the direction which gives the max subsequence
                    table[i][j][0] = max(table[i - 1][j][0], table[i][j - 1][0], table[i - 1][j - 1][0])

                    # Check for the location of the max subsequence
                    if table[i][j][0] == table[i - 1][j][0]:
                        table[i][j][1] = table[i - 1][j][1]
                        table[i][j][2] = table[i - 1][j][2]
                    elif table[i][j][0] == table[i][j - 1][0]:
                        table[i][j][1] = table[i][j - 1][1]
                        table[i][j][2] = table[i][j - 1][2]
                    else:
                        table[i][j][1] = table[i - 1][j - 1][1]
                        table[i][j][2] = table[i - 1][j - 1][2]

    # The longest common subsequence is in the last cell of the array (bottom right)
    lcs_lines1 = table[-1][-1][1].split('\t')
    lcs_lines2 = table[-1][-1][2].split('\t')
    return list(map(int, lcs_lines1[:-1])), list(map(int, lcs_lines2[:-1]))  # Convert strings to integers


def parse_file(path):
    """Reads the lines of a given file"""
    with open(path, 'r') as input_file:
        lines = []  # Stores a tuple containing a line and it's line number
        line_num = 1
        # Iterate through each character in the file
        for line in input_file:
            lines.append((line, line_num))  # Append the tuple to the list
            line_num += 1  # Increment the line counter
    return lines


def read_input(file_num):
    """Retrieves filenames from the user"""
    try:
        file_name = input("Enter the path to " + file_num + ": ")
        file_lines = parse_file(file_name)
        file = {'name': file_name, 'lines': file_lines}
        return file
    except FileNotFoundError as e:
        # Check if the input is not a file
        print("'" + e.filename + "' was not found")
        read_input(file_num)
    except IsADirectoryError as e:
        # Check if the input is a directory
        print("'" + e.filename + "' is a directory")
        read_input(file_num)


def print_row(option, name1, name2, range1, range2):
    """Prints a row of the output"""
    if option == 0:
        # Output for a match
        print("{: <20} {: <20} {: <20} {: <20} {: <20}".format("Match:", name1 + ":", range1, name2 +
                                                               ":", range2))
    elif option == 1:
        # Output for a mismatch
        print("{: <20} {: <20} {: <20} {: <20} {: <20}".format("Mismatch:", name1 + ":", range1, name2 +
                                                               ":", range2))


def output_diffs(input1, input2):
    """Computes match and mismatch sections between the two files"""
    block1 = []  # Stores matched blocks in file 1
    block2 = []  # Stores matched blocks in file 2

    # Check if the beginning of both files have matches
    if input1['matches'][0] == 1:
        block1.append(input1['matches'][0])  # Append the line number
    if input2['matches'][0] == 1:
        block2.append(input2['matches'][0])  # Append the line number

    # A mismatch exists in the beginning of one or both of the files
    if len(block1) == 0 and len(block2) == 0:
        print_row(1, input1['name'], input2['name'], "<1.." + str(input1['matches'][0] - 1) + ">", "<1.."
                  + str(input2['matches'][0] - 1) + ">")
    elif len(block1) == 0:
        print_row(1, input1['name'], input2['name'], "<1.." + str(input1['matches'][0] - 1) + ">", "None")
    elif len(block2) == 0:
        print_row(1, input1['name'], input2['name'], "None", "<1.." + str(input2['matches'][0] - 1) + ">")

    # Iterate through common lines in both files
    for idx in range(1, len(input1['matches']) - 1):
        block1.append(input1['matches'][idx])  # Append the line number
        block2.append(input2['matches'][idx])  # Append the line number

        if (input1['matches'][idx + 1] != input1['matches'][idx] + 1) or (input2['matches'][idx + 1] != input2['matches'][idx] + 1):
            print_row(0, input1['name'], input2['name'], "<" + str(block1[0]) + ".." + str(block1[-1]) + ">", "<" +
                      str(block2[0]) + ".." + str(block2[-1]) + ">")

            # Reset the matched blocks
            block1.clear()
            block2.clear()

            # Check the source of the mismatch
            if (input1['matches'][idx + 1] != input1['matches'][idx] + 1) and (input2['matches'][idx + 1] != input2['matches'][idx] + 1):
                # Both files have a mismatch for the block
                print_row(1, input1['name'], input2['name'], "<" + str(input1['matches'][idx] + 1) + ".." +
                          str(input1['matches'][idx + 1] - 1) + ">", "<" + str(input2['matches'][idx] + 1) + ".." +
                          str(input2['matches'][idx + 1] - 1) + ">")
            elif input1['matches'][idx + 1] != input1['matches'][idx] + 1:
                # Only the first file has a mismatch for the block
                print_row(1, input1['name'], input2['name'], "<" + str(input1['matches'][idx] + 1) + ".." +
                          str(input1['matches'][idx + 1] - 1) + ">", "None")
            else:
                # Only the second file has a mismatch for the block
                print_row(1, input1['name'], input2['name'], "None", "<" + str(input2['matches'][idx] + 1) + ".." +
                          str(input2['matches'][idx + 1] - 1) + ">")

    # Check the last element of the matched lines
    block1.append(input1['matches'][-1])
    block2.append(input2['matches'][-1])

    # Print the output for the last block of matches
    print_row(0, input1['name'], input2['name'], "<" + str(block1[0]) + ".." + str(block1[-1]) + ">", "<" +
              str(block2[0]) + ".." + str(block2[-1]) + ">")

    # Check if there is a mismatch at the ends of the files
    if input1['matches'][-1] != input1['max_line'] and input2['matches'][-1] != input2['max_line']:
        # Both files have a mismatch for the block
        print_row(1, input1['name'], input2['name'], "<" + str(input1['matches'][-1] + 1) + ".." +
                  str(input1['max_line']) + ">", "<" + str(input2['matches'][-1] + 1) + ".." +
                  str(input2['max_line']) + ">")
    elif input1['matches'][-1] != input1['max_line']:
        # Only the first file has a mismatch for the block
        print_row(1, input1['name'], input2['name'], "<" + str(input1['matches'][-1] + 1) + ".." +
                  str(input1['max_line']) + ">", "None")
    elif input2['matches'][-1] != input2['max_line']:
        # Only the second file has a mismatch for the block
        print_row(1, input1['name'], input2['name'], "None", "<" + str(input2['matches'][-1] + 1) + ".." +
                  str(input2['max_line']) + ">")


# Receive the files from the user
file1 = read_input("file 1")
file2 = read_input("file 2")

# Compute the lines corresponding to the lcs for both files
file1_matches, file2_matches = lcs(file1['lines'], file2['lines'])
file1_info = {'name': file1['name'], 'matches': file1_matches, 'max_line': file1['lines'][-1][1]}
file2_info = {'name': file2['name'], 'matches': file2_matches, 'max_line': file2['lines'][-1][1]}

# Output the similarities and differences for both files
output_diffs(file1_info, file2_info)

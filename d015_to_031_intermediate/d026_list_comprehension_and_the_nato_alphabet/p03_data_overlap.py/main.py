# Read both given lists, line by line, and save the individual numbers as ints to separate lists.
with open('d015_to_031_intermediate/d026_list_comprehension_and_the_nato_alphabet/p03_data_overlap.py/file1.txt') as f:
    list_1 = [int(item) for item in f.readlines()]
with open('d015_to_031_intermediate/d026_list_comprehension_and_the_nato_alphabet/p03_data_overlap.py/file2.txt') as f:
    list_2 = [int(item) for item in f.readlines()]

# Loop through one list, checking if each item can be found in the other, adding them to the result if true, then print.
result = [item for item in list_1 if item in list_2]
print(result)

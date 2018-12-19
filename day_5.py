import numpy as np

data = []
for line in open('input_day5'):
    data.append(line.split('\n')[0])

combos_to_split = []
for letter in set(data[0].upper()):
    combos_to_split.append('{}{}'.format(letter, letter.lower()))
    combos_to_split.append('{}{}'.format(letter.lower(), letter))
    
print('Part 1')
new_test_str = data[0]
print('orig', len(new_test_str))
prev_len = 0
while prev_len != len(new_test_str):
    prev_len = len(new_test_str)
    for combo in combos_to_split:
        new_test_str = ''.join(new_test_str.split(combo))
    print(prev_len, len(new_test_str))

print('Part 2')
# part 2

new_test_str = data[0]
letters = []
reaction_len = []

for letter in set(data[0].upper()):
    removed_upper_letter_str = ''.join(new_test_str.split(letter.upper()))
    removed_upper_letter_str = ''.join(removed_upper_letter_str.split(letter.lower()))

    prev_len = 0
    while prev_len != len(removed_upper_letter_str):
        prev_len = len(removed_upper_letter_str)
        for combo in combos_to_split:
            removed_upper_letter_str = ''.join(removed_upper_letter_str.split(combo))
    print('Removed Letter {}'.format(letter), len(removed_upper_letter_str))
    letters.append(letter)
    reaction_len.append(len(removed_upper_letter_str))

wh_min = np.argmin(reaction_len)
print('Winner:', np.array(letters)[wh_min], np.array(reaction_len)[wh_min] )

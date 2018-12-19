import numpy as np
from collections import OrderedDict

# part 1
data = open('input_day7')
#data = open('test.txt')

#Fresh start
to_do = []
requirement = []

for line in data:
    split_list = line.split()
    requirement.append(split_list[1])
    to_do.append(split_list[7])

to_do = np.array(to_do)
requirement = np.array(requirement)

# find which letter(s) aren't in the requirement; if there are more than 1,
#   then the first alphabetically goes first.
no_req = []
for l in requirement:
    wh_l = np.where(np.array(to_do) == l)[0]
    if len(wh_l) == 0:
        no_req.append(l)

av_l = []
no_req = np.unique(no_req)

if len(no_req) > 1:
    done = [np.sort(no_req)[0]]
    av_l.extend(np.sort(no_req)[1:])
else:
    done = [no_req[0]]

while len(done) < len(np.unique(np.concatenate([to_do, requirement]))):

    for l, r in zip(to_do, requirement):
        # Checking that all of the requirements for the letter to be added are
        #   met before adding it
        full_req = np.where(to_do == l)[0]
        add_to_av = True # start true and change to false if anything fails
        for r2, l2 in zip(requirement[full_req], to_do[full_req]):
            if (r2 not in done) == True:
                add_to_av = False
        # Adding it if it's right
        if r in done and l not in done and add_to_av ==  True:
            av_l.append(l)

    # adding the letter alphabetically
    temp_done_l = np.sort(av_l)[0]
    print('appending {}'.format(temp_done_l))
    done.append(temp_done_l)

    # Removing any repeat letters
    av_l = [l for l in av_l if l != temp_done_l]
    print('Beginning; Done:{}, Av:{}'.format(done, av_l))

print(''.join(done))

# part 2

# the index of the letter will be the amount of time spent on that letter
#   assuming all of the letters are present, which is true on my input
time_seconds = np.sort(np.unique(np.concatenate([to_do, requirement])))
nworkers = 5
# worker 2 can't start until the first letter is complete 

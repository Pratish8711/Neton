l = [[ 'aangoo', 'mangoo','angom','mangoo'],
     ['orangee', 'orrge', 'rangeo'],
     ['ananab', 'anaanb', 'annabn']]

l2 = ['mango', 'orange', 'banana']

l3 = []

for i in l:
    p = []
    for j in l2:
        for k in i:
            if len(k) == len(j):
                match = True
                for char in j:
                    if k.count(char) != j.count(char):
                        match = False
                        break
                if match:
                    p.append(j)
                    break
    l3.append(p)

print(l3)


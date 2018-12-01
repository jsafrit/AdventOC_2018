freq = 0
seen = set()
seen.add(0)
dup = None

while True:
    with open('input.txt', 'r') as infile:
        for change in infile:
            freq += int(change)
            if freq not in seen:
                seen.add(freq)
            else:
                print('Duplicate Freq Found: {}'.format(freq))
                dup = freq
                break
    if dup:
        break
    print(f'End freq: {freq}')

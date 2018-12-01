"""
Puzzles for Dec 1st
"""


def get_final_freq():
    freq = 0

    with open('input.txt', 'r') as infile:
        for change in infile:
            freq += int(change)
    print(f'Final freq: {freq}')
    return freq


def get_first_duplicate_freq():
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
                    print(f'Duplicate Freq Found: {freq}')
                    return freq
        # print(f'End freq: {freq}')


if __name__ == '__main__':
    get_final_freq()
    get_first_duplicate_freq()

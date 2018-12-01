from itertools import cycle

def duplicateFrequency(data_input):
    freq_flact = []
    cur_freq = 0
    f = 0


    for freq in cycle(data_input):
        cur_freq += int(freq)
        if cur_freq in freq_flact:
            return (cur_freq)
        freq_flact.append(cur_freq)



if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        data_input = [int(i) for i in f.read().splitlines()]
    
    print(sum(data_input))
    print(duplicateFrequency(data_input))


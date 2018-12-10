

class FreqCalc(object):
    def __init__(self, operations):
        self.final_freq = 0
        for o in operations:
            self.final_freq += int(o)


if __name__ == '__main__':
    with open('./d1_input.txt') as _file:
        data = _file.read()

    output = FreqCalc(data.split())
    print ('Output is {}'.format(output.final_freq))

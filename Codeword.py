

class Codeword:

    def checkbits_needed(self, databits):
        """From the equation m + r + 1 <= 2^r"""
        m = len(databits)
        r = 1

        while m + r + 1 > 2**r:
            r += 1
        return r

    def create_parity(self, databits, r):
        code = []
        codelength = len(databits) + r
        datalength = len(databits)
        exponent = 0
        j = 0
        i = 1

        while i <= codelength:
            if i == 2**exponent:
                code.append('_')
                exponent += 1
            elif j < datalength:
                code.append(databits[j])
                j += 1
            i += 1

        print(code)

        return code

    def create_codeword(self, array, even):
        i = 0
        if even is True:
            while i < len(array):
                if array[i] == '_':
                    temp = self.extract_bits(array, i + 1)
                    if self.count(temp) % 2 == 0:
                        array[i] = '0'
                    else:
                        array[i] = '1'
                i += 1

        elif even is False:
            while i < len(array):
                if array[i] == '_':
                    temp = self.extract_bits(array, i + 1)
                    if self.count(temp) % 2 != 0:
                        array[i] = '0'
                    else:
                        array[i] = '1'
                i += 1

        return array

    def extract_bits(self, incomplete, parity):
        i = parity - 1
        ctr = 1
        use_bits = []

        while i < len(incomplete):
            if ctr <= (parity*2)/2 and incomplete[i] != '_':
                use_bits.append(incomplete[i])
            if ctr == parity*2:
                ctr = 0
            ctr += 1
            i += 1

        # print("Extracted")
        # print(use_bits)
        return use_bits

    def count(self, extracted):
        return extracted.count('1')

    def error_detection(self, codeword,  even):
        error = []
        i = 0
        exponent = 0

        if even is True:
            while i < len(codeword):
                if i == (2**exponent)-1:
                    temp = self.extract_bits(codeword, i + 1)
                    # print(codeword[i])
                    # print(temp)
                    if self.count(temp) % 2 != 0:
                        error.append(i+1)
                    exponent += 1
                i += 1

        elif even is False:
            while i < len(codeword):
                if i == (2**exponent)-1:
                    temp = self.extract_bits(codeword, i + 1)
                    if self.count(temp) % 2 == 0:
                        error.append(i)
                    exponent += 1
                i += 1
        print(error)
        return error


"""===============================   MAIN   ======================================"""
# todo: check the error_detector function
# PART I:
# length = int(input("Data bits Length: "))
# index = 0
transmitted = "10011010"
ed = Codeword()
#
# while index < length:
#     transmitted += input()
#     index += 1
#
r = ed.checkbits_needed(transmitted)
# print("r = % i" % r)
temp = ed.create_parity(transmitted, r)
transmitted = "".join(ed.create_codeword(temp, True))
print("Codeword (transmitted): ", transmitted)
# print("PARITY\n1. Even Parity\n2. Odd Parity")

# PART II:
index = 0
exp = 0
length = len(transmitted)
print("Length:", length)
temp = list(transmitted)
while index < length:
    if index != (2**exp)-1:
        temp[index] = input()
    else:
        print(temp[index])
        exp += 1
    index += 1

received = "".join(temp)
print("Codeword (receiver): ", received)
temp = ed.error_detection(received, True)
if len(temp) == 0:
    print("No error!")
else:
    index = 0
    bit = 0
    while index < len(temp):
        bit += temp[index]
        index += 1
    print("Erroneous bit: ", bit)

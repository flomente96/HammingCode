

class Codeword:

    def checkbits_needed(self, data_bits):
        """From the equation m + r + 1 <= 2^r"""
        m = len(data_bits)
        r = 1

        while m + r + 1 > 2**r:
            r += 1
        return r

    def create_parity(self, databits, r):
        code = []
        code_length = len(databits) + r
        data_length = len(databits)
        exponent = 0
        j = 0
        i = 1

        while i <= code_length:
            if i == 2**exponent:
                code.append('_')
                exponent += 1
            elif j < data_length:
                code.append(databits[j])
                j += 1
            i += 1

        return code

    def create_codeword(self, array, iseven):
        i = 0
        if iseven is True:
            while i < len(array):
                if array[i] == '_':
                    temp = self.extract_bits(array, i + 1)
                    if self.count(temp) % 2 == 0:
                        array[i] = '0'
                    else:
                        array[i] = '1'
                i += 1

        elif iseven is False:
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

        return use_bits

    def count(self, extracted):
        return extracted.count('1')

    def error_detection(self, codeword,  iseven):
        error = []
        i = 0
        exponent = 0

        if iseven is True:
            while i < len(codeword):
                if i == (2**exponent)-1:
                    temp = self.extract_bits(codeword, i + 1)
                    if self.count(temp) % 2 != 0:
                        error.append(i+1)
                    exponent += 1
                i += 1

        elif iseven is False:
            while i < len(codeword):
                if i == (2**exponent)-1:
                    temp = self.extract_bits(codeword, i + 1)
                    if self.count(temp) % 2 == 0:
                        error.append(i+1)
                    exponent += 1
                i += 1
        print(error)
        return error


"""===============================   MAIN   ======================================"""
#------------------------ PART I -----------------------------
index = 0
transmitted = ""
ed = Codeword()
print("***********************PART I***********************")
length = int(input("Data bits Length: "))
print("Input DATA BITS:")
while index < length:
    transmitted += input()
    index += 1

checkbits = ed.checkbits_needed(transmitted)
temp = ed.create_parity(transmitted, checkbits)
print("DATA bits + CHECK bits:\n", temp)
choice = int(input("Choose PARITY\t1. Even Parity\t2. Odd Parity\n"))
if choice == 1:
    even = True
elif choice == 2:
    even = False
else:
    raise ValueError("Out of range. Only 1 or 2 are the responses allowed.")
transmitted = "".join(ed.create_codeword(temp, even))
print("Codeword(transmitted): ", transmitted)

#------------------------ PART II ----------------------------
index = 0
exp = 0
received = ""
print("\n***********************PART II**********************")
length = int(input("Data bits Length: "))
print("Input CODEWORD:")
while index < length:
    received += input()
    index += 1

print("Codeword(receiver): ", received)
choice = int(input("Choose PARITY\t1. Even Parity\t2. Odd Parity\n"))
if choice == 1:
    even = True
elif choice == 2:
    even = False
else:
    raise ValueError("Out of range. Only 1 or 2 are the responses allowed.")

t = ed.error_detection(received, even)
if len(t) == 0:
    print("No error!")
else:
    index = 0
    bit = 0
    while index < len(t):
        bit += t[index]
        index += 1
    print("Erroneous bit: ", bit)

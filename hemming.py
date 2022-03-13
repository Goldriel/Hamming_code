from chek_input import *
import sys

def binari(num):
    b = ''
    while num > 0:
        b = str(num % 2) + b
        num //= 2
    b = b[:0] + '0' + b[0:]
    return str(b)

def blocs(bin_code):
    blocs_list = []
    i = 0
    tmp = ''
    while i < len(bin_code):
        if len (bin_code) % 2 != 0 and i >= len(bin_code) - 1:
            tmp = bin_code[i] + "00000000"
        else:
            tmp = bin_code[i] + bin_code[i + 1]
        blocs_list.append(tmp)
        i += 2
    return blocs_list

def main(num):
    dec_code = []
    bin_code = []
    chek_input(num)
    for i in range(len(num)):
        dec_code.append(ord(num[i]))
    for i in range(len(dec_code)):
        bin_code.append(binari(dec_code[i]))
    blocs_list = blocs(bin_code)
    print(blocs_list)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(input())
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("input error")
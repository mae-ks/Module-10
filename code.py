import sys

def asci(shift, sentence):
    modif, res = "", ""
    tracker = 0
    for line in sentence:
        for letter in line:
            if letter.isalpha():
                modif += letter.upper()
    for tracker in range(len(modif)):
        new_ord = ord(modif[tracker]) + int(shift)
        if new_ord > 90:
            new_ord = new_ord - 26
        new_chr = chr(new_ord)
        if tracker%50==0 and tracker !=0:
            res += "\n"
        elif tracker%5 == 0 and tracker != 0:
            res += " "
        res += new_chr
    return res

sent = input()
print(asci(sys.argv[1], sent))

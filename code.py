import sys

def asci(shift):
    modif, res = "", ""
    tracker = 0
    file = input()
    for letter in file:
        if letter.isalpha():
            modif += letter.upper()
    for letter in sys.stdin.read():
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

print(asci(sys.argv[1]))

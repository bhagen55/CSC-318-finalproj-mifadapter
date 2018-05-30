import csv
# Takes in a csv file that has 60 rows and 80 columns
# Outputs file in MIF format, mapping to octal addresses
# of the characters in the character rom.

# Character Address Map in hex:
map = {'@' : "00", 'A' : "01", 'B' : "02", 'C' : "03", 'D' : "04", 'E' : "05", 'F' : "06", 'G' : "07", 'H' : "08", 'I' : "09", 'J' : "0a", 'K' : "0b", 'L' : "0c", 'M' : "0d", 'N' : "0e", 'O' : "0f",
       'P' : "10", 'Q' : "11", 'R' : "12", 'S' : "13", 'T' : "14", 'U' : "15", 'V' : "16", 'W' : "17", 'X' : "18", 'Y' : "19", 'Z' : "1a", '[': "1b", 'dn': "1c", ']' : "1d", 'up': "1e", 'lf': "1f",
       ''  : "20", '!' : "21", '\"' : "22", '#' : "23", '$' : "24", '%' : "25", '&' : "26", '\'': "27", '(': "28", ')' : "29", '*' : "2a", '+' : "2b", ',' : "2c", '-' : "2d", '.' : "2e", '/' : "2f",
       '0' : "30", '1' : "31", '2' : "32", '3'  : "33", '4' : "34", '5' : "35", '6' : "36", '7' : "37", '8': "38", '9' : "39"}

def get_hex(string, dict):
    string = string.upper()
    return map[string]

output_arr = []

with open('monitor-file.csv', 'rt', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    address = 0
    address_prev = 0

    for row in reader:
        for char in row:
            output_arr.append(str(address) + "  :  " + get_hex(char, map) + ";")
            if (address - address_prev == 79):
                address += 49
                address_prev = address
            else:
                address += 1

    output_f = open("sentence.mif", "w+")
    output_f.write("WIDTH=6;" + '\r' + '\n')
    output_f.write("DEPTH=8192;" + '\r' + '\n')
    output_f.write("ADDRESS_RADIX=UNS;" + '\r' + '\n')
    output_f.write("DATA_RADIX=HEX;" + '\r' + '\n')
    output_f.write("CONTENT" + '\r' + '\n')
    output_f.write("BEGIN" + '\r' + '\n')
    for address_item in output_arr:
        output_f.write(address_item + '\r' + '\n')
    output_f.write('\r' + '\n')
    output_f.write("END;" + '\r' + '\n')
    output_f.close()
#print(str(output_arr))

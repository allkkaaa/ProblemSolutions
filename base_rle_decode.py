#1

import re

pair = re.findall(r'\d*\w', input())
result = ''
for i in range(len(pair)): 
    if pair[i][:-1].isdigit():
        result += (int(pair[i][:-1]) * pair[i][-1])
    else:
        result += pair[i][-1]
        continue
    
print(result)


#2 (с функциями)

import re

def split_decode_series(string):
    pair = re.findall(r'\d*\w', string)
    return pair

def decode_series(string):
    result = ''
    for i in range(len(string)): 
        if string[i][:-1].isdigit():
            result += (int(string[i][:-1]) * string[i][-1])
        else:
            result += string[i][-1]
            continue
    return result

def rle_decode(string):
    return decode_series(split_decode_series(string))

print(rle_decode(input()))



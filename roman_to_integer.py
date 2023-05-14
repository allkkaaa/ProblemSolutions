#1

a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
num = input()
sum = 0
for i in range(len(num)-1):
    if a[num[i]] < a[num[i + 1]]:
        sum -= a[num[i]]
    else:
        sum += a[num[i]]
sum += a[num[len(num)-1]]
print(sum)


#2 (leetcode)

class Solution(object):
    def romanToInt(self, s):
            d = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }

            s = s.replace("IV", "IIII")
            s = s.replace("IX", "VIIII")
            s = s.replace("XL", "XXXX")
            s = s.replace("XC", "LXXXX")
            s = s.replace("CD", "CCCC")
            s = s.replace("CM", "DCCCC")
                
            res = 0
            
            for i in s:
                for k in d.keys():
                    if i == k:
                        res += d[k]
            return res
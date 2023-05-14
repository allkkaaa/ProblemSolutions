#1

word = sorted((input().lower()))
word_two = sorted((input().lower()))
if word == word_two:
    print(True)
else:
    print(False)
    
    
#2

word = sorted(input().lower())
word_two = sorted(input().lower())
print(word == word_two)


#3

print(sorted(input().lower()) == sorted(input().lower()))
# 문자열 대소문자 구분없이 순서대로
# a=97 A=65


word = list(input())


for i in range(len(word)):
    for j in range(i, 0, -1):
        if int(ord(word[j])) < int(ord(word[j-1])):
            word[j], word[j-1] = word[j-1], word[j]
print("".join(word))
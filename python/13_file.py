with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

#strip
#처음 끝 whitespace 없애기
# print("            abc           def            ".strip())

#split

my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))

#.split()은 whitespace로 나눠줌
#문자열임 inpur과 마찬가지로
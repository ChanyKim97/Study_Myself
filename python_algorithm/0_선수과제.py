def is_palindrome(word):
    check = True
    for i in range(len(word)//2):
        if word[i] != word[len(word) - 1 - i]:
            check = False

    return check


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
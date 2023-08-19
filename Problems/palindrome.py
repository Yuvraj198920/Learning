# Ques- Palindrome number
# An palindrome is number which reads same backward and forward
# e.g. x = 121 => output: true
# e.g. x = 10 => output: false

def isPalindrome(x):
    if isinstance(x, str):
        return "False"
    else:
        reversed_arr = ''
        for i in range(len(str(x))-1, -1, -1):
            reversed_arr +=str(x)[i]
        reversed_arr = int(reversed_arr)
        if x == reversed_arr:
            return "True"
        else:
            return "False"

def chatgpt_checkPalindrome(x):
    if not isinstance(x, (int, float)):
        return  False
    else:
        x_str = str(x)
        reversed_str = x_str[::-1]
        return x_str==reversed_str

# Find palindrom without converting input to string
def is_palindrome_withoutstring(x):
    if x < 0:
        return  False
    else:
        revers_num = 0
        while x > revers_num:
            revers_num = revers_num * 10 + x % 10
            x= x // 10

        return  x == revers_num  or x==revers_num//10
s = isPalindrome("radar")
s_gpt = chatgpt_checkPalindrome("radar")
reverse_withoutstring = is_palindrome_withoutstring(1221)

print(s)
print(s_gpt)

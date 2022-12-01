import string

def is_palindrome(my_str):
    s = my_str.translate(str.maketrans("", "", string.punctuation))
    return "".join(s.lower().split()) == "".join(s.lower().split())[::-1]

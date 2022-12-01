import string
import pytest

# Read palindrome lists
test_file = open("palindromes.txt")

# Run tests
@pytest.mark.parametrize("my_str", test_file.readlines())
def test_palindrome(my_str):
    s = my_str.translate(str.maketrans("", "", string.punctuation))
    assert "".join(s.lower().split()) == "".join(s.lower().split())[::-1]

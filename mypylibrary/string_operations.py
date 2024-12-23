# mypylibrary/string_operations.py

def reverse_string(s):
    """Returns the reversed version of a string."""
    return s[::-1]

def capitalize_words(s):
    """Capitalizes the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())
from string_operations import reverse_string, capitalize_words

print(reverse_string("hello"))         # Output: "olleh"
print(capitalize_words("hello world")) # Output: "Hello World"

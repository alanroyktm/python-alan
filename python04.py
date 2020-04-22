string_input = input("Enter the word to check palindrome")
string_lower = string_input.lower()
def reverse(string):
    return string[::-1]

string_reverse = reverse(string_lower)

if string_lower == string_reverse:
    print("The given word is palindrome")
else:
    print("The given word is not a palindrome")

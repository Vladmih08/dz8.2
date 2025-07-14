import string
def is_palindrome(text: str)->str:
    text = str(text)
    text = text.lower() #Із завдання з хештегом
    text = text.replace(' ', '')#Із завдання з хештегом
    text2 = ""
    for bukva in text:
        if bukva not in string.punctuation:
            text2 += bukva
    text_palindrome = text2[::-1]
    return text2 == text_palindrome
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
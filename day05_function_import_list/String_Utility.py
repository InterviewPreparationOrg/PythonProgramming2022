def reverse_string(string):  # 'ABCD'
    result = ''  # DCBA
    i = len(string) - 1
    while i >= 0:
        result += string[i]
        i -= 1

    return result


# print('Java'[::-1])

def is_palindrome(string):
    reverse = reverse_string(string)
    return reverse.lower() == str(string).lower()


"""
3. create a function named reverse that passes one string parameter, the method can return the reversed string

            Ex:
                str = "Java";

                reverse(str) ==> avaJ

4. By using the reverse method above to create another method named isPalindrome  that passes a String parameter, the method returns true if the string is palindrome, otherwise returns false

            Ex:
                str = "Level"

                isPalindrome(str) ===> true
                
                Anna
                
                annA
                
                
"""

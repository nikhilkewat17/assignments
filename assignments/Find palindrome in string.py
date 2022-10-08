''' Problem 3:
Find the longest palindrome from the given string. Palindrome is a word, phrase, or sequence that reads the
same backwards as forwards, e.g. madam, civic, radar'''

def find_longest_palindrome(s):
    longest = ''
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word
    return longest


print(find_longest_palindrome('babad'))

print(find_longest_palindrome('cbbd'))



def longest_palindromic_substring(s):
    if len(s) <2:
        return ""
    
    longest_palindrome = ""

    def extend_from_center(s,l,r):
        while l >= 0 and r <len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    for i in range(len(s)):
        single_center_palindrome = extend_from_center(s, i, i)
        double_center_palindrome = extend_from_center(s, i, i+1)
        
        if len(single_center_palindrome) > len(longest_palindrome):
            longest_palindrome = single_center_palindrome
        if len(double_center_palindrome) > len(longest_palindrome):
            longest_palindrome = double_center_palindrome
            
    if len(longest_palindrome) < 2:
        return ""

        
    return longest_palindrome




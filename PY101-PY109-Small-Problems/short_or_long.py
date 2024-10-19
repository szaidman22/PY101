# Write a function that takes two strings 
# as arguments, determines the length of the 
# two strings, and then returns the result of 
# concatenating the shorter string, the longer 
# string, and the shorter string once again. You 
# may assume that the strings are of different lengths.

def short_long(string1, string2):
    short = string1 if len(string2) >= len(string1) else string2

    long = string2 if short == string1 else string1

    return short + long + short

print(short_long('hhhhhhhhhhhhh' , 'squablafa'))

# interesting other solutions

# short, long = (str1, str2) if len(str1) < len(str2) else (str2, str1)

# sorted_strs = sorted([str1, str2], key=len)
# return sorted_strs[0] + sorted_strs[1] + sorted_strs[0]

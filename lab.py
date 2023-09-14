# Replace several characters in a string with other characters
# E.G. Replace "a" with "AA", "e" with "EE", "i" with "II"

# This string:
# 'This is just a string with chars to be replaced'

# becomes:
# 'Th  II  s   II  s just   AA   str  II  ng w  II  th ch  AA  rs to b  EE   r  EE  pl  AA  c  EE  d'

# When 'i' is replaced by '  II  ', 'e' is replaced by '  EE  ', 'a' is replaced by '  AA  '

def replace_char(my_string):
    replace_a = my_string.replace("a", "AA")
    replace_e = replace_a.replace("e", "EE")
    replace_i = replace_e.replace("i", "II")
    return replace_i

print(replace_char("the cow jumped over the moon"))
print(replace_char("hi there"))
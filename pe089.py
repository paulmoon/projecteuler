import re
import time

# Replace:
# VIIII with IX
# IIII  with IV
# LXXXX with XC
# XXXX  with XL
# CCCC  with CD
# DCCCC with CM

start = time.clock()
s = open("roman.txt", "r").read()
print (len(s) - len(re.sub("VIIII|IIII|LXXXX|XXXX|CCCC|DCCCC", "ZZ", s)))
print (time.clock() - start)

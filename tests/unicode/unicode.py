# Test a UTF-8 encoded literal
s = "asdf©qwer"
for i in range(len(s)):
    print("s[%d]: %s   %X"%(i, s[i], ord(s[i])))

# Test all three forms of Unicode escape, and
# all blocks of UTF-8 byte patterns
s = "a\xA9\xFF\u0123\u0800\uFFEE\U0001F44C"
for i in range(-len(s), len(s)):
    print("s[%d]: %s   %X"%(i, s[i], ord(s[i])))
    print("s[:%d]: %d chars, '%s'"%(i, len(s[:i]), s[:i]))
    for j in range(i, len(s)):
        print("s[%d:%d]: %d chars, '%s'"%(i, j, len(s[i:j]), s[i:j]))
    print("s[%d:]: %d chars, '%s'"%(i, len(s[i:]), s[i:]))

# Test UTF-8 encode and decode
enc = s.encode()
print(enc, enc.decode() == s)

def revv(s):
    def rev(s):
        if len(s) == 0 or len(s) == 1:
            return s
        else:
            return str(s[len(s) - 1] + rev(s[0:len(s) - 1]))
    if rev(s)==s:
        return True
    else:
        return False
s="aba"
print(revv(s))

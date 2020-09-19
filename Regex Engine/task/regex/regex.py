# write your code here
import sys
sys.setrecursionlimit(10000)


def test(r, s):

    if len(r) == 0:
        return True
    elif len(s) == 0:
        return False
    elif len(r) > 1 and r[0] == '\\':
        if s[0] == '\\':
            return test(r[2:], s[2:])
        elif len(r) > 3 and r[:1] == '\\\\' and r[1] in ['^', '$', '?', '*', '+', '.'] and r[1] == s[0]:
            return test(r[3:], s[1:])
        else:
            return test(r[1:], s)
    elif r[0] == '^':
        return test(r[2:], s[1:]) if r[1] == s[0] or r[1] == '.' else False
    elif len(r) > 1 and r[1] == '$':
        return True if r[0] == s or r[0] == '.' else False
    elif len(r) > 1 and r[1] == '*':
        return asterisk(r, s)
    elif len(r) > 1 and r[1] == '+':
        return plus(r, s)
    elif len(r) > 1 and r[1] == '?':
        if len(r) == 2:
            return True
        elif r[0] == s[0] and r[2] == s[1]:
            return test(r[2:], s[1:])
        elif r[2] == s[0]:
            return test(r[2:], s)
        else:
            return False
    elif r[0] == s[0] or r[0] == '.':
        return test(r[1:], s[1:])
    else:
        return test(r, s[1:])


def asterisk(r, s):
    if r[0] == s[0] or r[0] == '.':
        if len(r) == 2:
            return True
        if r[2] == s[1]:
            return test(r[2:], s[1:])
        else:
            return asterisk(r, s[1:])
    elif r[2] == s[0]:
        return test(r[2:], s)
    else:
        return asterisk(r, s[1:])


def plus(r, s):
    if r[0] == s[0] or r[0] == '.':
        return test(r[2:], s[1:])
    elif r[0] == r[1]:
        return plus(r[1:], s)
    else:
        return False


regexp, string = input().split('|')
print(test(regexp, string))


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    typesparan = ['(', ')', '[', ']', '{', '}']

    ret = True
    for i in range(0, len(typesparan), 2):
        if s.count(typesparan[i]) != s.count(typesparan[i + 1]):
            return False



    return ret

print(isValid('([)]'))
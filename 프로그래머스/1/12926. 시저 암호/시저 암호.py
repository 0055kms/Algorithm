def solution(s, n):
    answer = ''
    """
    A 65
    Z 90
    a 97
    z 122
    """
    for c in s:
        val = ord(c)
        if 65 <= val <= 90:
            if val + n > 90:
                val = val + n - 26
            else: val = val + n
        if 97 <= val <= 122:
            if val + n > 122:
                val = val + n - 26
            else: val = val + n
        answer += chr(val)
    return answer
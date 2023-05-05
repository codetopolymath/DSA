from collections import Counter

def check_pattern(pattern):
    if "b" in pattern and pattern.index("b") < pattern.index("a"):
        return False
    else:
        return True

print(check_pattern("baaaaaaabbbbbbb"))
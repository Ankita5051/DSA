import re

def solve(table, st):
    arr = [0] * 26
    lines = table.split("\n")   # correct split

    for line in lines:
        if not line.strip():
            continue
        
        # Split using both ',' and '|'
        parts = re.split('[,|]', line)
        parts = [p.strip() for p in parts if p.strip()]  # clean blanks

        value = int(parts[-1])  # the last value is 0/1

        for c in parts[:-1]:
            arr[ord(c) - ord('a')] = value

    # Convert input string
    result = []
    print(arr)
    print(result)


table = """a, b, c, g, e | 0
f, g, h, u | 0
i, j, k, l, o | 0
p, q, r, s, t | 0
u, v, w, x, y | 1
"""

st = "hello"
solve(table, st)

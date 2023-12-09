
nums = "0123456789"
nums2 = [k for k in nums] + ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums2r = [k[::-1] for k in nums2]
with open("2023/day1-input.txt", "r") as f:
    data = f.read().split("\n")
    # part 1
    s = 0
    for l in data:
        k = ""
        for c in l:
            if c in nums:
                k = c
                break
        for c in l[::-1]:
            if c in nums:
                k += c
                break
        s += int(k)
    print(s)

    # part 2
    s = 0
    for l in data:
        k = 0
        j = 0
        i = 1000000000
        for n in nums2:
            try:
                m = l.index(n)
                if m < i:
                    i = m
                    k = 10 * (nums2.index(n) % 10)
            except:
                pass
        i = 1000000000
        l2 = l[::-1]
        for n in nums2r:
            try:
                m = l2.index(n)
                if m < i:
                    i = m
                    j = nums2r.index(n) % 10
            except:
                pass
        s += k + j
    print(s)

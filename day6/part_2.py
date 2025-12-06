from functools import reduce
ops = {
    "*",
    "+"
}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    nums = []
    result = 0
    o = ""
    for col in range(len(lines[0])):
        b_c = 0
        c_val = ""
        for row in range(len(lines)):
            try:
                v = lines[row][col]               
                if v in ops:
                    o = v
                    continue
                if len(v.strip()) == 1:
                    c_val += v
                    b_c += 1
            except:
                pass
        if b_c != 0:
            nums.append(int(c_val))
        if b_c == 0:
            b_c = 0
            if o == "*":
                result += int(reduce(lambda x, y: x*y, nums, 1))
            elif o == "+":
                result += sum(nums)       
            o = ""
            nums = []
            
    print(result)

hcl_fields = set([str(i) for i in range(10)]+["a","b","c","d","e","f"])
ecl_fields = set(["amb","blu","brn","gry","grn","hzl","oth"])
def isValid(fields): 
    have = set(fields.keys())
    if have != required:
        return False 
    if not (1920 <= int(fields["byr"]) <= 2002): return False
    if not (2010 <= int(fields["iyr"]) <= 2020): return False 
    if not (2020 <= int(fields["eyr"]) <= 2030): return False

    system = fields["hgt"][-2:]
    if system not in ["cm", "in"]: return False 

    height = int(fields["hgt"][:-2])
    if system == "cm":
        if not (150 <= height <= 193): return False 
    if system == "in":
        if not(59 <= height <= 76): return False 

    hashtag = fields["hcl"][0]
    other = fields["hcl"][1:]
    if hashtag != "#":
        return False 
    for x in other:
        if x not in hcl_fields: return False
    if fields["ecl"] not in ecl_fields:
        return False 
    if not (fields["pid"].isdigit() and len(fields["pid"]) == 9):
        return False 
    # fields["cid"]
    return True 
ans = 0
required = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
while True:
    line = input()
    fields = {}
    valid = True 
    while line:
        split_by_space = line.split(" ")
        for x in split_by_space:
            key, val = x.split(":")
            if key != "cid": fields[key] = val
        line = input()
    if isValid(fields): ans += 1
    print(ans)
print(valid)
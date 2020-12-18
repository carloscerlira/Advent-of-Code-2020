from collections import defaultdict

def find_ways(adj):
    ans = [0]
    shiny = "shiny gold"
    # def dfs(bag):
    #     if bag in seen: return False 
    #     seen.add(bag)
    #     if bag == tar: return True
    #     if bag not in adj: return False 
    #     for inside_bag in adj[bag]:
    #         if dfs(inside_bag): return True 
    #     return False 
    
    def dfs(bag):
        if bag not in adj: return 1
        contains = 1
        for inside_bag, amount in adj[bag]:
            contains += amount*dfs(inside_bag)
        return contains
    # ans = 0
    # for bag in adj:
    #     if bag == tar: continue
    #     seen = set()
    #     if dfs(bag): ans += 1
    return dfs(shiny)-1


adj = defaultdict(list)
line = input()
while line: 
    space_split = line.split(" ") 
    n = len(space_split)
    bag = space_split[0]+" "+space_split[1]
    digits = [i for i in range(n) if space_split[i].isdigit()]
    for i in digits:
        amount = int(space_split[i])
        inside_bag = space_split[i+1]+" "+space_split[i+2]
        adj[bag].append([inside_bag, amount])
    line = input()

print(find_ways(adj))
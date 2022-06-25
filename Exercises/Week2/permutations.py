# returns all permutations of a set
def permutations(set):
    if len(set) <= 1: return set
    
    all_perms = []
 
    first_element = set[0:1]
    subset = set[1:]
    
    partial = permutations(subset)
    for permutation in partial:
        for index in range(len(set)):
            new_perm = list(permutation[:index])
            new_perm.extend(first_element)
            new_perm.extend(permutation[index:])
            all_perms.append(new_perm)
                
    return all_perms

def main():
    test = (["d","o","g"])
    for permutation in permutations(test):
        print(permutation)

main()

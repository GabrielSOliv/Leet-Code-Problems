def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hm = defaultdict(list)

    for i in strs:
        count = [0] * 26

        for caract in i:
            count[ord(caract) - ord('a')] += 1
        
        hm[tuple(count)].append(i)
    
    return hm.values()

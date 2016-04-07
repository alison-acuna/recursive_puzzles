def anagram(n):
    if n == "":
        return [n]
    else:
        answer_set = set()
        for w in anagram(n[1:]):
            for pos in range(len(w)+1):
                answer_set.add(w[:pos]+n[0]+w[pos:])
        return answer_set

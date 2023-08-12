
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances

    return distances[-1]



def jaro_similarity(s1, s2):
    if not s1 or not s2:
        return 0.0

    len1, len2 = len(s1), len(s2)
    max_dist = (max(len1, len2) // 2) - 1

    matches = 0
    transpositions = 0
    flagged_1 = []
    flagged_2 = []

    for i, c1 in enumerate(s1):
        left_bound = max(0, i - max_dist)
        right_bound = min(i + max_dist + 1, len2)
        for j, c2 in enumerate(s2[left_bound:right_bound], left_bound):
            if c1 == c2 and j not in flagged_2:
                matches += 1
                flagged_1.append(i)
                flagged_2.append(j)
                break

    flagged_2.sort()

    for i, j in zip(flagged_1, flagged_2):
        if s1[i] != s2[j]:
            transpositions += 1

    if matches == 0:
        return 0.0

    return (1/3) * (matches / len1 + matches / len2 + (matches - transpositions // 2) / matches)

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud")

    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

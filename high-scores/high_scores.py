def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    v = []
    if len(scores) >3:
        x = max(scores)
        scores.remove(x)
        v.append(x)
        y = max(scores)
        scores.remove(y)
        v.append(y)
        z = max(scores)
        scores.remove(z)
        v.append(z)
        return v
    else:
        
        return sorted(scores, reverse=True)[:3]
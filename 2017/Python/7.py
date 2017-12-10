#!/usr/bin/env python3

info = {}

try:
    while True:
        parts = input().split(' -> ')
        name, weight_str = parts[0].split(' ')
        weight = int(weight_str[1:-1])
        holding = parts[1].split(', ') if len(parts) > 1 else []
        info[name] = {
            'weight': weight,
            'holding': holding
        }
except EOFError:
    pass


## PART 1

bottom_program = list(filter(lambda p: not any(any(p in h for h in v['holding']) for v in info.values()), info.keys()))[0]
print(bottom_program)

## PART 2

def compound_weight(program):
    if '_compound_weight' in info[program]:
        return info[program]['_compound_weight']
    weight = info[program]['weight']
    weight += sum(compound_weight(p) for p in info[program]['holding'])
    info[program]['_compound_weight'] = weight
    return weight

def find_imbalance(program):
    foo = {}
    for subprogram in info[program]['holding']:
        weight = compound_weight(subprogram)
        elem = foo.get(weight, [])
        elem.append(subprogram)
        foo[weight] = elem
    if len(foo.keys()) < 2:
        return ''
    else:
        other_weight = sorted(foo.keys(), key=lambda k: len(foo[k]))[0]
        other = foo[other_weight][0]
        return find_imbalance(other) or other

def find_parent(program):
    ans = list(filter(lambda p: program in info[p]['holding'], info.keys()))
    if len(ans) != 1:
        return None
    return ans[0]

imbalanced = find_imbalance(bottom_program)
imbalanced_weight = info[imbalanced]['_compound_weight']
siblings = info[find_parent(imbalanced)]['holding']
for sibling in siblings:
    if sibling != imbalanced:
        diff = abs(info[sibling]['_compound_weight'] - imbalanced_weight)
        print(info[imbalanced]['weight'] - diff)
        break

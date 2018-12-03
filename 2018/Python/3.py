#!/usr/bin/env python3
import sys
import re

claim_re = re.compile(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')
claims = [list(map(int, claim_re.search(line).groups())) for line in sys.stdin]

claims_dict = {}

for claim in claims:
    claim_id, left, top, width, height = claim
    for x in range(left, left + width):
        for y in range(top, top + height):
            claims_dict[(x, y)] = claims_dict.get((x, y), 0) + 1

overlapping_claims_dict = { pos: claims_count for pos, claims_count in claims_dict.items()
                            if claims_count > 1 }

print(len(overlapping_claims_dict))


def is_not_overlapping(claim):
    global overlapping_claims_dict
    claim_id, left, top, width, height = claim
    for x in range(left, left + width):
        for y in range(top, top + height):
            if (x, y) in overlapping_claims_dict:
                return False
    return True


for claim in claims:
    if is_not_overlapping(claim):
        print(claim[0])

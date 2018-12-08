#!/usr/bin/env python3
import sys

input = list(map(int, sys.stdin.read().split(' ')))


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def __repr__(self, prefix=''):
        ans = f'{prefix}metadata: {self.metadata}, children ({len(self.children)}):\n'
        for child in self.children:
            ans += child.__repr__(prefix + '    ')
        return ans


def read_tree(input, start_index=0):
    children_count = input[start_index]
    metadata_count = input[start_index + 1]
    children = []
    metadata = []
    current_index = start_index + 2
    for _ in range(children_count):
        node, current_index = read_tree(input, current_index)
        children.append(node)
    for _ in range(metadata_count):
        metadata.append(input[current_index])
        current_index += 1
    return Node(children, metadata), current_index


def count_metadata(node):
    ans = sum(node.metadata)
    if node.children:
        ans += sum(map(count_metadata, node.children))
    return ans


def count_value_part2(node):
    ans = 0
    if node.children:
        for m in node.metadata:
            i = m - 1
            if i in range(len(node.children)):
                ans += count_value_part2(node.children[i])
    else:
        ans += sum(node.metadata)
    return ans


tree = read_tree(input)[0]
print(count_metadata(tree))
print(count_value_part2(tree))

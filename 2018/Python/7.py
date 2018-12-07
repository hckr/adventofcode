#!/usr/bin/env python3
import sys
import re

tasks = []
dependencies = {}

for dependency, task in re.findall(r'Step (.) must be finished before step (.) can begin', sys.stdin.read()):
    tasks.append(task)
    tasks.append(dependency)
    dependencies[task] = dependencies.get(task, []) + [dependency]

tasks = list(sorted(set(tasks)))


def try_do_task(task, done_tasks):
    for dependency in dependencies.get(task, []):
        if dependency not in done_tasks:
            return False
    return True


def order_tasks(tasks, dependencies):
    tasks_left = tasks[:]
    done_tasks = []
    while len(tasks_left) > 0:
        for task in tasks_left:
            if try_do_task(task, done_tasks):
                tasks_left.remove(task)
                done_tasks.append(task)
                break
    return done_tasks


print(''.join(order_tasks(tasks, dependencies)))

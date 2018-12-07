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


def can_be_done(task, done_tasks):
    for dependency in dependencies.get(task, []):
        if dependency not in done_tasks:
            return False
    return True


def order_tasks_workers(tasks, dependencies, workers=1, time_func=lambda task: 0):
    tasks_count = len(tasks)
    tasks_left = tasks[:]
    done_tasks = []
    workers_tasks = [None] * workers
    workers_time_left = [1] * workers
    time_elapsed = 0
    while len(done_tasks) < tasks_count:
        for w, time in enumerate(workers_time_left):
            if time == 0:
                if workers_tasks[w] is not None:
                    done_tasks.append(workers_tasks[w])
                    workers_tasks[w] = None
        for w, task in enumerate(workers_tasks):
            if task is None:
                for task in tasks_left:
                    if can_be_done(task, done_tasks):
                        tasks_left.remove(task)
                        workers_tasks[w] = task
                        workers_time_left[w] = time_func(task)
                        break
        try:
            subtrahend = min([t for t in workers_time_left if t > 0])
            time_elapsed += subtrahend
        except ValueError:  # min() arg is an empty sequence
            pass
        # print(time_elapsed, workers_tasks, done_tasks, workers_time_left, tasks_left)
        for w, time in enumerate(workers_time_left):
            if time > 0:
                workers_time_left[w] -= subtrahend
    return done_tasks, time_elapsed


print(''.join(order_tasks_workers(tasks, dependencies)[0]))
print(order_tasks_workers(tasks, dependencies, workers=5,
      time_func=lambda task: ord(task) - 4)[1])

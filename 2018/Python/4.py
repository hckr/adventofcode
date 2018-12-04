#!/usr/bin/env python3
import sys
import re
from pprint import pprint

log_re = re.compile(r'\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2})\] (.+)')
logs = [tuple(log_re.search(line).groups()) for line in sys.stdin]
logs.sort()

current_guard = None
last_fall_asleep_minute = None
sleep_info = {}
for log in logs:
    date, hour, minute, event = log
    minute = int(minute)
    if 'begins shift' in event:
        current_guard = int(re.search(r'(\d+)', event).group(1))
        continue
    if event == "falls asleep":
        last_fall_asleep_minute = minute
        continue
    if event == "wakes up":
        current_guard_sleep_info = sleep_info.get(current_guard, {
            'total': 0,
            'cumulated_minutes': [0] * 60
        })
        current_guard_sleep_info['total'] += minute - last_fall_asleep_minute
        for m in range(last_fall_asleep_minute, minute):
            current_guard_sleep_info['cumulated_minutes'][m] += 1
        sleep_info[current_guard] = current_guard_sleep_info
        continue

most_sleeping_guard = max(sleep_info.items(), key=lambda x: x[1]['total'])[0]
his_most_frequent_minute = (max(enumerate(sleep_info[most_sleeping_guard]['cumulated_minutes']),
                            key=lambda x: x[1])[0])
print(most_sleeping_guard * his_most_frequent_minute)

most_frequent_guard = None
his_minute = None
max_minute_frequency = 0

for guard, info in sleep_info.items():
    minute, freq = max(enumerate(info['cumulated_minutes']), key=lambda x: x[1])
    if freq > max_minute_frequency:
        max_minute_frequency = freq
        his_minute = minute
        most_frequent_guard = guard

print(most_frequent_guard * his_minute)

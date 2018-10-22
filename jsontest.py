#!/usr/bin/env python3

data = [
    {
        'user_id': 1000,
        'name': 'Shiyan',
        'pass': 10,
        'study_time': 50
    },
    {
        'user_id': 2000,
        'name': 'Lou',
        'pass': 15,
        'study_time': 171
    }
]

filename = "/tmp/jsontest.json"

import json

with open(filename, 'w+') as f:
    json.dump(data, f)
    f.seek(0)
    print(f.read())


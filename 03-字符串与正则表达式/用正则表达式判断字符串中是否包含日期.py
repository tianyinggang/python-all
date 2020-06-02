# q1

import re

print(re.match('.*hello', 'ahello'))

# q2

s = 'Today is 2013-12-01.'
m = re.match('.*\d{4}-\d{2}-\d{2}.*',s)

if m is not None:
    print(m.group())


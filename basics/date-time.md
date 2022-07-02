# Date and Time

- `time` module: `import time`
  - provides functions for working with times and for converting between representations.
  - `time.time()` returns the current system time in ticks since `00:00:00 hrs Jan 1, 1970`.

## Get current time

```python

import time

local_time = time.localtime(time.time())
print ("Local current time: " + local_time)

# output:
# Local current time : time.struct_time(tm_year=2013, tm_mon=7,
# tm_mday=17, tm_hour=21, tm_min=26, tm_sec=3, tm_wday=2, tm_yday=198, tm_isdst=0)

```

## Get formatted time

```python

import time
localtime = time.asctime(time.localtime(time.time()))
print("Local current time:", localtime)

# output:
# Local current time : Tue Jan 13 10:17:09 2009

```

## Get Calendar

```python

import calendar

cal = calendar.month(2008, 1)
print(cal)

```

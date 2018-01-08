'''
Date time related utility functions.
'''
import time
import datetime

def to_seconds(dt):
    '''
    Turn datetime object into seconds
    '''
    return time.mktime(dt.timetuple())

def round_to_bucket(start_time, secs, time_bucket):
    '''
    Round a time stamp in seconds into a time bucket.

    Args:
        start_time (int): epoch seconds for start of time buckets
        secs (int): Timestamp to be bucketed
        time_bucket (int): Time bucket size in seconds

    Example:
        >>> round_to_bucket(df['start_time'].min(), to_seconds(rec.start_time), 10*60)
    '''
    res = secs % time_bucket
    return (((secs - res) - start) / time_bucket)

def convert_duration(dur):
    '''
    Convert a duration string to seconds. Valid
    durations are:
        seconds = s
        minutes = m
        hours = h
        days = d

    Examples
        print(convert_duration("10m"))

    '''
    if isinstance(dur, int):
        return dur

    unit = dur[-1]
    if unit not in ['s', 'm', 'h', 'd']:
        raise ValueError('Converting duration requires denoating durations '
                         'current measurement. {} does not meet '
                         'the requirements of specifying seconds '
                         ', minutes, hours or days'.format(dur))

    dur = int(dur[:-1])
    if unit == 's':
        return dur
    elif unit == 'm':
        return dur * 60
    elif unit == 'h':
        return dur * 60 * 60
    elif unit == 'd':
        return dur * 60 * 60 * 24

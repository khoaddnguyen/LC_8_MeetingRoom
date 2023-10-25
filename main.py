# Given an array of meeting time intervals consisting of start and end times
# [[s1, e1], [s2, e2],...] (si < ei) (notes: each meeting time is a tuple or pair of values)
# determine if person could attend all meetings

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeeting(self, intervals):  # interval as an object of 2 members (start and end)
        intervals.sort(key=lambda i: i.start)  # input of i for interval

        for j in range(1, len(intervals)):  # j for index
            i1 = intervals[j - 1]
            i2 = intervals[j]

            if i1.end > i2.start:
                return False
        return True
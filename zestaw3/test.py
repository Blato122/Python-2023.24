class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print("{} {}".format(time1, time2))   # Python wywołuje str()
print("{}".format([time1, time2]))   # Python wywołuje repr()
class UndergroundSystem(object):

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = defaultdict(lambda: [0, 0])
    
    def checkIn(self, id, stationName, t):
        self.check_in_data[id] = [stationName, t]
    
    def checkOut(self, id, stationName, t):
        startStation, startTime = self.check_in_data[id]
        self.journey_data[(startStation, stationName)][0] += (t - startTime)
        self.journey_data[(startStation, stationName)][1] += 1
    
    def getAverageTime(self, startStation, endStation):
        total_time, total_trips = self.journey_data[(startStation, endStation)]
        if total_time == 0:
            return 0.0
        return float(total_time) / total_trips
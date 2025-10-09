class UndergroundSystem(object):

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = defaultdict(lambda: [0, 0])

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.check_in_data[id]
        self.journey_data[(startStation, stationName)][0] += (t - startTime)
        self.journey_data[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        total_time, total_trips = self.journey_data[(startStation, endStation)]
        if total_time == 0:
            return 0.0
        return float(total_time) / total_trips

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
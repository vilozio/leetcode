class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        stations.append([target, float('inf')])
        dp = [(startFuel, 0)]
        for station_position, station_fuel in stations:
            min_stops = float('inf')
            max_fuel = float('-inf')
            for state_fuel, state_stops in dp:
                if state_fuel >= station_position and state_stops <= min_stops:
                    if state_stops == min_stops:
                        max_fuel = max(max_fuel, state_fuel)
                    else:
                        max_fuel = state_fuel
                        min_stops = state_stops
            if min_stops == float('inf'):  # Station is not reachable.
                return -1
            dp.append((max_fuel + station_fuel, min_stops + 1))
        return dp[-1][1] - 1  # Last station stop doesn't count.

    
# target = 100, startFuel = 10, stations = [[10, 50], [20, 10], [50, 70]]
#
# stations  = [[10, 50], [20, 10], [50, 70], [100, inf]]
# dp        = [(10, 0), (60, 1), (70, 2), (130, 2)]
# station_position, station_fuel = 20, 10
# min_stops = 1
# max_fuel  = 60
# state.fuel, state.stops = 60, 1

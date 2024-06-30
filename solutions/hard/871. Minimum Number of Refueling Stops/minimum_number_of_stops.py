class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        elif not stations:
            return -1
        dp = [startFuel] + [-1 for _ in range(len(stations))]
        for station_i, (station_position, station_fuel) in enumerate(stations):
            new_state = []
            for max_fuel in dp[:station_i + 1]:
                if max_fuel >= station_position:
                    new_state.append(max_fuel + station_fuel)
                else:
                    new_state.append(-1)
            if sum(new_state) == -len(new_state):  # Station is not reachable.
                return -1
            for state_i, new_fuel in enumerate(new_state):
                dp[state_i + 1] = max(dp[state_i + 1], new_fuel)
        for stops, fuel in enumerate(dp):
            if fuel >= target:
                return stops
        return -1

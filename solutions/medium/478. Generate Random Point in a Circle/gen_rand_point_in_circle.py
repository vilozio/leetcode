import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
    def randPoint(self) -> List[float]:
        theta = uniform(0, 2 * pi)
        r = self.radius * sqrt(uniform(0, 1))
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return x + self.x_center, y + self.y_center
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

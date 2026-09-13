class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) 
        fleet =0
        slowest =0

        for pos,speed in cars:
            time = (target - pos)/speed

            if time > slowest:
                fleet +=1
                slowest = time

        return fleet
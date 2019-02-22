class SleepyCow:

    def __init__(self):
        self.input = open("herding.in", "r")
        self.output = open("herding.out", "w")
        self.positions = []
        self.distances = []
        self.maxDistance = 0
        for position in self.input.readline().split():
            self.positions.append(int(position))
        self.getDistance()

    def minMoves(self):

        if self.distances[0] == 1 and self.distances[1] == 1:
            self.output.write(str(0) + "\n")
        elif self.distances[0] == 2 or self.distances[1] == 2:
            self.output.write(str(1) + "\n")
        else:
            self.output.write(str(2) + "\n")

    def maxMoves(self):
        self.maxDistance = max(self.distances)
        self.output.write(str(self.maxDistance - 1))

    def getDistance(self):
        self.positions.sort()
        self.distances.append(self.positions[1] - self.positions[0])
        self.distances.append(self.positions[2] - self.positions[1])

def main():
    cow = SleepyCow()
    cow.minMoves()
    cow.maxMoves()

if __name__ == "__main__":
    main()
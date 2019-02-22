class TheGreatRevegetation:
    def __init__(self):
        self.input = open("revegetate.in", "r")
        self.output = open("revegetate.out", "w")
        self.lines = self.input.readlines()
        self.info = self.lines[0].split()
        self.numFields = int(self.info[0])
        self.numCows = int(self.info[1])
        self.cows = []
        self.fields = []
        for i in range(1, self.numCows + 1):
            self.cowInfo = self.lines[i].split()
            for i in range(0,2):
                self.cowInfo[i] = int(self.cowInfo[i])
            self.cows.append(self.cowInfo)
        self.sortCows()


    def sortCows(self):
        for cow in self.cows:
            cow.sort()
        self.cows.sort()

    def plantGrass(self):
        for i in range(0, self.numFields):
            self.fields.append(1)
        for cow in self.cows:
            if self.fields[cow[0]-1] == self.fields[cow[1]-1]:
                self.fields[cow[1]-1] = self.fields[cow[1]-1] + 1
        for field in self.fields:
            self.output.write(str(field))

def main():
    vegetate = TheGreatRevegetation()
    vegetate.plantGrass()

if __name__ == "__main__":
    main()
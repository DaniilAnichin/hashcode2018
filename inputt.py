
R, C, F, N, B, T = list(map(int, input().split(' ')))

rides = []

class Ride:
    def __init__(self, a, b, x, y, s, f):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
    def distance(self):
        return abs(self.x - self.a) + abs(self.y - self.b)
    def max_time(self):
        return self.f - self.s

for i in range(N):
     a, b, x, y, s, f = list(map(int, input().split(' ')))
     ride = Ride(a,b,x,y,s,f)
     if ride.distance() <= ride.max_time():
         rides.append(ride)

 

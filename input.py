
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


for i in range(N):
     a, b, x, y, s, f = list(map(int, input().split(' ')))
     rides.append(Ride(a,b,x,y,s,f))

 

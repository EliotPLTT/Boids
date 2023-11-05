from random import *
from math import *

class vec2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self,other):
        return vec2(self.x * other, self.y * other)
    def __truediv__(self,other):
        return vec2(self.x / other, self.y / other)
    def __mod__(self,other):
        return vec2(self.x % other, self.y % other)
    def norme(self):
        return sqrt(abs(self.x)**2 + abs(self.y)**2)
    def tup(self):
        return (self.x, self.y)

def dist(v1,v2):
    v1,v2 = v1.pos,v2.pos
    return sqrt(abs(v2.x - v1.x)**2 + abs(v2.y - v1.y)**2)

def norme(v):
    return sqrt(v.x**2 + v.y**2)

class Agent():
    def __init__(self,pos,velocity,faction,mass=100):
        self.pos = pos
        self.velocity = velocity
        self.faction = faction
        
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.color = (0,0,0)
        
    def updAgent(self,others):
        centreDeMassePercu = vec2(0,0)
        distanceEvitement = 5
        distanceEvitement2 = 50
        
        R2 = vec2(0,0) #Evitement
        R3 = vec2(0,0) #Vitesse
        
        for boid in others:
            if boid != self:
                if boid.faction == self.faction:
                    centreDeMassePercu += boid.pos

                    if dist(self,boid) < distanceEvitement:
                        R2 -= (boid.pos - self.pos)
                else:
                    if dist(self,boid) < distanceEvitement2:
                        R2 -= (boid.pos - self.pos)
                if boid.faction == self.faction: R3 += boid.velocity

        centreDeMassePercu = centreDeMassePercu / (N - 1)
        R1 = (centreDeMassePercu - self.pos) / 500 #Attraction

        R3 = R3 / (N - 1)
        R3 = (R3 - self.velocity) / 10

        #R4 - Murs
        R4 = vec2(0,0)
        
        x,y = self.pos.tup()
        if x > areaRadius:
            #print("X+")
            R4 = vec2(- abs(x - areaRadius),0)
        if x < 0:
            #print("X-")
            R4 = vec2(-x,0)
        if y > areaRadius:
            #print("Y+")
            R4 = vec2(0, - abs(y - areaRadius))
        if y < 0:
            #print("Y-")
            R4 = vec2(0, -y)

        R4 *= 1
        
        resultante = R1 + R2 + R3 + R4 #C'est l'accélération
        self.velocity += resultante #Que j'ajoute à la vitesse...
        
        self.limitSpeed()
        self.pos = (self.pos + self.velocity)

        self.color = (0,self.velocity.norme() / maxSpeed * 150,self.velocity.norme() / maxSpeed * 255)
        
    def limitSpeed(self):
        if norme(self.velocity) > maxSpeed:
            self.velocity = self.velocity * (maxSpeed / norme(self.velocity))



def initAgents(N, spawnCenter, spawnRadius, faction="NORMAL"):
    newAgents = []
    for i in range(N):
        A = Agent(spawnCenter + vec2(uniform(-spawnRadius, spawnRadius), uniform(-spawnRadius, spawnRadius)),
                  vec2(0,0), faction)
        newAgents.append(A)
    return newAgents

#SIM PARAMETER
N = 50
areaRadius = 700
spawnRadius = 100
maxSpeed = 10
    
if __name__ == "__main__":
    N = 150
    
    boids = initAgents(50, vec2(0,0), 10)
    updAgent(boids[0], boids)

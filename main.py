from vpython import * 
import math


ring(pos = vec(0,0,0), axis = vec(0,1,0), radius = math.pi + 5, thickness = 5, color = vector(1,0.65,1))

m = 0.155
r = 0.035 
ball = sphere(pos = vector(0,500,0), radius = r, color = vector(0.49,0.49,1), make_trail = True) # ball is being dropped from 500m in the air
rho = 1.3 # density of air
area = math.pi*r**2 # cross-sectional area of ball
C = 0.35 # drag coefficent

p = m * vector(0,9.81,0)
gravity = m * vector(0,-9.81,0)
t = 0
delta_t = 0.01

vertical_velocity = gcurve(color = vector(0.49,0.49,1))

while ball.pos.y > 0.035:
    rate(100)
    Fdrag = -0.5 * C * rho * area * (mag(p) / m)**2 * hat(p)  # using equation Fdrag = 1/2(C * rho * A * v**2)
    p = p + (gravity + Fdrag) * delta_t
    ball.pos = ball.pos + p/m * delta_t 

    vertical_velocity.plot(pos = (t, p.y / m))

    t = t + delta_t
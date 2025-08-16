from vpython import * 
import math 

scene = canvas(title = "Falling Object Simulation", caption = "Adjust constants then click on the screen to play the simulation!")

ring(pos = vec(0, 0, 0), axis = vec(0, 1, 0), radius = math.pi + 5, thickness = 5, color = vector(1, 0.65, 1))

# Ball and Constants:
m = 0.155 # mass of ball
r = 0.035 # radius of ball
h = vector(0, 500, 0) # initial height of ball
ball = sphere(pos = h, radius = r, color = vector(0.49, 0.49, 1), make_trail = False)
rho = 1.3 # density of air
area = math.pi * r**2 # cross-sectional area of ball
C = 0.35 # drag coefficent

# Slider Functions:
def set_radius(evt):
    global r
    r = evt.value
    ball.radius = r

def set_height(evt):
    global h
    h.y = evt.value
    ball.pos = h
    

# Sliders with Labels:

radius_slider = slider(bind = set_radius, max = 0.1, min = 0.05, step = 0.01)

height_slider = slider(bind = set_height, max = 500, min = 100, step = 1)


start_screen = scene.waitfor('click')   # Pauses screen on start-up
ball.make_trail = True


v = vector(0, 0, 0)
a = vector(0, 0, 0)
Fgravity = m * vector(0, -9.81, 0)
t = 0
delta_t = 0.01

g1 = graph(title = "Instantaneous Vertical Velocity", xtitle = "Time (s)", ytitle = "Vertical Velocity (m/s)")
vertical_velocity = gcurve(color = vector(0.49, 0.49, 1))
g2 = graph(title = "Instantaneous Acceleration", xtitle = "Time (s)", ytitle = "Acceleration (m/s^2)")
acceleration = gcurve(color = color.green)

running = True

while running:
   
    rate(100)
    area = math.pi * r**2
    
    if ball.pos.y > 0.035:

        Fdrag = -0.5 * C * rho * area * v.y**2 * hat(v)  # using equation Fdrag = 0.5(C * rho * A * v**2)
        a = (Fgravity + Fdrag) / m
        v = v + a * delta_t
        ball.pos = ball.pos + v * delta_t
        vertical_velocity.plot(pos = (t, v.y))
        acceleration.plot(pos = (t, a.y))
        t = t + delta_t


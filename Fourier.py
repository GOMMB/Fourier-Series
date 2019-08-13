from p5 import *
import scipy
from scipy.integrate import simps
from Svg2points import Svg2points
import numpy as np

SPEED = 0.001
VECTORS = 300
SCALE = 0.4

Svg2points.setup_svg()
bigpath = Svg2points.svg()

mouse_toggle = True


def complex_quadrature(paths, a, **kwargs):
    real_ = scipy.real(paths)

    imag_ = scipy.imag(paths)
    real_integral = simps(real_, a)
    imag_integral = simps(imag_, a)
    return real_integral + 1j*imag_integral


lines = [None for i in range(VECTORS)]
points = []
t_counter = 0
point_counter = 0


def setup():
    size(1000, 1000)
    x = 0
    y = 0
    xs = np.linspace(0, 1, len(bigpath))
    for i in range(VECTORS):
        if i % 2 == 0:
            n = int(-i/2)
        else:
            n = ceil(i/2)
        r = complex_quadrature(
            scipy.exp(-2*scipy.pi*1j*xs*n)*bigpath, xs)

        lines[i] = [n, r]


def draw():
    global t_counter
    global point_counter
    background(255)
    translate((width/2) - SCALE*scipy.real(lines[0][1]),
              (height/2) - SCALE*scipy.imag(lines[0][1]))
    scale(SCALE, SCALE)
    stroke(165, 0, 0)
    for x1, y1 in points:
        point(x1, y1)
    stroke(0, 0, 0)
    x = 0
    y = 0
    for num, l in enumerate(lines):
        part = l[1]*scipy.exp(l[0]*2*scipy.pi*1j*t_counter)
        if mouse_toggle:
            line((x, y), (x + scipy.real(part), y + scipy.imag(part)))
            circle((x, y), dist((x, y), (x + scipy.real(part),
                                         y + scipy.imag(part))), mode='RADIUS')
        x, y = (x + scipy.real(part), y + scipy.imag(part))
        if num == len(lines)-1 and point_counter < 1:
            points.append((x, y))
    t_counter += SPEED
    point_counter += SPEED
    if t_counter >= 1:
        t_counter = 0


def mouse_pressed():
    global mouse_toggle, point_counter

    if mouse_button == 'LEFT':
        mouse_toggle = not mouse_toggle
    elif mouse_button == 'RIGHT':
        points.clear()
        point_counter = 0


run(frame_rate=10000)

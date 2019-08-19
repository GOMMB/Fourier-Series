import scipy
import numpy as np
from svgpathtools import *
from functools import reduce


class Svg2points: # Partial credit of this class goes to https://github.com/mathandy/svgpathtools/blob/master/examples/compute-many-points-quickly-using-numpy-arrays.py

    pts = None

    @staticmethod
    def setup_svg():
        paths, attributes, svg_attributes = svg2paths2('path.svg')

        def points_in_each_seg_slow(path, tvals):
            return [seg.poly()(tvals) for seg in path]

        def points_in_each_seg(path, tvals):
            """Compute seg.point(t) for each seg in path and each t in tvals."""
            A = np.array([[-1,  3, -3,  1],  # transforms cubic bez to standard poly
                          [3, -6,  3,  0],
                          [-3,  3,  0,  0],
                          [1,  0,  0,  0]])
            B = [seg.bpoints() for seg in path]
            return np.dot(B, np.dot(A, np.power(tvals, [[3], [2], [1], [0]])))

        tvals = np.linspace(0, 1, 10)

        pts = map(lambda path: points_in_each_seg_slow(path, tvals), paths)
        pts = reduce(lambda paths, path: paths+path, pts)
        Svg2points.bigpath = []
        for pt in pts:
            Svg2points.bigpath.extend(pt)

    @staticmethod
    def svg():
        return np.array(Svg2points.bigpath)

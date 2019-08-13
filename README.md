## Requirements

Required Python modules include: p5, scipy, numpy, and svgpathtools.

## Usage

Just run the Fourier.py script. If you want to change the path being drawn, replace the svg image with one of your own and make sure is is named path.svg. Depending on your svg image, you may need to go into Fourier.py and adjust the <code>SCALE</code> variable for everything to be in frame.

### Customization

You can change the <code>SPEED</code> and/or <code>VECTORS</code> variables inside Fourier.py to adjust the animation.
* The <code>SPEED</code> variable, as you can probably guess, determines the speed of the animation, but know that the faster you make the animation, the fewer number of points of the path are drawn, and the shape may be difficult to see.
* The <code>VECTORS</code> variable determines the number of circles and rotating lines in the animation. Due to the nature of a Fourier series, as this variable gets higher and higher, the path drawn gets more and more accurate. However, due to calculation restrictions, the animation may bug out with over 300-400 vectors, so just keep that in mind.

### Controls

* **Left-Click:** Toggles whether the circles and  rotating lines are shown during the animation.
* **Right-Click:** Removes all currently drawn points.

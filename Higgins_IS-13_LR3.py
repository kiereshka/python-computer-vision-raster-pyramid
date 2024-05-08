
from graphics import *
import numpy as np
import matplotlib.colors as colors

pyramidVertices = np.array([
    [300, 100, 0, 1],
    [200, 250, 0, 1],
    [0, 250, 0, 1],
    [400, 250, 0, 1]
])

# Function to project the vertices of the pyramid onto the XY plane
def ProjectXY(Figure):
    f = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    ft = f.T
    Prxy = Figure.dot(ft)
    return Prxy

# Function to interpolate color gradient between two colors
def interpolateColor(startColor, endColor, numSteps):
    gradient = list(colors.to_hex(c) for c in np.linspace(startColor, endColor, numSteps))
    return gradient

# Function to draw the pyramid with gradient colors
def drawPyramid(Prxy, gradientColors):
    # Convert projected vertices to integer points
    vertices = [(int(point[0]), int(point[1]), point[2]) for point in Prxy]
    # Sort vertices by Y-coordinate
    verticesSortedY = sorted(vertices, key=lambda x: x[1])

    # Generate gradient steps for the bottom part
    gradientStepsBottom = interpolateColor((0, 0, 1), (1, 0, 0), abs(verticesSortedY[0][1] - verticesSortedY[1][1]) + 1)

    # Draw lines with gradient colors for the bottom part
    for i in range(len(gradientStepsBottom)):
        lineBottom = Line(Point(verticesSortedY[0][0] + i, verticesSortedY[0][1] + i), Point(verticesSortedY[1][0] + i, verticesSortedY[1][1] + i))
        lineBottom.setOutline(gradientStepsBottom[i])
        lineBottom.draw(pyramidWindow)

    # Generate gradient steps for the front part
    gradientStepsFront = interpolateColor((0, 0, 1), (1, 0, 0), abs(verticesSortedY[0][1] - verticesSortedY[3][1]) + 1)

    # Draw lines with gradient colors for the front part
    for i in range(len(gradientStepsFront)):
        lineFrontLeft = Line(Point(verticesSortedY[0][0] + i, verticesSortedY[0][1] + i), Point(verticesSortedY[3][0] + i, verticesSortedY[3][1] + i))
        lineFrontLeft.setOutline(gradientStepsFront[i])
        lineFrontLeft.draw(pyramidWindow)

        lineFrontRight = Line(Point(verticesSortedY[1][0] + i, verticesSortedY[1][1] + i), Point(verticesSortedY[3][0] + i, verticesSortedY[3][1] + i))
        lineFrontRight.setOutline(gradientStepsFront[i])
        lineFrontRight.draw(pyramidWindow)

# Create a graphics window to display the gradient pyramid
pyramidWindow = GraphWin("Gradient Pyramid", 800, 800)

# Project the vertices onto the XY plane
pyramidProjected = ProjectXY(pyramidVertices)
# Draw the pyramid with default gradient colors
drawPyramid(pyramidProjected, [])

pyramidWindow.getMouse()
pyramidWindow.close()

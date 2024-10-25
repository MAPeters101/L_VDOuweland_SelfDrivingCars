import os
from canvas import Canvas

track_image_path = os.path.join("images", "parkinglot.png")
canvas = Canvas(track_image_path)

canvas.simulate_generation()



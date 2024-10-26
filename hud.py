from pyglet.shapes import Circle
from pyglet.text import Label

class NeuronSprite:
    def __init__(self, x, y, batch):
        self.node_border = Circle(x, y, 22, color=(0, 0, 0, 255), batch=batch)
        self.node_fill = Circle(x, y, 20, color=(255, 255, 255, 255), batch=batch)
        self.node_value = Label(x=x, y=y, color=(255, 255, 255, 255), font_size=12, anchor_x="center",
                                anchor_y="center", batch=batch)

class Hud:
    def __init__(self, simulation_round, dimensions, batch):
        self.round_label = Label(f"Round: {simulation_round}", x=20, y=520, color=(0,0,0,255), batch=batch)
        self.population_label = Label(x=120, y=520, color=(0,0,0,255), batch=batch)
        self.speed_label = Label(x=280, y=520, color=(0,0,0,255), batch=batch)
        self.neurons = []
        x = 40
        for neuron_count in dimensions:
            total_height = neuron_count * 50 - 10
            y = 540 - (540 - total_height) / 2
            for _ in range(neuron_count):
                self.neurons.append(NeuronSprite(x, y, batch))
                y -= 50
            x += 50

    def update(self, alive, population, speed):
        self.population_label.text = f"Population: {alive}/{population}"
        self.speed_label.text = f"Speed: {speed:.2f}"






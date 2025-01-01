import pygame
import config
from phototransistor import Phototransistor

class ReversibleGate:
    def __init__(self, input1, input2, output1, output2, plane):
        self.input1 = input1
        self.input2 = input2
        self.output1 = output1
        self.output2 = output2
        self.plane = plane  # Track the plane on which the gate is located

    def operate(self):
        # Implement the logic for a reversible gate (example: Fredkin gate)
        if self.input1:
            self.output1 = self.input2
            self.output2 = not self.input2
        else:
            self.output1 = self.input1
            self.output2 = self.input2

        # Logic for moving between planes
        self.move_between_planes()

    def move_between_planes(self):
        # Example logic for changing planes (simplified)
        if self.output1 and self.output2:
            self.plane += 1  # Move to the next plane
        elif not self.output1 and not self.output2:
            self.plane -= 1  # Move to the previous plane

class Circuit:
    def __init__(self):
        self.gates = []
        self.planes = []

    def add_gate(self, gate):
        self.gates.append(gate)

    def run(self):
        for gate in self.gates:
            gate.operate()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

# Create and display the reversible logic gates
circuit = Circuit()
# Add gates to the circuit and simulate operation...

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 128, 128))  # Fill the screen with grey
    circuit.run()

    pygame.display.flip()

pygame.quit()


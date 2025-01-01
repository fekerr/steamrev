# phototransistor.py
# 20250101 fekerr & copilot
# Description: This file defines the Phototransistor class for the project.

class Phototransistor:
    def __init__(self, sensitivity=1.0):
        self.sensitivity = sensitivity
        self.light_level = 0.0

    def detect_light(self, light_intensity):
        self.light_level = light_intensity * self.sensitivity
        return self.light_level

    def is_active(self, threshold=0.5):
        return self.light_level > threshold

    def reset(self):
        self.light_level = 0.0


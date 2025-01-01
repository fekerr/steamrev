# config.py
# 20250101 fekerr & copilot
# Description: This file contains the configuration constants for the project.

# Gravitational constant
G = 0.001

# Boundaries
BOUNDARY_LIMIT = 20  # Adjusted boundary limit for fitting in the window

# Colors and names
COLORS = [
    (255, 0, 0),    # Red
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 128, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (238, 130, 238),# Violet
    (0, 0, 0),      # Black (white interior)
    (255, 255, 255) # White (black interior)
]

COLOR_NAMES = [
    "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White"
]

# Display settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 30

# Scaling factor
SCALE_FACTOR = 10  # Adjusted scaling factor for fitting in the window

# Log settings
LOG_DIR = "logs"
LOG_FILE_PREFIX = "game_info"
LOG_MAX_BYTES = 1000000
LOG_BACKUP_COUNT = 5
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'


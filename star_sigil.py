import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

# Inserisci la frase seed qui
seed_phrase = input("Inserisci la frase seed: ")
seed_length = len(seed_phrase)

# Define the symbols for the planets
planet_symbols = ['☉', '♁', '♀', '⨁', '♂', '♃', '♄', '♅', '♆', '♇', '☾', '☊', '☋', '☌', '☍', '☽', '⚳', '⚴', '⚵', '⚶', '⚷', '⚸', '⚹', '⚺', '⚻', '⚼']

# Inizializza il generatore di numeri casuali con la frase seed
random.seed(seed_phrase)

# Create a figure and axis
fig, ax = plt.subplots()

# Set the radius for the circle and star
circle_radius = 0.49
star_radius = 0.4

# Draw the circle (bottom layer)
circle = plt.Circle((0.5, 0.5), circle_radius, color='black', fill=False, lw=2)
ax.add_patch(circle)

# Define the positions for the astrology symbols (randomized within the circle)
symbol_positions = []

# Calcola un range casuale compreso tra 1 e la lunghezza di planet_symbols
random_range = random.randint(1, min(12, len(planet_symbols)))  # Imposta un limite massimo di 12

for _ in range(random_range):
    # Generate random angles within the circle
    angle = random.uniform(0, 2 * np.pi)
    # Calculate the position based on the angle and star_radius
    x = 0.5 + star_radius * np.cos(angle)
    y = 0.5 + star_radius * np.sin(angle)
    symbol_positions.append((x, y))

# Display planet symbols at the generated positions
for position, symbol in zip(symbol_positions, planet_symbols[:random_range]):
    ax.text(position[0], position[1], symbol, fontsize=20, ha='left', va='top', alpha=0.5)

# Connect planet symbols with lines (add lines before adding circles)
for i in range(random_range):
    start_x, start_y = symbol_positions[i]
    end_x, end_y = symbol_positions[(i + 1) % random_range]  # Connect to the next symbol
    ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=2, alpha=1)

# Add white circles with black borders (top layer)
for position in symbol_positions:
    # Add a white circle with a black border (completely opaque)
    circle = plt.Circle(position, radius=0.05, color='white', ec='black', lw=1.5, alpha=1.0)
    ax.add_patch(circle)

# Set aspect ratio to equal
ax.set_aspect('equal', adjustable='box')

# Set axis limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Aggiungi una legenda sotto al cerchio
#legend_text = "\n".join([f"{symbol}: Nome del Pianeta {planet_symbols.index(symbol) + 1}" for symbol in planet_symbols[:random_range]])
#plt.figtext(0.5, 0.01, legend_text, ha='center', fontsize=12)

# Show the plot
plt.savefig(f"{seed_phrase}.png")
plt.show()

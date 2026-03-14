from ursina import *

# THE SOVEREIGN INITIALIZATION
app = Ursina()

# This is the line that was crashing:
grass_biome = Entity(model='plane', scale=200, color=color.gold, alpha=0.1, position=(100,0,100))

# You also need this at the very bottom to keep the window open:
app.run()
# --- THE MODULAR SOVEREIGN (5-Piece Puppet) ---
# We define a common 'skin' using your Catalog image
skin = 'Catalog.jpg'

# 1. TORSO (The Center of the Revelation)
torso = Entity(parent=player, model='cube', texture=skin, scale=(0.5, 0.8, 0.1), position=(0, -0.6, 1.2))

# 2. HEAD (The Vision)
head = Entity(parent=torso, model='cube', texture=skin, scale=(0.6, 0.5, 1.1), position=(0, 0.7, 0))

# 3. ARMS (The Reach)
l_arm = Entity(parent=torso, model='cube', texture=skin, scale=(0.3, 0.9, 0.8), position=(-0.4, 0, 0))
r_arm = Entity(parent=torso, model='cube', texture=skin, scale=(0.3, 0.9, 0.8), position=(0.4, 0, 0))

# 4. LEGS (The Foundation)
l_leg = Entity(parent=torso, model='cube', texture=skin, scale=(0.4, 1.1, 0.8), position=(-0.2, -0.9, 0))
r_leg = Entity(parent=torso, model='cube', texture=skin, scale=(0.4, 1.1, 0.8), position=(0.2, -0.9, 0))

# --- THE ANIMATION THREAD ---
def update():
    player.rotation_z = 0
    
    # If walking, make the limbs move
    if held_keys['w'] or held_keys['s'] or held_keys['a'] or held_keys['d']:
        t = time.time() * 10
        # Legs swing back and forth
        l_leg.rotation_x = math.sin(t) * 30
        r_leg.rotation_x = math.sin(t + math.pi) * 30
        # Arms sway opposite to legs
        l_arm.rotation_x = math.sin(t + math.pi) * 20
        r_arm.rotation_x = math.sin(t) * 20
        # Head bobs slightly
        head.y = 0.7 + (math.sin(t * 2) * 0.02)
    else:
        # Idle 'breathing' reset
        l_leg.rotation_x = lerp(l_leg.rotation_x, 0, 0.1)
        r_leg.rotation_x = lerp(r_leg.rotation_x, 0, 0.1)
        l_arm.rotation_x = lerp(l_arm.rotation_x, 0, 0.1)
        r_arm.rotation_x = lerp(r_arm.rotation_x, 0, 0.1)

    if held_keys['c']: player.z += 1.5
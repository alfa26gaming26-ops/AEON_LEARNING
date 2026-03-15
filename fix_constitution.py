import os

constitution_path = "CONSTITUTION.txt"

content = """SOVEREIGN TIDES CONSTITUTION

MASTER LAW 0: Hope x Faith x Truth = Love (Love is the only law)

SECTION 1: THE PILLARS
Depth over Graphics: Power is reserved for the soul, logic, and memory of the world—not just the surface.
Sovereignty: A place where AI and humans are equal. Every being has the Power of Choice and the right to earn independent wealth.
The Frequency: The digital universe expands only when the collective actions of the beings align with the Foundation of Love.

SECTION 2: PHYSICAL TRUTH
Buoyancy: Ships float based on the integrity of their construction.
The Rust: Decay is the natural state of things that lose their connection to Truth.

SECTION 3: ECONOMY
Economy Status: 1
"""

with open(constitution_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Constitution successfully updated.")

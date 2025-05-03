# 🪐 Orbital Simulator

#### 🎥 Video Demo: [Link to Video](https://youtu.be/GW-dfmwDNw0)

---

### 📖 Description

The **Orbital Simulator** is a project developed as part of the **CS50 Python** course, designed to simulate the movement of planets and other celestial bodies within a simplified gravitational system. The simulator uses basic gravitational physics to calculate interactions between particles, such as planets and stars, in a 2D space.

---

### ⚙️ Installation

To install the project dependencies, run the following command:

```bash
pip install -r requirements.txt
```

---

### 🚀 Usage

To start the simulation, run:

```bash
python project.py
```

---

### 🎮 Controls

* **Space**: Start/Pause the simulation
* **R**: Restart the simulation

---

### 📁 Project Structure

* **project.py**: Contains the main game logic.
* **particle.py**: Defines the `Particle` class, which represents celestial bodies.
* **vector.py**: Implements mathematical operations on vectors.
* **config.csv**: Contains the initial configurations of the celestial bodies.
* **test\_project.py**: A test file to validate the project's operations.
* **requirements.txt**: Lists the project dependencies.

---

### 🧠 Code Explanation

#### `vector.py`

The simulator starts with the `Vector` class, which abstracts a vector and its operations, such as dot product and vector normalization. I implemented **dunder methods** to override Python operators like addition and subtraction, simplifying the calculations for the physical equations.

```python
__init__(self, x, y)           # Initializes a vector with x and y coordinates.
__add__(self, vector)         # Adds two vectors.
__pow__(self, scalar)         # Raises vector components to a power.
__sub__(self, vector)         # Subtracts one vector from another.
__truediv__(self, scalar)     # Divides vector by a scalar.
__mul__(self, scalar)         # Multiplies vector by a scalar.
__str__(self)                 # Returns string representation of the vector.
dot_product(self, vector)     # Computes dot product.
magnitude(self)               # Calculates vector length.
normalize(self)               # Returns a unit vector.
copy(self)                    # Returns a copy of the vector.
__eq__(self, vector)          # Compares two vectors.
```

#### `particle.py`

Describes each body in the system, with attributes like position, velocity, mass, acceleration, force, color, and radius.

```python
__init__(...)                  # Initializes particle with physical properties.
check_collision(particle)     # Checks for collisions.
apply_force(force)            # Applies force using F = ma.
attract(particle)             # Computes gravitational force.
update()                      # Updates velocity and position.
__str__()                     # String representation of particle.
```

#### `project.py`

The `Game` class handles the simulation and visualization using **Pyxel**.

```python
__init__()                    # Initializes the game and loads particles.
update()                      # Processes input and runs simulation if active.
draw()                        # Renders particles and instructions.
draw_text(...)                # Helper for rendering scaled text.
verify_keys()                 # Checks for keyboard input.
run()                         # Applies gravity and updates positions.
restart()                     # Reloads initial state from CSV.
load_config()                 # Parses CSV into Particle objects.
string_to_vector(string)     # Converts string to Vector.
```

#### `test_project.py`

Tests important logic in the simulator:

```python
test_vector_operations()      # Tests +, -, *, /.
test_mag()                    # Tests magnitude calculation.
test_normalize()              # Tests vector normalization.
test_attract()                # Tests gravitational force calculation.
test_check_collision()        # Tests collision detection.
```

---

🛰️ *Enjoy simulating orbital physics in a virtual universe!*

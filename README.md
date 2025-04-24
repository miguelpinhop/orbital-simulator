# Orbital Simulator

#### Video Demo: [Link to Video](<URL HERE>)

#### Description:
The **Orbital Simulator** is a project developed as part of the **CS50 Python** course, designed to simulate the movement of planets and other celestial bodies within a simplified gravitational system. The simulator uses basic gravitational physics to calculate interactions between particles, such as planets and stars, in a 2D space. 

#### Installation:
To install the project dependencies, run the following command: `pip install -r requirements.txt`

#### Usage:
To start the simulation, run: `python project.py`

#### Controls:
- **Space**: Start/Pause the simulation
- **R**: Restart the simulation

#### Project Structure:
- **project.py**: Contains the main game logic.
- **particle.py**: Defines the `Particle` class, which represents celestial bodies.
- **vector.py**: Implements mathematical operations on vectors.
- **config.csv**: Contains the initial configurations of the celestial bodies.
- **test_project.py**: A test file to validate the project's operations.
- **requirements.txt**: Lists the project dependencies.

#### Demo:
[Link to Video](<https://youtu.be/PlcgIq2bDAc>)

---

#### Code Explanation

### vector.py:
The simulator starts with the `Vector` class, which abstracts a vector and its operations, such as dot product and vector normalization. I implemented **dunder methods** to override Python operators like addition and subtraction, simplifying the calculations for the physical equations.

**def __init__(self, x, y):** --> Initializes a vector with x and y coordinates.

**def __add__(self, vector):** --> Implements vector addition, returning a new vector as the sum of two vectors.

**def __pow__(self, scalar):** --> Raises each component of the vector to the power of scalar, returning a new vector with the result.

**def __sub__(self, vector):** --> Implements vector subtraction, returning a new vector representing the difference between them.

**def __truediv__(self, scalar):** --> Divides the vector by a scalar.

**def __mul__(self, scalar):** --> Multiplies the vector by a scalar, useful for scaling forces or velocities.

**def __str__(self):** --> Returns a string representation of the vector in the format (x, y), useful for debugging and logging.

**def dot_product(self, vector):** --> Computes the dot product of two vectors, which can be used to find angles between directions.

**def magnitude(self):** --> Returns the length (magnitude) of the vector, calculated as the square root of the sum of the squares of its components.

**def normalize(self):** --> Returns a unit vector (magnitude 1) pointing in the same direction as the original vector. If the vector has zero magnitude, it returns itself to avoid division by zero.

**def copy(self):** --> Returns a copy of the vector.

**def __eq__(self, vector):** --> Checks if two vectors are equal.

### particle.py:
The `Particle` class describes each body in the system, with attributes such as position, velocity, mass, acceleration, force, color, and radius. Key functions include:

**def __init__(self, position, velocity, mass, acceleration, force, color, radius):** --> Initializes a particle with its physical properties and simulation constraints (like screen width and height).

**def check_collision(self, particle):** --> Checks if the current particle has collided with another particle by comparing the sum of their radii with the distance between their positions.

**def apply_force(self, force):** --> Applies a force to the particle by updating its force attribute and adjusting its acceleration based on Newton's second law (F = ma).

**def attract(self, particle):** --> Calculates the gravitational attraction between two particles using Newton’s Law of Universal Gravitation. The force is proportional to the product of their masses and inversely proportional to the square of the distance between them.

**def update(self):** --> Updates the particle’s velocity and position based on its acceleration. The force is then reset for the next iteration.

**def __str__(self):** --> Returns a string representation of the particle’s properties, including position, velocity, acceleration, and applied force.

### project.py:
The `Game` class manages the simulation logic and interacts with **Pyxel** for visualization. It includes:

**def __init__(self):** --> Initializes the game window with a resolution of 1920x1080 and loads the initial particle configurations from the config.csv file. The simulation starts in a paused state (self.pause = 1). The pyxel.run(self.update, self.draw) function is called to start the main game loop.

**def update(self):** --> This method runs once per frame and checks for user inputs via verify_keys(). If the simulation is not paused (self.pause == -1), it calls run() to update the physics simulation.

**def draw(self):** --> Clears the screen and draws all particles as circles using pyxel.circ(). Additionally, it displays the control instructions (SPACE) - RUN/PAUSE (R) - RESTART.

**def draw_text(self, x, y, text, color, scale):** --> A helper function to draw text on the screen with a given position (x, y), color, and scale. It iterates over each character in the text and manually adjusts its position to scale it properly.

**def verify_keys(self):** --> Checks if the spacebar or R key has been pressed.

**def run(self):** --> The core physics update loop, responsible for:

- Iterating through all particles and applying gravitational forces (particle.attract(other_particle)).
- Updating particle positions (particle.update()).
- Checking for collisions with the first particle (assumed to be the attractor, like the Sun). If a collision occurs, the particle is removed from the simulation.

**def restart(self):** --> Resets the simulation by clearing the screen (pyxel.cls(0)) and reloading the initial particle data from config.csv.

**def load_config(self):** --> Reads the config.csv file using pandas, extracts the particle properties (position, force, velocity, acceleration, mass, color, radius), and creates a list of Particle objects. Returns this list of particles for use in the simulation.

**def string_to_vector(self, string):** --> Converts a space-separated string (e.g., "1.0 2.0") into a Vector object by splitting the string and parsing the values as floats.

### test_project.py:

**def test_vector_operations():** --> Verifies if the basic operations (+, -, *, /) work correctly.

**def test_mag():** --> Tests if the function that calculates the magnitude (size) of the vector returns the correct value.

**def test_normalize():** --> Confirms that the normalization returns a unit vector (magnitude 1).

**def test_attract():** --> Tests if the gravitational attraction function correctly calculates the force applied between two particles.

**def test_check_collision():** --> Verifies if the collision detection system correctly identifies when two particles are touching or not.

---

from vector import Vector

class Particle:
    def __init__(self, position, velocity, mass, acceleration, force, color, radius):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
        self.acceleration = acceleration
        self.width = 1920
        self.height = 1080
        self.force = force
        self.last_force = Vector(1,1)
        self.color = color

    def check_collision(self, particle):
        distance = (particle.position - self.position).mag()

        if distance < particle.radius + self.radius:
            return True
        
        return False

    def apply_force(self, force):
        self.force += force
        self.acceleration += force/self.mass

    def attract(self, particle):
        direction = particle.position - self.position
        distance = direction.mag()**2
        mass_product = self.mass * particle.mass
        gravity_force = direction.normalize() * (mass_product/distance*-1) * 10
        particle.apply_force(gravity_force)

    def update(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + (self.velocity)
        self.acceleration = Vector(0,0)
        self.last_force = self.force
        self.force = Vector(0,0)

    def __str__(self):
        return f"position: {self.position}, velocity: {self.velocity}, acceleration: {self.acceleration}, force: {self.force}, last_force: {self.last_force}"
    
"""
BORDER AND ELASTIC COLISION DISABLED

    def border_colision(self):
        if self.position.x >= self.width - self.radius:
            self.position.x = self.width - self.radius - 0.1
            self.velocity.x = self.velocity.x * (-1)
        elif self.position.x <= 0 + self.radius:
            self.position.x = self.radius + 0.1
            self.velocity.x = self.velocity.x * (-1)

        if self.position.y >= self.height - self.radius:
            self.position.y = self.height - self.radius - 0.1
            self.velocity.y = self.velocity.y * (-1)
        elif self.position.y <= 0 + self.radius:
            self.position.y = self.radius + 0.1
            self.velocity.y = self.velocity.y * (-1)

    def is_coliding(self, particle):
        impact_vector = particle.position - self.position
        d = impact_vector.mag()

        if d < particle.radius + self.radius:
            overlap = d - (self.radius + particle.radius)

            dir = impact_vector.normalize()*(overlap * 0.5)
            self.position += dir
            particle.position -= dir

            d = self.radius + particle.radius
            impact_vector = impact_vector.normalize() * d

            m_sum = particle.mass + self.mass
            v_diff = particle.velocity - self.velocity

            # Particle A
            num = v_diff.dot_product(impact_vector)
            den = (m_sum) * d**2
            delta_vA = impact_vector.copy()
            delta_vA = delta_vA * (2*particle.mass * num/den)
            self.velocity += delta_vB

            # Particle B
            delta_vB = impact_vector.copy()
            delta_vB = delta_vB * (-2*particle.mass * num/den)
            self.velocity += delta_vA
"""
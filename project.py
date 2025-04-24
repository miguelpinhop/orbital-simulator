import pyxel # type: ignore
from vector import Vector
from particle import Particle
import pandas as pd
from pyxel import KEY_SPACE, KEY_R 


class Game:
    def __init__(self):
        pyxel.init(1920, 1080)
        self.particles = self.load_config()
        self.pause = 1
        pyxel.run(self.update, self.draw)

    def update(self):
        self.verify_keys()
        if self.pause == -1:
            self.run()

    def draw(self):
        for particle in self.particles:
            pyxel.circ(particle.position.x, particle.position.y, particle.radius, particle.color)

        self.draw_text(300, 175, "(SPACE) - RUN/PAUSE    (R) - RESTART", 7, 2)

    def draw_text(self, x, y, text, color, scale):
        for i, char in enumerate(text):
            for dx in range(scale):
                for dy in range(scale):
                    px = x + i * (4 * scale) + dx
                    py = y + dy
                    pyxel.text(px, py, char, color)

    def verify_keys(self):
        if pyxel.btnr(KEY_SPACE):
            self.pause *= -1

        if pyxel.btnr(KEY_R):
            self.restart()

    def run(self):
        removed_particles = []
        for index in range(len(self.particles)):
            particle = self.particles[index]
            for j in range(len(self.particles)):
                if index == j or j == 0:
                    continue
                other_particle = self.particles[j]
                particle.attract(other_particle)
            particle.update()
            is_coliding = particle.check_collision(self.particles[0])
            if is_coliding and index != 0:
               removed_particles.append(index)
        if len(removed_particles) > 0:
            self.particles.pop(removed_particles[0])

    def restart(self):
        pyxel.cls(0)
        self.particles = self.load_config()

    def load_config(self):
        df = pd.read_csv("config.csv")
        particles = []
        for i in range(df.shape[0]):
            row = df.iloc[i]

            position = self.string_to_vector(row.position)
            force = self.string_to_vector(row.force)
            velocity = self.string_to_vector(row.velocity)
            acceleration = self.string_to_vector(row.acceleration)
            mass = float(row.mass)
            color = int(row.color)
            radius = float(row.radius)

            particles.append(Particle(position, velocity, mass, acceleration, force, color, radius))
        return particles

    def string_to_vector(self, string):
        string_split = string.split(" ")
        vector = Vector(float(string_split[0]), float(string_split[1]))
        return vector


def main():
    Game()


if __name__ == "__main__":
    main()


import math


class Calculator:
    def __init__(self, length, force_magnitude):
        self.force_magnitude = force_magnitude
        self.length = length
        self.num_points = 100

    def ss_udl(self):
        # Number of points to calculate shear and bending moment
        num_points = self.num_points

        force_magnitude = self.force_magnitude
        length = self.length

        # Calculate shear force and bending moment at each point along the beam
        points = [(length / num_points) * i for i in range(num_points + 1)]
        shear_force = [force_magnitude * ((0.5 * length) - point) for point in points]
        bending_moment = [(0.5 * force_magnitude) * point * (length - point) for point in points]
        return points, shear_force, bending_moment

    def ss_pl(self, force_location):
        force_magnitude = self.force_magnitude
        length = self.length

        if force_location == length or force_location == 0:
            return

        # Number of points to calculate shear and bending moment
        num_points = self.num_points

        num_points_a = math.floor((force_location / length) * num_points)
        num_points_b = num_points - num_points_a

        # Calculate shear force and bending moment at each point along the beam

        points_a = [(force_location / num_points_a) * i for i in range(num_points_a + 1)]
        points_b = [force_location + (((length - force_location) / num_points_b) * i) for i in range(num_points_b + 1)]

        points = points_a + points_b

        # Shear Calc:
        shear_force_a = [((force_magnitude * (length - force_location)) / length) for point in points_a]
        shear_force_b = ([((-force_magnitude * force_location) / length) for point in points_b])
        shear_force = shear_force_a + shear_force_b

        max_moment = (force_magnitude * force_location * (length - force_location)) / (length)
        bending_moment_a = [(max_moment / force_location) * point for point in points_a]
        bending_moment_b = (
            [((max_moment / (length - force_location)) * length) + (-max_moment / (length - force_location)) * point for
             point
             in points_b])
        bending_moment = bending_moment_a + bending_moment_b
        return points, shear_force, bending_moment

    def ss_2pl(self, force_location):
        force_magnitude = self.force_magnitude
        length = self.length

        if force_location == length or force_location == 0:
            return

        # Number of points to calculate shear and bending moment
        num_points = self.num_points

        num_points_a = math.floor((force_location / length) * num_points)
        num_points_b = num_points_a
        num_points_c = num_points - num_points_a - num_points_b
        # Calculate shear force and bending moment at each point along the beam

        points_a = [(force_location / num_points_a) * i for i in range(num_points_a + 1)]
        points_b = [force_location + (((length - 2 * force_location) / num_points_b) * i) for i in
                    range(num_points_b + 1)]
        points_c = [(length - force_location) + (((length - force_location - force_location) / num_points_c) * i) for i
                    in
                    range(num_points_c + 1)]

        points = points_a + points_b + points_c
        print(points)

        # Shear Calc:
        shear_force_a = [force_magnitude for point in points_a]
        shear_force_b = [0 for point in points_b]
        shear_force_c = [-force_magnitude for point in points_c]

        shear_force = shear_force_a + shear_force_b + shear_force_c

        bending_moment_a = [(force_magnitude * point) for point in points_a]
        bending_moment_b = [force_magnitude * force_location for point in points_b]
        bending_moment_c = [(force_magnitude * length) - (force_magnitude * point) for point in points_c]

        bending_moment = bending_moment_a + bending_moment_b + bending_moment_c

        print('I ran well, I am going to plot, now, the two point load on simply supported')
        return points, shear_force, bending_moment

    def cant_udl(self):
        force_magnitude = self.force_magnitude
        length = self.length

        num_points = self.num_points

        points = [(length / num_points) * i for i in range(num_points + 1)]

        # Shear Calc:
        shear_force = [(force_magnitude * (length - point)) for point in points]
        bending_moment = [-(force_magnitude * (length - point) ** 2) / 2 for point in points]

        print('I ran well, I am going to plot, now')
        return points, shear_force, bending_moment

    def cant_tpl(self):
        force_magnitude = self.force_magnitude
        length = self.length

        num_points = self.num_points

        points = [(length / num_points) * i for i in range(num_points + 1)]

        # Shear Calc:
        shear_force = [force_magnitude * ((length - point) ** 2) / (2 * length) for point in points]
        bending_moment = [-force_magnitude * ((length - point) ** 3) / (6 * length) for point in points]

        print('I ran well, I am going to plot, now')
        return points, shear_force, bending_moment

    def cant_pl(self, force_location):
        force_magnitude = self.force_magnitude
        length = self.length
        num_points = self.num_points

        if force_location == 0:
            return

        elif force_location == length:
            points = [(length / num_points) * i for i in range(num_points + 1)]
            shear_force = [force_magnitude for point in points]
            bending_moment = [-force_magnitude * (length - point) for point in points]
            return points, shear_force, bending_moment

        else:
            num_points_a = math.floor((force_location / length) * num_points)
            num_points_b = num_points - num_points_a

            # Calculate shear force and bending moment at each point along the beam

            points_a = [(force_location / num_points_a) * i for i in range(num_points_a + 1)]
            points_b = [force_location + (((length - force_location) / num_points_b) * i) for i in
                        range(num_points_b + 1)]

            points = points_a + points_b

            # Shear Calc:
            shear_force_a = [force_magnitude for point in points_a]
            shear_force_b = ([0 for point in points_b])
            shear_force = shear_force_a + shear_force_b

            bending_moment_a = [-force_magnitude * (force_location - point) for point in points_a]
            bending_moment_b = ([0 for point in points_b])
            bending_moment = bending_moment_a + bending_moment_b

            print('I ran well, I am going to plot, now')
            return points, shear_force, bending_moment

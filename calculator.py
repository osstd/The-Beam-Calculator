class Calculator:
    def __init__(self, length, force_magnitude):
        self.force_magnitude = force_magnitude
        self.length = length
        self.num_points = 1000

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
        length = self.length
        num_points = self.num_points

        if force_location == length or force_location == 0:
            return

        points = [length * i / num_points for i in range(num_points + 1)]
        shear_force = [0] * (num_points + 1)
        bending_moment = [0] * (num_points + 1)

        force_magnitude = self.force_magnitude

        # Shear Calc:
        for i in range(num_points + 1):
            if points[i] <= force_location:
                shear_force[i] = ((force_magnitude * (length - force_location)) / length)
            elif points[i] > force_location:
                shear_force[i] = ((-force_magnitude * force_location) / length)

        # Moment Calc:
        max_moment = (force_magnitude * force_location * (length - force_location)) / length
        for i in range(num_points + 1):
            if points[i] <= force_location:
                bending_moment[i] = (max_moment / force_location) * points[i]
            elif points[i] > force_location:
                bending_moment[i] = ((max_moment / (length - force_location)) * length) + (
                        -max_moment / (length - force_location)) * points[i]

        return points, shear_force, bending_moment

    def ss_2pl(self, force_location):
        length = self.length
        num_points = self.num_points

        if force_location == 0 or force_location == self.length:
            raise ValueError("Error: Do not place loads at the support locations.")

        if force_location == length / 2:
            raise ValueError("Error, Two point loads can't be placed at mid-span. "
                             "Use a simple beam with one point load instead.")

        if force_location > length / 2:
            raise ValueError("Error, for this loading condition load location can't be beyond the center of the beam, "
                             "input load location 'a' from the left side of the beam")

        force_locations = [force_location, length - force_location]

        points = [length * i / num_points for i in range(num_points + 1)]
        shear_force = [0] * (num_points + 1)
        bending_moment = [0] * (num_points + 1)

        force_magnitude = self.force_magnitude

        # Shear Calc:
        for i in range(num_points + 1):
            if points[i] <= force_locations[0]:
                shear_force[i] = force_magnitude
            elif points[i] >= force_locations[1]:
                shear_force[i] = -force_magnitude

        # Moment Calc:
        for i in range(num_points + 1):
            if points[i] <= force_locations[0]:
                bending_moment[i] = force_magnitude * points[i]
            elif points[i] >= force_locations[1]:
                bending_moment[i] = (force_magnitude * length) - (force_magnitude * points[i])
            else:
                bending_moment[i] = force_magnitude * force_locations[0]

        return points, shear_force, bending_moment

    def cant_udl(self):
        length = self.length
        num_points = self.num_points

        points = [(length / num_points) * i for i in range(num_points + 1)]

        force_magnitude = self.force_magnitude

        # Shear Calc:
        shear_force = [(force_magnitude * (length - point)) for point in points]

        # Moment Calc:
        bending_moment = [-(force_magnitude * (length - point) ** 2) / 2 for point in points]

        return points, shear_force, bending_moment

    def cant_tpl(self):
        length = self.length
        num_points = self.num_points

        points = [(length / num_points) * i for i in range(num_points + 1)]

        force_magnitude = self.force_magnitude

        # Shear Calc:
        shear_force = [force_magnitude * ((length - point) ** 2) / (2 * length) for point in points]

        # Moment Calc:
        bending_moment = [-force_magnitude * ((length - point) ** 3) / (6 * length) for point in points]

        return points, shear_force, bending_moment

    def cant_pl(self, force_location):
        length = self.length
        num_points = self.num_points

        force_magnitude = self.force_magnitude

        if force_location == 0:
            return

        # Case where the load is at the tip of the cantilever
        elif force_location == length:
            points = [(length / num_points) * i for i in range(num_points + 1)]

            # Shear Calc:
            shear_force = [force_magnitude for _ in range(len(points))]

            # Moment Calc:
            bending_moment = [-force_magnitude * (length - point) for point in points]

            return points, shear_force, bending_moment

        # Case where the load is placed along the length of the cantilever
        else:
            points = [length * i / num_points for i in range(num_points + 1)]
            shear_force = [0] * (num_points + 1)
            bending_moment = [0] * (num_points + 1)

            # Shear Calc:
            for i in range(num_points + 1):
                if points[i] <= force_location:
                    shear_force[i] = force_magnitude
                elif points[i] > force_location:
                    shear_force[i] = 0

            # Moment Calc:
            for i in range(num_points + 1):
                if points[i] <= force_location:
                    bending_moment[i] = -force_magnitude * (force_location - points[i])
                elif points[i] > force_location:
                    bending_moment[i] = 0

            return points, shear_force, bending_moment

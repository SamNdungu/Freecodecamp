import copy
import random

class Hat:
    def __init__(self, **balls):
        # Initialize the hat with balls based on the input dictionary
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num):
        # Simulate drawing a specified number of balls from the hat
        if num >= len(self.contents):
            return self.contents
        else:
            drawn_balls = [
                self.contents.pop(random.randrange(len(self.contents)))
                for _ in range(num)
            ]
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    # Run experiments loop
    for _ in range(num_experiments):
        # Create a deep copy of the original hat for each experiment
        current_hat = copy.deepcopy(hat)

        # Draw a specified number of balls from the hat
        drawn_balls = current_hat.draw(num_balls_drawn)

        # Count the occurrences of each color in the drawn balls
        drawn_balls_count = {
            color: drawn_balls.count(color)
            for color in set(drawn_balls)
        }

        # Check if drawn balls match the expected criteria
        if all(
            drawn_balls_count.get(color, 0) >= count
            for color, count in expected_balls.items()
        ):
            success_count += 1

    # Calculate and return the probability of success
    success_probability = success_count / num_experiments
    return success_probability

random.seed(95)  # Set the seed for reproducibility
hat = Hat(blue=4, red=2, green=6)  # Create an instance of the Hat class
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000
)
print("Probability:", probability)

class MonkeyBananaProblem:
    def __init__(self):
        self.state = {
            "monkey": "floor",
            "box": "corner",
            "banana": "ceiling",
            "on_box": False,
            "has_banana": False
        }

    def solve(self):
        print("Monkey moves box under banana.")
        self.state.update({"box": "under_banana", "monkey": "under_banana"})

        print("Monkey climbs onto the box.")
        self.state["on_box"] = True

        print("Monkey grabs the banana!")
        self.state["has_banana"] = True

        print("Goal Achieved: Monkey has the banana.")

# Run
MonkeyBananaProblem().solve()

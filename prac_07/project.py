from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than comparison based on priority (for sorting)."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if the project is completed."""
        return self.completion_percentage == 100

    def update_completion(self, completion_percentage=None, priority=None):
        """Update the completion percentage and/or priority."""
        if completion_percentage is not None:
            self.completion_percentage = completion_percentage
        if priority is not None:
            self.priority = priority

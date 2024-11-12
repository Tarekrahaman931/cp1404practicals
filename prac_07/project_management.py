import csv
from datetime import datetime
from project import Project
import os


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")

    # Use try-except to handle FileNotFoundError
    try:
        projects = load_projects("projects.txt")
        print(f"Loaded {len(projects)} projects from projects.txt")
    except FileNotFoundError:
        print("Error: 'projects.txt' file not found. Please make sure it is in the correct directory.")
        projects = []  # Initialize an empty list if the file is not found

    while True:
        print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
              "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load from: ")
            try:
                projects = load_projects(filename)
            except FileNotFoundError:
                print(f"Error: '{filename}' not found. Please check the filename and try again.")
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_choice = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save_choice == "y":
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            name, start_date, priority, cost, completion = row
            project = Project(name, start_date, int(priority), float(cost), int(completion))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"), project.priority,
                             project.cost_estimate, project.completion_percentage])
    print(f"Projects saved to {filename}.")


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost, completion)
    projects.append(new_project)
    print(f"Added {new_project}")


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]
    print(selected_project)

    new_completion = input("New Percentage (leave blank to keep current): ")
    new_priority = input("New Priority (leave blank to keep current): ")

    selected_project.update_completion(
        completion_percentage=int(new_completion) if new_completion else None,
        priority=int(new_priority) if new_priority else None
    )


if __name__ == "__main__":
    main()

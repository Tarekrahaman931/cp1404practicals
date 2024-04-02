# project_management.py
"""
Project Management Program

Estimated Time: 5 hours

This program manages projects, including loading and saving data from/to a file,
displaying projects, filtering projects by date, adding new projects, and updating projects.

"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:,.2f}, completion: {self.completion}%"

    def update_completion(self, percentage):
        self.completion = percentage

    def update_priority(self, priority):
        self.priority = priority

def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip header
            for line in file:
                name, start_date_str, priority, estimate, completion = line.strip().split('\t')
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                priority = int(priority)
                estimate = float(estimate)
                completion = int(completion)
                projects.append(Project(name, start_date, priority, estimate, completion))
        print(f"Loaded {len(projects)} projects from {file_name}")
    except FileNotFoundError:
        print(f"{file_name} not found. No projects loaded.")
    return projects

def save_projects(projects, file_name):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}\n")
    print(f"Projects saved to {file_name}")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects_by_date(projects, date_str):
    filtered_projects = [project for project in projects if project.start_date > datetime.datetime.strptime(date_str, "%d/%m/%Y").date()]
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))

def update_project(projects):
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.update_completion(int(new_percentage))
    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))

def main():
    file_name = "projects.txt"
    projects = load_projects(file_name)

    print("Welcome to Pythonic Project Management")
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)

        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(projects, file_name)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            save_option = input("Would you like to save to projects.txt? ").lower()
            if save_option.startswith('y'):
                save_projects(projects, "projects.txt")
            print("Thank you for using custom-built project management software.")
            break

if __name__ == "__main__":
    main()

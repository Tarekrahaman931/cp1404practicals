"""
A program to interact with Wikipedia's API using the `wikipedia` Python library.
Prompts the user for a page title or search phrase and fetches details of the page.
Handles exceptions for disambiguation and page errors.
"""

import wikipedia

def get_wikipedia_page():
    """Prompt user for a Wikipedia page title or search phrase and print page details."""
    while True:
        user_input = input("Enter page title (or press Enter to quit): ").strip()
        if not user_input:
            print("Thank you.")
            break

        try:
            # Attempt to fetch a Wikipedia page
            page = wikipedia.page(user_input)
            print("\n" + page.title)
            print(page.summary[:500] + "...\n")  # Print the first 500 characters of the summary
            print(page.url + "\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options[:5])  # Show a sample of options
            print()

        except wikipedia.exceptions.PageError:
            print(f"\nPage id '{user_input}' does not match any pages. Try another id!\n")

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")

if __name__ == "__main__":
    print("Welcome to the Wikipedia search tool!")
    get_wikipedia_page()

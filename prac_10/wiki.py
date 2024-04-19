import wikipedia


def main():
    while True:
        search_input = input("Enter a page title or search phrase (blank to quit): ").strip()
        if not search_input:
            break

        try:
            page = wikipedia.page(search_input, auto_suggest=False)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("DisambiguationError: Please specify your search further.")
        except wikipedia.exceptions.PageError as e:
            print("PageError: Page not found. Please try a different search term.")


if __name__ == "__main__":
    main()

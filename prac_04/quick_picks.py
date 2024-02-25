import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PER_QUICK_PICK = 6

def generate_quick_pick():
    """Generate a single quick pick."""
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PER_QUICK_PICK))

def display_quick_picks(num_quick_picks):
    """Generate and display the specified number of quick picks."""
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)

if __name__ == "__main__":
    main()

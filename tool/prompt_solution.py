import sys
import pyperclip
import os

# Get the problem number from command line arguments
if len(sys.argv) != 2:
    print("Usage: python3 tool/prompt_solution.py <problem_number>")
    sys.exit(1)

problem_number = sys.argv[1]

# Read the prompt_get_solution_lc_problem.md file
file_path = os.path.join(os.path.dirname(__file__), 'prompt_get_solution_lc_problem.md')
with open(file_path, 'r') as file:
    content = file.read()

# Replace #{num} with the provided problem number
updated_content = content.replace("#{num}", f"#{problem_number}")

# Copy the updated content to clipboard
pyperclip.copy(updated_content)

print(f"Solution prompt for problem #{problem_number} has been copied to clipboard.")

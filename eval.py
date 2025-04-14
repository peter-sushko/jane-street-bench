#%%
from litellm import completion

def solve_puzzle_with_llm(text, model_name):
    """
    Solve a text-based puzzle using an LLM.
    
    Args:
        text (str): Text description of the puzzle
        model_name (str): Name of the LLM model to use (default: "gpt-4o")
    
    Returns:
        str: The LLM's solution to the puzzle
    """
    # Prepare the messages with the puzzle text
    messages = [
        {
            "role": "system",
            "content": "You are a puzzle-solving assistant."
        },
        {
            "role": "user",
            "content": f"Please solve this puzzle:\n\n{text}"
        }
    ]
    
    # Call the LLM using LiteLLM
    response = completion(
        model=model_name,
        messages=messages,
        extra_body={"no-log": True}
    )
    
    # Extract and return the solution
    solution = response.choices[0].message.content
    return solution

#%%
def solve_puzzle_from_file(file_path, model_name):
    with open(file_path, 'r') as file:
        puzzle_text = file.read()
    return solve_puzzle_with_llm(puzzle_text, model_name)

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
# Make sure OPENAI_API_KEY is set in the .env file

# Replace with the actual path to your puzzle file
puzzle_file = "puzzles/current.txt"
solution = solve_puzzle_from_file(puzzle_file, "openai/gpt-4o")
print(f"Solution:\n{solution}")
# %%

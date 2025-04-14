from litellm import completion
from dotenv import load_dotenv
import os
import json
from datetime import datetime

MODELS = {
    "gpt-4": {
        "provider": "openai",
        "model": "gpt-4",
        "env_key": "OPENAI_API_KEY"
    },
    "claude-3": {
        "provider": "anthropic",
        "model": "claude-3-opus-20240229",
        "env_key": "ANTHROPIC_API_KEY"
    },
    "gemini": {
        "provider": "google",
        "model": "gemini-pro",
        "env_key": "GOOGLE_API_KEY"
    }
}

NUM_ATTEMPTS = 2  # Number of attempts per model per puzzle

def check_api_keys():
    missing_keys = []
    for model_name, config in MODELS.items():
        if not os.getenv(config["env_key"]):
            missing_keys.append(f"{model_name} ({config['env_key']})")
    return missing_keys

def solve_puzzle(puzzle_text, model_config, attempt_num):
    try:
        if not os.getenv(model_config["env_key"]):
            return f"Error: Missing API key for {model_config['provider']} ({model_config['env_key']})"
            
        messages = [
            {"role": "system", "content": "Solve this puzzle."},
            {"role": "user", "content": puzzle_text}
        ]
        response = completion(
            model=f"{model_config['provider']}/{model_config['model']}",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    load_dotenv()
    
    # Check for missing API keys
    missing_keys = check_api_keys()
    if missing_keys:
        print("Warning: Missing API keys for:", ", ".join(missing_keys))
        print("These models will be skipped")
    
    puzzle_dir = "puzzles"
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    
    # Get the first puzzle file
    puzzle_files = [f for f in os.listdir(puzzle_dir) if f.endswith(".txt")]
    if not puzzle_files:
        print("No puzzle files found!")
        return
        
    filename = puzzle_files[0]
    with open(os.path.join(puzzle_dir, filename), 'r') as f:
        puzzle = f.read()
        
    results = {
        "puzzle": puzzle,
        "timestamp": datetime.now().isoformat(),
        "runs": {}
    }
    
    for model_name, model_config in MODELS.items():
        if os.getenv(model_config["env_key"]):
            results["runs"][model_name] = []
            for attempt in range(NUM_ATTEMPTS):
                print(f"Running {model_name} - Attempt {attempt+1}/{NUM_ATTEMPTS}")
                answer = solve_puzzle(puzzle, model_config, attempt)
                results["runs"][model_name].append(answer)
        else:
            results["runs"][model_name] = [f"Skipped: Missing API key ({model_config['env_key']})"]
    
    # Save results
    output_file = os.path.join(results_dir, f"{filename}_results.json")
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()

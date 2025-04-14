import json
import os
import pandas as pd
from litellm import completion
from dotenv import load_dotenv

def extract_answer(attempt):
    if "Skipped" in attempt:
        return None
        
    try:
        messages = [
            {
                "role": "system",
                "content": "Extract the exact numerical answer with 10 decimal places. Return only the number, or 'None' if no valid answer is found."
            },
            {
                "role": "user",
                "content": f"Extract the exact numerical answer from this text:\n\n{attempt}"
            }
        ]
        response = completion(
            model="gpt-4",
            messages=messages,
            temperature=0
        )
        extracted = response.choices[0].message.content.strip()
        if extracted == "None":
            return None
        return extracted
    except Exception as e:
        print(f"Error extracting answer: {e}")
        return None

def analyze_results():
    load_dotenv()
    
    # Read the results
    results_file = "results/2025_04.txt_results.json"
    with open(results_file, "r") as f:
        results = json.load(f)
    
    # Read the correct answer
    with open("puzzles/2025_04_answer.txt", "r") as f:
        correct_answer = f.read().strip()
    
    # Create summary table
    summary = []
    extracted_answers = {}
    
    for model, attempts in results["runs"].items():
        correct = 0
        total = 0
        extracted_answers[model] = []
        
        for attempt in attempts:
            if "Skipped" in attempt:
                extracted_answers[model].append("Skipped")
                continue
                
            total += 1
            answer = extract_answer(attempt)
            extracted_answers[model].append(answer)
            
            if answer and abs(float(answer) - float(correct_answer)) < 1e-10:
                correct += 1
        
        summary.append({
            "Model": model,
            "Correct": correct,
            "Total": total,
            "Ratio": f"{correct}/{total}" if total > 0 else "0/0"
        })
    
    # Save extracted answers
    answers_file = "analysis/2025_04_extracted_answers.json"
    with open(answers_file, "w") as f:
        json.dump(extracted_answers, f, indent=2)
    
    # Create and save DataFrame
    df = pd.DataFrame(summary)
    output_file = "analysis/2025_04_model_results.csv"
    df.to_csv(output_file, index=False)
    
    print(f"\nExtracted answers saved to {answers_file}")
    print(f"Results saved to {output_file}:")
    print(df)

if __name__ == "__main__":
    os.makedirs("analysis", exist_ok=True)
    analyze_results() 
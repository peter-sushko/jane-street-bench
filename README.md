# Jane Street Puzzle Benchmark

This repository is designed to benchmark the performance of various models in solving Jane Street puzzles. It automates the process of downloading the current puzzle from Jane Street's website and saves it in a structured format (`puzzles/YYYY_MM.txt`). The project aims to evaluate and improve the reasoning capabilities of different models by comparing their success rates on these puzzles.

## Features

- **Automated Puzzle Fetching:** Easily download the latest Jane Street puzzle with a single command using `get_puzzle.py`.
- **Model Evaluation:** Test and compare the performance of different models on the puzzles using `eval.py`.
- **Result Analysis:** Analyze and summarize model performance with `analyze_results.py`, which extracts answers and calculates success rates.

## Setup

1. Clone the repository:
```bash
git clone git@github.com:peter-sushko/jane-street-bench.git
cd jane-street-bench
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up API keys:
   - Ensure you have the necessary API keys in your `.env` file for the models you wish to use.

## Usage

- **Fetch the Current Puzzle:**
  ```bash
  python get_puzzle.py
  ```
  This command downloads the latest puzzle and saves it in the `puzzles` directory.

- **Evaluate Models:**
  ```bash
  python eval.py
  ```
  This script runs the models on the current puzzle and saves the results.

- **Analyze Results:**
  ```bash
  python analyze_results.py
  ```
  This script processes the results, extracts answers, and generates a summary CSV file.

## To-Do

- Implement functionality to use the correct answer for puzzles.
- Explore and integrate more models for solving puzzles.
- Enhance the user interface for better interaction.
- Add logging and error handling for robustness.
- Consider adding a feature to track puzzle-solving performance over time.

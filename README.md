# Jane Street Puzzle Fetcher

A simple Python script to fetch the current puzzle from Jane Street's website.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/petrsushko/jane-street-puzzle-fetcher.git
cd jane-street-puzzle-fetcher
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to fetch the current puzzle:
```bash
python src/fetch_puzzle.py
```

The puzzle will be saved in the `puzzles` directory.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── fetch_puzzle.py
├── puzzles/
│   └── current.txt
└── tests/
    └── test_fetch_puzzle.py
```

## License

MIT License 
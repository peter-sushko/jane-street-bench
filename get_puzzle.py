import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime

def get_puzzle():
    url = "https://www.janestreet.com/puzzles/current-puzzle/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    puzzle_div = soup.find('div', class_='current-puzzle')
    if not puzzle_div:
        return None
        
    text = puzzle_div.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    puzzle = max((line for line in lines if len(line) > 100 and 'submit' not in line.lower()), 
                key=len, default=None)
    
    return puzzle

# Create puzzles directory with year/month structure
now = datetime.now()
puzzles_dir = Path('puzzles') / str(now.year) / f"{now.month:02d}"
puzzles_dir.mkdir(parents=True, exist_ok=True)

# Save puzzle with timestamp
puzzle = get_puzzle()
if puzzle:
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"puzzle_{timestamp}.txt"
    with open(puzzles_dir / filename, 'w') as f:
        f.write(puzzle) 
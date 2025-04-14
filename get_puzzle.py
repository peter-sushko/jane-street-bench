import requests
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime

def get_puzzle():
    try:
        url = "https://www.janestreet.com/puzzles/current-puzzle/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        puzzle_div = soup.find('div', class_='puzzle-content') or soup.find('div', class_='content')
        
        if not puzzle_div:
            return None
            
        paragraphs = puzzle_div.find_all('p')
        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 100 and not any(x in text.lower() for x in ['submit', 'cookie', 'email', 'copyright', 'jane street', 'leaderboard']):
                return text
                
        return None
        
    except Exception:
        return None

puzzles_dir = Path('puzzles')
puzzles_dir.mkdir(exist_ok=True)

puzzle = get_puzzle()
if puzzle:
    now = datetime.now()
    filename = f"{now.year}_{now.month:02d}.txt"
    with open(puzzles_dir / filename, 'w') as f:
        f.write(puzzle) 
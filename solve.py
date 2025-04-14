import requests
from bs4 import BeautifulSoup
from pathlib import Path
import re

def get_puzzle():
    try:
        url = "https://www.janestreet.com/puzzles/current-puzzle/"
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Print out all divs and their classes for debugging
        print("\nAll divs and their classes:")
        for div in soup.find_all('div'):
            if div.get('class'):
                print(f"Class: {div.get('class')}")
                text = div.get_text().strip()
                if len(text) > 100:  # Only print long text that might be the puzzle
                    print(f"Text: {text[:200]}...")
                print()
        
        # Find the puzzle content
        puzzle_div = soup.find('div', class_='content')
        if not puzzle_div:
            print("Could not find content div")
            return None
            
        # Get all text content and clean it up
        paragraphs = puzzle_div.find_all('p')
        puzzle_text = ""
        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 100 and not any(x in text.lower() for x in ['submit', 'cookie', 'email', 'copyright', 'jane street']):
                puzzle_text = text
                break
                
        if not puzzle_text:
            print("Could not find puzzle text")
            return None
            
        return puzzle_text
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# Create puzzles directory
puzzles_dir = Path('puzzles')
puzzles_dir.mkdir(exist_ok=True)

# Get and save puzzle
puzzle = get_puzzle()
if puzzle:
    output_file = puzzles_dir / 'current2.txt'
    with open(output_file, 'w') as f:
        f.write(puzzle)
    print("Successfully saved puzzle")
else:
    print("Failed to get puzzle content") 
import requests
import os.path

def joke():
    """Parses API from icanhazdadjoke.com and returns a random joke"""
    r = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
    raw_joke = r.json()
    joke = raw_joke['joke']

    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, "./templates/joke.txt")
    
    # Writes joke for joke.txt in plain text
    with open(filepath, 'w') as f:
        f.write("Joke: "+ str(joke))

    return joke

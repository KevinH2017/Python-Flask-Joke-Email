import requests
import os.path


def joke():
    """Parses API from icanhazdadjoke.com and returns a random joke"""
    # Gets joke from website API
    r = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
    raw_joke = r.json()
    joke = raw_joke['joke']

    # Creates path relative to workspace
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, "./templates/joke.txt")
    
    with open(filepath, 'w') as f:
        f.write("Joke: "+ str(joke) + "\n")
        f.write("From https://icanhazdadjoke.com/")

    return joke

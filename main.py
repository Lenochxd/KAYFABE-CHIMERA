from data import strings
import itertools
import requests

print(len(strings))
print('starting')

for string in strings:
    char_combinations = [(char.lower(), char.upper()) for char in string]
    all_combinations = itertools.product(*char_combinations)
    result = [''.join(combination) for combination in all_combinations]
    print(len(result))
    for combo in result:
        print(combo)
        url = f"https://pastebin.com/raw/{combo}"
        response = requests.get(url)
        if '404' not in response.text:
            print('=========== FOUND ===========')
            print(response.text)
            with open(f"OUTPUT-{combo}.txt", "w") as f:
                f.write(response.text)



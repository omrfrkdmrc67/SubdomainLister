import requests

target_input = input("Enter Your Target Website: ")

with open("subdomain.txt", "r") as subdomain:
    for word in subdomain:
        word = word.strip()
        url = f"http://{word}.{target_input}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found: {url}")
            else:
                print(f"Not found (status code {response.status_code}): {url}")
        except requests.ConnectionError:
            print(f"Failed to connect: {url}")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

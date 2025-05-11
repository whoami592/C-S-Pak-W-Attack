import requests

def crash_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is up and running.")
        else:
            print("Website is down.")
    except:
        print("Website is down.")

# Example usage
crash_website("https://www.example.com")
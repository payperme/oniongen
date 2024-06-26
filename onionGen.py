import requests
import secrets
import time

def urlGenerator():

    alphabet = 'abcdefghijklmnopqrstuvwxyz234567'
    rand_string = ''.join(secrets.choice(alphabet) for _ in range(56))
    onion_url = 'http://' + rand_string + '.onion'
    print(f"Triying: {onion_url}")
    return onion_url

def listUrl(onion):
    with open("onionDirectory.txt", "a") as file:
        file.write(onion + "\n")

def checkOnline(url):
    torNet = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        r = requests.get(url, proxies=torNet, timeout=30)
        if r.status_code == 200:
            listUrl(url)
        else:
            print(r.status_code)
    except requests.exceptions.RequestException as e:
        if "SOCKSHTTPConnectionPool" in str(e):
            print('not lucky')
        else:
            print(f"{e}")

if __name__ == "__main__":
    while True:
        onion_url = urlGenerator()
        checkOnline(onion_url)
        time.sleep(3)

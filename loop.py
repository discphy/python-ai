from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://x.com",
    "facebook.com",
    "https://tictok.com"
)

results = {}

for x in websites:
    if not x.startswith("https://"):
        x = f"https://{x}"
    response = get(x)

    if response.status_code == 200:
        results[x] = 'ok'
    else:
        results[x] = 'failed'

print(results)
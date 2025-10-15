import webbrowser
from datetime import datetime

# Your website URL
url = "https://veggyshoppingcart.netlify.app/"

# Open the website in the default browser
webbrowser.open(url)

# Log the visit
with open("usage_log.txt", "a") as log_file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"[{timestamp}] Visited: {url}\n")

print("Website opened and visit logged!")

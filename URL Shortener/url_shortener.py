import pyshorteners

def shorten_url(long_url):
    # Create a Shortener object
    shortener = pyshorteners.Shortener()

    # Shorten the URL using TinyURL (default service)
    short_url = shortener.tinyurl.short(long_url)

    return short_url

def main():
    # Ask the user for a long URL
    long_url = input("Enter the URL to shorten: ")

    # Shorten the URL
    try:
        short_url = shorten_url(long_url)
        print(f"Shortened URL: {short_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
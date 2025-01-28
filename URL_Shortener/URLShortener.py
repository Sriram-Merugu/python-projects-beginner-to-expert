#  This library provides a simple interface to various URL shortening services.
import pyshorteners as py


# Function for shortening the given URL
def shorten_url(url):
    # Creating an instance of the Shortener class from the pyshorteners library.
    shortener = py.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url


# Enter the URL
url = input("Enter the URL: ")
short_url = shorten_url(url)
print("Shortened URL: ", short_url)

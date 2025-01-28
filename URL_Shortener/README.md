# URL-Shortener
This Python script demonstrates the usage of the pyshorteners library to shorten a given URL using various URL shortening services. It provides a simple interface for generating shorter and more manageable URLs.

# Dependencies
1. Python 3.x
2. pyshorteners library

# Here's how the code works:

1. The pyshorteners library is imported to provide the URL shortening functionality.
2. The shorten_url function is defined, which takes a URL as a parameter.
3. Inside the function, an instance of the Shortener class from the pyshorteners library is created. This instance allows us to access different URL shortening services.
4. The short method is called on the tinyurl attribute of the shortener instance, passing the original URL as an argument. This method returns the shortened URL.
5. The shortened URL is then returned from the shorten_url function.
6. The main part of the code prompts the user to enter a URL.
7. The shorten_url function is called with the user-provided URL, and the resulting shortened URL is stored in the short_url variable.
8. Finally, the shortened URL is printed as output.

# Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.



# Acknowledgements
1. The pyshorteners library: GitHub
2. GitHub Link: https://github.com/ellisonleao/pyshorteners/

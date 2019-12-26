from apps import jumpstart
import requests
import bs4

def main():
    jumpstart.print_title("WEATHER APP")
    postcode = input("What is your postcode? ")
    raw_html = get_web_data(postcode)
    fetched_data = parse_html(raw_html)

    print("The weather in {} is {} and {}.".format(fetched_data[0], fetched_data[1], fetched_data[2], ))

def get_web_data(postcode):
    url = "https://www.wunderground.com/weather/gb/{}".format(postcode)
    raw_data = requests.get(url)
    return raw_data.text

def parse_html(raw_html):
    soup = bs4.BeautifulSoup(raw_html, "html.parser")
    location = soup.find(class_="city-header").find("h1").get_text().split(",")[0]
    temperature = soup.find(class_="current-temp").get_text()
    condition = soup.find(class_="condition-icon").get_text()

    return (location, temperature, condition)

if __name__ == '__main__':
    main()
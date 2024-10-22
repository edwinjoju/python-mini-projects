import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path):
    websites = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[0]:
                websites.append(f'https://{row[0]}')
            else:
                websites.append(row[0])
    return websites

def get_useragent():
    ua = UserAgent()
    return ua.chrome

def get_status_desc(status_code):
    for value in HTTPStatus:
        if value == status_code:
            description = f'({value.value} | {value.name}) | {value.description}'
            return description
    return '(???) Unknown status code...'

def check_website(website, user_agent):
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_desc(code))
    except Exception as e:
        print(f"Could not get information for {website}: {e}")

def main():
    sites = get_websites('websites.csv')
    user_agent = get_useragent()
    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
    main()

import re


def read_file(filepath):
    with open(filepath,'r') as file:
        return file.read()


def extract_urls(text):
    url_pattern = r'https?://[^\s"\'>]+'
    return re.findall(url_pattern, text)

def main():
    text = read_file('webpage.txt')
    urls = extract_urls(text)
    for url in urls:
        print(f" - {url}")

if __name__ == "__main__":
    main()

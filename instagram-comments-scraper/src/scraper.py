thonimport requests
from bs4 import BeautifulSoup
import json
import os
from instagram_parser import parse_instagram_post

def scrape_comments(post_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Send GET request to the Instagram post URL
    response = requests.get(post_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page: {response.status_code}")

    # Parse the Instagram page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse the comments and metadata from the page
    comments_data = parse_instagram_post(soup)

    # Save the output to a file
    output_path = os.path.join('data', 'sample_output.json')
    with open(output_path, 'w') as outfile:
        json.dump(comments_data, outfile, indent=4)

    print(f"Scraping completed successfully. Output saved to {output_path}")
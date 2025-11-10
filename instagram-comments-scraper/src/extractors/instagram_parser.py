thonimport json
from bs4 import BeautifulSoup

def parse_instagram_post(soup):
    """
    Extracts comments and metadata from an Instagram post page.
    :param soup: BeautifulSoup object containing the Instagram post HTML
    :return: List of comments and metadata
    """
    data = []

    # Instagram posts are rendered as JavaScript JSON objects
    script = soup.find('script', text=lambda t: t and 'window._sharedData' in t)
    if not script:
        raise Exception("Unable to find post data in the page.")

    # Extract the JSON data from the script
    shared_data = script.string.split('= ', 1)[1].rstrip(';')
    shared_data = json.loads(shared_data)

    # Navigate through the post data
    media = shared_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    comments = media['edge_media_to_comment']['edges']

    for comment in comments:
        node = comment['node']
        comment_data = {
            'pk': node['id'],
            'user_id': node['owner']['id'],
            'created_at': node['created_at'],
            'media_id': media['id'],
            'text': node['text'],
            'comment_like_count': node['edge_liked_by']['count'],
            'user': {
                'username': node['owner']['username'],
                'full_name': node['owner']['full_name'],
                'profile_pic_url': node['owner']['profile_pic_url']
            }
        }
        data.append(comment_data)

    return data
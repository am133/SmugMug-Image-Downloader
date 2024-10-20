import os
import requests
from requests_oauthlib import OAuth1Session
from concurrent.futures import ThreadPoolExecutor, as_completed

# Replace these with your own values
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
USERNAME = 'your_smugmug_username'


# Set up OAuth1 session
oauth = OAuth1Session(API_KEY, client_secret=API_SECRET,
                      resource_owner_key=ACCESS_TOKEN, resource_owner_secret=ACCESS_TOKEN_SECRET)

# Function to fetch all folders
def fetch_folders():
    url = f'https://api.smugmug.com/api/v2/folder/user/{USERNAME}!folderlist'
    headers = {'Accept': 'application/json'}
    response = oauth.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()['Response']['FolderList']

# Function to fetch album list within a folder
def fetch_album_list(folder_url):
    url = f'https://api.smugmug.com{folder_url}!albumlist'
    headers = {'Accept': 'application/json'}
    response = oauth.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()['Response']['AlbumList']

# Function to fetch images in an album with pagination support
def fetch_images(album_url):
    images = []
    url = f'https://api.smugmug.com{album_url}!images'
    headers = {'Accept': 'application/json'}

    while url:
        response = oauth.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()['Response']
        images.extend(data['AlbumImage'])
        url = data.get('Pages', {}).get('NextPage')
        if url:
            url = f'https://api.smugmug.com{url}'

    return images

# Function to download an image
def download_image(image_info, download_path):
    # Check if file already exists
    if os.path.exists(download_path):
        print(f'Skipping {download_path}, file already exists.')
        return

    image_download_url = image_info['ArchivedUri']

    # Download the image
    with requests.get(image_download_url, stream=True) as r:
        r.raise_for_status()
        with open(download_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f'Downloaded image to {download_path}')

def process_album(album, folder_name):
    album_name = album['Name']
    album_url = album['Uri']
    album_path = os.path.join(folder_name, album_name)
    os.makedirs(album_path, exist_ok=True)

    images = fetch_images(album_url)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(download_image, image, os.path.join(album_path, image['FileName'])) for image in images]
        for future in as_completed(futures):
            future.result()  # To raise exceptions if any

def main():
    folders = fetch_folders()
    for folder in folders:
        folder_name = folder['Name']
        folder_url = folder['Uri']
        os.makedirs(folder_name, exist_ok=True)

        albums = fetch_album_list(folder_url)
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(process_album, album, folder_name) for album in albums]
            for future in as_completed(futures):
                future.result()  # To raise exceptions if any

if __name__ == '__main__':
    main()

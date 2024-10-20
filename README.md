# SmugMug Image Downloader

This Python script allows you to download all images from your SmugMug account by fetching folders and albums, then downloading images from those albums.

## Features

- Fetch all folders and albums from your SmugMug account.
- Download all images from each album.
- Supports pagination when fetching large image collections.
- Multi-threaded downloading to speed up the download process.

## Prerequisites

Before using the script, you will need:

1. **Python 3.x** installed on your machine.
2. The following Python libraries:
   - `requests`
   - `requests_oauthlib`
   - `concurrent.futures` (part of the standard library in Python 3.x)

You can install the required dependencies using pip:

```bash
pip install requests requests_oauthlib
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/am133/SmugMug-Image-Downloader.git
cd SmugMug-Image-Downloader
```

### 2. Set Up Your SmugMug API Credentials

You will need your SmugMug API credentials to use the script. Obtain the following values from your [SmugMug API account](https://api.smugmug.com):

- `API_KEY`
- `API_SECRET`
- `ACCESS_TOKEN`
- `ACCESS_TOKEN_SECRET`
- `USERNAME`

Replace the placeholder values in the script `SmugMugDownloader.py` with your own credentials:

```python
# Replace these with your own values
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
USERNAME = 'your_smugmug_username'
```

### 3. Run the Script

Once you have set up your credentials, you can run the script:

```bash
python SmugMugDownloader.py
```

The script will:

- Fetch all folders and albums from your SmugMug account.
- Download all images from the albums into directories matching the folder and album structure of your SmugMug account.

### 4. Folder Structure

The script will create directories for each folder and album in your current working directory. Images will be saved in the corresponding album folders.

```plaintext
/Folder1
    /Album1
        - image1.jpg
        - image2.jpg
    /Album2
        - image1.jpg
        - image2.jpg
/Folder2
    /Album1
        - image1.jpg
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This Markdown version ensures that the code blocks, lists, and headings are formatted properly for GitHub's markdown renderer. You can directly copy this into your `README.md` file, and it should display correctly on your repository page.

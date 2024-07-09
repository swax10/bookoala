import os
import requests
import json
import pandas as pd

def books(input_str):
    """
    Retrieve and process book information from the Google Books API based on the input string.

    Parameters:
    input_str (str): A JSON string representing a dictionary with keys 'category' and 'maxResults'.
                     Example: '{"category": "fiction", "maxResults": 50}' or "{'category': 'science', 'maxResults': 100}"

    Returns:
    pandas.DataFrame: A DataFrame containing processed book information, with 'rank' as the index.

    Raises:
    requests.exceptions.RequestException: If an error occurs during the API request.
    json.JSONDecodeError: If the input string is not a valid JSON.
    KeyError: If required keys are missing from the API response.
    ValueError: If the input parameters are invalid or missing.
    """
    try:
        input_data = json.loads(input_str)
        category = input_data['category']
        max_results = int(input_data['maxResults'])
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

    url = 'https://www.googleapis.com/books/v1/volumes'
    api_key = os.getenv('GOOGLE_BOOKS_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_BOOKS_API_KEY environment variable is not set")

    processed_results = []
    max_allowed_results = 40
    start_index = 0

    while len(processed_results) < max_results:
        params = {
            'q': f'subject:{category}',
            'maxResults': min(max_results - len(processed_results), max_allowed_results),
            'key': api_key,
            'orderBy': 'relevance',
            'startIndex': start_index
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Error fetching data from API: {e}")

        if 'items' not in data:
            break

        for item in data['items']:
            book = {
                'rank': len(processed_results) + 1,
                'title': item['volumeInfo'].get('title', 'Unknown Title'),
                'authors': item['volumeInfo'].get('authors', ['Unknown Author']),
                'publisher': item['volumeInfo'].get('publisher', 'Unknown Publisher'),
                'publishedDate': item['volumeInfo'].get('publishedDate', 'Unknown Date'),
                'description': item['volumeInfo'].get('description', 'No Description'),
                'categories': item['volumeInfo'].get('categories', ['Unknown Category']),
            }
            processed_results.append(book)

            if len(processed_results) >= max_results:
                break

        start_index += len(data['items'])

    df = pd.DataFrame(processed_results)

    df.set_index('rank', inplace=True)

    return df
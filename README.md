# NewsAPI

A simple Flask-based REST API to fetch the latest news from Ada Derana (Sri Lankan news website).

## Description

This API scrapes news articles from Ada Derana and provides them in a structured JSON format. It supports multiple news categories including hot news, sports, entertainment, and technology.

## Features

- Fetch latest news from Ada Derana
- Multiple news categories supported
- Clean JSON response format
- Easy to deploy on Vercel or any Python-compatible hosting

## Installation

1. Clone the repository:
```
git clone https://github.com/NandiyaLive/NewsAPI.git
cd NewsAPI
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Home
```
GET /
```
Returns API information and available endpoints.

### News Categories

#### Hot News
```
GET /hot-news
```

#### Sports News
```
GET /sports-news
```

#### Entertainment News
```
GET /entertainment-news
```

#### Technology News
```
GET /technology-news
```

## Response Format

```json
{
  "success": true,
  "category": "hot-news",
  "news": [
    {
      "title": "News Title",
      "url": "https://...",
      "summary": "Brief description...",
      "date": "01 Jan 2024",
      "time": "12:00 PM",
      "imageUrl": "https://..."
    }
  ]
}
```

## Error Response

```json
{
  "success": false,
  "category": "category-name",
  "error": "Error message"
}
```

## Technologies Used

- Python 3
- Flask - Web framework
- BeautifulSoup4 - Web scraping
- Requests - HTTP library
- LXML - XML/HTML parser

## Author

**Neranjana Prasad**
- Website: https://neranjana.me
- GitHub: [@NandiyaLive](https://github.com/NandiyaLive)

## License

See LICENSE file for details.

## Disclaimer

This API scrapes content from Ada Derana. Please ensure you comply with their terms of service and robots.txt when using this API.

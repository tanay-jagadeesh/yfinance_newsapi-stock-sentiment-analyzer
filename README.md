# Reddit Sentiment Analyzer for Stock Mentions

## What it does
Scrapes r/wallstreetbets, analyzes sentiment around stocks, correlates with price movements

## Data Science concepts covered
- Natural Language Processing (NLP)
- Sentiment analysis (VADER or transformers)
- Time series analysis
- Correlation analysis
- Data visualization

## Tech stack
- Python
- Reddit API (PRAW)
- NLTK/TextBlob
- pandas
- Streamlit

## Project phases

### Day 1-2: Set up Reddit scraping
- [ ] Get Reddit API credentials (free)
- [ ] Install PRAW: `pip install praw pandas`
- [ ] Create `reddit_scraper.py`
- [ ] Scrape last 100 posts from r/wallstreetbets
- [ ] Extract: post title, body, score, comments, timestamp
- [ ] Save to CSV
- [ ] Commit to GitHub

## Getting Started
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Reddit API credentials
4. Run the scraper: `python reddit_scraper.py`

## Author
tanay-jagadeesh

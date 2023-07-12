# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_twitterscraper.ipynb.

# %% auto 0
__all__ = ['scrape_twitter_page', 'extract_tweets_from_file']

# %% ../nbs/00_twitterscraper.ipynb 3
import time
def scrape_twitter_page(driver, url, scroll_limit=10, sleep_time=2):
    # Open the desired Twitter page
    driver.get(url)
    import time
    # Wait for the page to load
    time.sleep(sleep_time)

    # Scroll to the bottom of the page
    scroll_count = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while scroll_count <= scroll_limit:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_time)  # Adjust the sleep time as needed to ensure the page loads new content

        # Retrieve the HTML content of the page
        html_content = driver.page_source

        # Save the HTML content to a file
        with open(f"twitter_content_{scroll_count}.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        scroll_count += 1

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# %% ../nbs/00_twitterscraper.ipynb 4
def extract_tweets_from_file(file_path):
    from bs4 import BeautifulSoup

    with open(file_path, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')
    tweet_tags = soup.find_all('span', {'class': ['css-901oao', 'css-16my406', 'r-poiln3', 'r-bcqeeo', 'r-qvutc0']})
    
    tweets = []
    for tag in tweet_tags:
        tweets.append(tag.text)
    
    return tweets

from pathlib import Path
import datetime
import pytz

import feedparser

def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

def update_readme_medium_posts(medium_feed, readme_base, join_on):
    d = feedparser.parse(medium_feed)
    posts = []
    for item in d.entries:
        if item.get('tags'):
            posts.append(f" - [{item['title']}]({item['link']})")
    posts_joined = '\n'.join(posts)
    return readme_base[:readme_base.find(rss_title)] + f"{join_on}\n{posts_joined}"

rss_title = "### Check out my Medium Post" # Anchor for where to append posts
readme = Path('../README.md').read_text()
updated_readme = update_readme_medium_posts("https://medium.com/feed/@vedantkadam541", readme, rss_title)
with open('../README.md', "w+") as f:
    f.write(updated_readme + update_footer())

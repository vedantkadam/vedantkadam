from pathlib import Path
import datetime
import pytz

import feedparser

def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

readme = Path('../README.md').read_text()

with open('../README.md', "w+") as f:
    f.write(update_footer())

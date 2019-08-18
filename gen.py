from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

POSTS_DIR = 'posts'

env = Environment(loader=FileSystemLoader('./pages/'))
post_template = env.get_template('post.html')
home_template = env.get_template('home.html')


POSTS = {}
for markdown_post in os.listdir(POSTS_DIR):
    file_path = os.path.join(POSTS_DIR, markdown_post)

    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])

# sort posts by date
POSTS = {
    post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}

home_posts_metadata = [POSTS[post].metadata for post in POSTS]

home_html_content = home_template.render(posts=home_posts_metadata)

with open('site/home.html', 'w') as file:
    file.write(home_html_content)

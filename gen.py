from markdown2 import markdown
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime
from shutil import copyfile

POSTS_DIR = 'posts'
BUILD_DIR = 'site'
CSS_DIR = 'css'

env = Environment(loader=FileSystemLoader('./pages/'))
post_template = env.get_template('post.html')


def render_about():
    template = env.get_template('about.html')
    with open(f'{BUILD_DIR}/about.html', 'w') as file:
        file.write(template.render())


render_about()


POSTS = {}
for markdown_post in os.listdir(POSTS_DIR):
    file_path = os.path.join(POSTS_DIR, markdown_post)

    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])


def transform_metadata(post):
    post.metadata['tags'] = post.metadata['tags'].split(',')
    return post


# sort posts by date
# this should just be a list...
POSTS = {
    post: transform_metadata(POSTS[post]) for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d'), reverse=True)
}


def render_index():
    index_posts_metadata = [POSTS[post].metadata for post in POSTS]

    index_template = env.get_template('index.html')
    index_html_content = index_template.render(posts=index_posts_metadata)

    with open(f'{BUILD_DIR}/index.html', 'w') as file:
        file.write(index_html_content)


render_index()


def render_topics():
    tags = set()
    # map of category to list of paths
    posts_by_category = defaultdict(list)
    for path, post in POSTS.items():
        for tag in post.metadata['tags']:
            tags.add(tag)
            posts_by_category[tag].append(post.metadata)

    template = env.get_template('topics.html')
    with open(f'{BUILD_DIR}/topics.html', 'w') as file:
        file.write(template.render(topics=tags))

    topic_template = env.get_template('topic.html')
    for tag in tags:
        topic_path = f'{BUILD_DIR}/topics/{tag}/'
        os.makedirs(os.path.dirname(topic_path), exist_ok=True)
        with open(f'{topic_path}index.html', 'w') as file:
            print('writing', tag, posts_by_category[tag])
            file.write(topic_template.render(
                topic=tag, posts=posts_by_category[tag]))

    # each topic should have a blurb


render_topics()


for post in POSTS:
    post_metadata = POSTS[post].metadata

    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date'],
        'tags': post_metadata['tags'],
    }

    post_html_content = post_template.render(post=post_data)

    post_file_path = f"{BUILD_DIR}/posts/{post_metadata['slug']}/index.html"

    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html_content)

os.makedirs(os.path.join(BUILD_DIR, 'css'), exist_ok=True)
for css_file in os.listdir(CSS_DIR):
    copyfile(os.path.join(CSS_DIR, css_file), f'{BUILD_DIR}/css/{css_file}')

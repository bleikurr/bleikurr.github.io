#!/usr/bin/env python3

import os
import re
import json

GUIDE_DIRECTORY = './guides'
OUTPUT_FILE = './_data/nav.json'

def parse_title(filename):
    with open(filename, 'r') as file:
        content = file.read()
        match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if match:
            content = match.group(1)
            match = re.match(r'^title:(.*?)$', content)
            if match:
                stripped = match.group(1).strip()
                stripped = stripped.strip("\"'")
                return stripped
            else:
                return None
        else:
            return None


def create_nav_list():
    categories = [f for f in os.listdir(GUIDE_DIRECTORY) if os.path.isdir(f"{GUIDE_DIRECTORY}/{f}")]

    categories.sort(key = lambda c: c.lower())

    categories_list = []
    for category in categories:
        cat_guides = []
        directory = f"{GUIDE_DIRECTORY}/{category}"
        files = [f for f in os.listdir(directory) if os.path.isfile(f"{directory}/{f}")]

        for file in files:
            file_path = f"{directory}/{file}"
            title = parse_title(file_path)
            if title is None:
                continue
            url_path = os.path.splitext(file_path)[0][1:] # Get rid of .md and then the . in front of ./guides

            cat_guides.append({
                'title': title,
                'path': url_path
            })

        def sorting_key_guides(g):
            return g['title'].lower()

        cat_guides.sort(key=sorting_key_guides)
        categories_list.append({
            'name': category,
            'guides': cat_guides
        })


    return categories_list


# Example usage:
categories = create_nav_list()
categories_json = json.dumps(categories)

with open(OUTPUT_FILE, 'w') as f:
    f.write(categories_json)



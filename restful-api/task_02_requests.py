#!/usr/bin/env python3
import requests
import csv
"""
import module
"""


def fetch_and_print_posts():
    """
    function
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status = response.status_code
    posts = response.json()

    print(f"Status Code: {status}")

    for post in posts:
        print(post["title"])


def fetch_and_save_posts():
    """
    function 2
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status = response.status_code

    if status == 200:
        posts = response.json()
        with open("posts.csv", 'w') as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(posts)

fetch_and_save_posts()
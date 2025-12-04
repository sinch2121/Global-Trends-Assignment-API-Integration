import requests
import json
import os
import sys

CACHE_FILE = "cache.json"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"


# ------------------------------------------------------------
# Helper: Load cache
# ------------------------------------------------------------
def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


# ------------------------------------------------------------
# Helper: Save cache
# ------------------------------------------------------------
def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------------------------------------------------
# Fetch data from API with error handling
# ------------------------------------------------------------
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)

        # Network / Status error
        response.raise_for_status()

        # Validate JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            print("❌ Error: Malformed JSON response.")
            return None

    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("❌ Network Error: Unable to connect.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")

    return None


# ------------------------------------------------------------
# Initialize cache (fetch if not found)
# ------------------------------------------------------------
def initialize_cache():
    cache = load_cache()

    if "posts" not in cache:
        print("Fetching posts from API...")
        posts = fetch_data(POSTS_URL)
        if posts is None:
            print("❌ Unable to fetch posts.")
            sys.exit()
        cache["posts"] = posts

    if "users" not in cache:
        print("Fetching users from API...")
        users = fetch_data(USERS_URL)
        if users is None:
            print("❌ Unable to fetch users.")
            sys.exit()
        cache["users"] = users

    save_cache(cache)
    return cache


# ------------------------------------------------------------
# CLI Functions
# ------------------------------------------------------------
def list_posts(cache, user_filter=None):
    posts = cache.get("posts", [])

    if user_filter:
        posts = [p for p in posts if p.get("userId") == user_filter]

    if not posts:
        print("No posts found.")
        return

    for post in posts[:10]:  # limit output
        print(f"[ID: {post['id']}] {post['title']}")


def view_post(cache, post_id):
    posts = cache.get("posts", [])
    post = next((p for p in posts if p["id"] == post_id), None)

    if not post:
        print("❌ Post not found.")
        return

    print("\n==== POST DETAILS ====")
    print(f"ID: {post['id']}")
    print(f"User ID: {post['userId']}")
    print(f"Title: {post['title']}")
    print(f"Body:\n{post['body']}")


# ------------------------------------------------------------
# Main CLI Menu
# ------------------------------------------------------------
def main():
    cache = initialize_cache()

    while True:
        print("\n==== API MENU ====")
        print("1. List posts")
        print("2. List posts (filter by userId)")
        print("3. Show post details by ID")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_posts(cache)

        elif choice == "2":
            try:
                user_id = int(input("Enter userId: "))
                list_posts(cache, user_id)
            except ValueError:
                print("Invalid userId. Must be a number.")

        elif choice == "3":
            try:
                post_id = int(input("Enter post ID: "))
                view_post(cache, post_id)
            except ValueError:
                print("Invalid ID. Must be numeric.")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

GLOBAL TREND – API Integration Internship Assignment

This mini-application fetches data from two public REST API endpoints, caches the data locally, and allows users to view, filter, and inspect individual items using a simple CLI interface.

Features: 

Fetches data from two API endpoints (/posts and /users)

Caches data in a local file: cache.json

CLI interface to:

✔ List posts

✔ Filter posts by userId

✔ View post details by ID

Full error handling:

Network failures

Timeouts

Invalid / malformed JSON

Missing fields

Lightweight, fast, and simple to run

Tech Stack

Python 3

Requests library

JSONPlaceholder API (public, no authentication required)

API Endpoints Used

Posts:
https://jsonplaceholder.typicode.com/posts

Users:
https://jsonplaceholder.typicode.com/users

Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd globaltrend_api_assignment

2. Create virtual environment (optional)
python -m venv venv


Activate:

Windows:

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python main.py

How to Use the CLI

After running, the menu appears:

==== API MENU 
1. List posts
2. List posts (filter by userId)
3. Show post details by ID
4. Exit

✔ List all posts

Choose: 1

✔ Filter posts by userId

Choose: 2
Enter a numeric userId (e.g., 3)

✔ View single post details

Choose: 3
Enter post ID (e.g., 5)

Cache File

API results are stored in cache.json

This prevents repeated API calls and speeds up the program

Error Handling: 

The script handles:

Network issues

Timeout errors

Malformed or missing fields

Invalid user input

Missing post IDs

Assumptions: 

JSONPlaceholder API is stable and reliable

Data structure remains consistent

CLI output is acceptable as per assignment instructions

Author: 

Sinchana Salimath
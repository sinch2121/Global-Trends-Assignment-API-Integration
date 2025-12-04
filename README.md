GLOBAL TREND – API Integration Internship Assignment

This mini-application fetches data from two public REST API endpoints, caches the data locally, and allows users to view, filter, and inspect individual items using a simple CLI interface.

Features: 

1. Fetches data from two API endpoints (/posts and /users)

2. Caches data in a local file: cache.json

CLI interface to:

✔ List posts

✔ Filter posts by userId

✔ View post details by ID

Full error handling:

1. Network failures

2. Timeouts

3. Invalid / malformed JSON

4. Missing fields

5. Lightweight, fast, and simple to run

Tech Stack

1. Python 3

2. Requests library

3. JSONPlaceholder API (public, no authentication required)

4. API Endpoints Used

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

1. API results are stored in cache.json

This prevents repeated API calls and speeds up the program

Error Handling: 

The script handles:

1. Network issues

2. Timeout errors

3. Malformed or missing fields

4. Invalid user input

5. Missing post IDs

Assumptions: 

1. JSONPlaceholder API is stable and reliable

2. Data structure remains consistent

3. CLI output is acceptable as per assignment instructions

Author: 

Sinchana Salimath

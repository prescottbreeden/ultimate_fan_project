# ultimate_fan_project
trivia game about athletes from multiple categories, all web scraped

login to play.  passwords are hashed and salted with bcrypt.  all trivia questions were generated through webscraping with beautiful soup.  trivia answers were then censored before being written and saved as csv files before inserting to the db.

# Install
1. clone directory
2. create environment and run 'pip install -r requirements.txt'

# To Run
1. run 'python3 manage.py runserver' in CLI from project root (ctrl-c will terminate the process)
2. app will be running at 'localhost:8000' in your browser

# ultimate_fan_project
trivia game about athletes from multiple categories, all web scraped

login to play.  passwords are hashed and salted with bcrypt.  all trivia questions were generated from beautiful soup and filtered server-side before being written
and saved as csv files and then uploaded to the db.

To Do:
- fix responsive sizing on quiz selection page
- fix bar chart axis label color
- extend animation for questions to accomodate ultra wide displays
- make mobile version that can show correct/incorrect responses during quiz taking
- reduce registration to alias/email/password
- login with email or alias
- compare your overall quiz history with another user

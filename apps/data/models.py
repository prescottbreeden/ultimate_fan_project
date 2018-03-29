from django.db import models
from apps.quiz.models import *
import csv

# categories = ['football', 'soccer', 'baseball', 'basketball', 'hockey', 'boxing', 'golf', 'martial arts', 'tennis']
# for sport in categories:
# 	Category.objects.create(
# 		activity_type = sport,
# 	)


# with open('./apps/data/athletes.csv') as csvfile:
# 	csv_reader = csv.DictReader(csvfile)
# 	for row in csv_reader: 
# 		People.objects.create(
# 			name = row['Name'],
# 			category = Category.objects.get(id=row['Category']),
# 			abstract = row['Abstract'],
# 			)

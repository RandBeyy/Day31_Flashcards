import csv 

with open('data/french_words.csv') as f:
   for line in csv.DictReader(f, fieldnames=('fr', 'en')):
      print(line)
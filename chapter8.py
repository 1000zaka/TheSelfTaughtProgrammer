# No.2
import os
"""
with open("test.txt", "w",encoding="utf-8") as f:
    kmnrider = input("あなたが好きな仮面ライダーは？")
    f.write(kmnrider)
"""

# No.3
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("csv1.csv", "w") as movie_csvfile:
    movies_list = csv.writer(movie_csvfile, delimiter=",")
    for movie in movies:
        movies_list.writerow(movie)
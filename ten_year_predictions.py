from findMatariki import Matariki

file = open('ten_year_predictions.txt', 'w')

for year in range(1990, 2991, 10):
    file.write(Matariki.getMatariki(year) + "\n")

file.close()

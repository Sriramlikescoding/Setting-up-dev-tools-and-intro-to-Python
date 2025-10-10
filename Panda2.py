import pandas as p
mylist = {
    "Names":["Sriram", "Chris", "Aaron", "Sally", "Ghost", "Gary", "Sam", "Buddy"],
    "Age":[13, 23, 4, 15, 53, 11, 70, 14, ],
    "Score":[20, 30, 100, 10, 50, 70, 111, 80],
    "Gender":["Boy", "Boy", "Boy", "Girl", "Girl", "Boy", "Boy", "Boy"],
    "City":["Fremont", "Los Angeles", "New York", "Raleigh", "Denver", "Lincoln", "Washington D.C.", "Toronto"]
}
myTable = p.DataFrame(mylist, index = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7", "Day8"])



#Scores = {
 #   "Score": [150, 200, 70, 20, 500, 440, 360, 600],
  #  "Subjects": ["English", "Science","Geography", "History", ]
#}
for key in Scores:
    print(key)
myTable2 = p.DataFrame(Scores)
print(myTable2)
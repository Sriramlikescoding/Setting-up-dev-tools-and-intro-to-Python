studentData = { 'id1':
               {
                   'name' : ['Sara'],
                   'class': ['V'],
                   'subject_integration': ['english, math, science']
               },
               'id2':
               {
                   'name' : ['David'],
                   'class': ['V'],
                   'subject_integration': ['english, math, science']
               },
               'id3':
               {
                   'name' : ['Sara'],
                   'class': ['V'],
                   'subject_integration': ['english, math, science']
               },
               'id4':
               {
                   'name' : ['Surya'],
                   'class': ['V'],
                   'subject_integration': ['english, math, science']
               }
             
}

result = {}

for key,value in studentData.items():
    if value not in result.values():
        result[key] = value

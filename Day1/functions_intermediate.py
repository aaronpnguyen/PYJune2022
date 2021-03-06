x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change 10 to 15
x[1][0] = 15
print(x)

# Change last_name of first student to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# Change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# Iterate through the list and print each key and its associated value
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        print("first_name - {}, last_name - {}" .format(students[i]['first_name'], students[i]['last_name']))
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Iterate through a dictionary with list values, print the name of the key along with the size of its list, then print its associated values within each key's list.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i.upper())
        for j in range(len(some_dict[i])):
            print(some_dict[i][j])
        print("")
printInfo(dojo)
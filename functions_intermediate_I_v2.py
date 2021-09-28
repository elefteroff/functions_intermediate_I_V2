# 1. Update Values in Dictionaries and Lists

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

# 1.1 Change the value 10 in x to 15. 
x[1][0] = 15
print(x)

# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# 1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 1.4 Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.


edm_bands = [
    {'first_name': 'Armin', 'last_name':  'van Buuren'},
    {'first_name': 'Ferry', 'last_name':  'Corsten'},
    {'first_name': 'Dash', 'last_name':  'Berlin'},
    {'first_name': 'David', 'last_name':  'Guetta'}
]
def iterateDictionary(some_list):
    for pair in range(0, len(some_list)):
        print(some_list[pair])

iterateDictionary(edm_bands)

# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

edm_bands = [
    {'first_name': 'Armin', 'last_name':  'van Buuren'},
    {'first_name': 'Ferry', 'last_name':  'Corsten'},
    {'first_name': 'Dash', 'last_name':  'Berlin'},
    {'first_name': 'David', 'last_name':  'Guetta'}
]
def iterateDictionary(key, some_list):
    for band in some_list:
        print(band[key])

iterateDictionary('first_name', edm_bands)
iterateDictionary('last_name', edm_bands)

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

concerts = {
    'Locations': ['Seattle', 'San Franciso', 'Los Angeles', 'Denver', 'Chicago', 'New York', 'Miami', 'Dallas'],
    'Bands': ['Armin van Buuren', 'Ferry Corsten', 'Dash Berlin', 'David Guetta', 'Ronski Speed'],
    'Dates': ['October 1, 2021', 'October 4, 2021', 'October 7, 2021', 'October 14, 2021', 'October 17, 2021', 'October 20, 2021', 'October 23, 2021', 'October 27, 2021']
}
def printInfo(some_dict):
    for key in some_dict:
        print(key,len(some_dict[key]))
        for values in some_dict[key]:
            print(values)

printInfo(concerts)
empty_list = []
print(len(empty_list))

happi = ['coding','medic','music','sleep','draw','friends']
print('Number of things that ruined me:', len(happi))
# i cant list out things tho..
# or maybe i have no idea to do that shit

# so, negative number means the end of the list (wut)
print(happi[0])
print(happi[len(happi) // 2]) 
# you supposed to find the middle item by this method?
print(happi[-1])

mixed_data_types = ['Nathan','15','147','why','your mom']

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
# 'modify' means changing the existing one
# god why am i so stupid
it_companies[0] = 'Meta'
print(it_companies) # AFTER CHANGING

# To add a new item to the end of a list
# you use the .append() method.

it_companies.append('Twitter')
print(it_companies)

# To insert an item anywhere else (like right in the middle)
# you use the .insert() method.
# huhueye so the insert is number then the item

it_companies.insert(3, ' Netflix')
print(it_companies)

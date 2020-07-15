"""Generate sales report showing total melons each salesperson sold."""

# (name, total amount of the order, total number of melons sold)

salespeople = []
melons_sold = []

f = open('sales-report.txt')
# open text file and store object in f
for line in f:
    # loop through
    line = line.rstrip()
    # strip each line of whitespaces 
    entries = line.split('|')
    # split each line by '|' into a list of strings

    salesperson = entries[0]
    # saleperson's name is first string
    melons = int(entries[2])
    # last item in list is melon count, convert string into integer

    if salesperson in salespeople:
        # check if salesperson is in the list of sales people
        position = salespeople.index(salesperson)
        # store the index of salesperson that is stored in sales people list
        melons_sold[position] += melons
        # add saleperson's number of melons sold at specific index in list 

    else:
        # if salesperson not already in list of sales people
        salespeople.append(salesperson)
        # add new salesperson to the end of the sales people list
        melons_sold.append(melons)
        # add salesperson's melon count to the end of melons sold list


for i in range(len(salespeople)):
    # for index number in range starting at 0 to length of salespeople list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    # print salesperson's name at index and their melon count in corresponding index


'''
#find the line and word
def search_string_in_file(filename,string_to_search):
    lineno = 0
    list_of_result = []
    with open("C:\\users\\Admin\\Desktop\\Covid_Sample.txt", "r") as file:
        for line in file:
            lineno += 1
            if string_to_search in line:
                list_of_result.append((lineno,line.rstrip()))
        return list_of_result

matched = search_string_in_file('sample.txt', 'Covid_Cases')
print("total matched lines : ",len(matched))
for x in matched:
    print('line number = ',x[0],'; line = ',x[1])

'''


'''
#print(covidline)
#format output
with open("C:\\users\\Admin\\Desktop\\Covid_Sample.txt", "r") as file:
    covidline = (list(file)[8])
print(covidline)
covidline = covidline.split(" ")

covidline[0] = covidline[7]
covidline[9] = covidline[13]
covidline[15] = covidline[22]
covidline[25] = covidline[28]
print("Covid_Cases = ",covidline[0])
print("Covid_Death = ",covidline[9])
print("Covid_Processed = ",covidline[15])
print("Covid_Cured = ",covidline[25])
'''


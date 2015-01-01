import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # [matrix, i, j, value]
    matrix = record[0]

    if matrix == 'a':        
        i = record[1]
        j = record[2]      
        value = (j, record[3])
        for k in range(5):
            key = (i, k)            
            mr.emit_intermediate(key, value)
    else:
        j = record[1]
        k = record[2]  
        value = (j, record[3])
        for i in range(5):
            key = (i, k)
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    i,k = key
    temp = {}
    for j, val in list_of_values:
        l = temp.get(j,[])
        l.append(val)
        temp[j] = l

    prod = {}
    for key in temp.keys():
        if len(temp[key]) == 2:
            prod[key] = temp[key][0] * temp[key][1]

    s = 0
    for key in prod.keys():
        s += prod[key];

    mr.emit((i, k, s))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # [matrix, i, j, value]
    i = record[1]
    j = record[2]
    value = (j, record[3])
    for k in range(1,5):
        key = (record[1], i, k)
        mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of document ids
    matrix,i,k = key
    prod = {}
    for j, val in list_of_values:
        prod[j] = prod.get(j,1) * val
    
    sum = 0
    for key in prod.keys():
        sum += prod[key];
    
    mr.emit((i, k, sum))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

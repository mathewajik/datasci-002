import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate((key, value), 1)
    mr.emit_intermediate((value, key), -1)

def reducer(key, list_of_values):
    # key: person
    # value: friends count
    sum = 0
    for val in list_of_values:
        sum += val
        
    if sum != 0:
        mr.emit(key)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

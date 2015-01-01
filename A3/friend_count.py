import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: friends count
    mr.emit((key, len(list_of_values)))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

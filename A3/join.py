import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: order id
    # value: order or line_item record

    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order id
    # value: list of order or line_item records

    for record in list_of_values:
        if record[0] == 'order':
            order_record = record
            break

    for record in list_of_values:
        if record[0] == 'line_item':
            mr.emit(order_record + record)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

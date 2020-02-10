#  Hint:  You may not need all of these.  Remove the unused functions.
import json
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    # Populate hashtable with source and destination cities
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Assign itinerary starting point
    key = "NONE" 
    index = 0
    # Populate route array with itinerary
    while index < length:
        destintation = hash_table_retrieve(hashtable, key)
        route[index] = destintation
        key = destintation
        index += 1

    return route




# Helper function to handle hash table resizing
def handle_hash_table_capacity(hash_table):
    if len(hash_table.storage) == hash_table.capacity:
        hash_table_resize(hash_table)


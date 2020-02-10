#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    index = 0
    for weight in weights:
        # Manage hashtable capacity
        handle_hash_table_capacity(ht)
        # Populate hashtable with weights
        if hash_table_retrieve(ht, weight) is None:
            hash_table_insert(ht, weight, index)
        else:
            # Handle duplicate values
            if weight * 2 == limit:
                return (index, hash_table_retrieve(ht, weight))
        # Increment index
        index += 1

        # Search the hashtable for the addend
        addend = limit - weight
        if hash_table_retrieve(ht, addend):
            return (hash_table_retrieve(ht, weight), hash_table_retrieve(ht, addend))

    # Default return
    return None


# Helper function to handle hash table resizing
def handle_hash_table_capacity(hash_table):
    if len(hash_table.storage) == hash_table.capacity:
        hash_table_resize(hash_table)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# print(answer_2)

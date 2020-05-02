#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """
        Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: 
        O(1) single line of code to calculate # of Key-Value entries divided by 
        # of buckets. Returns calculation.
        """
        # Calculate load factor WORKS
        return self.size / len(self.buckets)
        # return Average of value-entries per bucket

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: 
        O(n) Need to loop through every item in each bucket n times.
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: 
        O(n) Need to loop through every item in each bucket n times.
        """
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time:
        O(n) Need to loop through every item in each of the buckets n times.
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items()) # .extend adds EVERYTHING to the list
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time:
        Best case O(1) If we keep track of a count variable, self.size(), return that variable instantly
        Worst case O(n) (Commented out) If we dont keep track of a count variable whenever a new entry 
                        is added/deleted, must search/loop through all buckets to count all entries that 
                        exist.
        """
        # Count number of key-value entries in each of the buckets
        # item_count = 0
        # for bucket in self.buckets:
        #     item_count += bucket.length()
        # return item_count
        # # Equivalent to this list comprehension:
        # return sum(bucket.length() for bucket in self.buckets)
        
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) If the target data is located in the first entry in a bucket (Head node).
        Worst case running time: O(l) or O(n/b)* because all buckets should ideally have same amount of 
                                entries, and worst case would be if the target data is located in the last 
                                entry in a bucket (Tail node).
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) If target data is located in the first entry in a bucket (Head node)
        Worst case running time: O(l) or O(n/b)* because all buckets should ideally have same amount of 
                                entries, and worst case would be if the target data is located in the 
                                last entry in a bucket (Tail node).
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) If target data is located in the first entry in a bucket (Head Node).
        Worst case running time: O(1) Instant access to the end of the linked list (Tail node).
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        # add size
        self.size += 1
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
        # ...
        # If so, automatically resize to reduce the load factor
            self._resize()
        # ...

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) If target data is located in the first entry in a bucket (Head Node).
        Worst case running time: O(l) or O(n/b)* If we have to loop through an entire bucket.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            # subtract size
            self.size -= 1

            if self.load_factor() <= 0.20:
                self._resize(0)
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(2n) having to create a new array and linked list while having
                                            to transfer the contents over both takes n time ==> 2n.
        Best and worst case space usage: O(2n) having to create a new array and linked list while having 
                                            to transfer the contents over both takes n space ==> 2n.
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        current_items = self.items()
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for i in range(int(new_size))]
        # self.buckets = []
        # for i in range(int(new_size)):
        #     buckets.append(LinkedList())
        self.size = 0
        # Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in current_items:
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()

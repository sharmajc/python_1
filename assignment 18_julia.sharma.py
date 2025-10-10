#Challenge: Ensure that the function works correctly with tuples of different lengths.
#=============================================
#Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.
...

def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2

tuplea = (1,2,3)
tupleb = (4,5,6)

results = concat_tuples(tuplea, tupleb)
print("Concatenated Tuple: ", results)

def exchange_first_last(seq):
	mid = seq[1:-1]
	new = seq[-1:] + mid + seq[:1]
	return new

assert exchange_first_last('this is a string ') == 'ghis is strint'
assert exchange_first_last([1,2,3,4,5,6,7,8,9]) == [9,2,3,4,5,6,7,8,1]
assert exchange_first_last((1,2,3,4,5,6,7,8,9)) == (9,2,3,4,5,6,7,8,1)





def every_second(seq):
	return seq[::2]


assert every_second('this is a string') == 'ti sasrn'
assert every_second([1,2,3,4,5,6,7,8,9]) == [1,3,5,7,9]


def remove_fourth(seq):
	seq = seq[4:-4]
	return seq [::2]








def third(seq):
	third2 = int(len(seq)/3)
	first_third = seq[:third2]
	remainder = seq[third2:]
	third3 = int(len(remainder)/2)
	second_third = remainder[:third3]
	third_third = remainder[third3:]
	return second_third + third_third + first_third


assert third('123456789') == '456789123'
assert third ([1,2,3,4,5,6,7,8,9,]) == [4,5,6,7,8,9,1,2,3]
assert third ((1,2,3,4,5,6,7,8,9,)) == (4,5,6,7,8,9,1,2,3)
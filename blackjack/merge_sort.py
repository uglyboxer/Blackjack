def merge_sort(lst):
	if len(lst) == 1:
		return lst
	else:
		mid = len(lst)//2
		left = merge_sort(lst[:mid])
		right = merge_sort(lst[mid:])
		temp_lst = []
		while left and right:
			if left[0] > right[0]:
				temp_lst.append(right.pop(0))
			else:
				temp_lst.append(left.pop(0))
		if left:
			temp_lst += left
		else:
			temp_lst += right
	return temp_lst





if __name__ == '__main__':
	a = [5, 3, 1234, 2, 5, 1, 6, 9, 23]
	assert merge_sort(a) == [1, 2, 3, 5, 5, 6, 9, 23, 1234]
	print("victory")
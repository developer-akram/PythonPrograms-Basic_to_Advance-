# 1. Check if a key is present in every segment of size k in an list
# Input :
# arr[] = { 21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25, 22, 26}
# x = 23
# k = 5
# Output :Yes
# There are three segments and last segment is not full {21, 23, 56, 65, 34}, {54, 76, 32, 23, 45} and {21, 23, 25}.
# 23 is present all window.
# Input :arr[] = { 5, 8, 7, 12, 14, 3, 9}
# x = 8
# k = 2
# Output : No

a = [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25, 22, 26]

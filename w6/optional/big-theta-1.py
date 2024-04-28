# Function to find whether a key exists in an
# array or not, using linear search
def linearSearch(a, n, key):

	# Traverse the given array, a[]
	for i in range(0, n):

		# Check if a[i] is equal to key
		if (a[i] == key):
			return True
	
	return False

# Driver Code

# Given Input
arr = 2, 3, 4, 10, 40
x = 30
n = len(arr)

# Function Call
if (linearSearch(arr, n, x)):
	print("Element is present in array")
else:
	print("Element is not present in array")
	

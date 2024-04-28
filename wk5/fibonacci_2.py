import sys
import time

def fibonacci(end):
    end = int(end)
    current = 0
    next = 1

    while next <= end:
        print(next, end=' ')
        next_value = current + next
        current = next
        next = next_value
    return

# prompt the user for an integer number up to which the fibonacci sequence shall run
end = sys.argv[1]  # input("Enter a number: ")

# calls the fibonacci function

start_time = time.time()

print("\n\nRunning the fibonacci sequence.\n\tPractice comparing recursion versions and non-recursive versions.")

fibonacci(end)

print("\n\n--- %s seconds ---" % (time.time() - start_time))
# this is a test folder.
import show_the_welcome as w
import chris.chrismodule as c

print("This is the main script.")
print("We're calling the library using the import statement and the alias of w.")
print("And so access the function (show_the_welcome) with the alias: w.show_the_welcome()")

print(w.show_the_welcome(1))
print(w.show_the_welcome(2))
print(w.show_the_welcome(3))

print("TEST OF CHRIS")
print(c.bye())
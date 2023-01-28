print ("== Fill-In-The-Missing-Lyrics ==")
print ()
print ("Figure out the missing lyrics quickly")
print ()

counter = 1
while True:
  blank = input("Never going to ______ you up.  ")
  if blank == "give":
    print (blank)
    print ("Correct!!!")
    break
  else:
    print (blank)
    print("Nope, try again.")
    counter += 1
print ("Well done! It only took you", counter, "attempt(s).")
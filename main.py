from lesson01.main import main as main1

# If you're here from my site, look in the folders on the 
# right to find the code for the lesson!
# Click 'run' up above to see the lesson run.

lessons = {
  "1": lambda: main1()
}

while True:
  user = input("Which lesson do you want to run? ").strip()
  if user in lessons:
    lessons[user]()
  else:
    print("Invalid input.")
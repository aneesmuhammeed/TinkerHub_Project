import bcrypt
import csv
import os 

# User Works 

def existingUser():
  e_username = input("Enter username : ")
  e_password = input("Enter password : ").encode('utf-8')
 
  userFound = False
  incorrectPassword = False

  with open('database.txt','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        
        if e_username == line['username']:
          userFound = True
          if  bcrypt.checkpw(e_password,line['password'].encode('utf-8')):
             print("\nLogin successful :)\n")
             loginUser(e_username)
             incorrectPassword =True
             break
    if not userFound:
       print("\nInvalid Username\n")
    elif not incorrectPassword:
       print("\nIncorrect Password !")
       print("Try Again\n")


def registerUser():
  r_username = input("Enter username : ")
  r_password = input("Enter password : ").encode('utf-8')
  r_hashed = bcrypt.hashpw(r_password, bcrypt.gensalt())

  with open('database.txt', 'a') as f:
     f.write(f"{r_username},{r_hashed.decode('utf-8')}\n")
   
  print("\nREGISTRATION PROCESS COMPLETED !")
  print("Now you can login with this username and password\n")


# Blog Works

blogFile = 'blogs.csv'

# create
def createPost(username):
    title = input("Enter blog title: ")
    content = input("Enter blog content: ")

    with open(blogFile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, title, content])
    print("Blog post created successfully.")



# modify
def modifyPost(username):
    title = input("Enter the title of the blog post to modify: ")

    rows = []
    found = False

    with open(blogFile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == title:
                found = True
                new_content = input(f"Enter new content for '{title}': ")
                rows.append([username, title, new_content])
            else:
                rows.append(row)

    if not found:
        print(f"No blog post with title '{title}' found.")
    else:
        with open(blogFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Blog post modified successfully.")


# modify
def deletePost(username):
    title = input("Enter the title of the blog post to delete: ")

    rows = []
    found = False

    with open(blogFile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == title:
                found = True
            else:
                rows.append(row)

    if not found:
        print(f"No blog post with title '{title}' found.")
    else:
        with open(blogFile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Blog post deleted successfully.")





def loginUser(username):
  print(f"\nWelcome {username}!")
  print("1. Create a new post") 
  print("2. Delete a post")  
  print("3. Modify a post") 
  choice = input("Enter your choice: ")


  match choice:
    case "1":
        createPost(username)
    case "2":
        deletePost(username)
    case "3":
        modifyPost(username)
    case _:
        print("Invalid Option")



while True:
  print("Choose an option:") 
  print("1) Existing User, Login ")
  print("2) New User, Register Now ")
  print("3) Exit ")
  
  choice = input("Enter the Choice : ")
  match choice:
      case "1":
          existingUser()
      case "2":
          registerUser()
      case "3":
          break
      case _:
          print("Invalid Option")


  
  
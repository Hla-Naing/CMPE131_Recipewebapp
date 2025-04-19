
## Functional Requirements

1. A visitor can create an account by providing a username, email, and password.

2. Registered users can log in using their email and password.

3. Logged-in users can log out of their account securely.

4. <write Edit Recipe requirement here (Cedric)>
5. <write Delete Recipe requirement here (Cedric)>
6. <write Create Recipe requirement here (Cedric)>
7. <write Rate Recipe requirement here (Cedric)>
8. <write Save Recipe requirement here (Kris)>
9. <write Comment on Recipe requirement here (Kris)>
10.<write View User Profile requirement here (Kris)>
11.<write Edit User Profile requirement here (Kris)>
   
12.The system would allow users to view a chosen reciepe’s information

13.The system allows users to view all the recipes saved in the database.

14.The system allows the users to Filter recipes depending on the category.

15.The system allows the user to search for recipe by titles


## Use Cases 

1. User Registration(Daniel)
- **Pre-condition:** The visitor is on the login page.
- **Trigger:** The visitor decides to create an account and clicks the "Register" button.
- **Primary Sequence:**
        1. The visitor navigates to the registration page.
        2. The visitor enters a desired username in the username field.
        3. The visitor enters their email address in the email field.
        4. The visitor enters a password in the password field.
        5. The visitor clicks the "Sign Up" button.
        6. The system validates the entered information (e.g., checks for unique username and email).
        7. If the information is valid, the system creates a new account for the visitor.
- **Primary Postconditions:** 
        1. The visitor's account is successfully created.
        2. The visitor can log in using their new account credentials.
- **Alternate Sequence:** 
        1. If the entered username is already taken: 
              i. The system displays an error message indicating the username is not available.
              ii. The visitor is prompted to enter a different username. 
- **Alternate Sequence <optional>:** 
        1. If the entered email address is already taken: 
              i. The visitor is prompted to enter another email address.
              ii. Alternative, if the email was already registered, the visitor is prompted to retrieve the password by clicking on “Forgot Password” link on the login page.

2. User Login(Daniel)
- **Pre-condition:** The user has a registered account with a valid email and password.
- **Trigger:** The user navigates to the login page and attempts to log in.
- **Primary Sequence:**
        1. The user navigates to the login page.
        2. The user enters their registered email address in the email field.
        3. The user enters their password in the password field.
        4. The user clicks the "Login" button.
        5. The system verifies the email address and password against the database.
        6. If the email and password are correct, the system logs the user in.
- **Primary Postconditions:** 
        1. The user is successfully logged into the app.
- **Alternate Sequence:** 
        1. If the user enters an incorrect email or password: 
              i. The system displays an error message indicating the login credentials are invalid.
              ii. The user is prompted to re-enter their email and password.
              iii. The user attempts to log in again.  

3. User Logout(Daniel)
- **Pre-condition:** The user is logged into the app.
- **Trigger:** The user clicks the logout button.
- **Primary Sequence:**
        1. The user clicks the logout button.
        2. The system displays a confirmation dialog asking if the user is sure they want to log out.
        3. The user reviews the confirmation dialog.
        4. The user clicks the "Confirm" button to proceed with the logout.
        5. The system logs the user out.
- **Primary Postconditions:** 
        1. The user is redirected to the home page.
- **Alternate Sequence:** 
        1. If the user clicks the "Cancel" button in the confirmation dialog:
              i. The system cancels the logout process. 
              ii. The user remains logged into the app. 
              iii. The user continues using the app without interruption. 

4. Edit Recipe(Cedric)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

5. Delete Recipe(Cedric)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

6. Create Recipe(Cedric)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

7. Rate Recipe(Cedric)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

8. Save Recipes(Kris)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

9. Comment on Recipes(Kris)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

10. View User Profile(Kris)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

11. Edit User Profile(Kris)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
        1. Ut enim ad minim veniam, quis nostrum e
        2. Et sequi incidunt
        3. Quis aute iure reprehenderit
        4. ...
        5. ...
        6. ...
        7. ...
        8. ...
        9. ...
        10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise and their outcomes>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
        1. Ut enim ad minim veniam, quis nostrum e
        2. Ut enim ad minim veniam, quis nostrum e
        3. ...

12. View Recipe(Hla)
- **Pre-condition:**  The recipe should be saved in the database
- **Trigger:** The user clicks on the specific recipe to view it. 
- **Primary Sequence:**
-    1. The user moves the cursor to a specific recipe.
     2. The user clicks on the recipe (preferably a view button).
     3. The system gets the recipe information from the database
     4. The system displays the recipe’s detailed information
     5. The user views the recipe information. 
- **Primary Postconditions:** The recipe is displayed to the user 
- **Alternate Sequence:**
-    1. The system cannot get recipe information from the database
   
        i. The system displays an error message.
        
        ii.The system lets users go back to try again or go back to the main menu page where many f other saved recipes are displayed. 

13. View All Recipes(Hla)
- **Pre-condition:**  The recipes should be saved in the database of the user. 
- **Trigger:** The user clicks on the view all recipes button.
- **Primary Sequence:**
-    1. The user clicks on the view all recipe button on the menn (preferably on homepage)
     2. The system gets the recipe data from the database
     3. The system displays all saved recipes of the user with the image, title and brief information about each of the recipe
           i. if the user wants to view much detailed information about a certain recipe, the process will transfer to “view recipe” use case.
     4. The user scrolls the page to view all recipes.
     5. The system reupdates everytime user goes to another page or scroll down to see more information.
- **Primary Postconditions:** The user is able to view all the saved recipes
- **Alternate Sequence:**
-    1. If the user hasn’t saved any recipe yet
        
        i. the system displays “there is no recipe saved” notice.
        
        ii. The system gives users an option  to create a new recipe

14. Filter Recipes(Hla)
- **Pre-condition:** Recipes associated to the chosen category already exist in the database. 
- **Trigger:** The user selects a category and clicks the filter button on the menu. 
- **Primary Sequence:**
-    1. The user moves the cursor to the filter recipe button.
     2. The system shows different categories to choose from such as desserts, soups, salad, main meals
     3. The user choose a specific category
     4. The user clicks filter button on the page
     5. The user clicks filter button on the page
- **Primary Postconditions:**
-    1. The system displays filtered recipes.
     2. The users can click on each recipe to view the detailed information
     3. The users can also go back to the filter section to choose more category or restart the filter.
- **Alternate Sequence:**
-    1. If the system cannot match the category to the recipes saved in the database
        
        i. The system displays an error message
        
        ii.The system allows the user to filter again or to create a new recipe for the chosen category
        
15. Search Recipe(Hla)
- **Pre-condition:**  The recipe exists in the system database. 
- **Trigger:** The user enters the recipe title on the search bar.
- **Primary Sequence:**
-    1. The user goes to the search bar on the menu
     2. The user enters the title of the recipe on the search bar
     3. The user clicks the search button to begin searching for a specific recipe
     4. The system process the user request and look for that recipe in the database
     5. The system gets the recipe from the database
     6. The system displays that certain recipe
- **Primary Postconditions:**
-    1. The system displays the recipe that the user wants to search
     2. The system allows the user to view that recipe (referenced to view recipe use case)
- **Alternate Sequence:**
-    1. If the system cannot find the recipe
        
        i. the system displays an error message saying that recipe doesn’t exist or not being saved
        
        ii.the system allows the user to try again or shows the closet match 


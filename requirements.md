
Functional Requirements
A visitor can create an account by providing a username, email, and password.

Registered users can log in using their email and password.

Logged-in users can log out of their account securely.

The system will let the user edit the text that details the recipe, and then save it to the database.

The system shall remove the recipe from the database it is stored in.

The system will allow the user to add a new recipe to the database.

The system should show five stars on the UI and the User clicks on the respective star to rate the recipe.

Users can mark a recipe as saved/favorite for future access.

Users can post comments onto existing recipes.

User can access their own or another user’s profile page.

The system will allow users to change the content displayed on their profile.

The system would allow users to view a chosen reciepe’s information

The system allows users to view all the recipes saved in the database.

The system allows the users to Filter recipes depending on the category.

The system allows the user to search for recipe by titles

EXTRA Functional Requirements
The system shall ensure that the user's password meets predefined strength criteria.

The system shall provide the first three characters of the user's password as a hint when the user selects the "Forgot Password" option.

The user can edit display name, email, and password. ("EditAccount")

Use Cases
User Registration(Daniel)
Pre-condition: The visitor is on the login page.
Trigger: The visitor decides to create an account and clicks the "Register" button.
Primary Sequence:
  1. The visitor navigates to the registration page.
  2. The visitor enters a desired username in the username field.
  3. The visitor enters their email address in the email field.
  4. The visitor enters a password in the password field.
  5. The visitor clicks the "Sign Up" button.
  6. The system validates the entered information (e.g., checks for unique username and email).
  7. If the information is valid, the system creates a new account for the visitor.
Primary Postconditions:
  1. The visitor's account is successfully created.
  2. The visitor can log in using their new account credentials.
Alternate Sequence 1:
  1. If the entered username is already taken: 
        i. The system displays an error message indicating the username is not available.
        ii. The visitor is prompted to enter a different username. 
Alternate Sequence 2:
  1. If the entered email address is already taken: 
        i. The visitor is prompted to enter another email address.
        ii. Alternative, if the email was already registered, the visitor is prompted to retrieve the password by clicking on “Forgot Password” link on the login page.
User Login(Daniel)
Pre-condition: The user has a registered account with a valid email and password.
Trigger: The user navigates to the login page and attempts to log in.
Primary Sequence:
  1. The user navigates to the login page.
  2. The user enters their registered email address in the email field.
  3. The user enters their password in the password field.
  4. The user clicks the "Login" button.
  5. The system verifies the email address and password against the database.
  6. If the email and password are correct, the system logs the user in.
Primary Postconditions:
  1. The user is successfully logged into the app.
Alternate Sequence:
  1. If the user enters an incorrect email or password: 
        i. The system displays an error message indicating the login credentials are invalid.
        ii. The user is prompted to re-enter their email and password.
        iii. The user attempts to log in again.  
User Logout(Daniel)
Pre-condition: The user is logged into the app.
Trigger: The user clicks the logout button.
Primary Sequence:
  1. The user clicks the logout button.
  2. The system displays a confirmation dialog asking if the user is sure they want to log out.
  3. The user reviews the confirmation dialog.
  4. The user clicks the "Confirm" button to proceed with the logout.
  5. The system logs the user out.
Primary Postconditions:
  1. The user is redirected to the home page.
Alternate Sequence:
  1. If the user clicks the "Cancel" button in the confirmation dialog:
        i. The system cancels the logout process. 
        ii. The user remains logged into the app. 
        iii. The user continues using the app without interruption. 
Edit Recipe(Cedric)
Pre-condition: The user is currently logged in and viewing a recipe. Information about the recipe is displayed on the screen. There are options to edit or delete.

Trigger: The user clicks on edit recipe button

Primary Sequence: 1. The system displays editable fields for the recipe details (title, ingredients, steps, etc.). 2. The user makes changes to the recipe text. 3. The user clicks the "Save" button. 4. The system validates the input and updates the recipe in the database. 5. The system displays a confirmation message and shows the updated recipe.

Primary Postconditions: The information in the recipe is changed and saved to the database (if saved). The updated recipe is displayed to the user.

Alternate Sequence: The user cancels any changes made 1. The user clicks the "Cancel" button. 2. The system prompts for confirmation to discard changes. 3. Upon confirmation, the system returns to the recipe view without saving.

Delete Recipe(Cedric)
Pre-condition: The user is currently logged in and viewing a recipe that they created. Information about the recipe is displayed on the screen. There are options to edit or delete.

Trigger: The user clicks on the delete recipe button.

Primary Sequence: 1. The system displays a confirmation dialog asking if the user wants to delete the recipe. 2. The user confirms deletion. 3. The system deletes the recipe from the database. 4. The system navigates the user back to the recipe list and shows a confirmation message.

Primary Postconditions: The recipe is removed from the database. The delete recipe can no longer be viewed.

Alternate Sequence: The user cancels the deletion of the recipe 1. The user clicks "Cancel" in the confirmation dialog. 2. The system closes the dialog and the recipe remains unchanged.

Create Recipe(Cedric)
Pre-condition: The user currently logged in and viewing a list of recipes.

Trigger: The user clicks on the create recipe button.

Primary Sequence: 1. The system displays a blank recipe form with fields for title, ingredients, and instructions. 2. The user fills in the recipe details. 3. The user clicks the "Save" button. 4. The system validates the input and adds the new recipe to the database. 5. The system displays a confirmation message and shows the new recipe.

Primary Postconditions: A recipe is added to the database. It can be viewed by anyone.

Alternate Sequence: If the user clicks the "Cancel" button in the confirmation dialog 1. The system prompts for confirmation to discard the recipe. 2. Upon confirmation, the system discards changes and returns to the recipe list.

Rate Recipe(Cedric)
Pre-condition: The user is logged in and is currently viewing a recipe.

Trigger: The user clicks on a star rating.

Primary Sequence: 1. The user clicks on a star to rate the recipe (1 to 5 stars). 2. The system captures the rating and stores it in the database. 3. The system updates the average rating of the recipe based on all user ratings. 4. The new average rating is displayed on the recipe page.

Primary Postconditions: The star rating on the recipe changes depending on how many users rate the recipe. New rating is saved.

Alternate Sequence: User tries to rate without being logged in 1. The user clicks a star while not logged in. 2. The system prompts the user to log in or register. 3. After successful login, the system redirects back to the recipe so the user can rate it.

Save Recipes(Kris)
Pre-condition: The user is logged in and able to view the recipe (not blocked or hidden from recipe creator).
Trigger: User selects “Save” button or symbol on recipe page.
Primary Sequence: 1. User selects “Save” button. 2. System adds route to recipe page into saved folder. 3. System displays a confirmation dialog showing their recipe has been saved and a button to the saved folder. 4. User exits dialog box and returns to page.
Primary Postconditions: User returns to the recipe page. Saved file can now be accessed from saved recipes folder.
Alternate Sequence: 1. User selects “Save” button. 2. System displays error message that the page cannot be saved. 3. System returns user to recipe page.
Comment on Recipes(Kris)
Pre-condition: The user is logged in and able to view the recipe (not blocked or hidden from recipe creator).
Trigger: The user selects “Comment” button on recipe page.
Primary Sequence: 1. User selects “Comment” button. 2. System opens a text box under recipe. 3. User enters dialog into text box. 4. User selects “post comment” button. 5. System adds comment content and contributing username to bottom of page.
Primary Postconditions: Comment remains on page unless deleted or hidden by commenter or recipe creator.
Alternate Sequence: 1. User selects “Comment” button. 2. System opens a text box under recipe. 3. User enters dialog into text box. 4. User selects “post comment” button. 5. System displays error message that comment could not be posted. 6. User is given the option to select “post comment” again.
View User Profile(Kris)
Pre-condition: The owner of the profile has a preexisting account.
Trigger: User selects “profile” from system menu.
Primary Sequence: 1. User selects “profile” from system menu or username. 2. System matches username to profile number. 3. System loads route for profile dedicated to user. 4. System displays text description, images and/or recipes on page.
Primary Postconditions: User can access links to recipe pages directly from profile.
Alternate Sequence: 1. User selects “profile” from system menu or username. 2. The user that matches the linked profile does not exist. 3. System displays an error message that the user does not exist or cannot be accessed. 4. User is redirected to the previous page.
Edit User Profile - Display Info(Kris)
Pre-condition: The owner of the profile has a preexisting account and is logged into the system.
Trigger: From profile, user selects “Edit Profile” button.
Primary Sequence: 1. User selects “Edit Profile” button. 2. System displays text box with all current text inside. 3. User can add or remove text from within the text box. 4. User selects “save changes” button under text box. 5. System rewrites new text content in place of old content.
Primary Postconditions: Text content remains on page unless changed again.
Alternate Sequence: 1. User selects “Edit Profile” button. 2. System displays text box with all current text inside. 3. User can add or remove text from within the text box. 4. User selects “save changes” button under text box. 5. System rewrites new text content in place of old content.
View Recipe(Hla)
Pre-condition: The recipe should be saved in the database
Trigger: The user clicks on the specific recipe to view it.
Primary Sequence:
The user moves the cursor to a specific recipe.
The user clicks on the recipe (preferably a view button).
The system gets the recipe information from the database
The system displays the recipe’s detailed information
The user views the recipe information.
Primary Postconditions: The recipe is displayed to the user
Alternate Sequence:
The system cannot get recipe information from the database

i. The system displays an error message.

ii.The system lets users go back to try again or go back to the main menu page where many f other saved recipes are displayed.

View All Recipes(Hla)
Pre-condition: The recipes should be saved in the database of the user.
Trigger: The user clicks on the view all recipes button.
Primary Sequence:
The user clicks on the view all recipe button on the menn (preferably on homepage)
The system gets the recipe data from the database
The system displays all saved recipes of the user with the image, title and brief information about each of the recipe i. if the user wants to view much detailed information about a certain recipe, the process will transfer to “view recipe” use case.
The user scrolls the page to view all recipes.
The system reupdates everytime user goes to another page or scroll down to see more information.
Primary Postconditions: The user is able to view all the saved recipes
Alternate Sequence:
If the user hasn’t saved any recipe yet

i. the system displays “there is no recipe saved” notice.

ii. The system gives users an option to create a new recipe

Filter Recipes(Hla)
Pre-condition: Recipes associated to the chosen category already exist in the database.
Trigger: The user selects a category and clicks the filter button on the menu.
Primary Sequence:
The user moves the cursor to the filter recipe button.
The system shows different categories to choose from such as desserts, soups, salad, main meals
The user choose a specific category
The user clicks filter button on the page
The user clicks filter button on the page
Primary Postconditions:
The system displays filtered recipes.
The users can click on each recipe to view the detailed information
The users can also go back to the filter section to choose more category or restart the filter.
Alternate Sequence:
If the system cannot match the category to the recipes saved in the database

i. The system displays an error message

ii.The system allows the user to filter again or to create a new recipe for the chosen category

Search Recipe(Hla)
Pre-condition: The recipe exists in the system database.
Trigger: The user enters the recipe title on the search bar.
Primary Sequence:
The user goes to the search bar on the menu
The user enters the title of the recipe on the search bar
The user clicks the search button to begin searching for a specific recipe
The system process the user request and look for that recipe in the database
The system gets the recipe from the database
The system displays that certain recipe
Primary Postconditions:
The system displays the recipe that the user wants to search
The system allows the user to view that recipe (referenced to view recipe use case)
Alternate Sequence:
If the system cannot find the recipe

i. the system displays an error message saying that recipe doesn’t exist or not being saved

ii.the system allows the user to try again or shows the closet match

Password Strength Check(Daniel)
Pre-condition: The user is on the registration page and has entered a password.
Trigger: The user submits the registration form.
Primary Sequence:
  1. The user enters their desired password in the registration form.
  2. The user submits the registration form.
  3. The system checks the password against predefined strength criteria (e.g., minimum length, inclusion of numbers).
  4. If the password meets the criteria, the system proceeds with the registration process.
Primary Postconditions:
  1. The user is successfully registered in the system.
Alternate Sequence:
  1. If the user fails to meet the password criteria after multiple attempts:  
        i. The system provides tips for creating a strong password.  
        ii. The user enters a new password based on the suggestions. 
        iii. The system rechecks the new password.
Forgot Password(Daniel)
Pre-condition: The user is on the login page and has forgotten their password.
Trigger: The user selects the "Forgot Password" option.
Primary Sequence:
  1. The user clicks the "Forgot Password" link on the login page.
  2. The system prompts the user to enter their registered email address.
  3. The user enters their email address and submits the form.
  4. The system verifies the email address against the database.
  5. If the email address is valid, the system retrieves the user's password.
  6. The system displays the first three characters of the password as a hint to the user.
  7. The user uses the hint to recall their password.
  8. The user enters the recalled password on the login page.
  9. The system verifies the entered password.
  10. If the password is correct, the user is successfully logged in.
Primary Postconditions:
  1. The user is logged into the system.
  2. The user can now access the app's features and functionalities.
Alternate Sequence:
  1. If the user enters an invalid email address:     
        i. The system displays an error message indicating the email address is not registered.  
        ii. The user is prompted to enter a valid registered email address.
Edit User Profile - Personal Account Info (Kris)
Pre-condition: The owner of the profile has a preexisting account>- Trigger: From profile, user selects “Edit Profile” button.
Trigger: From profile, user selects “Edit Account” button.
Primary Sequence: 1. User selects “Edit Account” button. 2. System displays text boxes for current display name, email and password. 3. User can rewrite the entry for one of the boxes. 4. System prompts user to confirm change with another text box. 5. User reenters the same string. 6. System rewrites new content in place of old content.
Primary Postconditions: Text content remains on page unless changed again.
Alternate Sequence: 1. User selects “Edit Account” button. 2. System displays text boxes for current display name, email and password. 3. User can rewrite the entry for one of the boxes. 4. System displays error message if value is invalid or same as before. 5. User can rewrite entry again or select a different box.



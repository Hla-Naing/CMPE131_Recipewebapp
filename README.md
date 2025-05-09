# CMPE131_Recipewebapp Team 4
- Cedric (@cvmaceda/cedrim)
- Hla/Maria (@Hla-Naing)
- Daniel (@dannyvasq)
- Kris (@krisros1)

**Welcome to our recipe sharing app!** This program allows logged in users to view and submit recipes. 
To run this app, the following libraries must be installed under a virtual environment and using “pip3 install library”:
- Flask (managing the package)
- Flask-SQLAlchemy (managing user, recipe, and profile databases) 
- Flask-WTF (managing login and submission forms)
- Pytz (retrieval of local time)
- Pillow (management of uploaded images).

Viewers must enter their email to see the list of recipes on the home page, but for further interaction with individual recipes, need to register an account through the ‘/register’ page.
Once a user ID is saved in our database, they can log in (‘/login’) to grant access to posting recipes (‘/make_recipe’), viewing individual recipes of others (‘/recipe/<int:id>’), and commenting on/rating/saving them.
Each user can edit their own recipes (‘/edit_recipe/<int:id>’) and specific user profile displaying a biography (‘/profile’), or change their registration data behind the scenes (to be added).
When finished, the user can then end their session by going to ‘/logout’. 


**Ethical Considerations (1):**
When building this food recipe web app, I have to think about doing things the right way. 
First, I need to keep user information safe. 
I’ll use Flask-Login so people have to log in before they can add or change recipes, and I’ll validate every form with Flask-WTF so no one can sneak in bad data or break the database. 
Encrypting passwords and using HTTPS means personal details stay private.
I also want the app to be easy for everyone. 
That means making sure people who use screen readers or only a keyboard can still browse recipes. 
I should avoid making unsupported health claims—if I list nutrition facts, I’ll get them from a trusted source so users don’t get wrong information.

On a bigger scale, this app could help promote local ingredients. 
If I add a feature to highlight seasonal produce, I’m helping small farmers and cutting down on shipping, which is better for the environment. 
Keeping my code clean and open-source lets other developers learn from it, but I must follow the licenses for any libraries I use.
Overall, I agree to follow a professional code of ethics—being honest about what my app can do, fixing bugs quickly, and making sure everyone can use it safely.


**Engineering Solutions (2):**
Any application or product that we make serves as a baseline for all future developments of our project. 
As engineers and professionals, we have to keep in mind that what we develop goes beyond our personal scope as producers, but additionally to others that both use the code and integrate it into their own variations. 
Because of this, clarity of content is the most important thing to account for. 
In both the README file and in comments throughout, our team needs to provide direct explanation of our work process and what different pages/imports contain. 
This also requires being honest about what we provide with the “client”, or range of app users. 
Many such cases, hidden data in sites can be used to access or even steal information from those who visit. 
There should not be other functions aside from what is listed in our requirements document, ensuring a 1:1 communication with the user base.

Additionally, wherever possible we need to incorporate engineering solutions into our work - finding methods that are safe and reliable while also efficient. 
Every problem has countless solutions, but limited by time, physical and financial resources. 
Therefore tailoring to particular needs has the most success. 
On a global or international scale, this can look like accounting for accessibility towards a range of languages or cultures. 
Societal accessibility is similar where variants of the same product can have different features, making them affordable and approachable to all crowds. 
Engineering solutions should also minimize strain on the environment, keeping energy needs and pollutants to a minimum. 
Especially with constant advancements in technology, we have the opportunity to select which tools best fit both the function and the restraints. 

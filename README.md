# Uncle Testsu Restaurant

![Responsive Devices](docs/responsive-devices.png)

[Visit live website](https://ut-restaurant-d71a0939b77c.herokuapp.com/)  
(Ctrl + click to open in new tab)

## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Uncle Tetsu is a fictional business, create for educational purpose. It allows users create an account, book a table, read and write reviews and view the food menu.
<hr>

### User Goals

- To book a table
- To be able to view and cancel bookings
- To view menus with a descritive ingredients

### Site Owner Goals

- To provide a solution to allow users to book a table online
- Provide a modern application with an easy navigation
- Fully responsive and accessible
- Get User's review for improvement
<hr>

## User Experience

### Target Audience
- **Food Enthusiasts:** Individuals who are passionate about trying new foods and exploring different cuisines.
- **Social Diners:** Friends and families looking for a convenient way to make restaurant reservations and enjoy a meal together.
- **Review Contributors:** Users who enjoy sharing their dining experiences with others. They like to write reviews about the restaurants they visit and read reviews from fellow diners to make informed decisions.
- **Local Explorers:** Residents of the area where Uncle Tetsu is located who are interested in discovering local eateries and supporting businesses in their community.

### User Requirements and Expectations

* Fully responsive Design
    * Users expect the website to be accessible and usable across a variety of devices, including desktops, tablets, and smartphones.
    <hr>

* Accessibility
    * The website should adhere to accessibility standards, making it easy to navigate and use for individuals with disabilities.
    <hr>

* A welcoming and Inviting Design
    * Users want a visually appealing and welcoming design that reflects the restaurant's ambiance and culinary identity.
    <hr>

* Social Media Integration
    * Users expect easy access to the restaurant's social media profiles to stay updated with the latest news, offers, and events.
    <hr>

* Contact information
    * Users need clear and accessible contact information, including the restaurant's address, phone number, and email.
    <hr>

* Comprehensive Food Menu
    * Each menu item should include descriptions, images, and pricing information for informed decision-making.
    <hr>

* Easy Reservation Process
    * Users anticipate a straightforward process to book a table. This includes selecting the date, time, number of guests, and any special requests.
    <hr>

* User Reviews and Ratings
    * Users want to read reviews and ratings from other diners to gauge the quality of the dining experience.
    

##### Back to [top](#table-of-contents)<hr>

## User Stories

### Users

1. Being a User, I am able to have easy navigation in order to move to each feature of the site.
2. Being a User, I am able to see dish information(description, image and price) in order to make an informed decision.
3. Being a User, I am able to easily find the address and location in order to view in a map the directions.
4. Being a User, I am able to find contact information and opening hours in order to when the business is open and how to contact via phone or email.
5. Being a User, I am able to find social media icons in order to follow the business social medias.
6. Being a User, I am able to write reviews, and rating in order to share my experience with others.
7. Being a User, I am able to edit or delete an existing review in order to update and provide my experience.
8. Being a User, I am able to sign in/sign up in order to make reservation and write reviews.
9. Being a User, I am able to make a reservation in order to to take a table for the chosen date, time and number of guests.
10. Being a User, I am able to see reservation details in order to to accept or delete my reservation.

### Admin / Authorised User

11. Being a Admin, I am able to manually make reservation in order to make reservation when a costumer calls or contact via social medias.
12. Being a Admin, I am able to authenticate and log into the admin dashboard in order to manage users informations, reservations history and reviews.
13. Being a Admin, I am able to manage menu items in order to add, delete menu items details.
14. Being a Admin, I am able to have access to the user reviews in order to manage and moderate all reviews.
15. Being a Admin, I am able to filter registered users by name, staff status, superuser status in order to easily find a specific user or staff member contact.
16. Being a Adimin, I am able to filter reservation in order to easily see a reservation by date, author or if reservation is cancelled.
17. Being a Admin, I am able to view a list of all reservations made by users in order to I can manage all reservations.

### Site Owner

18. Being a Site Owner, I can provide fully responsive site for my costumers in order to have a good experience.
19. Being a Site Owner, I can provide an intuitive and descritive menu with description, pictures and price for my costumers in order to have a informed decision-making.

### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>

![Epics](docs/epics.png)
![Epic 1](docs/epic1.png)
![Epic 2](docs/epic2.png)
![Epic 3](docs/epic3.png)
![Epic 4](docs/epic4.png)
</details>

<details><summary>User Stories</summary>

![User stories](docs/user_story.png)
</details>

<details><summary>Kanban</summary>

![Kanban](docs/kanban_board.png)
![Kanban finish](docs/kanban_board1.png)

</details>

##### Back to [top](#table-of-contents)<hr>

## Design

### Colours

In the process of craftingthe visual identity, I selected meticulously selected a palette of colors that encapsulate the essence of the brand. Each color holds a purpose and contributes to the overall aesthetic we wish to convey.

The colors I wanted to stay close to  [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>

![Palette Colors](docs/palette_colors.png)
</details>

### Fonts

 None font were selected using the default system font "Helvetica".

 ### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

* The sites consists of the folloowing pages:
    * **Home page** with a main banner that contains caroussel of pictures, a button that takes user to make a reservation and also the review section.
    * **Menu page** that also contains the main banner, a navbar that displays the differents categories of the dishes, images of the dishes in or menu and a description with price for each option when the cursor is over the image.
    * **Reservation page** that has a form where user can fill to book a table with personal information and choose date, time, number of guests and also leave a message.
    * **Contact Us page** contains the business contact informations such as phone number and email, address and a map link.
    * **Edit Review** for those logged user that want to edit their reviews, the page contains a message field and rating.
    * **Login / Logout** allows users to login to make bookings, view, edit, and delete bookings
    * **Register** allows the user to regiser so they can use the booking system and write reviews.
    * **Error page** to display if a 403, 404 500 error is raised.

#### Database
Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

<details><summary>Show diagram</summary>
![DataBase](docs/database.png)>
</details>

##### User Model
* The User Model contains the following:
    * id
    * username
    * name
    * email
    * phone
    * groups
    * user_permissions
    * is_staff
    * superUser
    
##### User Reviews Model
* The User Reviews Model contains the following:
    * id
    * author
    * comment
    * rating
    * created
    * approved
    * status
    * slug

##### Reservation Model
* The Reservation Model contains the following:
    * id
    * user
    * name
    * email
    * phone
    * numGuests
    * date
    * time
    * message
    * is_cancelled

##### Menu Model
* The Menu Model contains the following:
    * id
    * category
    * name
    * price
    * image
    * slug

##### User Login Forms
* The User Login Forms contains the following:
    * id
    * username
    * password

##### User Registration Form
* The User Registration Form contains the following:
    * id
    * username
    * password

### Wireframes
The wireframes were created using Miro
<details><summary>Home</summary>
<img src="docs/wireframe/wireframe_home.png">
</details>
<details><summary>Menu</summary>
<img src="docs/wireframe/wireframe_menu.png">
</details>
<details><summary>Reservation</summary>
<img src="docs/wireframe/wireframe_reservation.png">
</details>
<details><summary>Contact Us</summary>
<img src="docs/wireframe/wireframe_contactus.png">
</details>
<details><summary>Login</summary>
<img src="docs/wireframe/wireframe_login.png">
</details>
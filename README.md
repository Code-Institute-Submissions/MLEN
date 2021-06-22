![]("")
# [MLEN](https://tanya-mlen.herokuapp.com/) 

This is the 4th Milestone project undertaken as part of Code Institute and has been build in the Full Stack Framework using Django.

MLEN is an online store for anyone who have interest in magnetic eyelashes.
MLEN eyelashes can be reuseable, wear and remove in seconds! Natural soft magnetic eyelashes with various designs for you to complete your beauty. It is currently the most advanced magnetic eyelash.


## Design

***Color Theme***

The main colours used are Black and Canva to keep the site clean and balance with white background and brighter tones.

***Font***

'Open Sans Condensed' for all the fonts in the site.

***Wireframe***
[Desktop (Tablet is the same as desktop ver) and Mobile Wireframe.](./static/readme/mlen.pdf).

## Features and Functionality

***Elements Across the website***

Nav bar is fixed at the top for easier navigation and footer is fixed at the bottom
for social media. On smaller device, the nav bar will be compressed into a side slide
menu which can be open by clicking on the down arrow button.

***Home Page Elements***

A hero Image on top in-tune with the theme of the project with a button which takes the user to the products page and a writeup about the brand.

***Tutorial Elements***

A static page to explain how to apply and clean the eyelashes.

***Contact Us Page Elements***

This page displayes a form for both the user and non-user to send an email. By submitting the form, the email will be sends to the DB.

***Login Page Elements***

Registered user can input their username and password info to log in to the site. 
If the user is valid, a toast message is displayed and the user is redirected to the Homepage. If either one of the info is incorrect, an error message will appear to inform the user. The user can register or to reset their password.

***Registration Page Elements***

Non-user will have to input a valid username, email address and password on the form.
Submit button sends into the DB and show the user a verification page to confirm the sign up.

***Profile Page Elements***

User can check or update their address information and check their previous order here.

***Products(Eyelashes) Page Elements***

Display products using Bootstrap cards along with the associated image of the products.
By clicking the picture or product's name the user will be redirect to the product detail page which the user can get into a more detailed understanding of the product. 
On Clicking the "sort by .." dropdown button, the user will be able to display all the products for that category. At the bottom right of the screen is a Back to Top button.
If the user is a SuperUser, Edit/Delete button will be displayed to allow easy Workshop Management.

***Products Detail Page Elements***

In the detail page, to the left, the associated image of the product is displayed.
To the right the title, description, lash information and price along with quantity selector is displayed. Plus/Minus icons are placed either side of Number Input Field to increase and decrease quantity. Two buttons - add to cart and browse more lashes - are below the quantity input field. Browse more lashes returns the user to the All product page and add to cart adds items to the cart which displays a Toast success which will show the items of the bag and the total amount purchased.

***Shopping cart page elements***

This page display the user added items in cart and selects to do checkout.
The user will be able to adjust the quantity of the items in the basket using the plus/minus icons and clicking the update link or remove the whole line by clicking the remove link. The grand total along with the delivery charge is computed and displayed for a particular order. "Secure Checkout" button at the bottom allow the user to proceed with paying and takes them to the checkout page and "Browse more lashes" button return them to the all products page.

***Checkout Page Elements***

After the user finalizes their purchase, they can move ahead to do a checkout and make the payment of the purchase. This page is divided into two parts, on the right shows the order summary, on the left shows a form requesting for information about the user. The user must fill in the form on the left before being able to continue the checkout process. There are required fields in the form and this information will be saved to the DB and can be check in the user profile page if the user has logged in or creates an account prior to checkout. The credit card field is linked to STRIPE and the form inherits the stripe validations associated with credit cards. Buttons at the bottom allow the user to go back to the shopping cart and make adjustments to the quantity purchased or move ahead to pay and complete the order. Once the user submits the payment information a pink loading screen will appears to show that the payment is being processed.

***Checkout Success / Order Confirmation Page***

The order confirmation page lists out the order number and the detail of the purchase along with the subtotal and grandtotal. User can check for their order in the profile page. The user can browse back to the products page by clicking the "Browse more lashes" button below the form.

## Technologies Used

***Languages***

1. [HTML](https://en.wikipedia.org/wiki/HTML)
2. [CSS](https://en.wikipedia.org/wiki/CSS)
3. [Javascript](https://en.wikipedia.org/wiki/JavaScript)
4. [Python](https://www.python.org/)

***Frameworks, Libraries & Programs Used***

1. [Google Fonts](https://fonts.google.com/)  (Used to obtain my fonts.)
2. [Font Awesome Version 5.15.3](https://fontawesome.com/) (Used on all pages to add   icon for aesthetic and UX purposes.)
3. [GitPod](https://www.gitpod.io/) (Used terminal to git commit and git push to GitHub. Also used for version control.)
4. [GitHub](https://github.com/) (Store projects after being pushed from Gitpod.)
5. [Balsamiq](https://balsamiq.com/) (Used to design the layout of the website.)
6. [jQuery](https://jquery.com/)(A Javascript library that simplifies manipulation of of the HTML DOM.)
7. [Django](https://www.djangoproject.com/) (Web framework for creating modular websites.)
8. [Bootstrap](https://getbootstrap.com/docs/3.4/css/) (CSS used for responsive grid framework and general styling.)
9. [Stripe](https://stripe.com/en-dk) (Used for payment with credit card.)
10. [Heroku](https://www.heroku.com/) (Have been used to host the website.)
11. [AWS](https://aws.amazon.com/?nc2=h_lg) (For static and media files.)

***Database***

1. [SQLlite (In development)](https://www.sqlite.org/index.html)
2. [Postgres (At deployment)](https://www.postgresql.org/)


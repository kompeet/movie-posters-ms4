# Movie Posters

## <i> Fourth Milestone Project - Fullstack Frameworks with Django - Code institute </i>

---

Movie Posters is a fully responsive, custom-built full-stack website, designed and built with the users wants and needs first, whilst maintaining a high design standard and ease of use.

This is a full stack website developed for Code Institute milestone project 4. If you want to use the full functionality of this website, Stripe test payments are enabled with the card number 4242 4242 4242 4242 and any CVC, future expiry date, and postcode.

---

![AmIresponsive](https://github.com/kompeet/movie-posters-ms4/blob/master/static/images/AmIResponsive.JPG "Responsive")

---

## Contents

1. [**UX**](#Ux)
    - [**Project Goals**](#Project-Goals)
    - [**Site Owner Goals**](#Site-Owner-Goals)
    - [**User Stories**](#User-Stories)
    - [**Requirements**](#Requirements)
    - [**Expectations**](#Expectations)
2. [**Design Choices**](#Design-Choices)
    - [**Colours**](#Colours)
    - [**Fonts**](#Fonts)
    - [**Icons**](#Icons)
    - [**Styles**](#Styles)
    - [**Images**](#Images)
    - [**Wireframes**](#Wireframes)
3. [**Data Models**](#Data-Models)
    - [**Profiles App**](#Profiles-App)
    - [**Products App**](#Products-App)
    - [**Checkout App**](#Checkout-App)
    - [**Sendback App**](#Sendback-App)
    - [**Blog App**](#Blog-App)
4. [**Features**](#Features)
    - [**Implemented Features**](#Implemented-Features)
    - [**Planned Features**](#Planned-Features)
5. [**Technologies Used**](#Technologies-Used)
6. [**Testing & Bugs**](#Testing-&-Bugs)
7. [**Development & Deployment**](#Development-&-Deployment)
8. [**Credits**](#Credits)
9. [**Acknowledgements**](#Acknowledgements)
10. [**Disclaimer**](#Disclaimer)

---

## UX 

### Project Goals

To offer users original porsters for purchasing. Users will be able to browse products, view detailed information, create an account, order products, read and comment blogs, and receive support.

### Site Owner Goals

- Sell products to customers.
- Add, remove and update products.
- Update the website with blog articles.

### User Stories

#### Users (new)

New visitors to the website should be provided with the answers they need right away.

 - I want to view a list of products so that I can make a selection to purchase.
 - I want to be able to ask questions so that I can know more about these unique posters before making a decision.
 - I want to be able to easily register for an account so that I can see and save my personal details for quicker ordering in the future.
 - I want to be able to read the blogs and make comments.

#### Users (registered)

Registered users of the website will be provided with additional features which non-registered users will not benefit from.

 - As a registered user, I want to be able to easily log in and out of my account so that I can access my personal information and order history.
 - As a registered user, I want to be able to easily update my profile information so that I can update my personal details.
 - As a registered user, I want to be able to view my past orders so that I can keep track of my orders with the site.
 - As a registered user, I want to be able to have my delivery details prefilled so that I can save time in entering my details.

#### Users (website shoppper)

All shoppers of the website, new, returning or registered:

 - As a shopper, I want to be able to view all posters available so that I can decide which product I might like to buy.
 - As a shopper, I want to be able to choose the number of products I want to order so that I can decide how many of that product I would like to order.
 - As a shopper, I want to be able to add a product to my cart so that I can order my chosen product.
 - As a shopper, I want to be able to delete products from my cart so that I can update the products I would like to purchase.
 - As a shopper, I want to be able to update the number of products in my cart so that I can order more or less of the chosen product than I had originally intended.
 - As a shopper, I want to be able to use a secure payment method so that I can be confident my details are secure.
 - As a shopper, I want to be able to save my personal details from my order so that I can create an account and shop faster next time.
 - As a shopper, I want to be able to check out in a simple and easy way so that I can be confident my order has gone through with all my correct details.
 - As a shopper, I want to be able to receive an order confirmation so that I can be sure my order has gone through.
 - As a shopper, I want to be able to learn more about movie and poster blog articles, reviews and news, so that I can decide whether I want to buy their products.
 - As a shopper, I want to be able to contact the website owner so that I can ask them a question.
 - As a shopper, I want to ba able to return my product.

#### Users (site owner)

 - As the site owner, I want to be able to easily list my products to sell so that I can sell new products to my users.
 - As the site owner, I want to be able to update my product listings so that I can make sure the information is correct or amendments can be made.
 - As the site owner, I want to be able to easily delete product listings so that I can remove items I no longer wish to sell.
 - As the site owner, I want to be able to make it as easy as possible for users to purchase my products so that I can give them a great service, sell my products.
 - As the site owner, I want to be able to send auto emails to users so that I can inform them of successful registration and order confirmation.
 - As the site owner, I want to be able to inform visitors of my articles, blogs so that I can keep users returning and buying new products.
 - As the site owner, I want to be able to offer visitors free delivery based on a minimum amount ordered so that I can increase revenue and product sales via an incentive to the customer.
 - As a shopper, I want to be able to sort the products available on the site by category so that I can view just the products in that category.

### Requirements

- View products in a list and with detailed product information.
- Purchase the products using a secure checkout system.
- Create an account, view/update personal information and view previous orders.
- Contact the business for further information and sendback product.
- Providing blogs

### Expectations

- Website is visually appealing and easy to navigate on all devices.
- User can leave a comments of the blogs.
- Personal information will be stored securely.

## Design Choices

### Colours

Two of the most important colors are black and white. To make the site consistent and easy to read, I used these two colors for almost everything and also chose three more lighter colours for the bottoms and icons hover.
These colours balace well and make the site easy to read and use.

I used the basic Bootstrap colours for message alerts.

![ColourPalette](https://github.com/kompeet/movie-posters-ms4/blob/master/static/images/colour.JPG "Colour")

### Fonts

The font I selected for this page is [Anton](https://fonts.google.com/specimen/Anton?query=anton) from GoogleFonts, because it fits perfectly with the elegant, bohemian and represents the movie, film world.

### Icons

I have used a range of font awesome icons across the website to aid in displaying content and navigation options instead of using only text.

### Styles

I have chosen to use vw/vh on padding and margins in a lot of cases as I believe this allows for an even more responsive experience than using solely rem.

### Images

The images are taken from the internet and credited in the credits section of the readme.

### Wireframes

I made wireframes for each page of the site from three different types of devices. I used the Balsamiq. The wireframes can be viewed [here](https://github.com/kompeet/movie-posters-ms4/tree/master/wireframes).

The implementation ended up slightly different.

## Data Models

In order to map the relationships between the models in this project I created an entity relationship diagram. This can be viewed [here](https://github.com/kompeet/movie-posters-ms4/blob/master/static/images/datamodels.JPG).

### Profiles App

#### User Profile Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User|user|OneToOneField|django.contrib.auth.get_user_model(), on_delete.models.CASCADE
Phone Number|default_phone_number|CharField|max_length=20, null=True, blank=True
Street 1|default_street_address_1|CharField|max_length=80, null=True, blank=True
Street 2|default_street_address_2|CharField|max_length=80, null=True, blank=True
City|default_town_or_city|CharField|max_length=40, null=True, blank=True
County|default_county|CharField|max_length=80, null=True, blank=True
Postcode|default_postcode|CharField|max_length=20, null=True, blank=True
Country|default_country|CountryField|blank_label='Country', null=True, blank=True

### Products App

#### Category Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=254
Friendly Name|friendly_name|CharField|max_length=254, null=True, blank=True

#### Product Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Category|category|ForeignKey|'Category', null=True, blank=True, on_delete=models.SET_NULL
SKU|sku|CharField|max_length=254, null=True, blank=True
Name|name|CharField|max_length=254
Description|description|TextField|...
Year|year|IntegerField|default=2020
Size|has_sizes|BooleanField|default=True, null=True, blank=True
Price|price|DecimalField|max_digits=7, decimal_places=2
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Image|image|ImageField|null=True, blank=True

### Checkout App

#### Order Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order Number|order_number|CharField|max_length=32, null=False, editable=False
Related User|user_profile|ForeignKey|UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders'
Full Name|full_name|CharField|max_length=100, null=False, blank=False
Email|email|EmailField|max_length=254, null=False, blank=False
Phone Number|phone_number|CharField|max_length=20, null=True, blank=True
Country|country|CountryField|blank_label='Country', null=True, blank=True
Postcode|postcode|CharField|max_length=20, null=True, blank=True
City|city|CharField|max_length=50, null=True, blank=True
Street 1|street_address_1|CharField|max_length=100, null=True, blank=True
Street 2|street_address_2|CharField|max_length=100, null=True, blank=True
County|county|CharField|max_length=20, null=True, blank=True
Date|date|DateTimeField|auto_now_add=True
Order Total|order_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0
Grand Total|grand_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0
Original|original_bag|TextField|null=False, blank=False, default=''
Stripe|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''

#### Order Line Item Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Oder|order|ForeignKey|Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product|product|ForeignKey|Product, null=False, blank=False, on_delete=models.CASCADE
Product Size|product_size|CharField|max_length=8, null=True, blank=True
Quantity|quantity|IntegerField|null=False, blank=False, default=0
Line Item T|lineitem_total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False

### Sendback App

#### Send Back Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=80, blank=False
Email|email|EmailField|blank=False
Reason|reason|TextField|blank=False
Order Number|order_number|CharField|max_length=80, blank=False

### Blog App

#### Post Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Title|title|CharField|max_length=200, unique=True
Slug|slug|SlugField|max_length=200, unique=True
Author|author|ForeignKey|User, on_delete=models.CASCADE,related_name='blog_posts'
Updated|updated_on|DateTimeField|auto_now=True
Content|content|TextField|...
Created|created_on|DateTimeField|auto_now_add=True
Status|status|IntegerField|choices=STATUS, default=0
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Image|image|ImageField|null=True, blank=True

#### Comment Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Post|post|ForeignKey|Post,on_delete=models.CASCADE,related_name='comments'
Name|name|CharField|max_length=80
Email|email|EmailField|blank=False
Body|body|TextField|blank=False
Created|created_on|DateTimeField|auto_now_add=True
Active|active|BooleanField|default=False

## Features

### Implemented Features

#### Get all Products, Sort, Filter and Search

* The user can load all of the products or browse products sorting by categories. Filtering is available by Price (low to high or high to low), by Name (A-Z or Z-A) and by Category (A-Z or Z-A).
* The product page is split using Django Pagination to provide a transparent list of products.

#### Edit, Update and delete Products

* The superuser can easily edit or delete a product using the adequate button on the Product Detail page.
* They can add products on Product Management Page.In order to make it easy to upload a collection of products, when the superuser adds one product, they get redirected to the Add Product Page instead of All Product Page.

#### Get in touch

* The user can send an email using the Contact Form.

#### Sign up, Sign in, login

* The shopper can easily sign up, sign in, and reach their profile with the shipping and order information.
* I built the authentication system using Django Allauth.

#### Product returning

* If the shopper is not happy with the product, they can return it. The link to this return form is a part of the footer, so the user doesn't have to sign in, or sign up (as they can place order without authentication too). The idea is that the dissatisfied shopper provides some information about the problem, they give the order number, and contact details, and the owner gets this data in Django Admin, so she can answer, and start the process.

#### Blogging

* The user can easily enjoy the new articles, stories of movies and posters.
* The user can leave comments. Superuser(s) have to confirm to display.

#### Back to the top

* Some pages of the website can become a little long on mobile. To help users with this I have added a ‘back to top’ button on these longer pages.

### Planned Features

* Leave reviews beneath products: Reading reviews are a great way to help users decide to purchase a product. This feature would be great to include in the future but was not seen as imperative for launch.
* Subscription purchase model: a subscription service would provide them with regular deliveries and a reduced cost. This would also benefit the website owner so that they have pre-orders already in place each month.

## Technologies Used

- [GitHub](https://github.com/)

- [GitPod](https://gitpod.io/)

- [Heroku](https://dashboard.heroku.com/)

- [HTML](https://en.wikipedia.org/wiki/HTML5)

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Django](https://www.djangoproject.com/)

- [Jquery](https://jquery.com/)

- [Python](https://www.python.org/download/releases/3.0/)

- [Gmail](https://mail.google.com/)

- [MarkDownLit](https://dlaa.me/markdownlint/)

- [Balsamiq](https://balsamiq.com/)

- [HTMLValidator](https://validator.w3.org/)

- [CSSValidator](https://jigsaw.w3.org/css-validator/)

- [JavaScriptValidator](https://esprima.org/demo/validate.html)

- [CSSBeautifier](https://www.freeformatter.com/css-beautifier.html)

- [JSHint](https://jshint.com/)

- [PythonCodeChecker](https://extendsclass.com/python-tester.html)

- [Favicon](https://www.favicon-generator.org/)

- [GoogleFonts](https://fonts.google.com/)

- [AmIResponsive](http://ami.responsivedesign.is/)

- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

- [PyMongo](https://pymongo.readthedocs.io/en/stable/)

- [PEP8](http://pep8online.com/)

- [Bootstrap](https://getbootstrap.com/)

- [FontAwesome](https://fontawesome.com/)

- [Stripe](http://stripe.com/)

- [SqLite](https://www.sqlite.org/index.html)

- [AWS Amazon](https://aws.amazon.com/)

## Testing & Bugs

#### Homepage

* On the Homepage, you can see a navbar that is consistent on each page. It contains a menu and a User Menu with authentication and shopping bag. The navbar is collapsable on mobile devices and a search bar.

* Under the navbar, there is a responsive image.

* On the Homepage, you can find a small introduction to tell the user a little bit about the scope of the page and a shop button which leads to the all products page.

* The footer is another returning component on the page. The footer contains five FontAwesome icons leading to my GitHub page, Instagram, Facebook, Twitter and the return product red icon. All links are working, links load in a new tab and leads to the sendback form.

#### Product Page

* When the user wants to see Products, they can choose between browsing by categories or loading all products.

* If the user chooses to load product categories, they can see a badge telling which category is loaded.

* I used count() to let the user know how many products they can find on that page.

* I built Django Pagination to split the page and make it easier to navigate on.

* Besides sorting by categories, there is a SortBy function loading the products sorting them by the price or the name.

* On Detailed Product Page, there is a Bootstrap carousel to show the product images.

* Product details are visible for anyone, Edit and Delete buttons are available only for SuperUsers. Edit and delete functions works without a problem.

* The quantity is adjusable between 1-5 for limited reasons.

* When the user adds a product to their bag, a Bootstrap toast pops up to display a success message. These bootstrap messages appear after every operation. I used toast to display success, error, info, and warning.

#### Genre & Decades

* 10 each categoies lead to specific products.

#### Contact Page

* Users can submit a contact form to ask questions. Should be available to unregistered users.

#### Bag

* The default status of the bag is empty. When a user adds an item to it, they can see the product details, the bag total, the delivery cost, and the grand total, and change quantity. If they hit on Secure Checkout, a form appears where the user has to provide some information regarding the delivery and the payment. All fields are required to be filled out. After the checkout, they get redirected to a success page which contains an order summary and a button back to all product pages. The user gets a confirmation email. The whole checkout process was tested from different devices. Everything worked well. After the checkout, the admin can see the order in Django Admin and Stripe dashboard as well.

#### Authentication

* Authentication is provided by using Django Allauth. The user can sign up by setting a username, a password, and a valid email address. After clicking on Sign Up, they receive an email with a link to activate the profile. By clicking on the link, the user created a profile, so they can log in. Signed in users have a profile with delivery information (if they choosed to save it), and an order history with details about the product, and an order status. The order status has two mode: Processed and Awaiting, telling the user if their order is already seen by the shop owner. The status of the order can be changed in Django Admin.

* SuperUser can click on Product Managment page where they can add new products. This page is only available for the shop owner. The whole sign up, sign in, sign out process was tested, everything worked well.

#### Blog

* Blog button leads to a full page of blog articles.


#### Manual Testing

I manually tested the entire website across 3 desktop browsers (Chrome, Safari and Firefox) on tablet on 2 browsers (Chrome and Safari).

Tested devices:

- [x] laptop(width 1440px)

- [x] Moto G4

- [x] Galaxy S5

- [x] Pixel2, Pixel 2XL

- [x] Iphone 5/SE, Iphone 6/7/8

- [x] Iphone 6/7/8 Plus, IphoneX

- [x] Ipad and Ipad Pro

- [x] Xiaomi Redmi 4A

- [x] Xiaomi Redmi Note5

- [x] Xperia z5 Compact


#### User tests

Few of my friends and my family have tested the website by using it and did not report any bugs. The feedback was positive.


#### W3C HTML Validator

- [HTMLValidation](https://validator.w3.org/):

  - Unfortunately the HTML validator doesn't understand the Django templating syntax, so I got a bunch of errors because of this. Also you can find some errors caused by using base.html as a shell. No other error found.

- [CSSValidation](https://jigsaw.w3.org/css-validator/):

  - Bootstrap errors did occur, which I was advised to ignore.

  - All of my code otherwise passes without any errors.

- [JavaScript Validation](https://esprima.org/demo/validate.html):

  - No error found, code is syntactically valid.

- [PythonCodeChecker](https://extendsclass.com/python-tester.html):

  - There are no errors through the PEP8 check. However, there are a couple of highlighted rows of code where I have decided not to make the suggested corrections:

  ‘Avoid using null=True on string based fields.’ Pages with error
  ’Line too long’ Pages with error. 
   Imported but unused in some tests.pys


### Bugs

- There was a bug in my code where if the user typed in the quantity they could add as many as they like which is shown in the screenshot below. I fixed this issue by changing the quantity to a range between 1 and 999. This means that the user can physically type in anything from 1 to 999 when they update it in the cart. But if they type in 1000 or above then the item will be removed from the cart. This will also shop the site from crashing as they can only have a certain amount in the quantity.

- There is still an isteresting bug in the shopping bag only on large resolution quantity goes below 0 and above 5. On smaller(mobile) resolution this issue does not exist anymore, quantity pushed between 1 and 5. JS was checked. It looks like if it came from css.

## Development & Deployment



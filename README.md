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

- Sell products to customers
- Add, remove and update products
- Update the website with blog articles

### User Stories

#### Users (new)

New visitors to the website should be provided with the answers they need right away.

 - I want to view a list of products so that I can make a selection to purchase
 - I want to be able to ask questions so that I can know more about these unique posters before making a decision
 - I want to be able to easily register for an account so that I can see and save my personal details for quicker ordering in the future
 - I want to be able to read the blogs and make comments

#### Users (registered)

Registered users of the website will be provided with additional features which non-registered users will not benefit from.

 - As a registered user, I want to be able to easily log in and out of my account so that I can access my personal information and order history
 - As a registered user, I want to be able to easily update my profile information so that I can update my personal details
 - As a registered user, I want to be able to view my past orders so that I can keep track of my orders with the site
 - As a registered user, I want to be able to have my delivery details prefilled so that I can save time in entering my details

#### Users (website shoppper)

All shoppers of the website, new, returning or registered:

 - As a shopper, I want to be able to view all posters available so that I can decide which product I might like to buy
 - As a shopper, I want to be able to choose the number of products I want to order so that I can decide how many of that product I would like to order
 - As a shopper, I want to be able to add a product to my cart so that I can order my chosen product
 - As a shopper, I want to be able to delete products from my cart so that I can update the products I would like to purchase
 - As a shopper, I want to be able to update the number of products in my cart so that I can order more or less of the chosen product than I had originally intended
 - As a shopper, I want to be able to use a secure payment method so that I can be confident my details are secure
 - As a shopper, I want to be able to save my personal details from my order so that I can create an account and shop faster next time
 - As a shopper, I want to be able to check out in a simple and easy way so that I can be confident my order has gone through with all my correct details
 - As a shopper, I want to be able to receive an order confirmation so that I can be sure my order has gone through.
 - As a shopper, I want to be able to learn more about movie and poster blog articles, reviews and news, so that I can decide whether I want to buy their products
 - As a shopper, I want to be able to contact the website owner so that I can ask them a question
 - As a shopper, I want to ba able to return my product

#### Users (site owner)

 - As the site owner, I want to be able to easily list my products to sell so that I can sell new products to my users
 - As the site owner, I want to be able to update my product listings so that I can make sure the information is correct or amendments can be made
 - As the site owner, I want to be able to easily delete product listings so that I can remove items I no longer wish to sell
 - As the site owner, I want to be able to make it as easy as possible for users to purchase my products so that I can give them a great service, sell my products
 - As the site owner, I want to be able to send auto emails to users so that I can inform them of successful registration and order confirmation
 - As the site owner, I want to be able to inform visitors of my articles, blogs so that I can keep users returning and buying new products
 - As the site owner, I want to be able to offer visitors free delivery based on a minimum amount ordered so that I can increase revenue and product sales via an incentive to the customer
 - As a shopper, I want to be able to sort the products available on the site by category so that I can view just the products in that category

### Requirements

- View products in a list and with detailed product information
- Purchase the products using a secure checkout system
- Create an account, view/update personal information and view previous orders
- Contact the business for further information and sendback product
- Providing blogs

### Expectations

- Website is visually appealing and easy to navigate on all devices
- User can leave a comments of the blogs
- Personal information will be stored securely

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

* Profiles App

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

* Products App

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
Description|description|TextField|
Year|year|IntegerField|default=2020
Size|has_sizes|BooleanField|default=True, null=True, blank=True
Price|price|DecimalField|max_digits=7, decimal_places=2
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Image|image|ImageField|null=True, blank=True

* Checkout App

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

* Sendback App

#### Send Back Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name|name|CharField|max_length=80, blank=False
Email|email|EmailField|blank=False
Reason|reason|TextField|blank=False
Order Number|order_number|CharField|max_length=80, blank=False

* Blog App

#### Post Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Title|title|CharField|max_length=200, unique=True
Slug|slug|SlugField|max_length=200, unique=True
Author|author|ForeignKey|User, on_delete=models.CASCADE,related_name='blog_posts'
Updated|updated_on|DateTimeField|auto_now=True
Content|content|TextField|
Created|created_on|DateTimeField|auto_now_add=True
Status|status|IntegerField|choices=STATUS, default=0
Image URL|image_url|URLField|max_length=1024, null=True, blank=True
Image|image|ImageField|null=True, blank=True

#### Comment Model

Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Post|post|ForeignKey|Post,on_delete=models.CASCADE,related_name='comments'
Name|name|CharField|max_length=80
Email|email|EmailField|
Body|body|TextField|
Created|created_on|DateTimeField|auto_now_add=True
Active|active|BooleanField|default=False

## Features
# Portfolio Project 4, Soulspark - TESTING


---

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)

* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

* [BUGS](#bugs)
  * [Known Bugs](#known-bugs)

---

## AUTOMATED TESTING


###  W3C Validator

Validated the following pages:

* base.html: Passed except django code. I deliberately broke the rules to not put a button inside 'a' for style purposes.

* index.html: Passed except django code.
* reviews.html: Passed except django code.
* prices.html: Passed except django code.
* contact.html: Passed except django code.
* Leave_review: Passed except django code.


#### **CSS Validation**

CSS Validator passed without error

## MANUAL TESTING

### Testing User Stories

 #### First Time Visitor Goals:

|User goal |Result   |Pass / Fail |
| --- | --- | --- |
| To be able to see what kind of bussiness this is | There is a presentation of the service offered on the index page.  | Pass |
|To be able to see what services are offered | There is a page with list of services and prices. | Pass |
|To be able to see what previous costumers have said about the services. | There is a page where costumers can leave reviews. | Pass |
|To be able to find out more by links to social accounts. | There is a Contact page with links to social accounts| Pass |
|  | |  |


 #### Returning Visitor Goals:

|User goal |Result   |Pass / Fail |
| --- | --- | --- |
|To be able to find contact information to Sussie. | There is a Contact page with contact information.  | Pass |
|To find out how to book an appointment. | There is a link leading to a booking page on the Contact page. | Pass |
|To be able to write a review. | There is a service where costumers can log in and leave reviews.| Pass |
|  | |  |


 #### Frequent Visitor Goals:

  * To be able to keep updated with changes in services.
    - The service page can be adapted to changes in services.


### Full Testing

 #### Chrome Developer Tools
  Throughout the project Chrome Developer Tools were used to test how the project looked on different devices. The final deployed version works on the most common devices.

 #### Links
  * Testing all the links in the navigatin menu
    - All working.

  * Sign up link in Sign in page
    - Working

  * Sign in link in Sign up page
    - Working

  * Links to social accounts and booking in Contact page
    - Working

  #### Sign Up
    * Sign Up
      - Works
    
    * Verification e-mail
      -Works
  
  #### Sign In Services
    * Sign In
      - Works

    * Add and remove e-mail
      - Works

    * Sign out
      - Works

    * Changing password
      - Works

  #### Reviews
    * Leave a review
      - Works
    
    * Edit and delete you own reviews
      - Works when signed in

    * Read others reviews
      - Works

  #### Admin login
    * Superuser login to Admin
      - Works


## BUGS

### Known Bugs

No known bugs
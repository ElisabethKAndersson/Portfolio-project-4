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

|User goal |Result   |Pass / Fail |
| --- | --- | --- |
|To be able to keep updated with changes in services. | The service page can be adapted to changes in services.| Pass |
|  | |  |


### Full Testing

 #### Chrome Developer Tools
  Throughout the project Chrome Developer Tools were used to test how the project looked on different devices. The final deployed version works on the most common devices.


 #### Links

|Feature|Result |Pass / Fail |
| --- | --- | --- |
|Links in the navigatin menu. |All links lead to expected destination. | Pass |
|Sign up link in Sign in page.|Link leads to sign up page. | Pass |
|Sign in link in Sign up page.|Link leads to sign up page. | Pass |
|Links to social accounts and booking in Contact page. |All links lead to expected destination.| Pass |
|  | |  |

  #### Sign Up

|Feature|Result |Pass / Fail |
| --- | --- | --- |
|Sign Up|The user is able to sign up. | Pass |
|Verification e-mail|A Verification e-mail is sent to e-mail added in sign up. It is possible to verify e-mail address inVerifikation link in e-mail  | Pass |
|  | |  |
  
  #### Sign In Services

|Feature|Result |Pass / Fail |
| --- | --- | --- |
|Sign In|After signing up, the user can sign in to de page. | Pass |
|Add and remove e-mail|It is possible to change and remove e-mail after signing in. | Pass |
|Sign out|It is possible to sign out when signed in.| Pass |
|Changing password|Function to change password works through "forgot password" function. E-mail for password change is sent to user. | Pass 
|  | |  |

  #### Reviews

|Feature|Result |Pass / Fail |
| --- | --- | --- |
|Leave review|It is possible to leave a review after being signed in. | Pass |
|Edit and delete you own reviews. |Users can edit and delete reviews when being signed in. Only changes can be made on reviews from logged in user | Pass |
|Read others reviews|All reviews are shown after being published| Pass |
|  | |  |

  #### Admin login

|Feature|Result |Pass / Fail |
| --- | --- | --- |
|Superuser login to Admin|Superusers can log in to the Admin page | Pass |
|  | |  |


## BUGS

### Known Bugs

No known bugs
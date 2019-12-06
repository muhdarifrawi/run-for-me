 # Run for Me
Run for me (Run4Me) is a fictitious webpage application that allows users to register for an account and requests for help in running their errands with a fee paid. Other users can pick up their request and get paid for it. The payment system is targeted to be an honour system payment. Meaning to say that requesters would pay the amount they deem that is worth the errands.

## Getting Started

This application is deployed using Heroku. You can find the webpage by clicking [here]( https://mar-run-for-me.herokuapp.com/). This application would not be able to run properly as a Github deployment. Feel free to download the code if needed.

For demo usage, there are two accounts that are accessible. 
```
User submitted 1
user: tester
password: siaolongbao888
```
```
User submitted 1
user: tester2
password: charsiewbao888
```
```
User has not submitted any request
user: tester3
password: vegebao123
```

![Quick Demo Gif]()

## UI/UX

Potentially this webpage application may be used by senior folks. Hence the interface should be simple for them to explore or find. It should direct them to what they need.

Also, because of the reason as to why someone would use this application (i.e lack of time), the interface should be quick and intuitive for anyone to use. The process from form filling to the payment should be hassle-free. 

## Technologies

Coding languages: HTML/CSS, Python

Framework: Django

Database: AWS S3

## Wireframes

You can find some of my thought processes in this short [PowerPoint](https://github.com/muhdarifrawi/run-for-me/blob/master/frameworks/Project%204%20Brainstorm.pptx).

## Features

Users would be greeted by an index page showing the login screen. The navbar at the top, at this point of time, will only show the homepage link, the register link and the login link. After the user has logged in, the navbar will showcase homepage, profile, Request run, Relief Run and logout. 

Unregistered users can click on the register link to navigate to a form where they have to fill in the required information. After submitting the completed form, they will be redirected to the homepage. 

Registered users can check on their personal profile by clicking on the profile link found on the navbar. Here on this page, it shows their email and joined date information for now.

Registered user can also access the request run and relief run pages of the webpage. Clicking on to the request run tab, they would be led to the request run page. There, they would see any requests that they would have sent in. Else, it would show “No requests yet”. 

To send request, registered user would have to click on to the “Add Request”. It would lead users to the request form where all the required fields are to be filled. The only field that is optional is the image field. ***Please do take note that the date format is to be filled as such yyyy-mm-dd***

At the bottom-most of the form, registered user would have to fill up their credit card details. As this is handled by Stripe, no data is kept in the app database. 

When all required fields pass the validation, the form will be sent to the database and the form can be seen on the registered user’s request page and also the relief run page where any other registered user will be able to see and relief a run for them. 

The relief run page will show requests submitted by various users. A single request is kept in a card with tabs on them. The home tab would show the order number, the user that submitted it, urgency and how much they would be paid. The address tab shows the delivery address. The details tab shows the request that they would want to be fulfilled. Images would show any images that the requester may have sent in. 

## Testing

##### All testings are done manually. No auto-testing application were used.

Here you can see how the testing was done manually: [Testing Form](https://github.com/muhdarifrawi/run-for-me/blob/master/frameworks/Project%204%20Test%20Cases.pdf)

## Issues and Future Improvements

1. Uploading an empty image file will cause user unable to load the Relief a Run page. The temporary workaround is for the user to upload an image. 
2. There is no option to request a new password for now. The plan was to use mailgun. This can be implemented for future use. 
3. The SKU should not be keyed in by the user. It should automatically run in the background. Future implementation would be to automate this process. Find the last SKU entered and output a display to be shown on the form before submission.
4. Get the “Relief Request” to function. Clicking on should reflect on the requester’s request page and change the status to “Request picked’. Then another button should appear to confirm that the delivery was completed to push money into the runner’s wallet. 
5. Indicate in the request form in the date field that date is to be filled as such yyyy-mm-dd. The other solution is to use Django datepicker. 
 
## Deployment
 
 Deployment is done via Heroku with the following add-on installed. You can find the Heroku page [here]( https://dashboard.heroku.com/apps/mar-run-for-me) and the deployed page [here]( https://mar-run-for-me.herokuapp.com/). 
 
## Acknowledgements
 

## Final Note

The project was made for education purpose only. If you happen to come across this project and find it useful, feel free to use parts of my codes and link/acknowledge this page. Thank you!



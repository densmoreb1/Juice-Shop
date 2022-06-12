## Register Admin
- capture a create user request in burp
- add a section "role":"admin"

## Bjoern's Pet
- bjoern@owasp.org
- pets name is Zaya

## Captcha Bypass
- customer feedback page
- capture the review in burp
- send to intruder
- change to null payload and clear symbols
- send 10 times

## Database Schema
- capture /rest/produts/search
- insert banana'))UNION%20SELECT%20sql,2,3,4,5,6,7,8,9%20FROM%20sqlite_master--

## Deluxe Fraud
- navigate to become a member
- capture /rest/deluxe
- change to post
- add {"paymentMode":"none","paymentId":9}

## Forged Feedback
- capture customer feedback
- change userid 

## Forged Review
- caputre editing review
- change to PUT /rest/products/6/reviews
- change or add {"id":"6G3HpeSPsHZvoq8s7","message":"I bought it, would buy again."}

## GDPR Data Erasure
- login with chris.pike@juice-sh.op'--

## API Only XSS
- login as admin
- capture with burp to find the request to an api with the bearer token
- change to post
- add content-type: application/json
- add the payload to the description of a product
- putting \ infront of "

## Client-side XSS Protection
- capture creating user
- send to repeater
- change email to a script
- login to admin
- go to /administration

## Login Bender
- login with
- bender@juice-sh.op'--


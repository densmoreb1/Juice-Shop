## API Only XSS
- login as admin
- capture with burp to find the request to an api with the bearer token
- change to post
- add content-type: application/json
- add the payload to the description of a product
- putting \ infront of "

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

## Client-side XSS Protection
- capture creating user
- send to repeater
- change email to a script
- login to admin
- go to /administration
 
## Database Schema

## Login Bender
- login with
- bender@juice-sh.op'--


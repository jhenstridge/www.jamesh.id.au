---
title: 'What is in the SafeWA QR Codes?'
slug: safewa-qr-codes
date: 2020-12-23T11:23:43+08:00
draft: false
---

Earlier this month, the Western Australian government introduced the
[SafeWA contact tracing app](https://safewa.health.wa.gov.au/), which
relies on users scanning a QR code at a venue or event in order to be
added to the online register. The app doesn\'t request location
permission, so it is solely linking your SafeWA user account with the
information in the QR code.

The QR codes were quite large, so I was kind of curious what data was
held inside them. So I tried scanning one with a different barcode
scanning app, which showed a standard URL-style QR code. Here is what
was in a code displayed outside the Coles supermarket in Claremont:

    https://safewa.health.wa.gov.au/qr-code/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZW51ZUlkIjoiNWZkYzVkYjViMjdjNzY5MDJhN2NiMzU4Iiwic2NhbkxvY2F0aW9uSWQiOiI1ZmRjNWRiNWIyN2M3NjEyYzU3Y2IzNWEiLCJpYXQiOjE2MDgyNzc0MjksImV4cCI6MjIzODk5NzQyOX0.ruc9OkZ0KgjF8z00BBhMzUIh-kJb1DhxhW9nNqvVi5w?scanLocation=5fdc5db5b27c7612c57cb35a&venue=5fdc5db5b27c76902a7cb358

There\'s two query parameters in the URL holding what looks like
hexadecimal encoded data \-- `scanLocation` and `venue`. The location
identifier shares the prefix `5fdc5db5b27c76` with the venue ID: I\'m
not sure if that means the identifiers are encoding some common data, or
whether they were generated using a UUID-style algorithm that generates
IDs with a common authority prefix.

Before the query parameters, we have a large chunk of encoded data.
Interestingly, it consists of three dot separated chunks with the first
two starting with \"ey\". That\'s a strong indication that we\'re
looking at a [JSON Web Token](https://jwt.io/). Here, the header is:

    {"alg":"HS256","typ":"JWT"}

And the payload is:

    {"venueId":"5fdc5db5b27c76902a7cb358","scanLocationId":"5fdc5db5b27c7612c57cb35a","iat":1608277429,"exp":2238997429}

The last blob is an HMAC-SHA256 signature of the first two parts. So
we\'ve essentially got a signed duplicate of the query string parameters
together with what looks like issue and expiry time stamps. Assuming
these are standard UNIX time stamps, the token was issued at 3:43pm on
18th December. The expiry date has been set 7300 days after the issue
date, which would be 20 years if every year was 365 days long.

As they\'re using an HMAC signature, presumably the SafeWA app has no
way to verify the token: if it did, then anyone with a copy of the app
could extract the key and generate their own signed JWT blobs. If the
JWT is sent back to the server verbatim, I wonder how much trouble it
would be to just check that the (venue, scanLocation) pair is valid?

So there are a few ways they could simplify the QR codes:

1.  If the JWT signatures are actually necessary, dropping the query
    parameters would remove 20% of the data in the code.
2.  If the signature is unnecessary, dropping the JWT would remove 68%
    of the data in the code.
3.  Having the QR code take the form of a URL would be useful if the app
    was set up to claim that URL prefix, since it would allow you to
    start the check-in process through any barcode scanning app. They
    haven\'t done that though, so the URL prefix could be removed for a
    shorter plain text QR code.

Lastly, visiting the URL from the QR code directly in the a web browser
currently just redirects you to the SafeWA home page and tells you to
install the app. It seems like a missed opportunity not to let people
sign their attendance at that URL directly, in case they don\'t have the
app installed or if it is malfunctioning. It could open the door for
people spoofing the Health Dept website, but it\'s not clear that\'s
worse than the the status quo where some venues still seem to be running
their own contact registers.

**Update**: I played around with generating QR codes generated from
modified versions of the URL to see what the app would accept. The app
would accept a QR code with the query parameters stripped out, and fails
if the JWT is stripped from the URL. So it is definitely using the JWT
token to determine the parameters. It also seems to accept tokens with
the signature stripped off, so it seems possible that it doesn\'t
actually care about validity.

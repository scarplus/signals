How to get auth token and refresh token for api trading in TD Ameritrade

Instructions-
https://developer.tdameritrade.com/content/simple-auth-local-apps
https://www.reddit.com/r/algotrading/comments/914q22/successful_access_to_td_ameritrade_api/


https://developer.tdameritrade.com/
Create a developer account.
Then create an app in "My Apps"


<img width="181" alt="image" src="https://user-images.githubusercontent.com/112670649/206616542-7b818004-bccf-48dd-ad91-25904a991acb.png">
save the app.

Open the app and note down your "Consumer Key"

Now open the authentication api page. This will help to generate two tokens-  authorization_code ( for trading ) and 
refresh_token( for resetting authorization code that expires in 1800s or 30 minutes, refresh token lives for 90 days)
https://developer.tdameritrade.com/authentication/apis/post/token-0

But this page requires one key element called code. To generate the code, we need the actual "Consumer Key" value  in the below url and paste in the browser.
Replace the YOURCONSUMERKEY word in below with your actual consumer Key. it is after the client_id= and before the %40
https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https://localhost&client_id=YOURCONSUMERKEY%40AMER.OAUTHAP

Once you have replaced the actual consumer key paste this url in the web browser and click yes/go ahead.. even it is says unsafe. if you do not know how to go around unsafe, change the redirect url in the "My App" to http://localhost instead of https://localhost

After you enter id and password on a authentication page, it may show unsafe page as below.. select proceed ( this is only going to connect on your localhost)
![image](https://github.com/scarplus/signals/assets/112670649/42ef4ec9-fb0e-4c79-8ec0-d8737b6680d0)

After which it may show the below page. but do not close it. We need to same the string in browser url bar. Follw steps on next line.
![image](https://github.com/scarplus/signals/assets/112670649/13dde727-7b32-41de-828d-f470cb793ea0)

At the end you may get 404 error ( as above) , saying page not found, which is ok, but note down the url value now. save the part that is after code= in the browser url
clear instructions here https://developer.tdameritrade.com/content/simple-auth-local-apps 

Google search for "url decode online", then use that to convert the value obtained above to a URL decoded value.
Now this value url decoded one, is what we will use as actual code in code field here https://developer.tdameritrade.com/authentication/apis/post/token-0

above 4 steps in this picture
![image](https://github.com/scarplus/signals/assets/112670649/a9031287-ef03-47ee-b24a-1416e072b094)
 
client_id=YOURCONSUMERKEY@AMER.OAUTHP
redirect_uri=https://localhost or http://localhost ( based on what you used in "My Apps")
![image](https://user-images.githubusercontent.com/112670649/220813122-49de9e62-5915-4f06-8210-0b998ba0f1fb.png)



click SEND 
check response button, it will have a success message with Bearer auth code and refresh token key. Save these two keys.
use the value of access_token in the "your bearer key" field in sample program attached in this folder to test out a sample trade.

This access_token gets expired every 30 minutes, but we can use the refresh_token that was also provided along with this to get the access_token programtically as and when needed. And we have to repeated most of the above steps to get the refresh token again after 90 days.
![image](https://user-images.githubusercontent.com/112670649/220813238-1587f3bb-2645-4f8c-bb84-cbfe6eb0b5af.png)


Use the value generated for refresh_token and paste it against the refresh_token variable in tdsecrets.ini This is required every 90 days.






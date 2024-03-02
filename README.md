# Flask server + AWS Lambda Function Connection
This Lambda function is made publicly available through an API Gateway, which creates an HTTP method for it. The Lambda function receives a name sent through the HTTP request and returns the corresponding output.

Additionally, a Flask server is created to connect to this HTTP request, ultimately establishing a connection between two REST APIs.

# 📋 Steps in AWS

- Create Lambda function. You can choose any existing template, but if you decide to create it from scratch you can use the code in [lambda_function.py](lambda_function.py).
- Create REST API Gateway

![image](https://github.com/marcodavidg/AWS-Lambda-Function/assets/11068920/f182c320-a645-46cf-a32a-a94313eb8b42)

- Create GET method and link it to the Lambda function. Be sure to check the option to activate the lambda proxy integration.

![image](https://github.com/marcodavidg/AWS-Lambda-Function/assets/11068920/5c190945-4019-4b6e-9305-ea011a4bb123)

- Deploy the API Gateway and retrieve the public URL.

![image](https://github.com/marcodavidg/AWS-Lambda-Function/assets/11068920/cde4e3ed-36ff-4417-b8b7-cafc322d0a38)

# Run Flask server
 ```
python flask_server.py
```
After this, you can access it from any device connected to the same network.

![image](https://github.com/marcodavidg/AWS-Lambda-Function/assets/11068920/707dc425-7410-45c9-a3b2-6d1036fde563)

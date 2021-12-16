

														=======================
														     Weather API
														=======================

														
								/**
								 * @license Copyright (c) 2021, Salman Rakin, Dept. of CSE, BUET. All rights reserved.
								 */											



# Sample webhook implementation in Python Flask.

#This is a really simple webhook implementation that gets Dialogflow classification JSON (i.e. a JSON output of Dialogflow /query endpoint) 
and returns a fulfillment response.

# Using this powerful web service bot/AGENT can respond to users collecting information from external web services like weather APIs and even Databases!!

More info about Dialogflow webhooks could be found here:
[Dialogflow Webhook](https://dialogflow.com/docs/fulfillment#webhook)

# Deployment:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?

Using this service the Smart Weather Agent can simulate a conversation through providing weather information of cities and geographic coordinates on the globe
usign the [OpenWeathermapAPI](https://openweathermap.org/api). This application extract the required city from the user query and prepare the request url to call 
for getting back all the necessary weather parameters as JSON from the API. Finally, based on the response back from the API, an NLD based speech has been built 
to send as the final response to the user with meaningful weather information!!

Regarding three tier architecture with database at the third block this application actually works as a loosely coupled middleware and maintains interaction with Dialogflow using Webhook Protocol 
and communicate RESTFUL Web Services with python Request-Response mechanism. All these three tier applications have to work harmonically 
for completing a successfull response to a user.

#Example:
User: Tell me the weather in Dhaka today  ? 
User: Hello. Today the weather in Dhaka is Haze and the temperature is 22 C. Thanks !! 

#Features:

	1. Extended Database interaction capability.
	2. Fully supported with Python Request-Response mechanism.
	3. Could respond to multiple intents based on action parameters.
	4. Able to receive request parameters as JSON and prepare response for user intelligently. 
	5. Extract parametric values from user to generate sql query using different algoritms independently. 
	6. Nested requested could be invoked to interact external webservices as well as RESTFUL Web Services.

	
	
	
#Regards, 

Developer : Salman Rakin

	


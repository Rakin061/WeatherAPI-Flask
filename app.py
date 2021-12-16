#!/usr/bin/env python
# @@  Author: Salman Rakin  @@

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json,os

from flask import Flask,request,make_response


api_key="e092bd9bb54133607de3a0f326a04144"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("queryResult").get("action") == "yahooWeatherForecast":

        baseurl="https://api.openweathermap.org/data/2.5/weather?"
        yql_url = makeYqlQuery(req,baseurl)
        if yql_url is None:
            return {}
        result = urlopen(yql_url).read()
        data = json.loads(result)
        res = makeWebhookResult(data)
        return res

def makeYqlQuery(req,baseurl):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    yql_query=baseurl + urlencode({'q':city, 'appid':api_key}) + "&format=json"
    return yql_query

def makeWebhookResult(data):
    query = data.get('main')
    if query is None:
        return {}
    geo_city=data.get('name')
    weather_data=data.get('weather')
    condition=weather_data[0].get('main')

    # result = query.get('queryResult')
    # if result is None:
    #     return {}
    #
    # channel = result.get('channel')
    # if channel is None:
    #     return {}
    #
    # item = channel.get('item')
    # location = channel.get('location')
    # units = channel.get('units')
    # if (location is None) or (item is None) or (units is None):
    #     return {}
    #
    # condition = item.get('condition')
    # if condition is None:
    #     return {}

    # print(json.dumps(item, indent=4))

    temp=query.get('temp')
    temp=int(temp)
    temp = temp-273.15
    #temp=math.floor(temp)
    temp=str(temp)


    speech = " Hello !! Today the weather in " + geo_city + " is : " + condition + \
             " and the temperature is " + temp + " " + "C" + ".  Thanks!!"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Chatbot.models import Hotels, Restaurants
import requests
from django.conf import settings
from django.http import HttpResponse
import googlemaps
import creds
# usingapi

import requests
"GOOGLE_API_KEY = [add you google api here]"


# function to convert location parameter to lat and long (because nearbysearch endpoint doesnt except any other values rather than lat long value)

def get_lat_lng(location, GOOGLE_API_KEY):
    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
    geocode_result = gmaps.geocode(location)
    lat_lng = geocode_result[0]['geometry']['location']
    return f"{lat_lng['lat']},{lat_lng['lng']}"


# pass the place_ parameter to the getplace details function
def get_place_details(place_name):
    api_key = GOOGLE_API_KEY
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'  # set the endpoint
    params = {
        'query': place_name,
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        # Extract the necessary information from the response
        result = data['results'][0]
        place_info = {
            'name': result['name'],
            'address': result['formatted_address'],
            'description': result.get('description', ''),
            'rating': result.get('rating', ''),
            'url': result.get('url', ''),
            'location': result.get('geometry', {}).get('location', {})
        }

        latitude = place_info['location'].get('lat', '')
        longitude = place_info['location'].get('lng', '')
        maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
        place_info['maps_url'] = maps_url
        return place_info
    else:
        return None


def get_places_with_best_reviews(location, type, GOOGLE_API_KEY):
    lat_lng = get_lat_lng(location, GOOGLE_API_KEY)
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': lat_lng,
        'radius': '5000',  # Specify the radius in meters for the search area
        # Specify the place type (e.g., hotels, restaurants, etc.)
        'type': type,
        'key': GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    if 'results' in data and len(data['results']) > 0:

        # Filter the results by rating (greater than 4.5)
        results = [result for result in data['results']
                   if result.get('rating', 0) > 4.5]

        # Sort the results by rating in descending order
        results = sorted(data['results'], key=lambda x: x.get(
            'rating', 0), reverse=True)

        # Extract the necessary information from the results
        places = []
        for result in results:
            place_info = {
                'name': result['name'],
                'address': result['vicinity'],
                'rating': result.get('rating', ''),
                'url': result.get('url', '')
            }
            places.append(place_info)

        return places
    else:
        return None


def handle_best_places_intent(parameters, GOOGLE_API_KEY):
    type = parameters.get('type')
    location = parameters.get('location')

    places = get_places_with_best_reviews(location, type, GOOGLE_API_KEY)

    if places:
        # Generate the response message with the places information
        response_message = f"Here are some of the best {type} in {location}:\n"
        for place in places:
            response_message += f"- {place['name']}\n"
            response_message += f"  Address: {place['address']}\n"
            response_message += f"  Rating: {place['rating']}\n"
            response_message += f"  More Info: {place['url']}\n\n"
    else:
        response_message = f"Sorry, I couldn't find any {type} in {location} with the best reviews."

    response = {
        'fulfillmentText': response_message
    }

    return HttpResponse(json.dumps(response), content_type='application/json')


@csrf_exempt
def webhook(request):
    print(request.body)
    # Extract relevant data from the request
    request_data = json.loads(request.body)
    intent = request_data['queryResult']['intent']['displayName']
    parameters = request_data['queryResult']['parameters']
    print(intent)
    print(parameters)
    if intent == 'get_hotels':
        # Call the function to retrieve hotels based on parameters
        city_areaHot = parameters.get('city_areaHot')
        hotels = Hotels.objects.filter(city=city_areaHot)
        print(city_areaHot)
        print(hotels)
        # Generate the appropriate response using the retrieved hotels
        hotel_info = []
        for hotel in hotels:
            hotel_name = hotel.name
            hotel_location = f"{hotel.latitude},{hotel.longitude}"
            google_maps_url = f"https://www.google.com/maps/search/?api=1&query={hotel_location}"
            hotel_info.append(f'{hotel_name}: {google_maps_url}')

        response = {
            'fulfillmentText': f'Here are the hotels in the requested city area with the location:\n{"    ".join(hotel_info)}',
            'hotels': hotel_info,
        }

    # restaurants
    elif intent == 'get_restaurants':
        # Call the function to retrieve hotels based on parameters
        city_area = parameters.get('city_area')
        restaurants = Restaurants.objects.filter(city=city_area)
        print(city_area)
        print(restaurants)
        # Generate the appropriate response using the retrieved hotels
        restaurant_names = [restaurant.name for restaurant in restaurants]
        response = {
            # use list comprehension to join two dictionaries
            'fulfillmentText': f'Here are the restsurants in the requested city area: {", ".join(restaurant_names)}',
            'restaurants': restaurant_names,
            # Extracting only hotel names

        }

    # to handle any other place that user asks
    elif intent == 'get_other_places':
        place_name = parameters.get('place_name')
        place_info = get_place_details(place_name)

        if place_info:
            response = {
                'fulfillmentText': f"Here is information about {place_name}: {place_info} select and go to the above url to see the location of {place_name} ",
                'place_info': place_info
            }
        else:
            response = {
                'fulfillmentText': f"Sorry, I couldn't find information about {place_name}."
            }

    # provide best places with most reviews
    elif intent == 'get_best_places':
        response = handle_best_places_intent(parameters, GOOGLE_API_KEY)
        # Return the response to Dialogflow
        return response

    else:

        # Generate the appropriate response

        response = {
            'fulfillmentText': 'This is the response from the webhook.',
        }

    return JsonResponse(response)

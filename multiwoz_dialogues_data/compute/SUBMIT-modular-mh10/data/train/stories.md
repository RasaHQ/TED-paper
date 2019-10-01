## story_SNG0073
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4648
* inform
   - nooffer_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - request_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL2437
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - reqmore_general
* inform
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL2499
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL1575
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL0671
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - offerbook_train
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2636
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - request_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - reqmore_general
   - bye_general

## story_PMUL3027
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_train
* inform
   - reqmore_general
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_MUL1489
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_name": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - greet_general

## story_SNG01608
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0888
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - request_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2305
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - inform_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL2321
* inform
   - request_restaurant
   - greet_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1812
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general

## story_MUL2569
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - recommend_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1491
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1060
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - greet_general

## story_PMUL3647
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1045
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "attraction_name": "specific"}
   - request_taxi
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - bye_general

## story_SNG01936
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_MUL1642
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL2320
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL0550
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_MUL1612
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_name": "specific"}
   - select_restaurant
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
   - nobook_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL0088
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform
   - select_hotel
   - inform_hotel
* inform{"restaurant_name": "specific", "hotel_area": "dontcare"}
   - inform_booking_restaurant
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL0469
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_MUL1926
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1526
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_SNG0689
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4626
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
* inform
   - inform_train
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1283
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2376
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1024
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - inform_booking_hotel
* inform
   - inform_hotel
* inform
   - nobook_booking_hotel
* inform
   - inform_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0263
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1350
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general

## story_MUL1799
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL2405
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - greet_general
* bye
   - bye_general

## story_SNG0515
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* bye
   - bye_general

## story_MUL2294
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
* inform
   - inform_hotel
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL1066
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG01386
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2290
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - greet_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2162
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - greet_general
   - welcome_general
   - bye_general

## story_SNG0991
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - select_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL3596
* inform
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0409
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1192
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2755
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - recommend_hotel
   - nooffer_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - inform_booking_hotel
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - request_taxi
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_taxi
   - reqmore_general
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL3126
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general

## story_MUL1650
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0451
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3868
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2177
* inform{"hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform{"hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_stars": "dontcare"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform
   - nobook_booking_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL1276
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
   - greet_general
* inform
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0264
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* bye
   - greet_general
   - bye_general

## story_PMUL4134
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - bye_general
* bye
   - welcome_general

## story_MUL2675
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - welcome_general
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1883
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - welcome_general
* bye
   - bye_general

## story_MUL1139
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - recommend_hotel
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL1064
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4643
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL3890
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - reqmore_general
* inform{"restaurant_area": "specific"}
   - welcome_general

## story_PMUL0286
* inform
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - nooffer_restaurant
* inform{"taxi_departure": "specific", "restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_taxi
   - inform_restaurant
* inform
   - inform_booking_taxi
   - inform_restaurant
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1690
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform{"train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2124
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - recommend_restaurant
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"attraction_area": "specific"}
   - request_attraction
* inform
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL0265
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4919
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - nooffer_train
   - request_train
* inform
   - select_train
* bye
   - inform_train

## story_SNG0681
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
   - nooffer_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1374
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0085
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - bye_general

## story_SNG0898
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_MUL0842
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - select_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL1818
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* bye
   - welcome_general

## story_SNG0601
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - bye_general

## story_SNG02153
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - greet_general

## story_PMUL1316
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_type": "specific", "train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0937
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_booking_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"restaurant_name": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3012
* inform{"attraction_name": "specific"}
   - inform_attraction
   - greet_general
* inform
   - select_attraction
   - inform_attraction
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_pricerange": "specific"}
   - request_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0212
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_PMUL2215
* inform
   - request_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01270
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general

## story_MUL2119
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4622
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2491
* inform{"restaurant_food": "specific"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
   - greet_general
* inform
   - inform_restaurant
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - select_attraction
   - select_restaurant
* inform
   - recommend_attraction
   - reqmore_general
* inform{"taxi_departure": "specific"}
   - inform_attraction
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2703
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - greet_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* bye
   - inform_attraction

## story_PMUL4356
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
   - greet_general
* inform{"restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
   - greet_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL3162
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_destination": "specific"}
   - offerbook_train
* bye
   - bye_general

## story_SNG01679
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi

## story_PMUL3494
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - recommend_restaurant
   - book_booking_restaurant
* inform{"restaurant_food": "specific", "restaurant_name": "specific"}
   - bye_general

## story_SNG0006
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0831
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - nooffer_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0466
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2286
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0745
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL4515
* inform
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_type": "specific"}
   - select_hotel
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general

## story_SNG0360
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL2239
* inform
   - request_restaurant
   - greet_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform
   - request_taxi
* inform
   - greet_general
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - greet_general
   - reqmore_general
* bye
   - bye_general

## story_SNG1048
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare", "hotel_type": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4318
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL2497
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1276
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG1026
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform
   - inform_hotel
* bye
   - bye_general

## story_MUL2347
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
   - greet_general
   - reqmore_general
* inform
   - recommend_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4077
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - recommend_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL0457
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2116
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
   - greet_general
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_pricerange": "dontcare"}
   - select_hotel
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL1982
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL1091
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* bye
   - bye_general

## story_PMUL4388
* inform
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_MUL1228
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL1762
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1746
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2637
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - inform_attraction
   - bye_general

## story_MUL0896
* inform{"train_destination": "specific"}
   - request_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG01940
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3935
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - welcome_general
   - bye_general

## story_SNG1070
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_MUL2301
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4946
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG0471
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
   - request_booking_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1898
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_SNG01957
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_stars": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - book_booking_hotel
   - reqmore_general
* bye
   - greet_general

## story_MUL0484
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL3919
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL1180
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4660
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - greet_general
* bye
   - bye_general

## story_MUL2269
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"train_departure": "specific"}
   - inform_hotel
   - offerbook_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_SNG0767
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - book_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2942
* inform{"hotel_area": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - select_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3672
* inform
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL0323
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0345
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL0785
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4432
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"restaurant_name": "specific"}
   - welcome_general
   - bye_general

## story_MUL0810
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform
   - inform_restaurant
* inform
   - welcome_general
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4255
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform
   - request_attraction
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL4131
* inform
   - request_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
   - greet_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_booking_attraction
* bye
   - bye_general

## story_PMUL4610
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
   - reqmore_general
* bye
   - welcome_general
   - reqmore_general
   - bye_general

## story_MUL1137
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4059
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - recommend_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general

## story_PMUL2195
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01835
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2012
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - select_hotel
   - nooffer_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL0182
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_reference": "specific", "restaurant_day": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform
   - request_taxi
   - greet_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2980
* inform
   - request_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - book_booking_hotel
* inform{"attraction_type": "specific"}
   - inform_attraction
   - inform_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1546
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform{"train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1420
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - inform_train
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL2778
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general

## story_PMUL1966
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL4122
* inform
   - inform_attraction
   - request_attraction
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - inform_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
   - bye_general
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2359
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_name": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
   - reqmore_general
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"taxi_departure": "specific", "restaurant_name": "specific"}
   - request_taxi
   - greet_general
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1008
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_hotel
   - recommend_attraction
   - greet_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01323
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL0095
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1870
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_MUL2665
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
* inform
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_PMUL3668
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
   - greet_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
   - reqmore_general
* inform{"attraction_area": "specific"}
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL1247
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_SNG0391
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3376
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - greet_general
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL2483
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "attraction_name": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL2704
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - nobook_booking_attraction
* inform{"hotel_internet": "specific"}
   - request_hotel
* inform
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0309
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_PMUL4306
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general

## story_PMUL3336
* inform{"attraction_area": "specific"}
   - recommend_attraction
   - greet_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - recommend_hotel
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_PMUL4819
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0611
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - nobook_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - reqmore_general
* inform
   - welcome_general
* bye
   - bye_general

## story_PMUL0674
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL1883
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3737
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - nooffer_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01752
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG0775
* inform
   - inform_hotel
   - recommend_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - greet_general

## story_MUL0515
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
* inform
   - reqmore_general
* bye
   - welcome_general

## story_PMUL1739
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform{"train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG0348
* inform
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0818
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL1137
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - select_train
   - inform_train
* inform
   - inform_train
* inform
   - reqmore_general
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL4884
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"hotel_name": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_hotel
   - offerbooked_train
* inform
   - inform_hotel
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2609
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
* inform
   - bye_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0004
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform
   - select_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4239
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general

## story_SNG01819
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL0297
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - greet_general

## story_SNG0840
* inform{"hotel_internet": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1800
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - offerbook_train
   - request_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - inform_booking_attraction
   - request_booking_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL1806
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - greet_general
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_SNG02315
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG02205
* inform{"taxi_type": "specific", "taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_type": "specific", "taxi_departure": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* inform
   - reqmore_general
* bye
   - greet_general

## story_MUL1555
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0317
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL1424
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_SNG02240
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL2053
* inform
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_train
   - reqmore_general
* inform{"restaurant_food": "dontcare"}
   - bye_general

## story_MUL0761
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL1978
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG01530
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_SNG0617
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - welcome_general
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_SNG1042
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_area": "dontcare"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - greet_general

## story_PMUL2194
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - greet_general

## story_SNG0547
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1182
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1901
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"train_day": "specific"}
   - inform_attraction
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1613
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_MUL0072
* inform{"hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - request_booking_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
   - nooffer_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_hotel
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4316
* inform
   - welcome_general
* inform
   - welcome_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_booking_attraction
   - inform_train
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_SNG0005
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL3834
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL1183
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
* bye
   - bye_general

## story_SNG0256
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2279
* inform{"attraction_name": "specific"}
   - inform_attraction
   - greet_general
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL4366
* inform{"attraction_name": "specific"}
   - inform_attraction
   - inform_restaurant
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - request_train
* inform
   - inform_train
* bye
   - welcome_general

## story_PMUL3742
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
   - request_restaurant
* inform
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_arriveBy": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2708
* inform{"hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL2358
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0369
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_restaurant
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL0838
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_attraction
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL4713
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"hotel_type": "specific"}
   - request_hotel
* inform{"hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_hotel
   - recommend_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL0599
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - greet_general
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform
   - request_booking_restaurant
   - greet_general
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_PMUL1136
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "dontcare"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_train
   - request_train
* bye
   - inform_attraction

## story_PMUL4026
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - recommend_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG0433
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4780
* inform
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL1834
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform{"train_departure": "specific"}
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2380
* inform
   - request_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL0374
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_booking_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
* bye
   - bye_general

## story_SNG0994
* inform{"hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "dontcare"}
   - request_hotel
* inform{"hotel_type": "dontcare"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* bye
   - reqmore_general

## story_SNG0539
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1588
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL2729
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_PMUL4880
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_arriveBy": "dontcare"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01551
* inform
   - nooffer_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - nooffer_hotel
* inform
   - nooffer_hotel
* inform
   - nooffer_hotel
* inform
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG01775
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_leaveAt": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi

## story_PMUL4231
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - nooffer_restaurant
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL0628
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_parking": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_SNG01366
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi

## story_PMUL3506
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG0636
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - inform_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL4998
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - welcome_general
   - bye_general

## story_PMUL2009
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3858
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform
   - welcome_general
* inform
   - bye_general
* inform
   - welcome_general
* bye
   - bye_general

## story_PMUL1002
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01432
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
* bye
   - inform_train

## story_PMUL1920
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0573
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - offerbook_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_MUL2106
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_type": "specific"}
   - reqmore_general
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL1015
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - select_hotel
* inform{"taxi_destination": "specific", "hotel_name": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL1593
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL0694
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
   - request_hotel
* inform
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - bye_general

## story_PMUL4616
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_PMUL1106
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4229
* inform{"hotel_name": "specific"}
   - inform_hotel
   - greet_general
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_hotel
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_SNG02006
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG0799
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL4542
* inform
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* bye
   - inform_train

## story_MUL0772
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - inform_train
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0691
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG0280
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - reqmore_general
* inform
   - greet_general
* bye
   - bye_general

## story_PMUL3946
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG0964
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - greet_general

## story_SNG0690
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform
   - recommend_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01534
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_type": "specific"}
   - nooffer_hotel
* inform
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
   - request_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0293
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_SNG02018
* inform
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi

## story_PMUL4362
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - request_hotel
   - greet_general
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - recommend_hotel
* bye
   - bye_general

## story_SNG1147
* inform{"attraction_name": "specific"}
   - inform_attraction
   - inform_booking_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_area": "specific"}
   - greet_general

## story_SNG01919
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0198
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG1086
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL2080
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2452
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL3439
* inform{"restaurant_name": "dontcare"}
   - inform_booking_restaurant
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_area": "specific", "hotel_parking": "dontcare", "hotel_type": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1692
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1147
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL2137
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - book_booking_train
   - request_train
* inform{"train_destination": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0649
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL2432
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - recommend_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - greet_general
   - welcome_general
* bye
   - bye_general

## story_MUL2658
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - recommend_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_MUL1527
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - inform_train
   - recommend_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_PMUL3160
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL0938
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - nooffer_restaurant
   - request_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_day": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3514
* inform
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_SNG0803
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - bye_general

## story_PMUL3465
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - nooffer_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_MUL1505
* inform{"restaurant_food": "specific", "attraction_area": "dontcare"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - book_booking_train
* bye
   - bye_general

## story_SNG01850
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL0370
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG1012
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - select_hotel
   - inform_booking_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - request_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - reqmore_general

## story_PMUL4894
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL1623
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_departure": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "dontcare"}
   - inform_hotel
   - nooffer_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_MUL2130
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL1756
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_SNG1091
* inform
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL1210
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0927
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - greet_general

## story_PMUL0079
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_booking_hotel
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general

## story_PMUL2719
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL0399
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general

## story_PMUL4050
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_type": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG02202
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general

## story_MUL1763
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - select_train
   - offerbook_train
* bye
   - bye_general

## story_MUL2138
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "dontcare"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - greet_general

## story_SNG01884
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_MUL0391
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2634
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1763
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1202
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_booking_taxi
   - request_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0397
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform{"restaurant_name": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - offerbooked_train
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1788
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - nooffer_train
   - request_train
* inform
   - request_train
* bye
   - welcome_general
   - bye_general

## story_SNG01634
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL2193
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_departure": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - offerbook_train
* bye
   - inform_train

## story_PMUL0832
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - bye_general
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2491
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL1067
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL4155
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_booking_train
   - inform_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform{"train_day": "specific"}
   - bye_general

## story_MUL2195
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2072
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - inform_train
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - request_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL2882
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform
   - request_attraction
* inform
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "attraction_name": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - welcome_general
   - reqmore_general

## story_PMUL4603
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - inform_train
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - offerbook_train
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_PMUL1949
* inform
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - bye_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train

## story_MUL0450
* inform{"train_destination": "dontcare"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_arriveBy": "dontcare"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_name": "dontcare"}
   - inform_attraction
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL2403
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - request_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0267
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - greet_general
* inform{"hotel_name": "specific"}
   - inform_hotel
   - greet_general
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0205
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
   - greet_general
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - greet_general
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - greet_general
* inform
   - request_taxi
   - greet_general
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG0678
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - reqmore_general
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1211
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG0459
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL1274
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "dontcare"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_day": "specific"}
   - request_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0897
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL4054
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_MUL2386
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - greet_general
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - greet_general
   - reqmore_general
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL0947
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_taxi
   - greet_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL0864
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - recommend_restaurant
   - book_booking_restaurant
* inform{"restaurant_name": "specific", "train_day": "specific"}
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL0353
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_MUL2051
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - bye_general
* inform
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - book_booking_hotel
   - bye_general

## story_PMUL1330
* inform{"attraction_type": "specific"}
   - request_attraction
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - recommend_attraction
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1109
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_booking_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_MUL0474
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1853
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_pricerange": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL1347
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train

## story_PMUL4011
* inform{"hotel_area": "specific", "hotel_internet": "dontcare", "hotel_type": "specific"}
   - recommend_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_MUL1766
* inform{"train_destination": "specific"}
   - offerbook_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
   - request_train
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL2074
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0089
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_MUL1508
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2122
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - greet_general
* inform
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL1998
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - greet_general

## story_PMUL1241
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2756
* inform{"hotel_type": "specific"}
   - request_hotel
   - greet_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* bye
   - inform_hotel

## story_PMUL3282
* inform
   - reqmore_general
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4941
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_MUL2686
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
   - greet_general
* inform{"attraction_type": "dontcare"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0901
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL1087
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG0866
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG01391
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_SNG02342
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1342
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL1844
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - greet_general

## story_PMUL0262
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_pricerange": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG0830
* inform
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_PMUL1477
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - reqmore_general

## story_PMUL1463
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1867
* inform
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - request_booking_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_PMUL2272
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
   - greet_general
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - inform_attraction
   - recommend_attraction
   - greet_general
* bye
   - welcome_general
   - bye_general

## story_MUL0208
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - select_train
   - inform_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - offerbook_train
   - welcome_general
   - reqmore_general

## story_PMUL1931
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2917
* inform
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - select_hotel
* inform{"hotel_pricerange": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - select_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01692
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* bye
   - bye_general

## story_MUL0941
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - inform_attraction
* inform
   - select_attraction
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_attraction
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - greet_general
* inform
   - inform_taxi
   - greet_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4504
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL0899
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0364
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2275
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - greet_general
* bye
   - welcome_general
   - bye_general

## story_MUL1455
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform{"train_departure": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_MUL0340
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0714
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1113
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1118
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_day": "specific"}
   - inform_attraction
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1470
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"attraction_type": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2001
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_type": "specific"}
   - request_booking_hotel
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL0803
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - book_booking_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"taxi_destination": "specific"}
   - request_taxi
   - greet_general
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - greet_general
* inform
   - inform_taxi
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_MUL0555
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_SNG0644
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1412
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform
   - inform_attraction
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train

## story_MUL0738
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_hotel
   - request_train
* inform{"train_day": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_MUL0080
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* bye
   - bye_general

## story_PMUL0875
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - request_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_MUL0669
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_MUL0739
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - nooffer_hotel
* inform
   - nooffer_hotel
   - request_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbooked_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL0978
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - recommend_restaurant
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - bye_general

## story_SNG0832
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_MUL1828
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG0423
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL1258
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - request_taxi
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL2630
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "dontcare", "hotel_pricerange": "specific", "hotel_internet": "dontcare"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - select_hotel
   - nooffer_hotel
   - request_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform{"taxi_type": "specific", "taxi_destination": "specific", "taxi_departure": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0473
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL3283
* inform
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - request_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0518
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "dontcare"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2848
* inform{"hotel_type": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "dontcare"}
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_name": "specific"}
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* inform
   - welcome_general
   - reqmore_general
* bye
   - reqmore_general

## story_MUL1560
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general

## story_SNG0701
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1273
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_PMUL1944
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* bye
   - offerbooked_train
   - reqmore_general

## story_MUL0787
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "dontcare", "restaurant_area": "specific"}
   - bye_general

## story_PMUL3685
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4125
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_MUL0939
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
   - inform_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01797
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_MUL2525
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_attraction
   - inform_hotel
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - inform_attraction

## story_PMUL3348
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* inform
   - request_booking_restaurant
* bye
   - bye_general

## story_PMUL2351
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1365
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL0144
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "dontcare"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - recommend_hotel
   - request_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL2436
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG01503
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "restaurant_name": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general

## story_SNG02172
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "dontcare"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* bye
   - welcome_general

## story_SNG0781
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL0844
* inform
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1455
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train

## story_SNG0429
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL1050
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL3931
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_PMUL4303
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - select_train
   - inform_train
* inform
   - inform_train
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_PMUL1462
* inform{"train_departure": "specific"}
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL0090
* inform{"hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - recommend_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - bye_general

## story_MUL1110
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "dontcare", "attraction_area": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform
   - greet_general
* bye
   - bye_general

## story_PMUL3933
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL0373
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_SNG0519
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - recommend_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_PMUL3304
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
   - greet_general
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_SNG0590
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_area": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL1514
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_SNG0308
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - bye_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3759
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
   - request_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2466
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1422
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_MUL1638
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform
   - inform_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0323
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL3600
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL0316
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - reqmore_general
* inform
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4176
* inform{"attraction_area": "specific"}
   - request_attraction
   - greet_general
* inform{"attraction_name": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_type": "specific", "attraction_type": "specific"}
   - request_hotel
   - greet_general
* inform{"hotel_pricerange": "dontcare", "hotel_internet": "dontcare"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - recommend_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL3107
* inform
   - request_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - request_booking_hotel
* inform{"taxi_destination": "specific", "hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_taxi
   - reqmore_general
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL3897
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - select_hotel
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - nooffer_hotel
* inform{"hotel_stars": "dontcare"}
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "hotel_name": "specific", "hotel_internet": "specific"}
   - request_booking_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1342
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - welcome_general
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1600
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - inform_booking_hotel
* inform
   - nobook_booking_hotel
   - reqmore_general
* inform
   - nobook_booking_hotel
   - reqmore_general
* inform
   - inform_booking_hotel
   - recommend_hotel
   - greet_general
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - nobook_booking_hotel
   - request_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - nobook_booking_hotel
   - greet_general
* bye
   - bye_general

## story_PMUL1804
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4524
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - select_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL1779
* inform{"hotel_parking": "specific", "hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_MUL0222
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_train
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* inform
   - welcome_general
* bye
   - bye_general

## story_SNG0979
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - reqmore_general
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG01784
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "dontcare", "hotel_parking": "specific"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_SNG0779
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL1268
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - nooffer_hotel
* inform
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_type": "dontcare"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01380
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4911
* inform
   - reqmore_general
* inform
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL4800
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_MUL1678
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - select_train
   - inform_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - reqmore_general
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_train
   - reqmore_general
* bye
   - bye_general

## story_MUL2077
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_booking_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL2166
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01290
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - greet_general

## story_PMUL1329
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - welcome_general
* bye
   - bye_general

## story_MUL2646
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0610
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0537
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1266
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL4641
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_type": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general

## story_PMUL4294
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* inform
   - request_train
* inform
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4693
* inform{"hotel_area": "specific"}
   - recommend_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1987
* inform
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL1359
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2442
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1627
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific"}
   - welcome_general
   - bye_general

## story_MUL1787
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4567
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - select_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific", "hotel_type": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - reqmore_general
* bye
   - reqmore_general
   - bye_general

## story_MUL0018
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL1232
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL3992
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1253
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL2670
* inform
   - request_hotel
   - greet_general
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_MUL0844
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - recommend_attraction
* inform{"restaurant_name": "specific", "attraction_name": "specific"}
   - inform_booking_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - reqmore_general
* bye
   - bye_general

## story_SNG0661
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general

## story_SNG01262
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - request_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_name": "dontcare"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - greet_general

## story_MUL0621
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - request_booking_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - offerbook_train
   - request_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL0012
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - nooffer_hotel
* inform
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_SNG0305
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
   - welcome_general
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL1596
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - request_restaurant
   - greet_general
* inform{"restaurant_day": "specific", "restaurant_pricerange": "dontcare"}
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
* bye
   - book_booking_train
   - welcome_general
   - bye_general

## story_SNG01492
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3921
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
* inform
   - inform_attraction
* inform
   - welcome_general
   - reqmore_general
* inform{"attraction_name": "specific"}
   - bye_general

## story_MUL1475
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - greet_general
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform
   - bye_general
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL1105
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* bye
   - bye_general

## story_PMUL1148
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_SNG0483
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL0815
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
   - greet_general
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1486
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_name": "dontcare", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL2174
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL3328
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - inform_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL3918
* inform{"train_day": "specific"}
   - offerbook_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2523
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_pricerange": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG0098
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL3085
* inform
   - welcome_general
* inform{"attraction_name": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3976
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - welcome_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - welcome_general
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01907
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL4756
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3907
* inform{"restaurant_name": "specific"}
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_booking_restaurant
   - reqmore_general
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0468
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL1983
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - greet_general

## story_MUL1759
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform{"train_destination": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL1256
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - recommend_attraction
* inform
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0527
* inform
   - inform_attraction
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "dontcare"}
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL3425
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2311
* inform
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL4357
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "specific", "restaurant_name": "dontcare"}
   - inform_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction

## story_MUL0677
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
   - greet_general
* inform
   - inform_train
* inform
   - request_hotel
   - greet_general
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - reqmore_general

## story_MUL1117
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0568
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG0933
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "dontcare", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4247
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
   - greet_general
* inform{"hotel_internet": "specific"}
   - request_hotel
   - greet_general
* inform{"hotel_parking": "specific"}
   - recommend_hotel
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - offerbook_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_train
* inform
   - welcome_general
* inform
   - bye_general
* bye
   - reqmore_general
   - bye_general

## story_MUL2316
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01542
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - inform_taxi

## story_MUL0035
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform{"restaurant_name": "specific", "hotel_internet": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
* bye
   - inform_restaurant
   - bye_general

## story_PMUL1755
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL1848
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - greet_general

## story_MUL1248
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform{"restaurant_area": "specific"}
   - request_restaurant
   - greet_general
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
   - greet_general
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0296
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0099
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_leaveAt": "dontcare"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL1385
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL2000
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3141
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform
   - request_booking_hotel
* bye
   - reqmore_general

## story_PMUL2006
* inform
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general

## story_PMUL2746
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - inform_hotel
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0692
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - select_train
   - inform_train
* inform
   - offerbooked_train
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1240
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"taxi_destination": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_taxi
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL2627
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - recommend_hotel
* inform
   - inform_booking_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "attraction_name": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - reqmore_general
   - bye_general

## story_MUL1675
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL0594
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL3803
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0692
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1351
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
   - greet_general
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_pricerange": "specific"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01937
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0789
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_type": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
* inform
   - inform_hotel
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* inform
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - request_booking_hotel
* bye
   - bye_general

## story_SNG0613
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_SNG0081
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - greet_general
* bye
   - greet_general

## story_SNG0733
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG01710
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_MUL0510
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - select_train
   - inform_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - select_train
   - inform_train
* inform
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0388
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1986
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - select_train
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL1537
* inform{"hotel_type": "specific"}
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbook_train
   - request_train
* inform
   - reqmore_general
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_SNG0477
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - request_restaurant
* bye
   - bye_general

## story_PMUL3913
* inform
   - greet_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_SNG0954
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
   - recommend_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG01733
* inform{"train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4317
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL0843
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL2542
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - greet_general

## story_PMUL3293
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "dontcare"}
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - recommend_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
   - greet_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general

## story_PMUL3247
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3066
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG01673
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL1410
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1323
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1739
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - greet_general
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_MUL1983
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "dontcare"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_arriveBy": "dontcare"}
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1077
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_attraction
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general

## story_PMUL1981
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - reqmore_general
* inform
   - inform_hotel
* bye
   - bye_general

## story_SNG0874
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL0744
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - book_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_reference": "specific"}
   - bye_general

## story_SNG0616
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1980
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - request_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG01155
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - bye_general
* bye
   - bye_general

## story_MUL0034
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
* bye
   - bye_general

## story_SNG0274
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* bye
   - welcome_general
   - bye_general

## story_MUL2009
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - select_hotel
   - inform_hotel
* inform
   - select_hotel
   - inform_hotel
* bye
   - bye_general

## story_SNG0354
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL2362
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2859
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - request_restaurant
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - recommend_hotel
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
   - greet_general
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_PMUL4383
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific"}
   - greet_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - nooffer_restaurant
   - request_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL0071
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG1076
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL2254
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general

## story_PMUL0509
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - book_booking_restaurant
* bye
   - bye_general

## story_PMUL3239
* inform
   - select_attraction
   - reqmore_general
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - inform_booking_attraction
* inform{"attraction_name": "specific"}
   - nobook_booking_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_PMUL1344
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
* bye
   - bye_general

## story_SNG0940
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_internet": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* bye
   - bye_general

## story_MUL0073
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - recommend_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0448
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL2270
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - bye_general

## story_SNG0722
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL2482
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL1649
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "train_destination": "specific", "train_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL2664
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "attraction_name": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG0792
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_attraction
   - book_booking_hotel
* inform{"hotel_name": "specific"}
   - book_booking_hotel
* inform
   - inform_booking_hotel
* bye
   - bye_general

## story_MUL1515
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_SNG01403
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL0109
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - greet_general
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* inform
   - inform_hotel
   - greet_general
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0457
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - select_train
   - inform_train
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_train
* bye
   - inform_train
   - welcome_general
   - reqmore_general
   - bye_general

## story_MUL0233
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform{"train_departure": "specific"}
   - select_train
   - inform_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - reqmore_general

## story_PMUL4078
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - welcome_general
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1803
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - request_train
* bye
   - welcome_general
   - bye_general

## story_MUL1554
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_food": "specific", "restaurant_name": "specific"}
   - inform_booking_restaurant
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - greet_general
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3437
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - recommend_hotel
   - greet_general
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_name": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_name": "dontcare", "attraction_area": "dontcare"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL1854
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train

## story_SNG01898
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL2983
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - nooffer_hotel
   - request_hotel
* inform
   - inform_hotel
   - request_hotel
   - reqmore_general
* inform
   - select_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG0572
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1091
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL1332
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* bye
   - bye_general

## story_MUL0814
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_MUL1836
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4344
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "dontcare", "hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - reqmore_general

## story_MUL2657
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2953
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_MUL0332
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0113
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_booking_hotel
   - book_booking_hotel
* inform
   - welcome_general
   - bye_general
* bye
   - bye_general

## story_PMUL3662
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - bye_general

## story_PMUL4636
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_type": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"restaurant_name": "specific"}
   - reqmore_general
* inform
   - inform_booking_restaurant
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL0654
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - nooffer_train
* inform
   - request_train
* inform
   - offerbooked_train
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL4333
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* bye
   - welcome_general

## story_MUL0575
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - greet_general
   - welcome_general

## story_PMUL1775
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0078
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0389
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_arriveBy": "dontcare"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0941
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform
   - inform_hotel
* bye
   - bye_general

## story_MUL0021
* inform{"hotel_type": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1036
* inform{"train_day": "specific"}
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4569
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
   - greet_general
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - offerbook_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4220
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - inform_restaurant
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - greet_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4224
* inform
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - recommend_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - request_train
* inform
   - inform_train
   - offerbook_train
   - request_train
* bye
   - welcome_general
   - bye_general

## story_PMUL4246
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_attraction
   - inform_hotel
* inform
   - inform_attraction
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL1718
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - nooffer_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL3263
* inform
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - request_booking_restaurant
   - greet_general
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0589
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG01434
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* bye
   - greet_general

## story_MUL0432
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - select_train
   - inform_train
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* bye
   - greet_general

## story_PMUL4840
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_parking": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL2275
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - reqmore_general
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL0454
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG1004
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4025
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3649
* inform
   - greet_general
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_area": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_PMUL0129
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - welcome_general
* bye
   - bye_general

## story_PMUL3707
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - select_attraction
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - welcome_general
* bye
   - welcome_general

## story_MUL1569
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4368
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - recommend_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
   - greet_general
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL0798
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_MUL1376
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_type": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "hotel_name": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG01165
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1869
* inform{"train_destination": "specific"}
   - inform_train
   - reqmore_general
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL3423
* inform{"hotel_type": "specific"}
   - recommend_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_taxi
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - request_taxi
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general

## story_MUL1059
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2558
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3778
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL4234
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL2439
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - greet_general
   - welcome_general

## story_SNG0962
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG0016
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG0531
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4325
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_pricerange": "specific"}
   - recommend_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_MUL0528
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
   - request_train
* inform
   - bye_general
* bye
   - bye_general

## story_MUL2284
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3815
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - reqmore_general

## story_PMUL2945
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_type": "specific"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL0992
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL0346
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* bye
   - bye_general

## story_PMUL1844
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - select_train
   - inform_train
* inform{"train_leaveAt": "dontcare"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* bye
   - bye_general

## story_PMUL4905
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general

## story_PMUL1373
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - request_attraction
* inform
   - select_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL4672
* inform
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_SNG0289
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* inform
   - offerbook_train
   - request_train
* bye
   - bye_general

## story_SNG01538
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL1838
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4258
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "attraction_name": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - reqmore_general
* inform
   - inform_booking_restaurant
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general

## story_PMUL1435
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform
   - welcome_general
* bye
   - bye_general

## story_SNG01272
* inform
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - reqmore_general

## story_MUL0011
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "dontcare", "hotel_internet": "specific"}
   - select_hotel
   - inform_booking_hotel
   - inform_hotel
* inform
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
   - request_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general

## story_SNG01686
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL0558
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific"}
   - inform_train
   - request_train

## story_MUL1633
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"restaurant_name": "specific", "train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0742
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0782
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* bye
   - bye_general

## story_MUL0540
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL1833
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0805
* inform{"hotel_type": "dontcare"}
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL1484
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4605
* inform{"hotel_name": "specific"}
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_leaveAt": "dontcare"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0873
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0048
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - select_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL1952
* inform
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_type": "specific"}
   - select_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
* inform
   - inform_hotel
* bye
   - bye_general

## story_PMUL2489
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_area": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0732
* inform{"restaurant_food": "specific"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_SNG01367
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL3875
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - select_train
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3224
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3625
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG0855
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL0341
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL1320
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2410
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* bye
   - welcome_general

## story_PMUL4326
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - welcome_general
   - reqmore_general
* inform
   - greet_general
   - bye_general
* bye
   - bye_general

## story_MUL0869
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0456
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1008
* inform{"train_destination": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform{"attraction_type": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* bye
   - welcome_general

## story_SNG0416
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1661
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - select_train
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - inform_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL0371
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0367
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2317
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "dontcare"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
   - book_booking_restaurant
   - reqmore_general
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
   - reqmore_general
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL2099
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG0390
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL4044
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG01767
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* inform
   - inform_hotel
* bye
   - bye_general

## story_PMUL0982
* inform{"train_departure": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific"}
   - inform_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbook_train
* inform
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL3523
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - nobook_booking_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4949
* inform
   - request_restaurant
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
   - greet_general
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - request_booking_restaurant
* bye
   - inform_restaurant

## story_PMUL4731
* inform
   - reqmore_general
* inform{"restaurant_pricerange": "specific"}
   - request_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - welcome_general
* bye
   - bye_general

## story_MUL0524
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - select_attraction
* inform
   - inform_attraction
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG1090
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_SNG0659
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant

## story_MUL2086
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_taxi
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - select_train
* inform
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - recommend_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG02198
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL2477
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"attraction_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"attraction_type": "dontcare", "attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_SNG0908
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2330
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_restaurant
* inform
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0446
* inform{"restaurant_food": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - greet_general

## story_PMUL3415
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2578
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
* inform
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_hotel
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG0772
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* bye
   - inform_booking_hotel
   - bye_general

## story_PMUL3576
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL3364
* inform
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "attraction_name": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL2197
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_parking": "specific"}
   - nooffer_hotel
* inform
   - request_hotel
* inform
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "dontcare"}
   - recommend_hotel
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_SNG0571
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0881
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_name": "dontcare"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
* inform{"restaurant_area": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3708
* inform
   - greet_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - select_train
   - inform_train
* inform
   - offerbook_train
* inform
   - request_train
* bye
   - bye_general

## story_MUL0638
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbook_train
* inform{"hotel_name": "specific"}
   - reqmore_general
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_MUL0199
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1981
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL1200
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* bye
   - inform_train
   - offerbook_train

## story_PMUL0998
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL0225
* inform{"train_departure": "specific"}
   - bye_general
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0529
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general


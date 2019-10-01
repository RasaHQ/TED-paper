## story_SNG0253
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train

## story_SNG0580
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL1895
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare", "train_status": "available"}
   - select_train
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL1173
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL1071
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform{"hotel_pricerange": "specific", "attraction_name": "specific", "attraction_status": "available", "hotel_status": "available"}
   - inform_attraction
   - slot{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL1285
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0566
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific", "restaurant_name": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4842
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific", "hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1697
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - select_train
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - reqmore_general
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_restaurant
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - greet_general

## story_MUL2423
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - request_taxi
* inform
   - inform_attraction
* inform{"taxi_departure": "specific", "attraction_name": "specific", "attraction_status": "available", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - inform_attraction
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1772
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - reqmore_general
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - bye_general

## story_SNG0322
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL0286
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_SNG0715
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG0600
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL4930
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - slot{"restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"hotel_type": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG1150
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL0230
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - welcome_general
   - reqmore_general
* bye
   - bye_general

## story_SNG0528
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - welcome_general
   - bye_general

## story_PMUL0685
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL1189
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - greet_general
* inform{"hotel_internet": "dontcare", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_internet": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2139
* inform{"hotel_area": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - select_hotel
   - slot{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
   - slot{"hotel_status": "NA"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_parking": "dontcare", "hotel_internet": "dontcare", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL0116
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - slot{"hotel_status": "NA"}
   - nobook_booking_hotel
* inform{"hotel_name": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "NA"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - bye_general

## story_PMUL3521
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - request_attraction
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_SNG0721
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "dontcare", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL0148
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - greet_general
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - greet_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3156
* inform{"restaurant_name": "specific", "restaurant_status": "available", "hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_status": "NA"}
   - nooffer_hotel
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - bye_general
* inform
   - inform_taxi
* bye
   - bye_general

## story_PMUL3663
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - recommend_attraction
   - greet_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - greet_general
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_SNG1016
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL2151
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_status": "NA"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_status": "NA"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - slot{"hotel_status": "NA"}
   - nobook_booking_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* bye
   - bye_general

## story_PMUL4048
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3520
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - request_booking_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0990
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL0615
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - request_restaurant
   - greet_general
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_MUL1028
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_name": "specific", "attraction_status": "available"}
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

## story_PMUL0630
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0014
* inform{"hotel_area": "specific", "hotel_parking": "dontcare", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_stars": "dontcare", "hotel_status": "available"}
   - recommend_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1657
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - greet_general
   - welcome_general

## story_SNG01983
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - bye_general

## story_SNG0338
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL1657
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_SNG0755
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL0533
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - greet_general
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform
   - request_train
   - greet_general
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1311
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_train
* inform
   - inform_train
   - request_train
* bye
   - welcome_general
   - bye_general

## story_PMUL0441
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform
   - inform_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - welcome_general

## story_PMUL0522
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - greet_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2209
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
* bye
   - bye_general

## story_MUL0828
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_status": "unique"}
   - inform_booking_attraction
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL1278
* inform{"hotel_area": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - request_booking_hotel
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
   - slot{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1370
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - bye_general

## story_MUL1122
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL4462
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform
   - inform_attraction
* inform{"taxi_leaveAt": "specific", "taxi_destination": "specific", "attraction_name": "specific", "attraction_status": "available", "taxi_status": "available"}
   - inform_attraction
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL2155
* inform{"hotel_area": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - select_train
   - inform_train
* inform
   - inform_train
* bye
   - greet_general

## story_MUL1254
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - greet_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL2089
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - greet_general

## story_SNG01359
* inform
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
   - welcome_general
* inform{"taxi_leaveAt": "dontcare", "taxi_status": "available"}
   - request_taxi
   - welcome_general
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0095
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0498
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - reqmore_general

## story_PMUL4106
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL0578
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - request_train
* bye
   - bye_general

## story_MUL0197
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - greet_general
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2146
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
   - greet_general
* inform
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_MUL1695
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
   - slot{"restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_SNG01924
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3044
* inform
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL2225
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
   - greet_general
* inform{"hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* bye
   - bye_general

## story_MUL0890
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
   - slot{"restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - recommend_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* inform
   - reqmore_general
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* bye
   - reqmore_general

## story_MUL2365
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare", "attraction_status": "available"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - welcome_general
   - bye_general
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL1801
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - offerbook_train
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - recommend_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"attraction_area": "dontcare", "attraction_status": "available"}
   - welcome_general
   - bye_general

## story_MUL2281
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "NA"}
   - nooffer_train
* inform{"train_status": "NA"}
   - nooffer_train
   - reqmore_general
* inform
   - inform_train
* inform{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - bye_general

## story_SNG0008
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL0204
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "dontcare", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - request_booking_restaurant
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1935
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_attraction
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - welcome_general
   - bye_general

## story_PMUL3734
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform
   - inform_train
* inform{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG02096
* inform{"restaurant_name": "specific", "hotel_name": "specific", "hotel_status": "available", "restaurant_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - bye_general

## story_MUL2427
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - select_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_area": "dontcare", "attraction_status": "available", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform
   - request_taxi
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL1620
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - bye_general

## story_SNG0735
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL1533
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* bye
   - bye_general

## story_MUL2042
* inform{"train_destination": "specific", "train_status": "unique"}
   - offerbook_train
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_MUL1289
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3940
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
* inform{"attraction_type": "specific", "attraction_status": "NA"}
   - nooffer_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_SNG1105
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL0841
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "attraction_area": "specific", "attraction_status": "available", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL1607
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4259
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - offerbook_train
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL1809
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - bye_general

## story_PMUL2433
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - welcome_general
   - reqmore_general
   - bye_general

## story_MUL2567
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG1075
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01332
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG0055
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL2060
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"hotel_parking": "dontcare", "hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_parking": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL0117
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - request_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_SNG1078
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_MUL1606
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL3301
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL0682
* inform
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - inform_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - bye_general

## story_PMUL2146
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "dontcare", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific", "taxi_status": "unique", "train_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - reqmore_general

## story_PMUL3171
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - bye_general

## story_PMUL3731
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - greet_general
* bye
   - greet_general

## story_PMUL2933
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "dontcare", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1855
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - greet_general
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - greet_general
   - reqmore_general
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - inform_train
   - recommend_attraction
* inform
   - inform_attraction
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_SNG0007
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4343
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
   - greet_general
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_reference": "specific", "restaurant_status": "available"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - greet_general
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - greet_general
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL2205
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_booking_restaurant
* inform
   - inform_restaurant
   - greet_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG1126
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - recommend_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL1811
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - bye_general

## story_PMUL2503
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare", "attraction_status": "available"}
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "NA"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "dontcare", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1478
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_status": "unique"}
   - offerbook_train
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - welcome_general

## story_PMUL3127
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* bye
   - inform_attraction

## story_SNG01683
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - inform_restaurant
* bye
   - bye_general

## story_PMUL3275
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - bye_general

## story_PMUL3264
* inform
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL2368
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_booking_restaurant
* inform
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4958
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - greet_general
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - welcome_general
   - bye_general

## story_MUL2415
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare", "attraction_status": "available"}
   - inform_attraction
   - recommend_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_name": "specific", "attraction_status": "available", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL0306
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_destination": "specific", "train_status": "available"}
   - select_train
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
* inform
   - reqmore_general
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - greet_general
   - welcome_general

## story_PMUL0506
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "NA"}
   - nooffer_train
* inform
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - inform_train
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general

## story_SNG0983
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* bye
   - greet_general
   - bye_general

## story_MUL1493
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform{"train_status": "unique"}
   - offerbook_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* bye
   - bye_general

## story_SNG0500
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* bye
   - bye_general

## story_SNG0782
* inform{"hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL1273
* inform{"hotel_name": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_status": "NA"}
   - nobook_booking_restaurant
* bye
   - bye_general

## story_MUL1860
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - select_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0496
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_status": "NA"}
   - nooffer_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_MUL0352
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_booking_restaurant
* bye
   - bye_general

## story_MUL1418
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG01755
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - recommend_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1194
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_name": "specific", "attraction_area": "dontcare", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - select_train
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train

## story_SNG1036
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* bye
   - welcome_general

## story_MUL0237
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "dontcare", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - select_train
   - inform_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL1259
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3957
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL4716
* inform
   - greet_general
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL3309
* inform
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL2210
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01353
* inform{"hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - select_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - slot{"hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3424
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - greet_general

## story_PMUL0006
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG0069
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_leaveAt": "dontcare", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL2563
* inform
   - inform_attraction
   - request_attraction
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - recommend_attraction
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL0919
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "available"}
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0260
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_train
   - request_train
* inform{"restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - bye_general

## story_PMUL0069
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_status": "available"}
   - select_hotel
* inform{"hotel_pricerange": "dontcare", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL0713
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
   - reqmore_general
* inform
   - inform_restaurant
* bye
   - greet_general
   - bye_general

## story_PMUL3310
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1159
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_status": "available"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4644
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_status": "NA"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_type": "specific", "hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL0379
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - request_taxi
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - bye_general
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL4001
* inform
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3495
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare", "attraction_status": "available"}
   - recommend_attraction
* inform{"restaurant_food": "specific", "attraction_name": "specific", "attraction_status": "available", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0276
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
   - slot{"restaurant_status": "NA"}
   - nooffer_restaurant
* inform{"restaurant_status": "unique"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general

## story_SNG0412
* inform{"train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1046
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"attraction_area": "specific", "attraction_status": "NA"}
   - nooffer_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0527
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
* bye
   - bye_general

## story_PMUL0994
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_MUL0570
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
* inform{"train_status": "unique"}
   - offerbook_train
* bye
   - welcome_general
   - bye_general

## story_PMUL3785
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - reqmore_general
* inform
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0867
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_stars": "dontcare", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_SNG01873
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL0768
* inform{"restaurant_food": "specific", "restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_status": "NA"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_PMUL4034
* inform{"hotel_internet": "dontcare", "hotel_status": "available"}
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1899
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - greet_general

## story_MUL1466
* inform
   - request_restaurant
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general

## story_MUL0492
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - welcome_general

## story_SNG02207
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - reqmore_general

## story_MUL0383
* inform{"train_destination": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2063
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
* inform
   - bye_general
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1417
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - bye_general

## story_MUL2378
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform
   - select_attraction
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - greet_general
* bye
   - greet_general

## story_MUL1088
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - slot{"hotel_status": "NA"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
* inform{"hotel_day": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3557
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1055
* inform{"attraction_type": "specific", "attraction_status": "available"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
   - slot{"hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "available"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_status": "NA"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - greet_general

## story_PMUL0076
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - select_restaurant
   - inform_restaurant
   - greet_general
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - select_restaurant
   - slot{"restaurant_status": "unique"}
   - inform_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform
   - welcome_general
   - reqmore_general
* inform{"hotel_type": "specific", "hotel_status": "available"}
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_internet": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - request_booking_hotel
* inform
   - inform_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
   - request_booking_hotel
* bye
   - welcome_general
   - reqmore_general

## story_MUL0849
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_status": "NA"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform{"restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4440
* inform{"restaurant_name": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
   - reqmore_general
* inform
   - reqmore_general
* inform
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_status": "available"}
   - inform_hotel
   - slot{"hotel_status": "NA"}
   - nooffer_hotel
* inform{"hotel_status": "unique"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_status": "unique"}
   - action_book_hotel
   - slot{"hotel_status": "booked", "hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - slot{"hotel_status": "booked"}
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL0821
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - greet_general
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available", "restaurant_status": "available"}
   - inform_restaurant
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3549
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific", "train_status": "available"}
   - inform_train
   - slot{"train_status": "unique"}
   - offerbook_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
   - reqmore_general
* bye
   - bye_general

## story_SNG0797
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific", "hotel_status": "NA"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_status": "available"}
   - inform_hotel
   - request_hotel
* inform
   - recommend_hotel
* bye
   - bye_general

## story_SNG0061
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4547
* inform{"restaurant_name": "specific", "restaurant_status": "unique"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_departure": "specific", "taxi_status": "available"}
   - request_taxi
* inform{"taxi_status": "unique"}
   - action_book_taxi
   - slot{"taxi_status": "booked", "taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3158
* inform{"attraction_type": "specific", "attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_status": "available"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific", "restaurant_status": "available"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_status": "unique"}
   - action_book_restaurant
   - slot{"restaurant_status": "booked", "restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - slot{"restaurant_status": "booked"}
* bye
   - reqmore_general

## story_MUL0536
* inform{"attraction_name": "specific", "attraction_status": "available"}
   - inform_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific", "attraction_status": "available"}
   - welcome_general
   - reqmore_general
* inform{"train_destination": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_status": "available"}
   - inform_train
* inform
   - inform_train
   - greet_general
* inform
   - reqmore_general
* bye
   - welcome_general

## story_PMUL3688
* inform{"attraction_area": "specific", "attraction_status": "available"}
   - request_attraction
* inform
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_status": "available"}
   - request_train
* inform{"train_departure": "specific", "train_status": "available"}
   - inform_train
* inform{"train_status": "unique"}
   - action_book_train
   - slot{"train_status": "booked", "train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - slot{"train_status": "booked"}
* bye
   - welcome_general
   - bye_general


## story_PMUL3171
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3731
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - recommend_restaurant   <!-- predicted: request_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - reqmore_general   <!-- predicted: request_attraction -->
* inform
    - inform_attraction   <!-- predicted: inform_restaurant -->
* inform
    - request_taxi   <!-- predicted: inform_attraction -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - greet_general   <!-- predicted: inform_taxi -->
    - action_listen   <!-- predicted: welcome_general -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: welcome_general -->


## story_PMUL2933
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - select_hotel   <!-- predicted: inform_booking_hotel -->
    - inform_hotel
* inform{"hotel_pricerange": "dontcare"}
    - slot{"hotel_pricerange": "dontcare"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel   <!-- predicted: recommend_hotel -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_MUL1855
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - greet_general   <!-- predicted: offerbook_train -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - greet_general   <!-- predicted: action_listen -->
    - reqmore_general
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - inform_train   <!-- predicted: request_attraction -->
    - recommend_attraction   <!-- predicted: reqmore_general -->
* inform
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - bye_general


## story_SNG0007
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - reqmore_general   <!-- predicted: inform_taxi -->
* bye
    - bye_general


## story_PMUL4343
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - recommend_restaurant   <!-- predicted: reqmore_general -->
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_booking_restaurant   <!-- predicted: request_restaurant -->
    - greet_general   <!-- predicted: action_listen -->
* inform
    - request_booking_restaurant   <!-- predicted: request_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform{"restaurant_reference": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant   <!-- predicted: book_booking_attraction -->
    - greet_general   <!-- predicted: reqmore_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_attraction
    - recommend_attraction
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - greet_general   <!-- predicted: inform_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - bye_general


## story_PMUL2205
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant
* inform{"restaurant_name": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* inform
    - inform_restaurant
    - greet_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - request_attraction   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi   <!-- predicted: request_taxi -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG1126
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - recommend_attraction   <!-- predicted: inform_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1811
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL2503
* inform
    - request_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - request_attraction
* inform{"attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - recommend_attraction
* inform
    - inform_attraction
    - reqmore_general
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - nooffer_hotel   <!-- predicted: inform_hotel -->
    - reqmore_general   <!-- predicted: request_hotel -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "dontcare"}
    - slot{"hotel_area": "dontcare"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - inform_hotel   <!-- predicted: book_booking_hotel -->
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_MUL2423
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - recommend_restaurant   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: bye_general -->
    - reqmore_general
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - request_attraction   <!-- predicted: action_listen -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - request_taxi   <!-- predicted: inform_attraction -->
* inform
    - inform_attraction   <!-- predicted: request_taxi -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_departure": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi   <!-- predicted: inform_taxi -->
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - inform_attraction   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1478
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "dontcare"}
    - slot{"restaurant_food": "dontcare"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - request_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_PMUL3127
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general
* bye
    - inform_attraction   <!-- predicted: welcome_general -->


## story_SNG01683
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: request_booking_restaurant -->
    - action_listen   <!-- predicted: greet_general -->
* inform
    - inform_restaurant   <!-- predicted: greet_general -->
    - action_listen   <!-- predicted: greet_general -->
* bye
    - bye_general


## story_PMUL3275
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant
    - request_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_hotel -->
    - recommend_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3264
* inform
    - request_hotel   <!-- predicted: request_attraction -->
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - request_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform
    - request_train   <!-- predicted: inform_train -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL2368
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general   <!-- predicted: inform_restaurant -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi   <!-- predicted: request_taxi -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_PMUL4958
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: select_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - greet_general   <!-- predicted: action_listen -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL2415
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - recommend_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: select_restaurant -->
    - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - bye_general


## story_MUL0306
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - select_train   <!-- predicted: request_train -->
    - inform_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - recommend_restaurant   <!-- predicted: nooffer_restaurant -->
* inform
    - reqmore_general   <!-- predicted: inform_restaurant -->
* inform
    - request_booking_restaurant   <!-- predicted: welcome_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant
    - request_booking_restaurant
* inform
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_PMUL0506
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - nooffer_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - request_train   <!-- predicted: action_book_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - action_listen   <!-- predicted: offerbooked_train -->
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_PMUL1772
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_type": "specific"}
    - recommend_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel   <!-- predicted: action_book_hotel -->
    - action_listen   <!-- predicted: recommend_hotel -->
* inform
    - action_book_hotel   <!-- predicted: inform_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0983
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - reqmore_general
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - bye_general   <!-- predicted: action_listen -->


## story_MUL1493
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: request_train -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_pricerange": "dontcare"}
    - slot{"restaurant_pricerange": "dontcare"}
    - inform_booking_restaurant
    - recommend_restaurant
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0500
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - request_booking_restaurant   <!-- predicted: request_restaurant -->
* inform
    - inform_booking_restaurant   <!-- predicted: request_restaurant -->
    - recommend_restaurant
* bye
    - bye_general


## story_SNG0782
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1273
* inform{"hotel_name": "specific", "hotel_type": "specific"}
    - slot{"hotel_name": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant
    - recommend_restaurant
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: action_book_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_booking_restaurant   <!-- predicted: nobook_booking_restaurant -->
* inform
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - action_listen   <!-- predicted: request_booking_restaurant -->
* bye
    - bye_general   <!-- predicted: action_book_restaurant -->


## story_MUL1860
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - recommend_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - select_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: inform_train -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - welcome_general   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: bye_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL0496
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform
    - nooffer_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: request_attraction -->
* inform
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL0352
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - request_restaurant   <!-- predicted: nooffer_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1418
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - offerbook_train   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "dontcare"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - recommend_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
* bye
    - welcome_general
    - bye_general


## story_SNG01755
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform
    - recommend_restaurant
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: action_book_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: action_book_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_SNG0322
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - reqmore_general   <!-- predicted: action_book_train -->
* bye
    - bye_general


## story_PMUL1194
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"attraction_name": "specific", "attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_attraction
    - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - select_train   <!-- predicted: inform_train -->
    - request_train   <!-- predicted: inform_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->


## story_SNG1036
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: select_hotel -->
    - inform_hotel
* inform
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform
    - request_booking_hotel
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - action_listen   <!-- predicted: bye_general -->


## story_MUL0237
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - request_restaurant
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: request_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "dontcare"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "dontcare"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - select_train   <!-- predicted: inform_train -->
    - inform_train
* inform
    - request_train   <!-- predicted: inform_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1259
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - request_train   <!-- predicted: action_book_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general   <!-- predicted: welcome_general -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3957
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: inform_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: greet_general -->
* inform
    - reqmore_general   <!-- predicted: request_train -->
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4716
* inform
    - greet_general   <!-- predicted: request_attraction -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
    - request_train   <!-- predicted: action_listen -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_attraction   <!-- predicted: greet_general -->
* inform
    - recommend_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - offerbooked_train   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3309
* inform
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - offerbook_train   <!-- predicted: inform_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - select_restaurant   <!-- predicted: action_book_train -->
    - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general


## story_PMUL2210
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
* inform
    - inform_attraction
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant
    - request_restaurant
* inform
    - recommend_restaurant   <!-- predicted: inform_restaurant -->
    - action_listen   <!-- predicted: request_booking_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* inform
    - inform_taxi
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG01353
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - request_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_area": "dontcare"}
    - slot{"hotel_area": "dontcare"}
    - recommend_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - recommend_hotel   <!-- predicted: nobook_booking_hotel -->
    - action_listen   <!-- predicted: request_booking_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: request_booking_hotel -->
    - nobook_booking_hotel   <!-- predicted: action_listen -->
    - request_booking_hotel
* inform
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_PMUL3424
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - reqmore_general   <!-- predicted: request_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* inform
    - request_train   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - request_train
* inform
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* bye
    - greet_general   <!-- predicted: welcome_general -->


## story_MUL0286
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - reqmore_general   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - nooffer_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: nobook_booking_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
    - action_listen   <!-- predicted: request_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - welcome_general
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0006
* inform
    - inform_hotel   <!-- predicted: request_attraction -->
    - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_restaurant
* inform
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL2563
* inform
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_attraction -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_day": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - recommend_attraction   <!-- predicted: select_attraction -->
* inform
    - reqmore_general   <!-- predicted: inform_attraction -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0919
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant
    - recommend_restaurant   <!-- predicted: request_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: action_book_restaurant -->
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - book_booking_restaurant   <!-- predicted: welcome_general -->
* inform
    - action_book_restaurant   <!-- predicted: welcome_general -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - reqmore_general   <!-- predicted: inform_train -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_MUL0260
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_train   <!-- predicted: inform_restaurant -->
    - request_train   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - nooffer_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0069
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - nooffer_restaurant   <!-- predicted: inform_restaurant -->
    - request_restaurant
* inform
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - recommend_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_parking": "specific"}
    - select_hotel   <!-- predicted: action_book_hotel -->
    - action_listen   <!-- predicted: inform_hotel -->
* inform{"hotel_pricerange": "dontcare", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "dontcare"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: recommend_hotel -->
    - recommend_hotel   <!-- predicted: action_listen -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* bye
    - bye_general


## story_PMUL0713
* inform
    - request_train   <!-- predicted: request_attraction -->
    - greet_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant
    - inform_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant
    - recommend_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_restaurant   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3310
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - action_listen   <!-- predicted: request_restaurant -->
* inform
    - nooffer_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - request_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant   <!-- predicted: select_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: request_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
    - request_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_MUL1159
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - request_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - request_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - request_hotel   <!-- predicted: reqmore_general -->
* inform{"hotel_day": "specific", "hotel_internet": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_internet": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_PMUL4644
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - nooffer_hotel   <!-- predicted: select_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - nooffer_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - recommend_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant
    - inform_restaurant
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0715
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - recommend_restaurant   <!-- predicted: nooffer_restaurant -->
* inform{"restaurant_name": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0379
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_taxi   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: inform_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - bye_general   <!-- predicted: greet_general -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4001
* inform
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - reqmore_general   <!-- predicted: inform_attraction -->
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform
    - request_train
* inform
    - action_book_train   <!-- predicted: request_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - bye_general   <!-- predicted: inform_attraction -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3495
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - recommend_attraction
* inform{"restaurant_food": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"restaurant_food": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_pricerange": "dontcare"}
    - slot{"restaurant_pricerange": "dontcare"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - recommend_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - welcome_general   <!-- predicted: inform_taxi -->
    - reqmore_general   <!-- predicted: bye_general -->
    - action_listen   <!-- predicted: bye_general -->
* bye
    - welcome_general
    - bye_general


## story_PMUL0276
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant
    - reqmore_general   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - nooffer_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform
    - inform_booking_restaurant   <!-- predicted: request_restaurant -->
    - recommend_restaurant
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_SNG0412
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_PMUL1046
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction   <!-- predicted: welcome_general -->
    - reqmore_general
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_SNG0527
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0994
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - request_restaurant
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - inform_restaurant   <!-- predicted: book_booking_restaurant -->
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0570
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform
    - inform_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: request_train -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3785
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - reqmore_general
* inform
    - request_booking_hotel   <!-- predicted: welcome_general -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - recommend_restaurant   <!-- predicted: select_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_SNG0600
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: greet_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: greet_general -->
* inform
    - bye_general   <!-- predicted: inform_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0867
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_stars": "dontcare"}
    - slot{"hotel_stars": "dontcare"}
    - inform_booking_hotel   <!-- predicted: recommend_hotel -->
    - inform_hotel
* inform
    - reqmore_general   <!-- predicted: request_booking_hotel -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG01873
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0768
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant   <!-- predicted: action_listen -->
* inform
    - nooffer_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4034
* inform{"hotel_internet": "dontcare"}
    - slot{"hotel_internet": "dontcare"}
    - reqmore_general   <!-- predicted: request_hotel -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train   <!-- predicted: request_train -->
* inform
    - request_train
* inform
    - action_book_train   <!-- predicted: request_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_MUL1899
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train   <!-- predicted: request_attraction -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train   <!-- predicted: reqmore_general -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: welcome_general -->


## story_MUL1466
* inform
    - request_restaurant   <!-- predicted: request_attraction -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: greet_general -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_MUL0492
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - recommend_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: request_attraction -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_SNG02207
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - reqmore_general   <!-- predicted: inform_taxi -->
* bye
    - reqmore_general   <!-- predicted: bye_general -->


## story_MUL0383
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - recommend_restaurant
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant
    - request_booking_restaurant
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_MUL2063
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - action_listen   <!-- predicted: request_hotel -->
* inform
    - bye_general   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: request_train -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: offerbook_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4930
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - nooffer_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_restaurant
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi   <!-- predicted: request_taxi -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1417
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: action_book_train -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL2378
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - inform_restaurant   <!-- predicted: book_booking_restaurant -->
    - book_booking_restaurant
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform
    - select_attraction   <!-- predicted: recommend_attraction -->
    - recommend_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - greet_general   <!-- predicted: welcome_general -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: welcome_general -->


## story_MUL1088
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - recommend_attraction   <!-- predicted: request_attraction -->
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - nooffer_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - select_hotel
    - inform_hotel
* inform
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel   <!-- predicted: request_booking_hotel -->
    - action_listen   <!-- predicted: inform_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - action_listen   <!-- predicted: request_booking_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform
    - inform_attraction   <!-- predicted: request_attraction -->
    - reqmore_general
* inform
    - reqmore_general   <!-- predicted: request_attraction -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3557
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - welcome_general
    - bye_general


## story_MUL1055
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform{"attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - nooffer_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - nooffer_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_day": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - action_book_hotel   <!-- predicted: inform_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - inform_taxi
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: welcome_general -->


## story_PMUL0076
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant
    - greet_general   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_booking_restaurant
    - action_listen   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - welcome_general
    - reqmore_general
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: inform_hotel -->
* inform
    - inform_hotel
* inform
    - inform_booking_hotel   <!-- predicted: reqmore_general -->
    - inform_hotel
    - request_booking_hotel   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - reqmore_general   <!-- predicted: bye_general -->


## story_MUL0849
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_restaurant   <!-- predicted: welcome_general -->
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant
    - request_booking_restaurant
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - inform_restaurant   <!-- predicted: book_booking_restaurant -->
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_PMUL4440
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: inform_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: greet_general -->
* inform
    - reqmore_general   <!-- predicted: inform_train -->
* inform
    - request_hotel   <!-- predicted: inform_train -->
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: recommend_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - nooffer_hotel   <!-- predicted: action_listen -->
* inform
    - inform_booking_hotel   <!-- predicted: welcome_general -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* inform
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0821
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - greet_general   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific", "attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_attraction -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform
    - inform_attraction   <!-- predicted: recommend_restaurant -->
    - recommend_attraction   <!-- predicted: reqmore_general -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi   <!-- predicted: request_taxi -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_PMUL3549
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG1150
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - request_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0797
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_hotel
    - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - nooffer_hotel   <!-- predicted: select_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - request_hotel   <!-- predicted: action_listen -->
* inform
    - recommend_hotel
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0061
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - reqmore_general   <!-- predicted: inform_taxi -->
* bye
    - bye_general


## story_PMUL4547
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: greet_general -->
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - action_book_restaurant   <!-- predicted: request_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction   <!-- predicted: reqmore_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3158
* inform{"attraction_type": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
* inform
    - inform_attraction
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - request_restaurant
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* bye
    - reqmore_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: bye_general -->


## story_MUL0536
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - welcome_general   <!-- predicted: inform_attraction -->
    - reqmore_general
    - action_listen   <!-- predicted: bye_general -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - greet_general   <!-- predicted: offerbook_train -->
* inform
    - reqmore_general   <!-- predicted: inform_train -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_PMUL3688
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - request_attraction   <!-- predicted: inform_attraction -->
* inform
    - inform_attraction
    - recommend_attraction   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* bye
    - welcome_general
    - bye_general


## story_MUL0230
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: action_book_train -->
* inform
    - welcome_general
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general


## story_SNG0528
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant   <!-- predicted: nooffer_restaurant -->
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: request_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_SNG0253
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->


## story_PMUL0685
* inform
    - inform_restaurant   <!-- predicted: request_attraction -->
    - request_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - request_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
    - action_listen   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1189
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - greet_general   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_internet": "dontcare"}
    - slot{"hotel_internet": "dontcare"}
    - inform_hotel
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - request_hotel
* inform{"hotel_day": "specific", "hotel_internet": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_internet": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_MUL2139
* inform{"hotel_area": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - request_hotel
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
    - nooffer_hotel   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_day": "specific", "hotel_parking": "dontcare", "hotel_internet": "dontcare"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_internet": "dontcare"}
    - slot{"hotel_parking": "dontcare"}
    - action_book_hotel   <!-- predicted: request_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - inform_hotel   <!-- predicted: book_booking_hotel -->
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_train   <!-- predicted: request_hotel -->
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - action_book_train   <!-- predicted: request_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform
    - inform_train   <!-- predicted: request_hotel -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_train   <!-- predicted: request_hotel -->
* inform
    - inform_train   <!-- predicted: request_hotel -->
    - offerbook_train   <!-- predicted: action_listen -->
* inform
    - action_book_train   <!-- predicted: request_hotel -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0116
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - request_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: select_restaurant -->
    - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel   <!-- predicted: action_book_hotel -->
    - nobook_booking_hotel   <!-- predicted: request_booking_hotel -->
    - action_listen   <!-- predicted: request_booking_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - nobook_booking_hotel
    - request_booking_hotel
* inform
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - reqmore_general   <!-- predicted: request_booking_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - bye_general   <!-- predicted: book_booking_hotel -->


## story_PMUL3521
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - request_attraction
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - recommend_attraction   <!-- predicted: inform_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - recommend_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0721
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_restaurant
* inform{"restaurant_pricerange": "dontcare", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "dontcare"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general   <!-- predicted: welcome_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0148
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: request_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - greet_general   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform
    - inform_booking_hotel   <!-- predicted: welcome_general -->
    - inform_hotel
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: recommend_hotel -->
    - greet_general   <!-- predicted: action_listen -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3156
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - nooffer_hotel   <!-- predicted: inform_booking_restaurant -->
* inform
    - nooffer_hotel   <!-- predicted: inform_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi   <!-- predicted: request_taxi -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - bye_general   <!-- predicted: welcome_general -->
* inform
    - inform_taxi   <!-- predicted: welcome_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL3663
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - recommend_attraction   <!-- predicted: request_attraction -->
    - greet_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - greet_general   <!-- predicted: reqmore_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - bye_general


## story_SNG1016
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_type": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0580
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: greet_general -->
* inform
    - inform_restaurant
    - request_booking_restaurant   <!-- predicted: request_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_MUL2151
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - nooffer_hotel   <!-- predicted: select_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - nooffer_hotel   <!-- predicted: inform_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_booking_hotel   <!-- predicted: select_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: book_booking_hotel -->
    - request_booking_hotel   <!-- predicted: reqmore_general -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - inform_booking_hotel   <!-- predicted: action_book_hotel -->
    - nobook_booking_hotel   <!-- predicted: recommend_hotel -->
* inform
    - inform_hotel   <!-- predicted: action_book_hotel -->
    - request_hotel   <!-- predicted: reqmore_general -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - select_hotel   <!-- predicted: action_book_hotel -->
    - inform_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: action_book_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4048
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - welcome_general   <!-- predicted: inform_taxi -->
    - bye_general
* bye
    - welcome_general
    - bye_general


## story_PMUL3520
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - action_book_train   <!-- predicted: request_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_booking_restaurant   <!-- predicted: select_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - request_booking_restaurant   <!-- predicted: nobook_booking_restaurant -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - recommend_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform
    - request_booking_restaurant   <!-- predicted: action_book_restaurant -->
* inform
    - reqmore_general   <!-- predicted: action_book_restaurant -->
* bye
    - welcome_general
    - bye_general


## story_MUL0990
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant
    - inform_restaurant   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: greet_general -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction   <!-- predicted: inform_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - welcome_general
    - bye_general


## story_PMUL0615
* inform
    - request_restaurant   <!-- predicted: request_attraction -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
    - greet_general   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - recommend_restaurant   <!-- predicted: request_booking_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_train   <!-- predicted: request_booking_restaurant -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - bye_general   <!-- predicted: action_listen -->


## story_MUL1028
* inform
    - inform_hotel   <!-- predicted: request_attraction -->
    - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_pricerange": "dontcare"}
    - inform_booking_hotel   <!-- predicted: select_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: inform_booking_hotel -->
* inform
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_attraction
* inform
    - inform_attraction
* inform
    - reqmore_general   <!-- predicted: inform_attraction -->
* bye
    - bye_general   <!-- predicted: greet_general -->


## story_PMUL0630
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train
    - greet_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
    - request_restaurant   <!-- predicted: action_listen -->
* inform
    - inform_restaurant   <!-- predicted: request_booking_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_restaurant
    - recommend_restaurant   <!-- predicted: reqmore_general -->
* inform
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform
    - reqmore_general   <!-- predicted: inform_restaurant -->
* bye
    - welcome_general
    - bye_general


## story_MUL0014
* inform{"hotel_area": "specific", "hotel_parking": "dontcare"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_parking": "dontcare"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_stars": "dontcare"}
    - slot{"hotel_pricerange": "specific"}
    - slot{"hotel_stars": "dontcare"}
    - recommend_hotel   <!-- predicted: inform_hotel -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - book_booking_hotel   <!-- predicted: action_listen -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant   <!-- predicted: reqmore_general -->
    - inform_restaurant   <!-- predicted: reqmore_general -->
* inform
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_MUL1657
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
    - request_booking_restaurant   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_SNG01983
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1895
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_leaveAt": "dontcare"}
    - slot{"train_leaveAt": "dontcare"}
    - select_train   <!-- predicted: inform_train -->
    - inform_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0338
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1657
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - offerbooked_train
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_SNG0755
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "dontcare"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - inform_hotel   <!-- predicted: action_book_hotel -->
* inform
    - inform_hotel   <!-- predicted: nobook_booking_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_area": "dontcare"}
    - slot{"hotel_area": "dontcare"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - inform_hotel   <!-- predicted: book_booking_hotel -->
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - bye_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0533
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - greet_general   <!-- predicted: action_listen -->
    - reqmore_general
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - request_train   <!-- predicted: inform_train -->
    - greet_general   <!-- predicted: action_listen -->
* inform
    - inform_train   <!-- predicted: inform_booking_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - reqmore_general   <!-- predicted: inform_train -->
* bye
    - welcome_general
    - bye_general


## story_PMUL1311
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform{"attraction_type": "dontcare"}
    - slot{"attraction_type": "dontcare"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform
    - request_train   <!-- predicted: inform_attraction -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - request_train   <!-- predicted: offerbook_train -->
* bye
    - welcome_general
    - bye_general


## story_PMUL0441
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - request_booking_hotel   <!-- predicted: inform_hotel -->
* inform
    - inform_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant
    - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_PMUL0522
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - offerbook_train   <!-- predicted: inform_train -->
* inform
    - inform_train
    - reqmore_general   <!-- predicted: offerbook_train -->
* inform
    - inform_train
    - greet_general   <!-- predicted: offerbook_train -->
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_PMUL2209
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_restaurant   <!-- predicted: welcome_general -->
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - inform_restaurant
    - request_restaurant
* inform
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_taxi   <!-- predicted: bye_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0828
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - recommend_attraction
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - inform_booking_attraction   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: action_listen -->
* inform
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform
    - inform_attraction   <!-- predicted: inform_booking_restaurant -->
* bye
    - welcome_general
    - bye_general


## story_MUL1278
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_booking_hotel   <!-- predicted: select_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: request_hotel -->
* inform
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_booking_hotel   <!-- predicted: action_listen -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
* inform
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_PMUL1173
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - recommend_attraction   <!-- predicted: inform_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform
    - request_train   <!-- predicted: inform_train -->
* inform
    - select_train   <!-- predicted: inform_train -->
    - inform_train   <!-- predicted: action_listen -->
* inform
    - request_train   <!-- predicted: action_book_train -->
* inform
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1370
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
* inform
    - recommend_attraction   <!-- predicted: inform_attraction -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1122
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - recommend_attraction   <!-- predicted: request_attraction -->
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4462
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - inform_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - action_listen   <!-- predicted: request_booking_restaurant -->
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: greet_general -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
    - action_listen   <!-- predicted: inform_restaurant -->
* inform
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_leaveAt": "specific", "taxi_destination": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"taxi_destination": "specific"}
    - slot{"taxi_leaveAt": "specific"}
    - inform_attraction   <!-- predicted: request_taxi -->
    - request_taxi   <!-- predicted: action_listen -->
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - inform_taxi   <!-- predicted: welcome_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL2155
* inform{"hotel_area": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - request_hotel
* inform
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel   <!-- predicted: recommend_hotel -->
    - action_listen   <!-- predicted: recommend_hotel -->
* inform
    - inform_hotel
* inform{"hotel_name": "specific", "hotel_type": "specific"}
    - slot{"hotel_name": "specific"}
    - slot{"hotel_type": "specific"}
    - request_booking_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: reqmore_general -->
    - offerbook_train
* inform
    - select_train   <!-- predicted: reqmore_general -->
    - inform_train   <!-- predicted: action_listen -->
* inform
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - greet_general   <!-- predicted: welcome_general -->


## story_MUL1254
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - nooffer_restaurant
    - request_restaurant
* inform{"restaurant_food": "dontcare", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "dontcare"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: recommend_restaurant -->
* inform
    - inform_booking_restaurant
    - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - book_booking_hotel   <!-- predicted: inform_hotel -->
    - greet_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - welcome_general   <!-- predicted: action_listen -->
    - bye_general


## story_MUL2089
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - reqmore_general
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel
* inform
    - inform_booking_hotel   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: inform_hotel -->
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train   <!-- predicted: action_book_train -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: bye_general -->


## story_SNG01359
* inform
    - request_taxi   <!-- predicted: request_attraction -->
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
    - welcome_general   <!-- predicted: action_listen -->
* inform{"taxi_leaveAt": "dontcare"}
    - slot{"taxi_leaveAt": "dontcare"}
    - request_taxi
    - welcome_general   <!-- predicted: action_listen -->
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_SNG0095
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general


## story_MUL0498
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: request_attraction -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform{"train_leaveAt": "dontcare"}
    - slot{"train_leaveAt": "dontcare"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - welcome_general
    - reqmore_general   <!-- predicted: bye_general -->


## story_PMUL4106
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
    - reqmore_general
* inform
    - request_train   <!-- predicted: request_attraction -->
    - greet_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1071
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
* inform{"hotel_pricerange": "specific", "attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_attraction   <!-- predicted: inform_hotel -->
    - inform_booking_hotel   <!-- predicted: action_listen -->
    - inform_hotel
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
    - action_listen   <!-- predicted: request_booking_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform
    - bye_general   <!-- predicted: request_attraction -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0578
* inform
    - inform_restaurant   <!-- predicted: request_attraction -->
    - request_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - reqmore_general   <!-- predicted: request_booking_restaurant -->
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform
    - inform_train
    - offerbook_train   <!-- predicted: action_listen -->
* inform
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0197
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "dontcare"}
    - slot{"restaurant_food": "dontcare"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - recommend_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific", "hotel_parking": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_parking": "specific"}
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - greet_general   <!-- predicted: action_listen -->
* inform
    - welcome_general   <!-- predicted: inform_taxi -->
    - reqmore_general   <!-- predicted: bye_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL2146
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: action_listen -->
    - greet_general   <!-- predicted: reqmore_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - greet_general   <!-- predicted: reqmore_general -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - reqmore_general   <!-- predicted: offerbooked_train -->
* bye
    - welcome_general
    - action_listen   <!-- predicted: bye_general -->


## story_MUL1695
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - nooffer_restaurant   <!-- predicted: inform_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - nooffer_restaurant   <!-- predicted: select_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: select_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
    - action_listen   <!-- predicted: request_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG01924
* inform
    - request_taxi   <!-- predicted: request_attraction -->
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* inform
    - reqmore_general   <!-- predicted: inform_taxi -->
* bye
    - bye_general


## story_PMUL3044
* inform
    - request_hotel   <!-- predicted: request_attraction -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_day": "specific", "hotel_parking": "specific", "hotel_type": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: action_book_hotel -->
    - inform_hotel
* inform
    - inform_hotel   <!-- predicted: action_book_hotel -->
* inform
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL2225
* inform{"hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
    - greet_general   <!-- predicted: action_listen -->
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_booking_hotel   <!-- predicted: request_hotel -->
    - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - offerbook_train
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0890
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - nooffer_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - nooffer_restaurant   <!-- predicted: select_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - recommend_restaurant   <!-- predicted: request_booking_restaurant -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - recommend_attraction   <!-- predicted: reqmore_general -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - reqmore_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: bye_general -->


## story_MUL2365
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform{"attraction_type": "dontcare"}
    - slot{"attraction_type": "dontcare"}
    - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - recommend_restaurant   <!-- predicted: nooffer_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - welcome_general   <!-- predicted: request_booking_restaurant -->
    - bye_general   <!-- predicted: action_listen -->
* inform
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1801
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - request_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_hotel   <!-- predicted: greet_general -->
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_booking_hotel
    - recommend_hotel   <!-- predicted: inform_hotel -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - welcome_general   <!-- predicted: inform_attraction -->
    - bye_general   <!-- predicted: reqmore_general -->


## story_MUL1285
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: recommend_restaurant -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: inform_booking_restaurant -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel   <!-- predicted: nobook_booking_hotel -->
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - welcome_general
    - bye_general


## story_MUL2281
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_type": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_hotel
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - nooffer_train   <!-- predicted: inform_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - nooffer_train   <!-- predicted: reqmore_general -->
    - reqmore_general
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - offerbook_train   <!-- predicted: inform_train -->
* inform
    - action_book_train   <!-- predicted: reqmore_general -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0008
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general


## story_PMUL0204
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant
* inform{"restaurant_pricerange": "dontcare"}
    - slot{"restaurant_pricerange": "dontcare"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant
    - inform_restaurant
* inform
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_booking_hotel
    - inform_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_hotel
    - reqmore_general
* inform
    - inform_hotel
    - reqmore_general
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_MUL1935
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_train   <!-- predicted: action_book_train -->
* inform
    - inform_train
    - offerbook_train
* inform
    - inform_attraction   <!-- predicted: action_book_train -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - welcome_general   <!-- predicted: inform_attraction -->
    - bye_general   <!-- predicted: reqmore_general -->


## story_PMUL3734
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - inform_hotel   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_day": "specific", "hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
* inform
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - reqmore_general   <!-- predicted: request_train -->
* inform
    - reqmore_general   <!-- predicted: request_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG02096
* inform{"restaurant_name": "specific", "hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: greet_general -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - action_listen   <!-- predicted: request_booking_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL2427
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform
    - select_attraction   <!-- predicted: recommend_attraction -->
    - action_listen   <!-- predicted: inform_attraction -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_area": "dontcare"}
    - slot{"attraction_area": "dontcare"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant
    - request_restaurant   <!-- predicted: nooffer_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_booking_restaurant   <!-- predicted: select_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_taxi   <!-- predicted: request_attraction -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - request_taxi   <!-- predicted: inform_attraction -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1620
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - reqmore_general   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_booking_restaurant   <!-- predicted: request_booking_restaurant -->
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG0735
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform
    - inform_booking_restaurant   <!-- predicted: recommend_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - request_booking_restaurant   <!-- predicted: inform_booking_restaurant -->
* bye
    - welcome_general   <!-- predicted: bye_general -->
    - bye_general


## story_PMUL1533
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - offerbook_train   <!-- predicted: inform_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: request_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
    - slot{"hotel_parking": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: book_booking_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel   <!-- predicted: book_booking_hotel -->
    - inform_hotel
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0566
* inform
    - inform_restaurant   <!-- predicted: request_attraction -->
    - request_restaurant   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform
    - recommend_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train   <!-- predicted: inform_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general   <!-- predicted: welcome_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL2042
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - offerbook_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: action_listen -->
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - offerbook_train
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - reqmore_general   <!-- predicted: request_hotel -->
* inform
    - inform_booking_hotel   <!-- predicted: request_train -->
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - reqmore_general   <!-- predicted: greet_general -->
* inform
    - inform_hotel   <!-- predicted: request_booking_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - welcome_general
    - bye_general


## story_MUL1289
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_internet": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - inform_hotel   <!-- predicted: request_hotel -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3940
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform{"attraction_type": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - nooffer_attraction   <!-- predicted: inform_attraction -->
    - action_listen   <!-- predicted: request_attraction -->
* inform
    - inform_attraction
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_SNG1105
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - request_attraction
* inform
    - select_attraction   <!-- predicted: inform_attraction -->
    - inform_attraction
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0841
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant
* inform{"restaurant_food": "specific", "attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_booking_restaurant   <!-- predicted: inform_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform
    - inform_restaurant   <!-- predicted: select_restaurant -->
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - request_taxi   <!-- predicted: select_attraction -->
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction   <!-- predicted: select_attraction -->
    - action_listen   <!-- predicted: recommend_attraction -->
* bye
    - welcome_general
    - bye_general


## story_MUL1607
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: request_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "dontcare"}
    - slot{"restaurant_food": "dontcare"}
    - recommend_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4259
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - reqmore_general   <!-- predicted: request_restaurant -->
* inform{"restaurant_food": "dontcare", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "dontcare"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - request_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"train_destination": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train
    - offerbook_train
    - action_listen   <!-- predicted: request_train -->
* inform
    - offerbook_train   <!-- predicted: action_book_train -->
    - reqmore_general   <!-- predicted: request_train -->
* inform
    - bye_general   <!-- predicted: inform_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL1809
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - request_hotel
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - recommend_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL2433
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - select_attraction   <!-- predicted: request_attraction -->
    - inform_attraction
    - action_listen   <!-- predicted: request_attraction -->
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant
    - request_restaurant
* inform{"restaurant_food": "dontcare"}
    - slot{"restaurant_food": "dontcare"}
    - request_booking_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
* bye
    - welcome_general
    - reqmore_general   <!-- predicted: bye_general -->
    - bye_general


## story_MUL2567
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific", "hotel_type": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_stars": "dontcare", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_stars": "dontcare"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - inform_hotel
    - request_hotel   <!-- predicted: action_listen -->
* inform
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel   <!-- predicted: recommend_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: action_book_hotel -->
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi   <!-- predicted: action_book_taxi -->
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL4842
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - inform_restaurant   <!-- predicted: nooffer_restaurant -->
    - action_listen   <!-- predicted: request_restaurant -->
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - recommend_restaurant   <!-- predicted: inform_booking_restaurant -->
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
    - slot{"restaurant_day": "specific"}
    - slot{"restaurant_name": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: reqmore_general -->
* inform
    - reqmore_general   <!-- predicted: welcome_general -->
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_type": "specific"}
    - inform_hotel
    - request_hotel   <!-- predicted: action_listen -->
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific"}
    - slot{"hotel_area": "dontcare"}
    - slot{"hotel_pricerange": "specific"}
    - nooffer_hotel   <!-- predicted: recommend_hotel -->
* inform{"hotel_pricerange": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - request_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - recommend_hotel   <!-- predicted: nooffer_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - select_hotel   <!-- predicted: inform_booking_hotel -->
    - inform_hotel
* inform
    - reqmore_general   <!-- predicted: request_booking_taxi -->
* bye
    - welcome_general
    - bye_general


## story_SNG1075
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction   <!-- predicted: request_attraction -->
    - request_attraction
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - action_listen   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - action_listen   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction   <!-- predicted: recommend_attraction -->
    - reqmore_general   <!-- predicted: recommend_attraction -->
* bye
    - bye_general


## story_SNG01332
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - request_taxi
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - reqmore_general   <!-- predicted: action_listen -->
* inform
    - reqmore_general   <!-- predicted: greet_general -->
* bye
    - bye_general


## story_SNG0055
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform{"taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL2060
* inform{"train_destination": "specific", "train_day": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_destination": "specific"}
    - request_train
* inform{"train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - offerbook_train
* inform{"hotel_parking": "dontcare", "hotel_pricerange": "specific"}
    - slot{"hotel_parking": "dontcare"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel   <!-- predicted: request_hotel -->
    - request_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_booking_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_booking_hotel
    - request_booking_hotel   <!-- predicted: inform_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform{"hotel_parking": "specific"}
    - slot{"hotel_parking": "specific"}
    - select_hotel   <!-- predicted: action_book_hotel -->
    - inform_hotel   <!-- predicted: action_listen -->
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_name": "specific"}
    - nobook_booking_hotel   <!-- predicted: action_book_hotel -->
    - request_booking_hotel
* inform
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL0117
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_pricerange": "specific"}
    - inform_hotel
* inform
    - inform_hotel   <!-- predicted: request_booking_hotel -->
    - action_listen   <!-- predicted: request_hotel -->
* inform{"hotel_day": "specific", "hotel_name": "specific", "hotel_area": "specific", "hotel_parking": "specific"}
    - slot{"hotel_area": "specific"}
    - slot{"hotel_day": "specific"}
    - slot{"hotel_name": "specific"}
    - slot{"hotel_parking": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - request_attraction   <!-- predicted: recommend_attraction -->
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - slot{"restaurant_food": "specific"}
    - nooffer_restaurant
    - request_restaurant
* inform
    - nooffer_restaurant   <!-- predicted: inform_restaurant -->
    - request_restaurant
* inform{"restaurant_food": "specific"}
    - slot{"restaurant_food": "specific"}
    - select_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant
* inform
    - inform_restaurant   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
* inform
    - action_book_taxi
    - slot{"taxi_type": "specific"}
    - inform_taxi
* bye
    - welcome_general
    - bye_general


## story_SNG1078
* inform{"attraction_name": "specific"}
    - slot{"attraction_name": "specific"}
    - inform_attraction
* inform
    - inform_attraction
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL1606
* inform{"restaurant_name": "specific"}
    - slot{"restaurant_name": "specific"}
    - inform_restaurant   <!-- predicted: inform_booking_restaurant -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - action_listen   <!-- predicted: greet_general -->
* inform{"train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - offerbook_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - inform_train   <!-- predicted: offerbooked_train -->
    - action_listen   <!-- predicted: offerbooked_train -->
* bye
    - welcome_general
    - bye_general


## story_PMUL3301
* inform{"hotel_area": "specific"}
    - slot{"hotel_area": "specific"}
    - inform_hotel   <!-- predicted: select_hotel -->
    - recommend_hotel   <!-- predicted: request_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - request_booking_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_name": "specific"}
    - slot{"hotel_name": "specific"}
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"hotel_day": "specific"}
    - slot{"hotel_day": "specific"}
    - action_book_hotel
    - slot{"hotel_name": "specific"}
    - slot{"hotel_reference": "specific"}
    - book_booking_hotel
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - inform_train   <!-- predicted: action_book_train -->
    - action_listen   <!-- predicted: offerbook_train -->
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_MUL0682
* inform
    - reqmore_general   <!-- predicted: request_attraction -->
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
    - slot{"hotel_internet": "specific"}
    - slot{"hotel_type": "specific"}
    - select_hotel   <!-- predicted: inform_hotel -->
    - inform_hotel
* inform
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform
    - inform_hotel   <!-- predicted: inform_booking_hotel -->
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train
    - action_listen   <!-- predicted: offerbook_train -->
* inform
    - action_book_train   <!-- predicted: inform_train -->
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
* bye
    - bye_general   <!-- predicted: welcome_general -->


## story_PMUL2146
* inform{"restaurant_area": "specific"}
    - slot{"restaurant_area": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_food": "specific", "restaurant_pricerange": "dontcare"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "dontcare"}
    - inform_booking_restaurant   <!-- predicted: nooffer_restaurant -->
    - inform_restaurant   <!-- predicted: recommend_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - action_book_restaurant   <!-- predicted: nobook_booking_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general
* inform{"attraction_type": "specific"}
    - slot{"attraction_type": "specific"}
    - inform_attraction
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"attraction_area": "specific"}
    - slot{"attraction_area": "specific"}
    - inform_attraction
    - action_listen   <!-- predicted: recommend_attraction -->
* inform
    - inform_attraction
    - reqmore_general
* inform
    - inform_attraction   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: reqmore_general -->
* inform{"taxi_destination": "specific"}
    - slot{"taxi_destination": "specific"}
    - request_taxi
    - action_listen   <!-- predicted: greet_general -->
* inform
    - request_taxi   <!-- predicted: action_book_taxi -->
    - action_listen   <!-- predicted: greet_general -->
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
    - slot{"taxi_departure": "specific"}
    - slot{"taxi_destination": "specific"}
    - slot{"train_day": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - action_book_taxi   <!-- predicted: offerbook_train -->
    - slot{"taxi_type": "specific"}
    - inform_taxi
    - action_listen   <!-- predicted: reqmore_general -->
* bye
    - reqmore_general   <!-- predicted: welcome_general -->


## story_MUL1697
* inform{"train_destination": "specific", "train_departure": "specific"}
    - slot{"train_departure": "specific"}
    - slot{"train_destination": "specific"}
    - inform_train   <!-- predicted: request_train -->
    - request_train
* inform{"train_day": "specific"}
    - slot{"train_day": "specific"}
    - select_train   <!-- predicted: inform_train -->
    - inform_train
* inform
    - action_book_train
    - slot{"train_trainID": "specific"}
    - slot{"train_reference": "specific"}
    - offerbooked_train
    - reqmore_general   <!-- predicted: action_listen -->
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
    - slot{"restaurant_food": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - request_restaurant   <!-- predicted: inform_restaurant -->
* inform{"restaurant_day": "specific"}
    - slot{"restaurant_day": "specific"}
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - reqmore_general   <!-- predicted: action_book_restaurant -->
* inform
    - nobook_booking_restaurant
    - request_restaurant   <!-- predicted: request_booking_restaurant -->
* inform
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform
    - nobook_booking_restaurant   <!-- predicted: action_book_restaurant -->
    - request_booking_restaurant
* inform{"restaurant_pricerange": "specific"}
    - slot{"restaurant_pricerange": "specific"}
    - action_book_restaurant   <!-- predicted: inform_restaurant -->
    - slot{"restaurant_name": "specific"}
    - slot{"restaurant_reference": "specific"}
    - book_booking_restaurant
    - reqmore_general   <!-- predicted: action_listen -->
* bye
    - greet_general   <!-- predicted: welcome_general -->
    - action_listen   <!-- predicted: welcome_general -->



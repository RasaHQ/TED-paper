
import re


class SlotParser:

    def __init__(self, simplify=1):
        self.simplify = simplify

    def value_valid(self, value):
        if self.simplify > 0:
            value = value.lower().strip()
            regex = re.compile('[^a-zA-Z ]')
            value = regex.sub(repl="", string=value)
        return value not in ["not mentioned", "", "none"]

    def value_simplify(self, slot: str, value: str):
        if self.simplify > 0:
            value = value.lower().strip()
            regex = re.compile('[^a-zA-Z]')
            value = regex.sub(repl="", string=value)
        if self.simplify == 2:
            if slot not in [
                # "attraction_area",
                "restaurant_area",
                "hotel_area",
                "attraction_type",
                # "hotel_internet",
                # "hotel_day",
                # "restaurant_day",
                "train_day",
                "hotel_parking",
                "hotel_pricerange",
                "hotel_stars",
                "restaurant_pricerange",
                "hotel_type",
                "hotel_parking",
                "hotel_internet",
                # "hotel_people",
                # "train_people",
                # "restaurant_people",
            ]:
                value = "specific" if value != "dontcare" else "dontcare"
        elif self.simplify == 3:
            value = "specific" if value != "dontcare" else "dontcare"
        elif self.simplify == 4:
            value = "specific"
        return value


# Shortest category lengths
#
# bus_departure: 1
# bus_leaveAt: 1
# bus_day: 1
# hotel_parking: 4
# hotel_internet: 4
# bus_destination: 4
# hotel_type: 5
# restaurant_pricerange: 5
# hotel_area: 7
# attraction_area: 7
# restaurant_area: 7
# hotel_pricerange: 8
# hotel_people: 8
# train_day: 8
# hospital_reference: 8
# hospital_time: 8
# hotel_stars: 9
# restaurant_people: 9

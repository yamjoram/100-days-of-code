capital = {
    "Tamil Nadu" : "Chennai",
    "Karnataka" : "Bangaluru"
}

Travel_log ={
    "cities" : ["Salem", "Coimbatore", "Erode"],
     "cities" : ["Whitefield", "Ramagondanalli", "Marathalli"]

}
Travel_log = [

    {
        "state" : "Tamil Nadu",
        "visits" : 5,
        "cities" : ["Salem", "Coimbatore", "Erode"]
    },
    {
        "state" : "Karnataka",
        "visits" : 3,
        "cities" : ["Whitefield", "Ramagondanalli", "Marathalli"]
    }
]

def add_new_state(state_visited, time_visited, cities_visited):
    new_state = {}
    new_state["state"] = state_visited
    new_state["visits"] = time_visited
    new_state["cities"] = cities_visited
    Travel_log.append(new_state)


add_new_state("Arunachal", "100", ["Itamagar", "Naharlagun"])
print(Travel_log)



































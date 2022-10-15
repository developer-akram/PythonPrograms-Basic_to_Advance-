# def names(a, b, c, d):
#     print(a, b, c, d)
# names("Akram","Khan","King","Fisher")

def name_lists(cities, *nama, **hd_name) :
    print(local)
    for item in nama :
        print(item)
    print(cities)
    for key, value in hd_name.items() :
        print(key,"\t\t\t" ,value)
sd_name = ["Dhoom", "Don","Big BOSS", "RaOne","Sing is King","Stree"]
hd_name = {"Kolkata":"Wset Bengal", "Malda" : "Enlish BAZAR", "Dinajpur" : "Balurghat"
            ,"Murshidabad":"Berhampore","Nadia":"Krishnanagar"}
local = "Movie names list :"
cities = "\nCity Names :"
name_lists(cities, *sd_name, **hd_name)

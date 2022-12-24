from geopy.geocoders import Nominatim
 
# calling the nominatim tool
geoLoc = Nominatim(user_agent="GetLoc")
 
# passing the coordinates
la = -6.2959704
lo = 106.685136
locname = geoLoc.reverse(str(la)+","+str(lo))
 
# printing the address/location name

print(locname.address.rsplit(", ")[0])

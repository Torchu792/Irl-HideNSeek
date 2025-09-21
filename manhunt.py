from random import randrange
import simplekml
from geopy.distance import distance
from geopy.point import Point
from polycircles import polycircles
# 50.4153294N, 14.9079847E
offset = 50
radius = 200 + offset
lat, lon = 50.0797717, 14.4297200

def move_point(latf, lonf, meters, angle):
    new_location = distance(meters=meters).destination(Point(latf, lonf), angle)
    return new_location.latitude, new_location.longitude


########
kml = simplekml.Kml()

for x in range(0, 5):
    polycircle = polycircles.Polycircle(latitude=lat,
                                        longitude=lon,
                                        radius=radius,
                                        number_of_vertices=36)
    rng = randrange(0, 361)
    print(rng)
    lat, lon = move_point( lat, lon , offset, rng)

    pol = kml.newpolygon(name=f"{x}",outerboundaryis=polycircle.to_kml())
    pol.style.polystyle.color = simplekml.Color.changealphaint(10, simplekml.Color.green)
    # pol.style.
    radius -= offset


kml.save("prha2.kml")
import simplekml
from polycircles import polycircles
kml = simplekml.Kml()

lat, lon = 50.0797717, 14.4297200 # Stred kruhu
circles = [10, 6, 4, 2, 1] # Kruhy v km

for kilometers_radius in circles:
    polycircle = polycircles.Polycircle(latitude=lat, longitude=lon, radius=kilometers_radius/2 * 1000, number_of_vertices=36)

    pol = kml.newpolygon(name=f"{kilometers_radius}",outerboundaryis=polycircle.to_kml())
    pol.style.polystyle.color = simplekml.Color.changealphaint(30, simplekml.Color.green)

kml.save("Prg2025v1.kml")
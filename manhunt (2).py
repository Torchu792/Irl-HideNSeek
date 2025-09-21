import simplekml
# from geopy.distance import distance
# from geopy.point import Point

center = (50.08804, 14.42076)
radius = 20
circle_coords = simplekml.Shape.circle(center, radius)

# Create a KML object and add a polygon for the circle
kml = simplekml.Kml()
circle = kml.newpolygon(name="Circle", outerboundaryis=circle_coords)
circle.style.polystyle.color = simplekml.Color.changealpha('80', simplekml.Color.blue)  # semi-transparent blue

# Save the KML file
kml.save("circle.kml")
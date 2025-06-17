import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets 

# Load the world map dataset
world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

world.plot( edgecolor='orange')
plt.title('World Map')
plt.show()


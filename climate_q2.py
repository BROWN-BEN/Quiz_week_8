import matplotlib.pyplot as plt
import pandas as pd

years = list(cur.execute("SELECT year FROM ClimateData"))
co2 = list(cur.execute("SELECT CO2 FROM ClimateData"))
temp = list(cur.execute("SELECT temperature FROM ClimateData"))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 


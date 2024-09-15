# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts latitude, longitude, and height above ellipsoid to position in ECEF coordinates (rx,ry,rz) in km
# Parameters:
#  lat_deg: latitude in degrees
#  lon_deg: longitude in degrees
#  hae_km: height above ellipsoid in km
#  ...
# Output:
#  Print the ECEF coordinates (rx,ry,rz) in km
#
# Written by Erika Ashley
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456
# helper functions

## calc_denom
##
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-ecc**2.0*math.sin(lat_rad)**2.0)
## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
lat_deg=float('nan') # latitude in degrees
lon_deg=float('nan') # longitude in degrees
hae_km=float('nan') #height above ellipsoid in km
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
if len(sys.argv)==4:
    lat_deg=float(sys.argv[1])
    lon_deg=float(sys.argv[2])
    hae_km=float(sys.argv[3])
else:
   print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
   exit()

# write script below this line
lat_rad=lat_deg*math.pi/180.0
lon_rad=lon_deg*math.pi/180.0
denom=calc_denom(E_E,lat_rad)
c_E=R_E_KM/denom
s_E=R_E_KM*(1.0-E_E*E_E)/denom
r_x_km=(c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km=(c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km=(s_E+hae_km)*math.sin(lat_rad)
print('r_x_km:  '+str(r_x_km))
print('r_y_km:  '+str(r_y_km))
print('r_z_km:  '+str(r_z_km))

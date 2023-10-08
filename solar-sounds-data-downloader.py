import sunpy
import os
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time
from astropy.visualization import ImageNormalize, SqrtStretch
import sunpy.coordinates  # NOQA
import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a

#you need to register your email with jsoc in order to download things yourself
#this can be done at the following url http://jsoc.stanford.edu/ajax/lookdata.html
jsoc_email = ["your registered email here"]

#select the start time for the event you want to look at
#if you are planning to sonify a particular event
start_time = Time('2023-09-30T12:00:00', scale='utc', format='isot')

#wavelengths of interest 171 and 304
#the query looks 6hrs previous to start time to find evolution of the event
query = Fido.search(
    a.Time(start_time - 6*u.h, start_time + 6*u.h),
    a.Wavelength(304*u.angstrom),
    a.Sample(1*u.h),
    a.jsoc.Series.aia_lev1_euv_12s,
    a.jsoc.Notify(jsoc_email),
    a.jsoc.Segment.image,
)
print(query)

files = Fido.fetch(query)
files.sort()

#put the images into a sunpy map in order to plot them sequentially as a movie
sequence = sunpy.map.Map(files, sequence=True)

#plot the images using matplotlib
#this commented code returns a little movie of the images you have downloaded
'''fig = plt.figure()
ax = fig.add_subplot(projection=sequence.maps[0])
ani = sequence.plot(axes=ax, norm=ImageNormalize(vmin=0, vmax=5e3, stretch=SqrtStretch()))

plt.show()'''

#this makes them into a list of individual sunpy maps
static_files = sunpy.map.Map(files)

#this selects the first file
smap = static_files[0]

'''figure = plt.figure(frameon=False)
ax2 = plt.axes([0, 0, 1, 1])
# Disable the axis
ax2.set_axis_off()

# Plot the map.
norm = smap.plot_settings['norm']
norm.vmin, norm.vmax = np.percentile(smap.data, [1, 99.9])
ax2.imshow(smap.data,
          norm=norm,
          cmap=smap.plot_settings['cmap'],
          origin="lower")

#plt.show()
plt.savefig("smap0.png")'''

len(static_files)
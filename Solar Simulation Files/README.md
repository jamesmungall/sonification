SOLAR SIMULATION, Benjy


References:
https://www.solarsystemscope.com

https://assetstore.unity.com/packages/2d/textures-materials/milky-way-skybox-94001

https://nssdc.gsfc.nasa.gov/planetary/factsheet/

-----------------------------------------------------------------------------------------------------

These scripts are the main c # scripts controlling the Unity 3D simulation:

camera.cs is the script that moves the camera through the solar system and changes the time scale.

planet_generator.cs is the script that instantiates the planet prefabs 8 times for 8 planets.

planet.cs is the script that calculates its position using the parameters orbit_time, orbit_distance and diameter from nasa planetary data. This script also adds the correct material to the object, plays the correct audio source and creates a trail behind it. 

Scaled : 𝑥 seconds = 1 earth year | 1 m = diameter of earth | 5m = earth’s orbital distance | Sun not to scale
Trail distance is proportional to planet’s diameter
Audio volume is proportional to planet’s diameter
Audio clip is scaled to play clip twice per orbit

Credit to https://astromattrusso.gumroad.com and Matt Russo for a lot of this code. 
## SUN SONG CREATION:  

The CSV read in represents the pixels in the grayscale image (ranging from 0 to 255).   
  
**app.py**  
This code takes the whole histogram intensity CSV and takes the average frequency of 5 intensity levels (0-5, 6-10 and so on until 256) and then maps each average to notes in the lydian C scale. The file can then be put into Logic or any other DAW.  
*The example mp3 is 'sunsong.mp3' and mid file is sunsong.mid*  

**apptwo.py**  
This piece of code takes the top 68 most frequent intensity and places them in a C scale with varying markers to define the pitch, the velocity, the timing and the length of the note.  
The idea is that we would work down the intensity levels handling a section of the histogram at a time to build a more unique piece of music.   
   
Pitch is determined by the frequency.  
Timing/ when the note occurs is determined by the difference between one frequency, and the frequency after it in a sorted list
Length of note is determined by the difference between one frequency and the frequency following it in an unsorted list (i.e. pixel intensity 0 - pixel intensity 1).  
The idea is that the music some how represents the distribution of light and dark patches in a sun image.   
   
  
The files can then be put into Logic or any other DAW and assigned to which ever instrument is thought to be a good representation of that pixel intensity (i.e. dark spots played by the bassoon, lighter colours played by the violin).  
*The example mp3 is 'sunsong2.mp3' and the midi files for this are 'section_one.mid' and 'section_two.mid'.*  

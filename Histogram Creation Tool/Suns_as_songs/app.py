import pandas as pd
import matplotlib.pylab as plt
from midiutil import MIDIFile
import numpy as np
from audiolazy import str2midi
import math
#  import csv 
df = pd.read_csv('data.csv', names=['Pixel Value', 'Frequency'])
filename = "nasa_stuff"

def get_top_two_values(df):
    df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce')
    df['Pixel Value'] = pd.to_numeric(df['Pixel Value'], errors='coerce')
    column_name = 'Frequency'
    filtered_values = df.loc[df[column_name] >= 10, column_name]
    value_counts = filtered_values.value_counts()
    sorted_counts = value_counts.sort_values(ascending=False)
    top_two_values = sorted_counts.head(2)
    return top_two_values.axes[0][0] - top_two_values.axes[0][1]

def mapper_value(df):
    result_array = []
    for i in range(0, len(df), 5):
        group = df.iloc[i:i+5]

        # group_range = group[frequency_column].max() - group[frequency_column].min()
        group_range = group['Frequency'].mean()
    
        result_array.append(group_range)
    return result_array

def time_mapper(df):
        result_array = []
        for i in range(0, len(df), 5):
            group = df.iloc[i:i+5]
            group_range = group['Frequency'].max() - group['Frequency'].min()
          
            
            result_array.append(group_range)
        return result_array



def map_value(array, min_value, max_value, min_result, max_result):
    '''maps values (or array of values) from one range to another'''
    
    result = []

    for value in array:
        mapped_value = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result)
        result.append(int(mapped_value))

    return result



notes_array = [
    "C1","C1", "D1", "E1", "F#1", "G1", "A1", "B1", "C2", "D2", "E2", "F#2", "G2", "A2", "B2",
    "C3", "D3", "E3", "F#3", "G3", "A3", "B3", "C4", "D4", "E4", "F#4", "G4", "A4", "B4", "C5", "D5",
    "E5", "F#5", "G5", "A5", "B5", "C6", "D6", "E6", "F#6", "G6", "A6", "B6", "C7", "D7", "E7", "F#7", 
    "G7", "A7", "B7", "C8", "C8"
]
  

range_for_time = get_top_two_values(df)


mapped_values = mapper_value(df)
time_mapped = time_mapper(df)
mapped_velocities = map_value(mapped_values,  df['Frequency'].min(),df['Frequency'].max(), 30, 137)


time_mapped_correct = map_value(time_mapped, min(time_mapped), max(time_mapped), 1, 50 )
note_midis = [str2midi(n) for n in notes_array]
my_midi_file = MIDIFile(1) #one track 
my_midi_file.addTempo(track=0, time=0, tempo=60) 


for i in range(len(notes_array)):
    my_midi_file.addNote(track=0, channel=0, pitch=note_midis[i], time=time_mapped_correct[i], duration=(time_mapped_correct[i]/2), volume=mapped_velocities[i])


with open(filename + '.mid', "wb") as f:
    my_midi_file.writeFile(f) 

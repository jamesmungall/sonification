import pandas as pd
import matplotlib.pylab as plt
from midiutil import MIDIFile
import numpy as np
from audiolazy import str2midi
import math


#  get histogram 
df = pd.read_csv('data.csv', names=['Pixel Value', 'Frequency'])
df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce').fillna(1)
df['Pixel Value'] = pd.to_numeric(df['Pixel Value'], errors='coerce').fillna(1)
df['Difference'] = df['Frequency'].diff()

# Replace the NaN in the first row with 0
df['Difference'] = df['Difference'].fillna(0)
df['Difference'] = df['Difference'].abs()
df = df[(df != 0).all(1)]


def get_top_68(df):
    sorted_df = df.sort_values(by='Frequency', ascending=False)

    # Take the top 50 rows from the sorted DataFrame
    return sorted_df.head(68)
    

def get_top_18(df):
    sorted_df = df.sort_values(by='Pixel Value', ascending=False)

    return sorted_df.head(18)

def get_next_50(df):
    sorted_df = df.sort_values(by='Pixel Value', ascending=False)

    # Take the top 50 rows from the sorted DataFrame
    return sorted_df.iloc[18:68]

def map_value(array, min_value, max_value, min_result, max_result):
    '''maps values (or array of values) from one range to another'''
    
    result = []

    for value in array:
        mapped_value = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result)
        result.append(int(mapped_value))

    return result



def get_note_length(array):
    result_array = []
    for i in range(len(array)-1):
        result_array.append(i+1 - i)

def map_value(array, min_value, max_value, min_result, max_result):
    '''maps values (or array of values) from one range to another'''
    result = []
    for value in array:
    
        mapped_value = min_result + (value - min_value)/(max_value - min_value)*(max_result - min_result)
        result.append(mapped_value)

    return result

def get_timings(array):
    result_array = []

    for i in range(len(array) - 1):
        num = array.iloc[i + 1] - array.iloc[i]

        result_array.append(abs(num))
    result_array.append(result_array[-1])
    return result_array


def create_midi(filename, array, note_midi, time, duration, velocity):

    my_midi_file = MIDIFile(1)  # one track
    my_midi_file.addTempo(track=0, time=0, tempo=60)

    velocity = [int(v) for v in velocity]

    for i in range(len(array)):
        my_midi_file.addNote(track=0, channel=0, pitch=note_midi[array[i]], time=time[i], duration=duration[i],
                             volume=velocity[i])

    with open(filename + '.mid', "wb") as f:
        my_midi_file.writeFile(f)


section_one_note_array =["C7", "F7",  "G7"," A7", "C7", "D7", "F8",  "G8"," A8"]
section_two_note_array =[ "C4", "D4", "F4",  "G4"," A5","C5", "D5", "F5",  "G5"," A6",
                 "C6", "D6", "F6",  "G6"," A6","C6", "D6", "F6",  "G6"," A7",
                 "C7", "E7", "G7", "A8", "C8"]

top_18_high_frequencies = get_top_18(df)
fifty_high_frequencies = get_next_50(df)


section_one_velocity = map_value(top_18_high_frequencies['Frequency'], top_18_high_frequencies['Frequency'].min(), top_18_high_frequencies['Frequency'].max(), 35, 120)
section_one_velocity_int = [int(x)for x in section_one_velocity]
section_two_velocity = map_value(fifty_high_frequencies['Frequency'], fifty_high_frequencies['Frequency'].min(), fifty_high_frequencies['Frequency'].max(), 35, 120)
section_one_length = map_value(top_18_high_frequencies['Difference'], top_18_high_frequencies['Difference'].min(), top_18_high_frequencies['Difference'].max(), 1, 5)
section_one_length_int = [int(x) for x in section_one_length]
section_two_length = map_value(fifty_high_frequencies['Difference'],  fifty_high_frequencies['Difference'].min(), fifty_high_frequencies['Difference'].max(), 1, 5)
section_two_length_int = [int(x) for x in section_two_length]
section_one_timing = get_timings(top_18_high_frequencies['Frequency'])
section_two_timing = get_timings(fifty_high_frequencies['Frequency'])
section_one_map_timing = map_value(section_one_timing, min(section_one_timing), max(section_one_timing), 1, 50 )
section_one_map_timing_int = [int(x) for x in section_one_map_timing]
section_two_map_timing = map_value(section_two_timing, min(section_two_timing), max(section_two_timing), 1, 50 )
section_two_map_timing_int = [int(x) for x in section_two_map_timing]
note_section_one = map_value(top_18_high_frequencies['Frequency'],min(top_18_high_frequencies['Frequency']), max(top_18_high_frequencies['Frequency']), 0, 8) 
note_section_one_ints = [int(x) for x in note_section_one]
note_section_two = map_value(fifty_high_frequencies['Frequency'], min(fifty_high_frequencies['Frequency']), max(fifty_high_frequencies['Frequency']), 0, 24)
note_section_two_ints = [int(x) for x in note_section_two]
section_one_note_midis = [str2midi(n) for n in section_one_note_array]
section_two_note_midis = [str2midi(n) for n in section_two_note_array]
create_midi('section one', note_section_one_ints, section_one_note_midis, section_one_map_timing_int, section_one_length_int, section_one_velocity) 
create_midi('section two', note_section_two_ints, section_two_note_midis, section_two_map_timing_int, section_two_length_int, section_two_velocity) 

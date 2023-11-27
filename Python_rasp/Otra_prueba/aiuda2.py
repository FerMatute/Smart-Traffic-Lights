import serial
import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate
import time  # Import the time module

num_microphones = 1  # Adjust based on your setup
buffer_size = 512

timestamps = [0] * num_microphones
microphone_data = [[0] * buffer_size for _ in range(num_microphones)]

# We have to change the port of connection
# For the rasp it's written like '/dev/ttyUSB0'
ser = serial.Serial('COM11', 9600)  # Adjust serial port and baud rate

# Load the recorded ambulance sound sample from a WAV file
# We need to change it based on the name and place were the wave is located
# Important, the sample_rate should be the same as the one of the recordings
# made by the arduino
sample_rate, ambulance_sample = wavfile.read('ambulance_sample.wav')

def calculate_time_differences():
    # Calculate time differences based on timestamps
    time_differences = [timestamps[i] - timestamps[0] for i in range(1, num_microphones)]
    return time_differences

def compare_with_ambulance_sound(sound_data):
    # Placeholder: Cross-correlation with the recorded ambulance sound sample
    correlation = correlate(sound_data, ambulance_sample, mode='same')
    similarity_score = np.max(correlation)
    return similarity_score

while True:
    # Read timestamped sound data from Arduino
    data = ser.readline().decode('utf-8').strip().split(',')
    
    mic_index = int(data[0])
    timestamps[mic_index] = int(data[1])
    microphone_data[mic_index] = [float(x) for x in data[2:]]

    # Calculate time differences and perform real-time comparison
    time_differences = calculate_time_differences()

    # Compare with the recorded ambulance sound sample
    similarity_score = compare_with_ambulance_sound(microphone_data[0])

    # Output or trigger alert based on similarity score
    print(f"Similarity Score: {similarity_score}")
    
    time.sleep(0.1)  # Adjust the sleep duration based on your requirements

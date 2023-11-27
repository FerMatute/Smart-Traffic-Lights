const int microphonePin = A0;  // Analog input pin for the microphone
const int sampleRate = 4000;   // Sampling rate in Hz
const int adcResolution = 10;  // ADC resolution (bits), adjust based on your Arduino
const float referenceVoltage = 5.0;  // Reference voltage of the ADC, adjust based on your setup
const int baudRate = 9600;     // Serial communication baud rate

void setup() {
  Serial.begin(baudRate);  // Initialize serial communication
}

void loop() {
  unsigned long currentTime = micros();
  static unsigned long previousTime = 0;
  
  // Sample the audio signal at a specified rate
  if (currentTime - previousTime >= 1000000 / sampleRate) {
    int audioValue = analogRead(microphonePin); // Read analog value from the microphone
    float amplitude = audioValue; //* 100 / 1024;
    
    // Convert ADC value to sound amplitude
    //float amplitude = (float(audioValue) / pow(2, adcResolution - 1)) * referenceVoltage;
    
    // Send the amplitude data to Raspberry Pi
    Serial.println(audioValue);
    
    previousTime = currentTime;  // Update the previous time
  }
}

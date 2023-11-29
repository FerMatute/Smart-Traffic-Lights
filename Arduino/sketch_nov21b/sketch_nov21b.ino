const int microphonePin = A0;  // Analog input pin for the microphone
const int sampleRate = 4000;   // Sampling rate in Hz
const int adcResolution = 10;  // ADC resolution (bits), adjust based on your Arduino
const float referenceVoltage = 5.0;  // Reference voltage of the ADC, adjust based on your setup
const int baudRate = 115200;     // Serial communication baud rate

void setup() {
  Serial.begin(baudRate);  // Initialize serial communication
}

void loop() {
  unsigned long currentTime = micros();
  static unsigned long previousTime = 0;
  
  // Sample the audio signal at a specified rate
  if (currentTime - previousTime >= 1000000 / sampleRate) {
    int sensorValue = analogRead(microphonePin);
    float voltage = sensorValue * (5.0 / 1023.0);
    Serial.println(voltage, 4); // Print voltage with 4 decimal places
    
    previousTime = currentTime;  // Update the previous time
  }
}

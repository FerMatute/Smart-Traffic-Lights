const int numMicrophones = 1;  // Adjust based on your setup
const int sampleRate = 4000;   // Adjust based on your microphone specifications
const int bufferSize = 512;    // Adjust based on your requirements

unsigned long timestamps[numMicrophones];
float microphoneData[numMicrophones][bufferSize];

void setup() {
  Serial.begin(9600);
  // Initialize your microphone and set up communication (if necessary)
}

void loop() {
  // Capture sound data
  captureSoundData(0);  // Assuming one microphone

  // Send timestamped sound data to the Raspberry Pi
  sendDataToRaspberryPi();

  // If we don't need delay, we erase it
  delay(10);  // Adjust delay based on your requirements
}

void captureSoundData(int micIndex) {
  // Implement sound data capture for the specified microphone
  // You may need to use external libraries or hardware for microphone interfacing
  // Example: Read analog signal from a microphone sensor
  // microphoneData[micIndex][0] = analogRead(micPin);

  // Placeholder: Use a simple sine wave for demonstration
  float frequency = 1000;  // Adjust frequency based on your requirements
  float amplitude = 100.0; // Adjust amplitude based on your requirements
  for (int i = 0; i < bufferSize; i++) {
    float t = (float)i / sampleRate;
    microphoneData[micIndex][i] = amplitude * sin(2 * PI * frequency * t);
  }
}

void sendDataToRaspberryPi() {
  // Send timestamped sound data to Raspberry Pi over serial communication
  for (int i = 0; i < numMicrophones; i++) {
    Serial.print(i);
    Serial.print(",");
    Serial.print(millis());  // Use millis() for timestamps
    Serial.print(",");
    
    // Send raw data
    for (int j = 0; j < bufferSize; j++) {
      Serial.print(microphoneData[i][j], 6);  // 6 decimal places for float
      if (j < bufferSize - 1) {
        Serial.print(",");
      }
    }
    Serial.println();
  }
}

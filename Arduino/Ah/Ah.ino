void setup() {
  Serial.begin(115200);  // Adjust baud rate as needed
}

void loop() {
  // Read analog value from pin A0 using direct port manipulation
  int sensorValue = analogRead(A0);

  // Send data via Serial
  Serial.print("A");
  Serial.println(sensorValue);

  int sensorValue2 = analogRead(A1);

  // Send data via Serial
  Serial.print("B");
  Serial.println(sensorValue2);

  int sensorValue3 = analogRead(A2);

  // Send data via Serial
  Serial.print("C");
  Serial.println(sensorValue3);

  int sensorValue4 = analogRead(A3);

  // Send data via Serial
  Serial.print("D");
  Serial.println(sensorValue4);
}

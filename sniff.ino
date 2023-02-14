void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char character = Serial.read();
    Serial.println(character);
    delay(10); // Add a small delay to avoid overwhelming the serial monitor
  }
}
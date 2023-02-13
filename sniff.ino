String character;

void setup(){
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available()) {
  character = Serial.readString();
  Serial.println((String)character);
}
}
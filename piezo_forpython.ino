int sensorPin = 2;
int buzzPin = 3;
int freq = 500;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
  pinMode(buzzPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorVal = digitalRead(sensorPin);
  if (sensorVal == 1) {
    tone(buzzPin, freq);  
    Serial.write('1');
    Serial.write('\n');
  }
  else {
    noTone(buzzPin);
    Serial.write('0');
    Serial.write('\n');
  }
  delay(25);
}

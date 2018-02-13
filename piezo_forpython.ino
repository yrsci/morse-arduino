// Initialise variables
int sensorPin = 2;
int buzzPin = 3;
int freq = 500;

// Setup code, run once at beginning
void setup() {
  // Open serial port
  Serial.begin(9600);
  // State which pin to read from & which to output to
  pinMode(sensorPin, INPUT);
  pinMode(buzzPin, OUTPUT);
}

// Main code, looped repeatedly
void loop() {
  // Read status of sensor; 1 = pressed, 0 = not pressed
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

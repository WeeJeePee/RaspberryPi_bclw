#define GPSSerial Serial


void setup() {
  // wait for hardware serial to appear
  while (!Serial);

  // make this baud rate fast enough to we aren't waiting on it
  Serial.begin(115200);

  // 9600 baud is the default rate for the Ultimate GPS
  GPSSerial.begin(9600);
}

     
void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    GPSSerial.write(c);
  }
  if (GPSSerial.available()) {
    char c = GPSSerial.read();
    Serial.write(c);
  }
}

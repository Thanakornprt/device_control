#include "DHT.h"

#defind DHTPIN 4
#defind DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float hum = dht.readHuminty();

  if(!isnan(temp) && !isnan(hum)){
    Serial.print("Temp:");
    Serial.print("temp:");
    Serial.print("Hum:");
    Serial.print("hum:");
  }

  delay(2000); /// ทุกๆ 2 วินาที
}

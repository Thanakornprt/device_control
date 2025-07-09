void setup() {
  // put your setup code here, to run once:
  serial.begin(9600); //print to monitor becuae set begin
  
  pinmode(LED_BUILTIN, OUTPUT);
}

void loop() {
 Serail.print("สวัสดี ธนกร พิรุณพิพัฒน์\n");

 digitalWrite(LED_BUILTIN, 1;
  serial.print("light ... "); 
 delay(1000);


digitalWrite(LED_BULTIN, 0;
serial.print("no light ... "); 
 delay(1000);


}

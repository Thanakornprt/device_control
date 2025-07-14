void setup() {
  Serial.begin(115200);
  delay(1000); // รอ Serial พร้อม
}

void loop() {
  Serial.print("ASCII Table");
  Serial.print("Dec\tHex\tChar");
  Serial.print("--------------------");

  for (int i = 32; i <= 126; i++) {
    Serial.print(i);
    Serial.print("\t");
    Serial.print(String(i, HEX));
    Serial.print("\t");
    Serial.write(i);
    Serial.println();
  }

  Serial.println("\n--------------------\n");
  delay(5000); // หน่วงเวลา 5 วินาทีก่อนแสดงตารางใหม่อีกครั้ง
}

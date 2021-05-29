#define interrupt_pin1 0 //인터럽트 핀번호
#define interrupt_pin2 1 //인터럽트 핀번호
#define pin_num1 2 //핀번호
#define pin_num2 3 //핀번호


volatile unsigned long left_servo = 0;
volatile unsigned long right_servo = 0;

void setup()
{
  Serial.begin(19200); 
}

void loop()
{
  left_servo = pulseIn(pin_num1, HIGH);
  Serial.println(left_servo);
  right_servo = pulseIn(pin_num2, HIGH);
  Serial.println(right_servo);
  delay(1000);
}
#include "DHT.h"

#define NITROGENIO 15
#define FOSFORO 4
#define POTASSIO 5

#define DHTPIN 13
#define DHTTYPE DHT22

#define RELE 18

#define LDR 34

DHT dht(DHTPIN, DHTTYPE);


#define LED 2

void setup() {

  dht.begin();
  
  Serial.begin(115200);

  pinMode(NITROGENIO, INPUT_PULLUP);
  pinMode(FOSFORO, INPUT_PULLUP);
  pinMode(POTASSIO, INPUT_PULLUP);

  pinMode(RELE, OUTPUT);

  pinMode(LED, OUTPUT);
}

void loop() {

  int n = digitalRead(NITROGENIO);
  int p = digitalRead(FOSFORO);
  int k = digitalRead(POTASSIO);
  int ph = analogRead(LDR);

  float umidade = dht.readHumidity();

  Serial.print("N: ");
  Serial.print(n);

  Serial.print(" || P: ");
  Serial.print(p);

  Serial.print(" || K: ");
  Serial.print(k);

  Serial.print(" || Umidade: ");
  Serial.print(umidade);

  Serial.print(" || pH: ");
  Serial.print(ph);

  Serial.println();

  if (umidade < 50 || n == 1 || p == 1 || k == 1 || ph < 1500 || ph > 3000) {

  digitalWrite(LED, HIGH);
  digitalWrite(RELE, LOW);

  Serial.println("IRRIGACAO LIGADA");


} else {

  digitalWrite(LED, LOW);
  digitalWrite(RELE, LOW);

  Serial.println("IRRIGACAO DESLIGADA");
}

  delay(500);
}

#include <DHT.h>
#include <DHT_U.h>
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include "secrets.h"

#define AWS_THING_NAME "esp32"
#define AWS_IOT_PUBLISH_TOPIC   "main/publish"
#define AWS_IOT_SUBSCRIBE_TOPIC "main/subscribe"
#define TEMP_SENSOR_PIN 4 //D4
#define DHT_TYPE DHT11
#define HUM_SENSOR_PIN 2 //D2

#define ARDUINO_ID "ESP32-0000"


WiFiClientSecure net = WiFiClientSecure();
MQTTClient client = MQTTClient(512);
DHT dht(TEMP_SENSOR_PIN, DHT_TYPE);


void setup() { 
  Serial.begin(115200);
  dht.begin();

  connectWiFi();
  connectAWS();

  pinMode(HUM_SENSOR_PIN, INPUT);

  //subscribe to a topic for receiving messages
  client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC); 
  client.onMessage(messageHandler);
}

void messageHandler(String &topic, String &payload) {
  Serial.println("Receiving MQTT message:");
  Serial.println(topic + " " + payload);
}

// the loop function runs over and over again forever
void loop() {
  // Sends and receives packets
  client.loop();


  //logica para obtener datos de sensor
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();

  // Publish to a topic the json parsed to string
  client.publish(AWS_IOT_PUBLISH_TOPIC,  "{\"temperatura\":" + String(temp) + ",\"humedad\":" + String(hum) + ",\"ARDUINO_ID\":\"" + ARDUINO_ID + "\"}");
  delay(10000); // 10 seconds delay
}

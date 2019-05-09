//This example will set up a static IP - in this case 192.168.1.99
 
#include <ESP8266WiFi.h>
#include <Servo.h>
 
const char* ssid = "203";
const char* password = "tanay@12345";
 
int ledPin = D5;
int ServoPin = D7;
int SirenPin = D2;
Servo myservo;
WiFiServer server(80);
IPAddress ip(192, 168, 0, 123); // where xx is the desired IP Address
IPAddress gateway(192, 168, 0, 1); // set gateway to match your network
 
void setup() {
  Serial.begin(115200);
  delay(10);

  myservo.attach(ServoPin);
 
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
 
  pinMode(SirenPin, OUTPUT);
  digitalWrite(SirenPin, LOW);
  
  Serial.print(F("Setting static ip to : "));
  Serial.println(ip);
 
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  IPAddress subnet(255, 255, 255, 0); // set subnet mask to match your network
  WiFi.config(ip, gateway, subnet); 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Use this URL : ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
 
}
 
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
 
  // Match the request
 
  int value = LOW;
  int siren = LOW;
  int pos = 0;
  if (request.indexOf("/LED=ON") != -1) {
    digitalWrite(ledPin, HIGH);
    value = HIGH;
  } 
  if (request.indexOf("/LED=OFF") != -1){
    digitalWrite(ledPin, LOW);
    value = LOW;
  }
  if (request.indexOf("/DOORLOCK=ON") != -1){
      pos = 90;
      myservo.write(pos);
  }
  if (request.indexOf("/DOORLOCK=OFF") != -1){
      pos = 0;
      myservo.write(pos);
  }

  if (request.indexOf("/SIREN=ON") != -1) {
    digitalWrite(SirenPin, HIGH);
    siren = HIGH;
  } 
  if (request.indexOf("/SIREN=OFF") != -1){
    digitalWrite(SirenPin, LOW);
    siren = LOW;
  }
  
  // Return the response
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
 
  client.print("Led pin is now: ");
 
  if(value == HIGH) {
    client.print("On");  
  } else {
    client.print("Off");
  }
  
  client.println("<br><br>");
  client.println("Click <a href=\"/LED=ON\">here</a> turn the LED on pin 5 ON<br>");
  client.println("Click <a href=\"/LED=OFF\">here</a> turn the LED on pin 5 OFF<br>");
  client.println("Click <a href=\"/DOORLOCK=ON\">here</a> Doorlock ON<br>");
  client.println("Click <a href=\"/DOORLOCK=OFF\">here</a> Doorlock OFF<br>");
  client.println("Click <a href=\"/SIREN=ON\">here</a> turn the LED on pin 5 ON<br>");
  client.println("Click <a href=\"/SIREN=OFF\">here</a> turn the LED on pin 5 OFF<br>");
  client.println("</html>");
 
  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");
 
}

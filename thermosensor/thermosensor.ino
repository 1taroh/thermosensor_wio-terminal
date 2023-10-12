#include <seeed_line_chart.h>

TFT_eSPI tft;

#define max_size 50 //maximum size of data
doubles data; //Initilising a doubles type to store data
TFT_eSprite spr = TFT_eSprite(&tft);  // Sprite 

double AIN2V(double AIN){
  // V is 0[V] <= V <= 3.3[V]
  // 3.3[V] -> AIN = 1023
  // 5.0[V] -> AIN = 524 = (1023 + 524) - 1023

  double V = 3.3/1023 * AIN;
  return V;
}

double V2Temperature(double V){
  // use MCP9700A
  double mV = V * 1000;
  //                   [mV] [mV]  [mV]
  double temperature = (mV - 500)/10;
  return temperature;
}

void setup() {
    // IO
    Serial.begin(115200);
    pinMode(A0, INPUT);

    // LCD
    tft.begin();
    tft.setRotation(3);
    spr.createSprite(TFT_HEIGHT,TFT_WIDTH);
}

void loop() {
    spr.fillSprite(TFT_WHITE);
    if (data.size() == max_size) {
        data.pop();//this is used to remove the first read variable
    }
    double loudness = analogRead(A0);
    double V = AIN2V(loudness);
    double temperature = V2Temperature(V);
    data.push(temperature); //read variables and store in data

    //Settings for the line graph title
    text_t title = "temperature [C]";
    auto header =  text(0, 0)
                .value(title)
                .align(center)
                .valign(vcenter)
                .width(tft.width())
                .thickness(3);

    header.height(header.font_height() * 2);
    header.draw(); //Header height is the twice the height of the font

  //Settings for the line graph
    auto content = line_chart(20, header.height()); //(x,y) where the line graph begins
         content
                .height(tft.height() - header.height() * 1.5) //actual height of the line chart
                .width(tft.width() - content.x() * 2) //actual width of the line chart
                .based_on(0.0) //Starting point of y-axis, must be a float
                .show_circle(true) //drawing a cirle at each point, default is on.
                .value(data) //passing through the data to line graph
                .color(TFT_PURPLE) //Setting the color for the line
                .draw();

    spr.pushSprite(0, 0);
    delay(250);

    // serial output
    // Serial.print("title: ");
    // Serial.println(title);
    // Serial.print("Loudness: ");
    // Serial.println(loudness);
    // Serial.print("V: ");
    // Serial.println(V);
    // Serial.print("Temperature: ");
    Serial.println(temperature);
    delay(50);
}
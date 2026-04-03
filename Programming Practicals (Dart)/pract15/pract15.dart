import 'dart:io';
import 'dart:math';

// Challenge #1 - Write a sayName function that prints out your name.
void sayName() {
  print('My name is Tristan Budd');
}

// Challenge #2 - Write a studentDetails function that outputs my student details.
void studentDetails() {
  String output = 'My name is Tristan Budd\n';
  output += 'My student number is 2271413\n';
  output += 'My email address is up2271413@myport.ac.uk';

  print(output);
}

// Challenge #3 - Write a eurosToPounds function that converts euros to pounds.
double eurosToPounds(double euros) {
  return euros * 0.86;
}

// Challenge #4 - Write a fahrenheitToCelsius function that converts fahrenheit to celsius.
double fahrenheitToCelsius(double fahrenheit) {
  return (fahrenheit - 32) * (5 / 9);
}

// Challenge #5 - Write a areaOfCircle function that calculates the area of a circle.
double areaOfCircle() {
  print('Please enter the radius of the circle: ');
  String? userInput = stdin.readLineSync();
  double radius = double.parse(userInput!);

  return 3.14159 * (radius * radius);
}

double circumferenceOfCircle() {
  print('Please enter the radius of the circle: ');
  String? userInput = stdin.readLineSync();
  double radius = double.parse(userInput!);

  return 2 * 3.14159 * radius;
}

double areaOfCircle2(double radius) {
  return 3.14159 * (radius * radius);
}

double circumferenceOfCircle2(double radius) {
  return 2 * 3.14159 * radius;
}

void circleInfo() {
  print('Please enter the radius of the circle: ');
  String? userInput = stdin.readLineSync();
  double radius = double.parse(userInput!);

  print('The area of the circle is ${areaOfCircle2(radius)}');
  print('The circumference of the circle is ${circumferenceOfCircle2(radius)}');
}

// Challenges #6, #7, #8 - See burger.dart

// Challenge #9 - Write a hypotenuseOfTriangle function that calculates hypotenuse of a right-angled triangle.
double hypotenuseOfTriangle(double a, double b) {
  return sqrt((a * a) + (b * b));
}

void main() {
  // sayName();
  // studentDetails();
  // print(eurosToPounds(100));
  // print(fahrenheitToCelsius(100));
  // print(areaOfCircle());
  // print(circumferenceOfCircle());
  // circleInfo();
  // print(hypotenuseOfTriangle(3, 4));
}
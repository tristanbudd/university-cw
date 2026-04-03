import 'dart:io';
import 'dart:math';

void main() {
  print("Welcome to the guessing game, please guess a number 1-100, or 0 to exit.");

  int randomNumber = Random().nextInt(100) + 1;
  print("DEBUG: Random number is ${randomNumber}");

  while (true) {
    String? userInput = stdin.readLineSync();
    int guessedNumber = int.parse(userInput!);

    if (guessedNumber == 0) {
      break;
    } else if (guessedNumber == randomNumber) {
      print("You guessed the correct number! It was ${randomNumber}");
      break;
    } else if (guessedNumber > randomNumber) {
      print("High");
    } else {
      print("Low");
    }
  }
}
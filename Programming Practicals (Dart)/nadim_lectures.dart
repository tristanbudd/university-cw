import 'dart:io';
import 'dart:math';

int multiply(int a, int b) {
  return a * b;
}

int multiplyV2(int a, int b) => a * b;

// void main() {
//   // Returns to the power of.
//   print(pow(16, 2)); // 256
//   print(pow(3, 2)); // 9
//
//   for (int i = 0; i < 10; i++) {
//     String? user_input = stdin.readLineSync();
//
//     try {
//       int number_to_use = int.parse(user_input!);
//
//       print(multiplyV2(number_to_use, 5));
//       break;
//     } on FormatException {
//       print("Invalid number format entered.");
//     } catch (error) {
//       print("Error found: ${error}");
//     }
//   }
// }

/*
Checking for input
if (input == null || input.trim().isEmpty) {
  continue (or something else)'
}

Round to 2 decimal places
.toStringAsFixed(2)
*/

int inputNumber() {
  while (true) {
    String? user_input = stdin.readLineSync();

    try {
      int output = int.parse(user_input!);
      return output;
    } on FormatException {
       print("Invalid number format entered.");
    } catch (error) {
      print("Invalid Input");
    }
  }
}

int inputNumber2() {
  while (true) {
    String? user_input = stdin.readLineSync();
    if (user_input == null || user_input.trim().isEmpty) {
      print("Invalid Input");
      continue;
    }

    int? output = int.tryParse(user_input);
  }
}

void main() {
  print(inputNumber());
}

// Don't use num for now.
num? tryParse(String input) {
  String source = input.trim();
  return int.tryParse(source) ?? double.tryParse(source);
}
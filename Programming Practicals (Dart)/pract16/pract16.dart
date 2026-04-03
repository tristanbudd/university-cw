import 'dart:math';

// Challenge #1 - maxNumbers function that returns the larger number.
int maxNumbers(int number1, int number2) {
  if (number1 > number2) {
    return number1;
  } else {
    return number2;
  }
}

// Challenge #2 - daysInMonth that returns number of days in a month.
int daysInMonth(String month) {
  switch (month.toLowerCase()) {
    case 'february':
      return 28;
    case 'april':
    case 'june':
    case 'september':
    case 'november':
      return 30;
    case 'january':
    case 'march':
    case 'may':
    case 'july':
    case 'august':
    case 'october':
    case 'december':
      return 31;
    default:
      return 0;
  }
}

// Challenge #2b (My way of doing it)
// int? daysInMonth(String month) {
//   const months_of_year = {
//     'january': 31,
//     'february': 28,
//     'march': 31,
//     'april': 30,
//     'may': 31,
//     'june': 30,
//     'july': 31,
//     'august': 31,
//     'september': 30,
//     'october': 31,
//     'november': 30,
//     'december': 31
//   };
//
//   return months_of_year[month.toLowerCase()];
// }

// Challenge #3 - Arrow Functions
int multiplyBy2(int number) => number * 2;
void birthdayMessage(int age) => print("I'm ${age.toString()} years old.\n" + ("🕯️" * age));
void speedCalculator(double distance, double time) => print("Speed: ${distance / time}");

// Challenge #4 - heartMonitor function.
void heartMonitor(int age, int bpm) {
  int maxBPM;

  if (age <= 20) {
    maxBPM = 170;
  } else if (age <= 40) {
    maxBPM = 155;
  } else if (age <= 60) {
    maxBPM = 140;
  } else if (age <= 80) {
    maxBPM = 130;
  } else {
    maxBPM = 100;
  }

  if (bpm > maxBPM) {
    print("High heart rate for specified age range.");
  }
}

// Challenge #5 - basicCalculator function.
// Using 'num' as IDE was begging for me to use it, supports int and double return types.
num basicCalculator(String operationType, int number1, int number2) {
  switch(operationType.toLowerCase()) {
    case 'add':
      return number1 + number2;
    case 'subtract':
      return number1 - number2;
    case 'multiply':
      return number1 * number2;
    case 'divide':
      return number1 / number2;
    default:
      return 0;
  }
}

// Challenge #6 - isPrime function. (Had to research this one)
bool isPrime(int number) {
  if (number <= 1) {
    return false;
  }

  for (int i = 2; i <= sqrt(number); i++) {
    if (number % i == 0) {
      return false;
    }
  }

  return true;
}

// Challenge #7 - customisedGreeting function.
void customisedGreeting(int time) {
  if (time >= 600 && time <= 1200) {
    print("Have a great morning");
  } else if (time > 1200 && time <= 1800) {
    print("Have a good evening");
  } else if (time > 1800 && time <= 2400) {
    print("Have a good afternoon");
  } else {
    print("Have a good night");
  }
}

// Challenge #8 - gcd function.
int gcd(int number1, int number2) {
  if (number1 == number2) {
    return number1;
  } else if (number1 > number2) {
    return gcd(number2, (number1 - number2));
  } else {
    return gcd(number1, (number2 - number1));
  }
}

// Challenge #9, #10 External.

// Challenge #11 - romanToInt function. (Decided to go beyond 10)
int romanToInt(String data) {
  int total = 0;
  int prevValue = 0;

  for (int i = data.length - 1; i >= 0; i--) {
    int currentValue;

    if (data[i] == 'I') {
      currentValue = 1;
    } else if (data[i] == 'V') {
      currentValue = 5;
    } else if (data[i] == 'X') {
      currentValue = 10;
    } else if (data[i] == 'L') {
      currentValue = 50;
    } else if (data[i] == 'C') {
      currentValue = 100;
    } else if (data[i] == 'D') {
      currentValue = 500;
    } else if (data[i] == 'M') {
      currentValue = 1000;
    } else {
      currentValue = 0;
    }

    if (currentValue < prevValue) {
      total -= currentValue;
    } else {
      total += currentValue;
    }

    prevValue = currentValue;
  }

  return total;
}

String intToRoman(int data) {
  String output = "";
  int remainingToConvert = data;

  while (true) {
    if (remainingToConvert >= 1000) {
      output += "M";
      remainingToConvert -= 1000;
    } else if (remainingToConvert >= 500) {
      output += "D";
      remainingToConvert -= 500;
    } else if (remainingToConvert >= 100) {
      output += "C";
      remainingToConvert -= 100;
    } else if (remainingToConvert >= 50) {
      output += "L";
      remainingToConvert -= 50;
    } else if (remainingToConvert >= 10) {
      output += "X";
      remainingToConvert -= 10;
    } else if (remainingToConvert >= 5) {
      output += "V";
      remainingToConvert -= 5;
    } else if (remainingToConvert >= 1) {
      output += "I";
      remainingToConvert -= 1;
    } else {
      break;
    }
  }

  return output;
}

// Challenge #12 - External.

void main() {
  // print(maxNumbers(1, 5));
  // print(maxNumbers(3, 2));
  // print(daysInMonth('February'));
  // print(daysInMonth('July'));
  // print(multiplyBy2(5));
  // birthdayMessage(18);
  // speedCalculator(20, 5);
  // heartMonitor(20, 180);
  // heartMonitor(60, 100);
  // print(basicCalculator('multiply', 5, 5));
  // print(basicCalculator('subtract', 3, 1));
  // print(basicCalculator('divide', 5, 2));
  //print(isPrime(3));
  //print(isPrime(10));
  // customisedGreeting(1200);
  // customisedGreeting(1800);
  // print(gcd(2, 2));
  // print(gcd(5, 14));
  // print(gcd(12, 24));
  // print(romanToInt("IX"));
  // print(romanToInt("MCIII"));
  // print(intToRoman(102));
  // print(intToRoman(1032));
}
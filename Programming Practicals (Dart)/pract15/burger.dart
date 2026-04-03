import 'dart:io';

// Challenge #6 - Write a displayBurgerOrder function that calculates the total order.
void displayBurgerOrder(int amount, double cost_per) {
  print('Your order: ${'🍔' * amount}');
  print('Total: £${amount * cost_per}');
}

// Challenge #7 - Write a howManyBurgers function that calculates how many burgers a user can buy with an amount.
int howManyBurgers(double amount, double cost_per) {
  return (amount / cost_per).floor();
}

// Challenge #8 - Write a burgerOrder function that combines the use of both functions.
void burgerOrder() {
  print('Please enter the amount you have: ');
  String? user_input = stdin.readLineSync();
  double amount = double.parse(user_input!);

  print('Please enter the cost per burger: ');
  user_input = stdin.readLineSync();
  double cost_per = double.parse(user_input!);

  int burgers = howManyBurgers(amount, cost_per);
  displayBurgerOrder(burgers, cost_per);
}

void main() {
  burgerOrder();
}
import 'dart:math';

String generatePassword([int amountOfCharacters = 8]) {
  const String letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const String numbers = '0123456789';
  const String symbols = '!@#\$%^&*()_+-=[]{}|;:,.<>?';
  const String allChars = letters + numbers + symbols;

  String password = '';

  for (int i = 0; i < amountOfCharacters; i++) {
    int randomIndex = Random().nextInt(allChars.length);
    password += String.fromCharCode(allChars.codeUnitAt(randomIndex));
  }

  return password;
}

void main(List<String> args) {
  int amountOfCharacters;
  if (args.isNotEmpty) {
    amountOfCharacters = int.parse(args[0]);
  } else {
    amountOfCharacters = 8;
  }

  String password = generatePassword(amountOfCharacters);
  print('Generated password: $password');
}
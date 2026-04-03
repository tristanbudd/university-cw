void main(List<String> args) {
  String operationType = args[0];
  int number1 = int.parse(args[1]);
  int number2 = int.parse(args[2]);

  switch(operationType.toLowerCase()) {
    case 'add':
      print(number1 + number2);
    case 'subtract':
      print(number1 - number2);
    case 'multiply':
      print(number1 * number2);
    case 'divide':
      print(number1 / number2);
    default:
      print("Invalid operation type.");
  }
}
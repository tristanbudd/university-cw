import 'user.dart';

void main() {
  Person alice = Person('Alice', 20);
  alice.age = 21;
  print('Alice is ${alice.age} years old');

  print('Next year, Alice will be ${alice.ageNextYear()} years old');
  print('Alice has a valid name: ${alice.hasValidName()}');

  print(alice);
  print(alice.runtimeType);

  Rectangle rect = Rectangle(0, 0, 5, 10);
  print('Rectangle area: ${rect.getArea()}');
  print('Rectangle perimeter: ${rect.getPerimiter()}');

  Product washingLiquid = Product("Washing-up liquid", 1.5);
  Product frozenPeas = Product("Forzen peas", 1.75, clubcardItem: true);
  Product sausages = Product("Sausages", 3.5, clubcardItem: true);

  ShoppingCart cart = ShoppingCart();
  cart.addProduct(washingLiquid);
  cart.addProduct(frozenPeas);
  cart.addProduct(sausages);
  print(cart);

  ShoppingCart cart2 = ShoppingCart(hasClubcard: true);
  cart2.addProduct(washingLiquid);
  cart2.addProduct(frozenPeas);
  cart2.addProduct(sausages);
  print(cart2);

  User user = User('john_doe');
  print(user);
  user.login('wrong_password');
  user.changePassword('wrong_password', 'new_password');
  user.login('new_password');
}

class Person {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  int ageNextYear() {
    return age + 1;
  }

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  bool isAdult() {
    return age >= 18;
  }

  String toString() {
    return 'Person(name: $name, age: $age, isAdult: ${isAdult()})';
  }
}

class Student extends Person {
  int level = 4;
  String? _phoneNumber;

  Student(String name, int age, this._phoneNumber) : super(name, age);

  void graduate() {
    level++;
  }

  String greet() => 'Hello, $name!';

  String get phoneNumber {
    String lastFourDigits = _phoneNumber!.substring(6);
    return '***-***-$lastFourDigits';
  }

  void set phoneNumber(String phoneNumber) {
    if (phoneNumber.length == 10) {
      _phoneNumber = phoneNumber;
    }
  }

  @override
  String toString() {
    return 'Student(name: $name, age: $age, level: $level, isAdult: ${isAdult()})';
  }
}

class Module {
  String name;
  int credits;

  Module(this.name, {this.credits = 20});
}

class Course {
  String name;
  List<Module> modules = [];
  int totalCredits = 0;
  int _maxCredits = 120;

  Course(this.name);

  void addModule(Module module) {
    if (totalCredits + module.credits <= maxCredits) {
      modules.add(module);
      totalCredits += module.credits;
    }
  }

  int get maxCredits => _maxCredits;

  String toString() {
    String output = 'Course name: $name, Modules:\n';
    for (Module module in modules) {
      output += '  ${module.name} (${module.credits} credits)\n';
    }
    output += 'Total credits: $totalCredits';
    return output;
  }
}

class Shape {
  double x = 0.0;
  double y = 0.0;

  Shape(this.x, this.y);

  void move(double dx, double dy) {
    x += dx;
    y += dy;
  }

  String toString() => 'x: $x, y: $y';
}

class Circle extends Shape {
  double radius = 0.0;

  // Circle(double x, double y, double radius) : super(x, y) {
  //   this.radius = radius;
  // }

  Circle(double x, double y, this.radius) : super(x, y);

  String toString() => '${super.toString()}, radius: $radius';
}

class Rectangle extends Shape {
  double width = 0.0;
  double height = 0.0;

  Rectangle(double x, double y, this.width, this.height) : super(x, y);

  double getArea() {
    return width * height;
  }

  double getPerimiter() {
    return 2 * (width + height);
  }

  String toString() => '${super.toString()}, width: $width, height: $height';
}

class Product {
  String name;
  double price;
  bool clubcardItem = false;

  Product(this.name, this.price, {this.clubcardItem = false});
}

class ShoppingCart {
  List<Product> products = [];
  double totalPrice = 0.0;
  bool hasClubcard = false;

  ShoppingCart({this.hasClubcard = false});

  void addProduct(Product product) {
    products.add(product);
    totalPrice += product.price;
  }

  void removeProduct(Product product) {
    products.remove(product);
    totalPrice -= product.price;
  }

  void applyDiscount() {
    if (hasClubcard) {
      for (Product product in products) {
        if (product.clubcardItem) {
          totalPrice -= product.price * 0.1;
        }
      }
      totalPrice = double.parse((totalPrice).toStringAsFixed(2));
    }
  }

  String toString() {
    String output = 'Shopping Cart:\n';
    for (Product product in products) {
      output += '  ${product.name}: ${product.price}\n';
    }
    applyDiscount();
    if (hasClubcard) {
      output += 'Club Card Accepted! (Applying 10% Discount)\n';
    }
    output += 'Total: £${totalPrice}';
    return output;
  }
}
import '../pract16/password.dart';

class User {
  String username;
  String _password = generatePassword();

  User(this.username);

  void changePassword(String oldPassword, String newPassword) {
    if (_password == oldPassword) {
      _password = newPassword;
    } else {
      print("Incorrect old password.");
    }
  }

  void login(String password) {
    if (_password == password) {
      print("Login successful.");
    } else {
      print("Incorrect password.");
    }
  }

  String toString() {
    return "User: $username";
  }
}
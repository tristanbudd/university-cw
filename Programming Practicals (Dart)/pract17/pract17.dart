import 'dart:io';

// Challenge #1 - isValidEmail Function
bool isValidEmail(String emailAddress) => emailAddress.endsWith("@myport.ac.uk");

// Challenge #2 - checkExpenses Function
bool checkExpenses(List<double> expenditures, int employeeLimit) {
  for(double expenditure in expenditures) {
    if (expenditure > employeeLimit) {
      return true;
    }
  }
  return false;
}

// Challenge #3 - weatherDifference Function
double weatherDifference(List<double> temperatures) {
  double firstTemperature = temperatures.first;
  double lastTemperature = temperatures.last;

  return (firstTemperature - lastTemperature).abs();
  // .abs used to return positive integers only.
}

// Challenge #4 - removeMilk Function
List<String> removeMilk(List<String> foodNames) {
  foodNames.removeWhere((food) => food.toLowerCase().contains("milk"));
  return foodNames;
}
// https://api.flutter.dev/flutter/dart-core/List/removeWhere.html

// Challenge #5 - capMarks Function
Map<String, List<int>> capMarks(String moduleName, Map<String, List<int>> data) {
  for (String module in data.keys) {
    if (module == moduleName) {
      for (int i = 0; i < data[module]!.length; i++) {
        if (data[module]![i] > 40) {
          data[module]![i] = 40;
        }
      }
    }
  }
  return data;
}

// Challenge #6 - priceRise Function
Map<String, double> priceRise(Map<String, double> prices) {
  for (String item in prices.keys) {
    prices[item] = double.parse((prices[item]! * 1.1).toStringAsFixed(2));
  }
  return prices;
}

// Challenge #7 - capitalise Function
String capitalise(String text) {
  return text[0].toUpperCase() + text.substring(1).toLowerCase();
}

// Challenge #8 - extractHashtags Function
Set<String> extractHashtags(List<String> posts) {
  Set<String> hashtags = {};
  for (String post in posts) {
    List<String> words = post.split(" ");
    for (String word in words) {
      if (word.startsWith("#")) {
        hashtags.add(word);
      }
    }
  }
  return hashtags;
}

// Challenge #9 - capitalise Function (Sequence of words)
String capitaliseSentence(String text) {
  List<String> words = text.split(" ");
  String capitalisedText = "";
  for (String word in words) {
    capitalisedText += word[0].toUpperCase() + word.substring(1).toLowerCase() + " ";
  }
  return capitalisedText.trim();
}

// Challenge #10 - snakeToCamel Function
String snakeToCamel(String text) {
  List<String> words = text.split("_");
  String camelCaseText = words.first.toLowerCase(); // Keep the first word lowercase
  for (int i = 1; i < words.length; i++) {
    camelCaseText += words[i][0].toUpperCase() + words[i].substring(1).toLowerCase();
  }
  return camelCaseText;
}

// Challenge #11 - compress Function
String compress(int number, String text, bool debug) {
  String compressedText = "";
  Map<String, List<String>> coordinates = {};
  List<String> lines = text.split("\n");

  for (int lineNumber = 0; lineNumber < lines.length; lineNumber++) {
    String line = lines[lineNumber];
    int count = 1;
    String compressedLine = "";

    for (int i = 0; i < line.length; i++) {
      if (i < line.length - 1 && line[i] == line[i + 1]) {
        count++;
      } else {
        compressedLine += line[i];
        if (count >= number) {
          compressedLine += count.toString();
          String substring = line[i];
          if (!coordinates.containsKey(substring)) {
            coordinates[substring] = [];
          }
          coordinates[substring]!.add("Line ${lineNumber + 1}, Index ${compressedLine.length - count.toString().length - 1}");
        }
        count = 1;
      }
    }
    compressedText += compressedLine;
    if (lineNumber < lines.length - 1) {
      compressedText += "\n";
    }
  }

  if (debug) {
    compressedText += "\n";

    coordinates.forEach((substring, positions) {
      compressedText += "$substring: ${positions.join(", ")}\n";
    });
  }

  return compressedText;
}

// Challenge #11b - decompress Function
String decompress(String compressedText) {
  String decompressedText = "";
  List<String> lines = compressedText.split("\n");

  for (String line in lines) {
    if (line.contains(":")) break;

    String decompressedLine = "";
    int i = 0;

    while (i < line.length) {
      String currentChar = line[i];
      int count = 1;

      if (i + 1 < line.length && line[i + 1].contains(RegExp(r'[0-9]'))) {
        count = int.parse(line[i + 1]);
        i++;
      }

      decompressedLine += currentChar * count;
      i++;
    }
    decompressedText += decompressedLine + "\n";
  }

  return decompressedText.trim();
}

// Challenge 11c - zip & unzip Functions. (For files)
void zip(String filePath) {
  File file = File(filePath);
  String contents = file.readAsStringSync();
  String compressedContents = compress(3, contents, false);
  File compressedFile = File(filePath);
  compressedFile.writeAsStringSync(compressedContents);

  print("File compressed: ${compressedFile.path}");
}

void unzip(String filePath) {
  File file = File(filePath);
  String contents = file.readAsStringSync();
  String decompressedContents = decompress(contents);
  File decompressedFile = File(filePath);
  decompressedFile.writeAsStringSync(decompressedContents);

  print("File decompressed: ${decompressedFile.path}");
}

void main() {
  //print(isValidEmail("test@gmail.com"));
  //print(isValidEmail("up2271413@myport.ac.uk"));
  List<double> expenditures = [100.0, 200.0, 300.0, 400.0, 500.0];
  //print(checkExpenses(expenditures, 1000));
  List<double> expenditures2 = [100.0, 200.0, 300.0, 400.0, 500.0];
  //print(checkExpenses(expenditures2, 200));
  List<double> temperatures = [10.0, 12.5, 14.0, 16.5, 15.0, 12.0];
  //print(weatherDifference(temperatures));
  List<double> temperatures2 = [11.5, 12.0, 14.0, 16.0, 15.5, 12.0, 10.5];
  //print(weatherDifference(temperatures2));
  List<String> foodNames = ["milkshake", "yoghurt", "burger", "banana milk"];
  //print(removeMilk(foodNames));
  Map<String, List<int>> data = {
    "Module1": [39, 60, 22, 91],
    "Module2": [80, 90, 100, 21],
    "Module3": [30, 40, 50, 54]
  };
  //print(capMarks("Module1", data));
  Map<String, double> prices = {
    'Tesco Finest Yogurt': 1.20,
    'Robinson\'s orange squash': 2.00,
    'Tesco Finest Macaroni Cheese': 4.25,
    'Doritos Cool Original': 2.50,
    'Milk': 1.45,
  };
  //print(priceRise(prices));
  //print(capitalise("hello"));
  //print(capitalise("HELLO"));
  List<String> posts = [
    "I love #coding and #testing!",
    "Check out my new #blog post!",
    "Learning #Dart and #Flutter is fun!",
    "Just another day in paradise #sunshine"
  ];
  //print(extractHashtags(posts));
  //print(capitaliseSentence("hello world! this is a test."));
  //print(capitaliseSentence("HELLO WORLD! THIS IS A TEST."));
  //print(snakeToCamel("hello_world_this_is_a_test"));
  //print(snakeToCamel("testing_snake_case"));
  // print(compress(3, "aaabbbcccccddddddeee", true));
  // print(compress(2, "aabbccddeee", true));
  // print(compress(2, "aaaabbbb\nccccddddffffggg\neee", true));
  // print(decompress("a4b4"));
  // print(decompress("a2b2c2d2e2\nc2d2f2g3\ne2"));
  //zip("test.txt");
  //unzip("test.txt");
}
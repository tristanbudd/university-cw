class Movie {
  String title;
  String genre;
  int year;
  double rating;

  Movie(this.title, this.genre, this.year, this.rating);

  @override
  String toString() {
    return 'Movie{title: $title, genre: $genre, year: $year, rating: $rating}';
  }
}

class Series {
  String title;
  String genre;
  int seasons;
  double rating;

  Series(this.title, this.genre, this.seasons, this.rating);

  @override
  String toString() {
    return 'Series{title: $title, genre: $genre, seasons: $seasons, rating: $rating}';
  }
}

class Netflix {
  List<Movie> movies = [];
  List<Series> series = [];

  void addMovie(Movie movie) {
    movies.add(movie);
  }

  void addSeries(Series series) {
    this.series.add(series);
  }

  List<Movie> getMovies() {
    return movies;
  }

  List<Series> getSeries() {
    return series;
  }
}

void main() {
  Netflix netflix = Netflix();

  Movie movie1 = Movie('Inception', 'Sci-Fi', 2010, 8.8);
  Movie movie2 = Movie('The Dark Knight', 'Action', 2008, 9.0);
  Series series1 = Series('Stranger Things', 'Horror', 4, 8.7);
  Series series2 = Series('Breaking Bad', 'Crime', 5, 9.5);

  netflix.addMovie(movie1);
  netflix.addMovie(movie2);
  netflix.addSeries(series1);
  netflix.addSeries(series2);

  print('Movies on Netflix:');
  for (Movie movie in netflix.getMovies()) {
    print(movie);
  }

  print('\nSeries on Netflix:');
  for (Series series in netflix.getSeries()) {
    print(series);
  }
}
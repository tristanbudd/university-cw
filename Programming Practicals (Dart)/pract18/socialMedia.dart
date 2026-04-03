class Post {
  String content;
  String author;
  int date;

  Post(this.content, this.author, {this.date = 150424});
}

class SocialMediaFeed {
  List<Post> posts = [];

  void addPost(Post post) {
    posts.add(post);
  }

  void removePost(Post post) {
    posts.remove(post);
  }

  void displayFeed() {
    for (Post post in posts) {
      print('${post.author} (${post.date}): ${post.content}');
    }
  }
}

void main() {
  SocialMediaFeed feed = SocialMediaFeed();

  Post post1 = Post('Hello, world!', 'Alice', date: 150424);
  Post post2 = Post('Dart is awesome!', 'Bob', date: 150425);
  Post post3 = Post('I love programming!', 'Charlie', date: 150426);

  feed.addPost(post1);
  feed.addPost(post2);
  feed.addPost(post3);

  feed.displayFeed();
}
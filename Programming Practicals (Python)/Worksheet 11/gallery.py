# Challenge #6 - Art Gallery
class ArtPiece:
    def __init__(self, title, artist, price):
        self.title = title
        self.artist = artist
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.artist} (£{self.price})"


class Exhibition:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.art_pieces = []

    def add_art_piece(self, art_piece):
        if art_piece not in self.art_pieces:
            self.art_pieces.append(art_piece)
    
    def remove_art_piece(self, art_piece):
        if art_piece in self.art_pieces:
            self.art_pieces.remove(art_piece)

    def update_art_price(self, art_piece, new_price):
        art_piece.price = new_price

    def __str__(self):
        output = f"{self.name} Exhibition:\n"
        output += f"Start Date: {self.start_date}\n"
        output += f"End Date: {self.end_date}\n"
        output += "Art Pieces:\n"
        for art_piece in self.art_pieces:
            output += f"{art_piece}\n"
        return output


class Gallery:
    def __init__(self, name):
        self.name = name
        self.exhibitions = []
        self.current_exhibition = None

    def add_exhibition(self, exhibition):
        if exhibition not in self.exhibitions:
            self.exhibitions.append(exhibition)

    def remove_exhibition(self, exhibition):
        if exhibition in self.exhibitions:
            self.exhibitions.remove(exhibition)

    def set_current_exhibition(self, exhibition):
        if exhibition in self.exhibitions:
            self.current_exhibition = exhibition

    def get_current_exhibition(self):
        return self.current_exhibition

    def __str__(self):
        output = f"{self.name} Art Gallery\nAll Exhibitions:\n"
        for exhibition in self.exhibitions:
            output += f"{exhibition}\n"
        output += f"Current Exhibition:\n"
        if self.current_exhibition:
            output += f"{self.current_exhibition}\n"
        else:
            output += "No current exhibition."
        return output


def test_art_gallery():
    # Create multiple art pieces
    art_piece1 = ArtPiece("Starry Night", "Van Gogh", 1000000)
    art_piece2 = ArtPiece("The Scream", "Munch", 2000000)
    art_piece3 = ArtPiece("Mona Lisa", "Da Vinci", 3000000)
    art_piece4 = ArtPiece("Water Lilies", "Monet", 1500000)
    art_piece5 = ArtPiece("Guernica", "Picasso", 2500000)

    # Create two exhibitions
    exhibition1 = Exhibition("Modern Art", "2025-06-01", "2025-06-30")
    exhibition1.add_art_piece(art_piece1)
    exhibition1.add_art_piece(art_piece3)
    exhibition1.add_art_piece(art_piece5)

    exhibition2 = Exhibition("Classic Masterpieces", "2025-07-01", "2025-07-31")
    exhibition2.add_art_piece(art_piece2)
    exhibition2.add_art_piece(art_piece4)

    # Create a gallery and add exhibitions
    gallery = Gallery("London")
    gallery.add_exhibition(exhibition1)
    gallery.add_exhibition(exhibition2)

    # Remove and add art pieces to exhibitions
    print("Removing 'Starry Night' from 'Modern Art'...")
    exhibition1.remove_art_piece(art_piece1)
    print("Adding 'The Scream' to 'Modern Art'...")
    exhibition1.add_art_piece(art_piece2)

    # Update art piece prices
    print("Updating price of 'Mona Lisa' to £3500000...")
    exhibition1.update_art_price(art_piece3, 3500000)
    print("Updating price of 'Water Lilies' to £1600000...")
    exhibition2.update_art_price(art_piece4, 1600000)

    # Setting the current exhibition and printing
    print("Setting 'Modern Art' as the current exhibition...")
    gallery.set_current_exhibition(exhibition1)
    print(gallery)

test_art_gallery()
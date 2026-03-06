# Bakery Pastry Batch
class PastryBatch:
    def __init__(self, pastry_name, price_per_piece, piece_count):
        self.pastry_name = pastry_name
        self.price_per_piece = price_per_piece
        self.piece_count = piece_count
    def __str__(self):
        return self.pastry_name + ": " + str(self.piece_count) + " piece(s) at $" + str(self.price_per_piece)
    def __repr__(self):
        return "PastryBatch('" + self.pastry_name + "', " + str(self.price_per_piece) + ", " + str(self.piece_count) + ")"
    def __add__(self, other):
        if isinstance(other, PastryBatch):
            if self.pastry_name == other.pastry_name:
                new_count = self.piece_count + other.piece_count
                return PastryBatch(self.pastry_name, self.price_per_piece, new_count)
            else:
                return NotImplemented
        if isinstance(other, int):
            new_count = self.piece_count + other
            return PastryBatch(self.pastry_name, self.price_per_piece, new_count)
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, PastryBatch):
            if self.pastry_name == other.pastry_name and self.price_per_piece == other.price_per_piece:
                return True
            else:
                return False
        return NotImplemented
    def __bool__(self):
        if self.piece_count > 0:
            return True
        else:
            return False
batch1 = PastryBatch("Croissant", 3.5, 12)
batch2 = PastryBatch("Croissant", 3.5, 6)
batch3 = PastryBatch("Muffin", 4.0, 0)
print(str(batch1))
print(repr(batch1))
print(batch1 + batch2)
print(batch1 + 10)
print(batch1 == batch2)
print(bool(batch1))
print(bool(batch3))


# Expected Output
# Croissant: 12 piece(s) at $3.5
# PastryBatch('Croissant', 3.5, 12)
# Croissant: 18 piece(s) at $3.5
# Croissant: 22 piece(s) at $3.5
# True
# True
# False
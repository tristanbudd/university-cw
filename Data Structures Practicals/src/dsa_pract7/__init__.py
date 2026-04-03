import random
import matplotlib.pyplot as plt

"""
Question #1

Collisions are inevitable when mapping many keys to fewer hash values. Modulo Hashing uses the operation h(k) = k mod m,
mapping key k to a hash value with modulus m. Hash 100 random and unique integer keys with different values of m and
compare the distribution and collision rates across multiple trials.
"""
def modulo_hashing(keys, m):
    hash_table = [0] * m
    collisions = 0
    for key in keys:
        h = key % m
        if hash_table[h] != 0:
            collisions += 1
        hash_table[h] += 1
    return hash_table, collisions

"""
Question #2

Apply Modulo Hashing, h(k) = k mod m, to insert keys (5, 10, 12, 14, 17, 25, 27, 30, 33, 45, 56, 64, 128, 129) into a
hash table with 7 slots, using a modulus of m=7. Analyse collisions and adjust both the modulus m and hash table size
to minimise collisions. Compare the impact on hash table size.
"""
def analyze_modulo_hashing(keys, m_values):
    results = {}
    for m in m_values:
        _, collisions = modulo_hashing(keys, m)
        results[m] = collisions
    min_m = min(results, key=lambda x: results[x])
    return results, min_m

"""
Question #3

Further to Ex 2, implement Chaining to resolve collisions.
"""
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        h = key % self.size
        self.table[h].append((key, value))

    def search(self, key):
        h = key % self.size
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

    def delete(self, key):
        h = key % self.size
        for i, (k, _) in enumerate(self.table[h]):
            if k == key:
                self.table[h].pop(i)
                return True
        return False

"""
Question #4

Further to Ex 2, implement Linear Probing to resolve collisions.
"""
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        h = key % self.size
        start = h
        while self.table[h] is not None:
            h = (h + 1) % self.size
            if h == start:
                raise Exception("Hash table full")
        self.table[h] = (key, value)

    def search(self, key):
        h = key % self.size
        start = h
        while self.table[h] is not None:
            if self.table[h][0] == key:
                return self.table[h][1]
            h = (h + 1) % self.size
            if h == start:
                break
        return None

    def delete(self, key):
        h = key % self.size
        start = h
        while self.table[h] is not None:
            if self.table[h][0] == key:
                self.table[h] = None
                return True
            h = (h + 1) % self.size
            if h == start:
                break
        return False

"""
Question #5

Further to Ex 2, implement Quadratic Probing to resolve collisions.
"""
class HashTableQuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        start = key % self.size
        for i in range(self.size):
            h = (start + i * i) % self.size
            if self.table[h] is None:
                self.table[h] = (key, value)
                return
        raise Exception("Hash table full")

    def search(self, key):
        start = key % self.size
        for i in range(self.size):
            h = (start + i * i) % self.size
            if self.table[h] is None:
                return None
            if self.table[h][0] == key:
                return self.table[h][1]
        return None

    def delete(self, key):
        start = key % self.size
        for i in range(self.size):
            h = (start + i * i) % self.size
            if self.table[h] is None:
                return False
            if self.table[h][0] == key:
                self.table[h] = None
                return True
        return False

"""
Question #6

Further to Ex 2, implement Double Hashing to resolve collisions
Hint: Define the 2nd hash function as needed.
"""
class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def second_hash(self, key):
        # Secondary hash function: must be non-zero and < size
        return 1 + (key % (self.size - 1))

    def insert(self, key, value):
        h1 = key % self.size
        h2 = self.second_hash(key)
        i = 0
        while i < self.size:
            h = (h1 + i * h2) % self.size
            if self.table[h] is None:
                self.table[h] = (key, value)
                return
            i += 1
        raise Exception("Hash table full")

    def search(self, key):
        h1 = key % self.size
        h2 = self.second_hash(key)
        for i in range(self.size):
            h = (h1 + i * h2) % self.size
            if self.table[h] is None:
                return None
            if self.table[h][0] == key:
                return self.table[h][1]
        return None

    def delete(self, key):
        h1 = key % self.size
        h2 = self.second_hash(key)
        for i in range(self.size):
            h = (h1 + i * h2) % self.size
            if self.table[h] is None:
                return False
            if self.table[h][0] == key:
                self.table[h] = None
                return True
        return False



def main():
    # Question #1: Modulo Hashing
    print("--- Question #1 ---")
    keys = random.sample(range(1000), 100)
    m_values = [10, 20, 50, 100, 200]
    distributions = {}

    for m in m_values:
        hash_table = [0] * m
        collisions = 0
        for key in keys:
            index = key % m
            if hash_table[index] > 0:
                collisions += 1
            hash_table[index] += 1
        distributions[m] = hash_table
        print(f"m = {m}, Collisions = {collisions}, Distribution = {hash_table}")

    # Plot distributions
    fig, axes = plt.subplots(len(m_values), 1, figsize=(10, 15))
    fig.suptitle('Question #1: Hash Value Distributions for Different m')
    for i, m in enumerate(m_values):
        axes[i].bar(range(m), distributions[m])
        axes[i].set_title(f'm = {m}')
        axes[i].set_xlabel('Hash Table Slot')
        axes[i].set_ylabel('Number of Keys')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # Question #2: Optimal Modulus
    print("\n--- Question #2 ---")
    keys = [5, 10, 12, 14, 17, 25, 27, 30, 33, 45, 56, 64, 128, 129]
    m_values = range(5, 50)
    collisions_analysis = {}

    for m in m_values:
        hash_table = [0] * m
        collisions = 0
        for key in keys:
            index = key % m
            if hash_table[index] > 0:
                collisions += 1
            hash_table[index] += 1
        collisions_analysis[m] = collisions

    # Find optimal m
    optimal_m = min(collisions_analysis, key=lambda x: collisions_analysis[x])
    print(f"Optimal m with minimum collisions: {optimal_m}")
    print("Collision results:", collisions_analysis)

    # Plot original table (e.g., m = 7) and collision analysis
    original_m = 7
    original_table = [0] * original_m
    for key in keys:
        original_table[key % original_m] += 1

    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    axes[0].bar(range(original_m), original_table)
    axes[0].set_title(f'Original Hash Table Distribution (m={original_m})')
    axes[0].set_xlabel('Hash Table Slot')
    axes[0].set_ylabel('Number of Keys')

    axes[1].plot(list(collisions_analysis.keys()), list(collisions_analysis.values()), marker='o', color='red')
    axes[1].axvline(x=optimal_m, color='green', linestyle='--', label=f'Optimal m = {optimal_m}')
    axes[1].set_title('Collision Analysis for Different Hash Table Sizes')
    axes[1].set_xlabel('Hash Table Size (m)')
    axes[1].set_ylabel('Number of Collisions')
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

    # Question #3: Chaining
    print("\n--- Question #3: Chaining ---")
    chaining_table = HashTableChaining(size=7)
    for i, k in enumerate(keys):
        chaining_table.insert(k, f"Data{k}")
    print("Chaining Hash Table:", chaining_table.table)

    # Question #4: Linear Probing
    print("\n--- Question #4: Linear Probing ---")
    linear_table = HashTableLinearProbing(size=17)
    for k in keys:
        linear_table.insert(k, f"Data{k}")
    print("Linear Probing Hash Table:", linear_table.table)

    # Question #5: Quadratic Probing
    print("\n--- Question #5: Quadratic Probing ---")
    quadratic_table = HashTableQuadraticProbing(size=17)
    for k in keys:
        quadratic_table.insert(k, f"Data{k}")
    print("Quadratic Probing Hash Table:", quadratic_table.table)

    # Question #6: Double Hashing
    print("\n--- Question #6: Double Hashing ---")
    double_hash_table = HashTableDoubleHashing(size=17)
    for k in keys:
        double_hash_table.insert(k, f"Data{k}")
    print("Double Hashing Hash Table:", double_hash_table.table)


if __name__ == "__main__":
    main()

import random
import matplotlib.pyplot as plt

"""
Question #1

Collisions are inevitable when mapping many keys to fewer hash values.
Modulo Hashing uses the operation h(k) = k mod m, mapping key k to a hash
value with modulus m. Hash 100 random and unique integer keys with
different values of m and compare the distribution and collision rates across
multiple trials.
"""
def modulo_hashing(keys, m):
    """Hash keys using h(k) = k mod m and return distribution"""
    distribution = [0] * m
    for key in keys:
        hash_value = key % m
        distribution[hash_value] += 1
    return distribution


def modulo_hashing_analysis(keys, m_values):
    """Analyze collisions for different m values"""
    analysis_results = {}
    for m in m_values:
        distribution = modulo_hashing(keys, m)
        collisions = sum(count - 1 for count in distribution if count > 1)
        analysis_results[m] = (collisions, distribution)
    return analysis_results


def question1():
    """Compare collision rates for 100 random keys with different m values"""
    keys = random.sample(range(1, 1000), 100)
    m_values = [10, 20, 50, 100, 200]

    results = {}
    for m in m_values:
        distribution = modulo_hashing(keys, m)
        collisions = sum(count - 1 for count in distribution if count > 1)
        results[m] = {'collisions': collisions, 'distribution': distribution}
        print(f"m={m}: {collisions} collisions")

    return results


"""
Question #2

Apply Modulo Hashing, h(k) = k mod m, to insert keys (5, 10, 12, 14, 17, 25,
27, 30, 33, 45, 56, 64, 128, 129) into a hash table with 7 slots, using a modulus
of m=7. Analyse collisions and adjust both the modulus m and hash table size
to minimise collisions. Compare the impact on hash table size.
"""
def question2():
    """Analyze and optimize hash table for given keys"""
    keys = [5, 10, 12, 14, 17, 25, 27, 30, 33, 45, 56, 64, 128, 129]
    m_original = 7

    original_distribution = modulo_hashing(keys, m_original)
    m_values = range(5, 50)
    collision_analysis = modulo_hashing_analysis(keys, m_values)

    min_collisions_m = min(collision_analysis, key=lambda m: collision_analysis[m][0])
    min_collisions, optimal_distribution = collision_analysis[min_collisions_m]

    print(f"Original m={m_original}: Distribution = {original_distribution}")
    print(f"Optimal m={min_collisions_m}: Collisions = {min_collisions}")

    # Plotting
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    axes[0].bar(range(m_original), original_distribution)
    axes[0].set_title(f'Original Hash Table Distribution (m={m_original})')
    axes[0].set_xlabel('Hash Value')
    axes[0].set_ylabel('Number of Keys')

    m_values_plot = list(collision_analysis.keys())
    collisions_plot = [collision_analysis[m][0] for m in m_values_plot]
    axes[1].plot(m_values_plot, collisions_plot, label='Collisions', color='red', marker='o')
    axes[1].axvline(x=min_collisions_m, color='green', linestyle='--', label=f'Optimal m={min_collisions_m}')
    axes[1].set_title('Collision Analysis')
    axes[1].set_xlabel('Hash Table Size (m)')
    axes[1].set_ylabel('Collisions')
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

    return min_collisions_m, min_collisions


"""
Question #3

Further to Ex 2, implement Chaining to resolve collisions.
"""
class HashChaining:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_fun(self, key):
        return key % self.size

    def insert(self, key, data):
        address = self.hash_fun(key)
        self.hash_table[address].append([key, data])
        print(f"Inserted key {key} at index {address}")

    def search(self, key):
        address = self.hash_fun(key)
        for item in self.hash_table[address]:
            if item[0] == key:
                print(f"Found: key={key}, data={item[1]} at index {address}")
                return address
        print("Not found")
        return -1

    def delete(self, key):
        address = self.hash_fun(key)
        for i, item in enumerate(self.hash_table[address]):
            if item[0] == key:
                print(f"Deleted: key={key}, data={item[1]} from index {address}")
                self.hash_table[address].pop(i)
                return
        print("Not found")


"""
Question #4

Further to Ex 2, implement Linear Probing to resolve collisions.
"""
class HashLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_fun(self, key):
        return key % self.size

    def insert(self, key, data):
        start = self.hash_fun(key)
        for i in range(self.size):
            address = (start + i) % self.size
            if len(self.hash_table[address]) == 0:
                self.hash_table[address].append([key, data])
                print(f"Inserted key {key} at index {address}")
                return
        print("Hash table full")

    def search(self, key):
        start = self.hash_fun(key)
        for i in range(self.size):
            address = (start + i) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return -1
            elif self.hash_table[address][0][0] == key:
                print(f"Found: key={key}, data={self.hash_table[address][0][1]} at index {address}")
                return address
        print("Not found")
        return -1

    def delete(self, key):
        start = self.hash_fun(key)
        for i in range(self.size):
            address = (start + i) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return
            elif self.hash_table[address][0][0] == key:
                print(f"Deleted: key={key}, data={self.hash_table[address][0][1]} from index {address}")
                self.hash_table[address].pop(0)
                return
        print("Not found")


"""
Question #5

Further to Ex 2, implement Quadratic Probing to resolve collisions.
"""
class HashQuadraticProbing:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_fun(self, key):
        return key % self.size

    def insert(self, key, data):
        start = self.hash_fun(key)
        for i in range(self.size * self.size):
            address = (start + i * i) % self.size
            if len(self.hash_table[address]) == 0:
                self.hash_table[address].append([key, data])
                print(f"Inserted key {key} at index {address}")
                return
        print("Hash table full")

    def search(self, key):
        start = self.hash_fun(key)
        for i in range(self.size * self.size):
            address = (start + i * i) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return -1
            elif self.hash_table[address][0][0] == key:
                print(f"Found: key={key}, data={self.hash_table[address][0][1]} at index {address}")
                return address
        print("Not found")
        return -1

    def delete(self, key):
        start = self.hash_fun(key)
        for i in range(self.size * self.size):
            address = (start + i * i) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return
            elif self.hash_table[address][0][0] == key:
                print(f"Deleted: key={key}, data={self.hash_table[address][0][1]} from index {address}")
                self.hash_table[address].pop(0)
                return
        print("Not found")


"""
Question #6

Further to Ex 2, implement Double Hashing to resolve collisions.
Hint: Define the 2nd hash function as needed.
"""
class HashDoubleHashing:
    def __init__(self, size=10):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_fun(self, key):
        return key % self.size

    def hash_fun2(self, key):
        return 7 - (key % 7)

    def insert(self, key, data):
        start = self.hash_fun(key)
        step = self.hash_fun2(key)
        for i in range(self.size):
            address = (start + i * step) % self.size
            if len(self.hash_table[address]) == 0:
                self.hash_table[address].append([key, data])
                print(f"Inserted key {key} at index {address}")
                return
        print("Hash table full")

    def search(self, key):
        start = self.hash_fun(key)
        step = self.hash_fun2(key)
        for i in range(self.size):
            address = (start + i * step) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return -1
            elif self.hash_table[address][0][0] == key:
                print(f"Found: key={key}, data={self.hash_table[address][0][1]} at index {address}")
                return address
        print("Not found")
        return -1

    def delete(self, key):
        start = self.hash_fun(key)
        step = self.hash_fun2(key)
        for i in range(self.size):
            address = (start + i * step) % self.size
            if len(self.hash_table[address]) == 0:
                print("Not found")
                return
            elif self.hash_table[address][0][0] == key:
                print(f"Deleted: key={key}, data={self.hash_table[address][0][1]} from index {address}")
                self.hash_table[address].pop(0)
                return
        print("Not found")

def main():
    print("\n=== Testing Chaining ===")
    h = HashChaining(7)
    keys = [5, 10, 12, 14, 17, 25, 27, 30, 33, 45, 56, 64, 128, 129]
    for key in keys:
        h.insert(key, f"data_{key}")
    h.search(25)
    h.delete(25)
    h.search(25)

    print("\n=== Testing Linear Probing ===")
    h = HashLinearProbing(7)
    keys = [5, 10, 12, 14, 17, 25, 27]
    for key in keys:
        h.insert(key, f"data_{key}")
    h.search(25)
    h.delete(25)
    h.search(25)

    print("\n=== Testing Quadratic Probing ===")
    h = HashQuadraticProbing(7)
    keys = [5, 10, 12, 14, 17, 25, 27]
    for key in keys:
        h.insert(key, f"data_{key}")
    h.search(25)
    h.delete(25)
    h.search(25)

    print("\n=== Testing Double Hashing ===")
    h = HashDoubleHashing(7)
    keys = [5, 10, 12, 14, 17, 25, 27]
    for key in keys:
        h.insert(key, f"data_{key}")
    h.search(25)
    h.delete(25)
    h.search(25)


if __name__ == "__main__":
    main()
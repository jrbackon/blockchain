import hashlib

class BabsonCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Kali sends 2 BabC to Jacob"
t2 = "Evie sends 4.1 BabC to Jacob"
t3 = "Kristen sends 3.2 BabC to Jacob"
t4 = "Jacob sends 0.3 BabC to Kali"
t5 = "Jacob sends 1 BabC to Evie"
t6 = "Kali sends 5.4 BabC to Kristen"

initial_block = BabsonCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = BabsonCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = BabsonCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
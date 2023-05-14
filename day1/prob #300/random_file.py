import random
import struct


def generate_random_file(file_path, size_in_kb):
    with open(file_path, 'wb') as file:
        for _ in range(size_in_kb):
            voter_id = random.randint(1, 1000)  # Generate a random voter ID between 1 and 1000
            candidate_id = random.randint(1, 10)  # Generate a random candidate ID between 1 and 10

            # Pack the voter_id and candidate_id as 8-byte binary data
            data = struct.pack('ii', voter_id, candidate_id)
            file.write(data)


if __name__ == "__main__":
    # Example usage: Generate a random file named 'random_file.txt' of size 5 KB
    generate_random_file('voting_machine.txt', 5000)

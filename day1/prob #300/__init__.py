import struct
from collections import defaultdict
from typing import Dict


class TopCandidates:
    candidate_votes: Dict[int, int] = defaultdict(int)  # candidate id : total number of votes
    votes_casted_candidate: Dict[int, int] = {}

    def __init__(self, path):
        self._file_path = path

    def read_file(self):
        chunk_size = 1024 * 1024  # 1MB chunk size (can be adjusted as per your needs)
        print(f"It has been identified that the ", end="")
        with open(self._file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                # Process the chunk
                while len(
                        chunk) >= 8:  # Assuming each entry is 8 bytes (4 bytes for voter_id and 4 bytes for candidate_id)
                    print(chunk)
                    voter_id, candidate_id = struct.unpack('ii', chunk[:8])

                    if not self.cast_a_vote(candidate_id, voter_id):
                        print(voter_id, end=',')
                    chunk = chunk[8:]  # Move to the next entry within the chunk
        print(" ids exhibit fradualent behaviour.")

    def cast_a_vote(self, candidate_id: int, voter_id: int) -> bool:
        if voter_id not in self.votes_casted_candidate:
            self.votes_casted_candidate[voter_id] = candidate_id
            self.candidate_votes[candidate_id] += 1
            return True

        casted_to_cand = self.votes_casted_candidate[voter_id]
        self.candidate_votes[casted_to_cand] -= 1
        return False


if __name__ == "__main__":
    top_candidate = TopCandidates("voting_machine.txt")
    top_candidate.read_file()
    print(top_candidate.candidate_votes)
    print(top_candidate.votes_casted_candidate)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True


class TransactionHashTable:
    def __init__(self):
        self.table = {}

    def insert(self, transaction_id, transaction_data):
        self.table[transaction_id] = transaction_data

    def get(self, transaction_id):
        return self.table.get(transaction_id)

import heapq

class TopKTransactions:
    def __init__(self, k):
        self.k = k
        self.min_heap = []

    def add_transaction(self, transaction, risk_score):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, (risk_score, transaction))
        elif risk_score > self.min_heap[0][0]:
            heapq.heapreplace(self.min_heap, (risk_score, transaction))

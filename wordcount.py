"""テキストの単語数を数える小さなスクリプト（brain-demo の試験用）。"""
import sys
from collections import Counter


def count_words(text):
    """空白区切りの単語を小文字にして数える。"""
    return Counter(text.lower().split())


def main(argv):
    text = sys.stdin.read() if len(argv) < 2 else open(argv[1], encoding="utf-8").read()
    for word, n in count_words(text).most_common(10):
        print(f"{n}\t{word}")


if __name__ == "__main__":
    main(sys.argv)

#! /usr/bin/env python3
import re

# doesn't solve the problem, due to subreddit seems to suggest it's an oversight on input and edge cases
def find_unique_matches(input_str, patterns):
    # Sort patterns by length in descending order
    patterns.sort(key=len, reverse=True)

    # Create a regular expression pattern with named groups for each pattern
    combined_pattern = "|".join(f"(?P<match{i}>{pattern})" for i, pattern in enumerate(patterns))

    # Find all matches using the combined pattern
    matches = re.finditer(combined_pattern, input_str)

    # Filter out matches that are part of a previously found match
    unique_matches = []
    seen_indices = set()

    for match in matches:
        for i, pattern in enumerate(patterns):
            if match.group(f"match{i}") and match.start(f"match{i}") not in seen_indices:
                unique_matches.append(match.group())
                seen_indices.update(range(match.start(f"match{i}"), match.end(f"match{i}")))

    return unique_matches

STR_TO_NUMS = {
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9',
}

def num_or_str(num):
    return num if num.isnumeric() else STR_TO_NUMS[num]

patterns=[key for key in STR_TO_NUMS.keys()] + [r"[1-9]"]
combined_pattern = "|".join(f"(?P<match{i}>{pattern})" for i, pattern in enumerate([key for key in STR_TO_NUMS.keys()] + [r"[1-9]"]))
regex = re.compile(combined_pattern)

total = 0
with open("../input") as fin:
    for data in fin.readlines():
        print(data.strip())
        # nums = [d for d in regex.findall(data)]
        nums = find_unique_matches(data, patterns)
        print(nums)
        sub = int((''.join([num_or_str(nums[0]), num_or_str(nums[-1])])))
        print(sub)
        total = total + sub
print(total)

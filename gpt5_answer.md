Below you’ll find a comprehensive, production‑oriented toolkit for identifying (and partially parsing) Polish postal addresses in Python. It includes:

Strategy & caveats
Core building blocks (character classes, tokens)
Multiple regex patterns (strict vs. broader)
Specialized variants (street address, rural, PO Box, multi‑line)
A composite extractor with normalization heuristics
Test examples & recommended post‑processing
You will rarely want “one gigantic regex” for all Polish address forms—layered patterns give better precision + maintainability.

1. General Strategy

Polish address typical segments:

(Optional) street type: ul., al., pl., os., rondo, rynek, bulwar, skwer, most, park, droga …
Street name: can contain honorific abbreviations (św., ks., gen., marsz., prof., dr., im.), multiple words, digits (3 Maja), Roman numerals (II, III), hyphens (Bielsko-Biała), apostrophes.
Building number: 12, 12A, 12a, 12-14, 12A-14B
Unit / apartment: /7, /7A, lok. 3, m. 2, lokal 12B
Postal code: NN-NNN (00-001)
City: Capitalized, may have hyphens/spaces: Nowy Sącz, Bielsko-Biała
Voivodeship (optional, often lowercase adjectives)
Rural form: Village + number + postal code + (larger administrative city)
PO Box: (skrytka pocztowa|skr. poczt.) 45
Diacritics: ĄĆĘŁŃÓŚŹŻąćęłńóśźż
No regex can fully validate semantic correctness (e.g., that postal code fits the city). Use regex for extraction, then apply post-lookup (e.g., PNA dataset).

2. Character Classes & Token Fragments

Python’s built-in re module (as of 3.12) does NOT fully support \p{L}; for robust Unicode property usage, install the third‑party regex module. Below I provide (a) patterns using explicit Polish ranges, and (b) optional regex module forms.

Polish letter sets:

Upper: A-ZĄĆĘŁŃÓŚŹŻ
Lower: a-ząćęłńóśźż
Combined letter (no digits): [A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]
Wordy (allow digits in tokens inside names like “3” in “3 Maja”): [A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9]
Honorific / intra-name abbreviations: św\.|ks\.|bp\.|gen\.|marsz\.|prof\.|dr\.|im\.

Street types (extendable):


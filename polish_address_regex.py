import re
# If you install the 'regex' module (pip install regex), you can swap 're' for 'import regex as re'
# and (optionally) replace explicit Polish ranges with \p{L}.

FULL_ADDRESS_PATTERN = r"""
(?xi)
(?:
  (?P<street_type>ul\.|al\.|pl\.|os\.|rondo|rynek|bulwar|skwer|most|park|droga)\s+
)?
(?P<street_name>
  (?:
    (?:św\.|ks\.|bp\.|gen\.|marsz\.|prof\.|dr\.|im\.)|
    [A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9\-']+|
    [IVXLCDM]{1,5}|
    \d{1,3}
  )
  (?:\s+
    (?:
      (?:św\.|ks\.|bp\.|gen\.|marsz\.|prof\.|dr\.|im\.)|
      [A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9\-']+|
      [IVXLCDM]{1,5}|
      \d{1,3}
    )
  )*
)
\s+
(?P<building>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)
(?:
  (?P<unit_slash>/\d+[A-Za-z]?) |
  (?:\s*,?\s*(?:lok\.?|lokal|m\.)\s*(?P<unit_label>\d+[A-Za-z]?))
)?
(?:\s*,?\s*)
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
(?:\s*,\s*(?P<voivodeship>
  (?:woj\.\s*)?
  (?:dolnośląskie|kujawsko-pomorskie|lubelskie|lubuskie|łódzkie|małopolskie|mazowieckie|
     opolskie|podkarpackie|podlaskie|pomorskie|śląskie|świętokrzyskie|warmińsko-mazurskie|
     wielkopolskie|zachodniopomorskie)
))?
"""

POSTAL_CITY = r"""
(?xi)
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
"""

RURAL_ADDRESS = r"""
(?xi)
(?P<village>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
\s+
(?P<house>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)
\s+
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
"""

PO_BOX = r"""
(?xi)
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
\s+
(?:(?:skrytka\spocztowa)|(?:skr\.?\s*poczt\.?)|skrytka)
\s*(?P<po_box>\d+)
"""

MULTILINE_ADDRESS = r"""
(?xi)
(?P<street_block>
  (?:
    (?:(?:ul\.|al\.|pl\.|os\.|rondo|rynek|bulwar|skwer|most|park|droga)\s+)?
    (?:
      (?:św\.|ks\.|bp\.|gen\.|marsz\.|prof\.|dr\.|im\.)|
      [A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9\-']+|
      [IVXLCDM]{1,5}|
      \d{1,3}
    )
    (?:\s+
      (?:
        (?:św\.|ks\.|bp\.|gen\.|marsz\.|prof\.|dr\.|im\.)|
        [A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż0-9\-']+|
        [IVXLCDM]{1,5}|
        \d{1,3}
      )
    )*
    \s+\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?(?:/\d+[A-Za-z]?)?
    (?:\s*(?:,)?\s*(?:lok\.?|lokal|m\.)\s*\d+[A-Za-z]?)?
  )
)
\s*[\r\n]+\s*
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
"""

# Compile (you can reuse compiled objects)
compiled_patterns = {
    "full": re.compile(FULL_ADDRESS_PATTERN, re.VERBOSE | re.IGNORECASE),
    "postal_city": re.compile(POSTAL_CITY, re.VERBOSE | re.IGNORECASE),
    "rural": re.compile(RURAL_ADDRESS, re.VERBOSE | re.IGNORECASE),
    "po_box": re.compile(PO_BOX, re.VERBOSE | re.IGNORECASE),
    "multiline": re.compile(MULTILINE_ADDRESS, re.VERBOSE | re.IGNORECASE),
}

def normalize_street_type(street_type: str | None) -> str | None:
    if not street_type:
        return None
    mapping = {
        "ul.": "ulica",
        "al.": "aleja",
        "pl.": "plac",
        "os.": "osiedle",
    }
    st = street_type.lower()
    return mapping.get(st, st)

def pick_unit(matchdict):
    # unify unit field (prefers slash form)
    unit = matchdict.get("unit_slash")
    if unit:
        return unit.lstrip("/")
    unit_label = matchdict.get("unit_label")
    if unit_label:
        return unit_label
    return None

def score_address(d: dict) -> int:
    score = 0
    if d.get("postal_code"):
        score += 5
    if d.get("city"):
        score += 3
    if d.get("street_name"):
        score += 3
    if d.get("building"):
        score += 2
    if d.get("unit"):
        score += 1
    return score

def extract_addresses(text: str):
    results = []

    def add(kind, m):
        d = m.groupdict()
        if kind == "full":
            d["street_type_norm"] = normalize_street_type(d.get("street_type"))
            d["unit"] = pick_unit(d)
        elif kind == "multiline":
            d["unit"] = None
        elif kind == "rural":
            # create harmonized fields
            d["street_name"] = None
            d["building"] = d.get("house")
        d["kind"] = kind
        d["score"] = score_address(d)
        d["span"] = m.span()
        results.append(d)

    for kind, pattern in compiled_patterns.items():
        for m in pattern.finditer(text):
            add(kind, m)

    # De-duplicate overlaps: keep highest score for overlapping spans
    pruned = []
    used = []
    for r in sorted(results, key=lambda x: (-x["score"], x["span"][0], x["span"][1])):
        s, e = r["span"]
        if any(not (e <= us or s >= ue) for (us, ue) in used):
            # Overlaps with a better or equal previous -> skip
            continue
        used.append((s, e))
        pruned.append(r)

    # Sort by start position
    pruned.sort(key=lambda x: x["span"][0])
    return pruned

if __name__ == "__main__":
    sample = """
    ul. Jana Pawła II 12/7, 00-175 Warszawa, woj. mazowieckie
    Al. 3 Maja 5 lok. 12 31-001 Kraków
    Bielsko-Biała 43-300
    Wieś Lipowa 4 12-345 Olsztyn
    60-001 Poznań skrytka pocztowa 45
    Rondo Gen. Maczka 10 01-234 Warszawa
    ul Kwiatowa 5 m. 7 00-001 Warszawa
    """

    for addr in extract_addresses(sample):
        print(addr)

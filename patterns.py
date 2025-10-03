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



PO_BOX = r"""
(?xi)
(?P<postal_code>(?<!\d)\d{2}-\d{3}(?!\d))
\s+
(?P<city>[A-ZĄĆĘŁŃÓŚŹŻ][A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\- ]*[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])
\s+
(?:
  skrytka\spocztowa|
  skr\.?\s*poczt\.?|
  skrytka
)
\s*
(?P<po_box>\d+)
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



STREET_LINE = r"""
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
  (?:\s*(?:,)?\s*(?:lok\.?|lokal|m\.)\s*(?P<unit_label>\d+[A-Za-z]?))
)?
"""



FULL_ADDRESS_PATTERN = r"""
(?xi)                                         # Ignore case + verbose
^
(?:
  (?P<street_type>
    ul\.|al\.|pl\.|os\.|rondo|rynek|bulwar|skwer|most|park|droga
  )\s+
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
$
"""


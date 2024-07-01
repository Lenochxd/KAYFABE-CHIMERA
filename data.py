j = """
6 CHIMERA
3 CHICA & BONNIE
1 GLAMROCK CENTIPEDE
2 SOEUR LOCATION
5 KAYFABE
4 GEM KARSON
"""

def reverse_dict(dict):
    return 


ALBUM = {
    1: "GLAMROCK CENTIPEDE",
    2: "SOEUR LOCATION",
    3: "CHICA & BONNIE",
    4: "GEM KARSON",
    5: "KAYFABE",
    6: "CHIMERA",
}

ALBUM_FNAF_ORDER = [
    {
        4: "GEM KARSON",
        5: "KAYFABE",
        2: "SOEUR LOCATION",
        1: "GLAMROCK CENTIPEDE",
        6: "CHIMERA",
        3: "CHICA & BONNIE",
    },
    {
        5: "KAYFABE",
        4: "GEM KARSON",
        2: "SOEUR LOCATION",
        1: "GLAMROCK CENTIPEDE",
        6: "CHIMERA",
        3: "CHICA & BONNIE",
    },
]

ALBUM_REVERSE = reverse_dict(ALBUM)
fnaf_order = [
    [4, 5, 2, 1, 3, 6],
    [5, 4, 2, 1, 3, 6]
]


strings = [
    "GCSLGKKC", # album order  | without CHICA & BONNIE
    "GCSLCBGK", # album order  | without KAYFABE + CHIMERA
    "GKKSLGCC", # fnaf order 1 | without CHICA & BONNIE
    "GKSLGCCB", # fnaf order 1 | without KAYFABE + CHIMERA     +     fnaf order 2 | without KAYFABE + CHIMERA
    "KGKSLGCC", # fnaf order 2 | without CHICA & BONNIE
    "CKKGLSCG", # album order  | without CHICA & BONNIE                                                            + TRUE REVERSE
    "KGBCLSCG", # album order  | without KAYFABE + CHIMERA                                                         + TRUE REVERSE
    "CCGLSKKG", # fnaf order 1 | without CHICA & BONNIE                                                            + TRUE REVERSE
    "BCCGLSKG", # fnaf order 1 | without KAYFABE + CHIMERA     +     fnaf order 2 | without KAYFABE + CHIMERA      + TRUE REVERSE
    "CCGLSKGK", # fnaf order 2 | without CHICA & BONNIE                                                            + TRUE REVERSE
    "CKGKSLGC", # album order  | without CHICA & BONNIE        + REVERSE
    "GKCBSLGC", # album order  | without KAYFABE + CHIMERA     + REVERSE
    "CGCSLKGK", # fnaf order 1 | without CHICA & BONNIE        + REVERSE
    "CBGCSLGK", # fnaf order 1 | without KAYFABE + CHIMERA     + REVERSE
    "CGCSLGKK", # fnaf order 2 | without CHICA & BONNIE        + REVERSE
    "CNGCSMGK", # fnaf order 2 | without KAYFABE + CHIMERA     + REVERSE
]
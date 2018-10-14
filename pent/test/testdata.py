r"""*Supporting test data for* ``pent`` *test suite*.

``pent`` Extracts Numerical Text.

**Author**
    Brian Skinn (bskinn@alum.mit.edu)

**File Created**
    3 Sep 2018

**Copyright**
    \(c) Brian Skinn 2018

**Source Repository**
    http://www.github.com/bskinn/pent

**Documentation**
    http://pent.readthedocs.io

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

*(none documented)*

"""

from textwrap import dedent

from pent import Number, Sign


mblock_repeated_result = [
    [
        [["0.2", "0.3", "0.4"], ["0.3", "0.4", "0.6"]],
        [["0.1", "0.1", "0.1"], ["0.5", "0.5", "0.5"]],
    ],
    [
        [["0.2", "0.2", "0.2"], ["0.6", "0.6", "0.6"]],
        [["0.4", "0.4", "0.4"], ["0.8", "0.8", "0.8"]],
    ],
]

mblock_result = [
    [
        [["2.5", "-3.5", "0.8"], ["-1.2", "8.1", "-9.2"]],
        [["-0.1", "3.5", "8.1"], ["1.4", "2.2", "-4.7"]],
    ]
]


# ## OPTIONAL LINE TESTING ##

opt_1line_tail_data = [
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            FOOT
            4 5 6
            4. 5. 6.
            """
    ),
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            FOOT
            4 5 6
            4. 5. 6.
            FOOT
            """
    ),
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            4 5 6
            4. 5. 6.
            """
    ),
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            FOOT
            4 5 6
            4. 5. 6.
            FOOT
            7 8 9
            7. 8. 9.
            """
    ),
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            4 5 6
            4. 5. 6.
            FOOT
            7 8 9
            7. 8. 9.
            """
    ),
    dedent(
        """
            HEAD
            1 2 3
            1. 2. 3.
            4 5 6
            4. 5. 6.
            FOOT
            7 8 9
            7. 8. 9.
            1 2 3
            1. 2. 3.
            4 5 6
            4. 5. 6.
            7 8 9
            7. 8. 9.
            """
    ),
]

opt_1line_tail_expect_block = [
    [[[["1.", "2.", "3."]], [["4.", "5.", "6."]]]],
    [[[["1.", "2.", "3."]], [["4.", "5.", "6."]]]],
    [[[["1.", "2.", "3."]], [["4.", "5.", "6."]]]],
    [[[["1.", "2.", "3."]], [["4.", "5.", "6."]], [["7.", "8.", "9."]]]],
    [[[["1.", "2.", "3."]], [["4.", "5.", "6."]], [["7.", "8.", "9."]]]],
    [
        [
            [["1.", "2.", "3."]],
            [["4.", "5.", "6."]],
            [["7.", "8.", "9."]],
            [["1.", "2.", "3."]],
            [["4.", "5.", "6."]],
            [["7.", "8.", "9."]],
        ]
    ],
]


opt_1line_tail_expect_struct = [
    [[["FOOT"]], [[None]]],
    [[["FOOT"]], [["FOOT"]]],
    [[[None]], [[None]]],
    [[["FOOT"]], [["FOOT"]], [[None]]],
    [[[None]], [["FOOT"]], [[None]]],
    [[[None]], [["FOOT"]], [[None]], [[None]], [[None]], [[None]]],
]


# ## RESULTS FROM MeCl2F TRAJECTORY ##

orca_opt_trajectory = [
    [
        ["C", "-3.081564", "2.283942", "0.044943"],
        ["Cl", "-1.303141", "2.255173", "0.064645"],
        ["Cl", "-3.706406", "3.411601", "-1.180577"],
        ["F", "-3.541771", "2.647036", "1.270358"],
        ["H", "-3.439068", "1.277858", "-0.199370"],
    ],
    [
        ["C", "-3.081648", "2.283825", "0.044998"],
        ["Cl", "-1.303549", "2.255447", "0.064410"],
        ["Cl", "-3.705932", "3.411451", "-1.180356"],
        ["F", "-3.541734", "2.647080", "1.270327"],
        ["H", "-3.439088", "1.277807", "-0.199379"],
    ],
    [
        ["C", "-3.081658", "2.283823", "0.045015"],
        ["Cl", "-1.303660", "2.255530", "0.064310"],
        ["Cl", "-3.705773", "3.411404", "-1.180315"],
        ["F", "-3.541755", "2.647054", "1.270344"],
        ["H", "-3.439104", "1.277799", "-0.199355"],
    ],
    [
        ["C", "-3.081652", "2.283830", "0.045009"],
        ["Cl", "-1.303667", "2.255543", "0.064291"],
        ["Cl", "-3.705749", "3.411402", "-1.180318"],
        ["F", "-3.541768", "2.647034", "1.270350"],
        ["H", "-3.439114", "1.277801", "-0.199333"],
    ],
    [
        ["C", "-3.081644", "2.283834", "0.044998"],
        ["Cl", "-1.303664", "2.255550", "0.064283"],
        ["Cl", "-3.705739", "3.411406", "-1.180323"],
        ["F", "-3.541778", "2.647018", "1.270354"],
        ["H", "-3.439125", "1.277801", "-0.199312"],
    ],
    [
        ["C", "-3.081641", "2.283833", "0.044991"],
        ["Cl", "-1.303664", "2.255552", "0.064285"],
        ["Cl", "-3.705739", "3.411409", "-1.180321"],
        ["F", "-3.541778", "2.647016", "1.270352"],
        ["H", "-3.439128", "1.277800", "-0.199306"],
    ],
    [
        ["C", "-3.081640", "2.283831", "0.044988"],
        ["Cl", "-1.303664", "2.255552", "0.064288"],
        ["Cl", "-3.705742", "3.411409", "-1.180319"],
        ["F", "-3.541776", "2.647018", "1.270351"],
        ["H", "-3.439128", "1.277799", "-0.199307"],
    ],
]


# ## RESULTS FROM THE MeCl2F OPT ##

orca_opt_status = [
    [
        ["0.0024289062", "NO"],
        ["0.0065808923", "NO"],
        ["0.0048284586", "NO"],
        ["0.0108762300", "NO"],
    ],
    [
        ["-0.0000653231", "NO"],
        ["0.0005199502", "NO"],
        ["0.0015186205", "NO"],
        ["0.0012185918", "NO"],
        ["0.0032642139", "NO"],
    ],
    [
        ["-0.0000039726", "NO"],
        ["0.0001930565", "NO"],
        ["0.0002722358", "NO"],
        ["0.0008093394", "NO"],
        ["0.0013068540", "NO"],
    ],
    [
        ["-0.0000009297", "YES"],
        ["0.0000709147", "NO"],
        ["0.0000900825", "NO"],
        ["0.0002786532", "YES"],
        ["0.0004283776", "YES"],
    ],
    [
        ["-0.0000000980", "YES"],
        ["0.0000166787", "NO"],
        ["0.0000402499", "NO"],
        ["0.0000461600", "YES"],
        ["0.0000852600", "YES"],
    ],
    [
        ["-0.0000000039", "YES"],
        ["0.0000035084", "NO"],
        ["0.0000054911", "NO"],
        ["0.0000111518", "YES"],
        ["0.0000176674", "YES"],
    ],
    [
        ["-0.0000000003", "YES"],
        ["0.0000007831", "NO"],
        ["0.0000014120", "NO"],
        ["0.0000033697", "YES"],
        ["0.0000063852", "YES"],
    ],
]

orca_opt_status_optline = [
    [
        [
            None,
            None,
            "0.0024289062",
            "NO",
            "0.0065808923",
            "NO",
            "0.0048284586",
            "NO",
            "0.0108762300",
            "NO",
            "0.0058",
            "0.25",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000653231",
            "NO",
            "0.0005199502",
            "NO",
            "0.0015186205",
            "NO",
            "0.0012185918",
            "NO",
            "0.0032642139",
            "NO",
            "0.0017",
            "0.08",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000039726",
            "NO",
            "0.0001930565",
            "NO",
            "0.0002722358",
            "NO",
            "0.0008093394",
            "NO",
            "0.0013068540",
            "NO",
            "0.0007",
            "0.06",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000009297",
            "YES",
            "0.0000709147",
            "NO",
            "0.0000900825",
            "NO",
            "0.0002786532",
            "YES",
            "0.0004283776",
            "YES",
            "0.0002",
            "0.02",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000000980",
            "YES",
            "0.0000166787",
            "NO",
            "0.0000402499",
            "NO",
            "0.0000461600",
            "YES",
            "0.0000852600",
            "YES",
            "0.0000",
            "0.00",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000000039",
            "YES",
            "0.0000035084",
            "NO",
            "0.0000054911",
            "NO",
            "0.0000111518",
            "YES",
            "0.0000176674",
            "YES",
            "0.0000",
            "0.00",
            "0.00",
            "0.00",
        ]
    ],
    [
        [
            "-0.0000000003",
            "YES",
            "0.0000007831",
            "NO",
            "0.0000014120",
            "NO",
            "0.0000033697",
            "YES",
            "0.0000063852",
            "YES",
            "0.0000",
            "0.00",
            "0.00",
            "0.00",
        ]
    ],
]


# ## RESULTS FROM THE CU_CAS ##

orca_cas_states = [
    [
        [
            ["0.55109", "7", "1211101"],
            ["0.25785", "13", "1121011"],
            ["0.15330", "0", "2111110"],
            ["0.02415", "6", "1211110"],
            ["0.00449", "35", "1011121"],
            ["0.00303", "29", "1101211"],
        ],
        [
            ["0.93636", "6", "1211110"],
            ["0.02120", "0", "2111110"],
            ["0.01554", "13", "1121011"],
            ["0.01547", "1", "2111101"],
            ["0.00278", "41", "0111121"],
            ["0.00253", "8", "1211011"],
        ],
        [
            ["0.69127", "8", "1211011"],
            ["0.25478", "12", "1121101"],
            ["0.03002", "2", "2111011"],
            ["0.00388", "7", "1211101"],
            ["0.00380", "30", "1101121"],
            ["0.00337", "23", "1111021"],
            ["0.00334", "6", "1211110"],
            ["0.00271", "11", "1121110"],
        ],
        [
            ["0.65472", "0", "2111110"],
            ["0.15679", "11", "1121110"],
            ["0.07698", "7", "1211101"],
            ["0.04636", "13", "1121011"],
            ["0.04407", "1", "2111101"],
            ["0.00506", "21", "1111111"],
            ["0.00335", "2", "2111011"],
            ["0.00321", "42", "0111112"],
            ["0.00259", "12", "1121101"],
        ],
    ],
    [
        [
            ["0.48295", "68", "1221001"],
            ["0.32173", "0", "2211100"],
            ["0.15917", "11", "2121010"],
            ["0.01379", "67", "1221010"],
            ["0.00650", "126", "1111111"],
            ["0.00278", "92", "1201201"],
            ["0.00259", "160", "1021021"],
        ],
        [
            ["0.88192", "66", "1221100"],
            ["0.05916", "1", "2211010"],
            ["0.03329", "2", "2211001"],
            ["0.00418", "10", "2121100"],
            ["0.00388", "157", "1021120"],
            ["0.00339", "123", "1111210"],
            ["0.00274", "214", "0121111"],
        ],
        [
            ["0.76084", "67", "1221010"],
            ["0.09245", "0", "2211100"],
            ["0.05911", "68", "1221001"],
            ["0.05725", "11", "2121010"],
            ["0.00500", "1", "2211010"],
            ["0.00351", "12", "2121001"],
            ["0.00349", "91", "1201210"],
            ["0.00306", "125", "1111120"],
        ],
        [
            ["0.40671", "68", "1221001"],
            ["0.30328", "0", "2211100"],
            ["0.17898", "67", "1221010"],
            ["0.04452", "11", "2121010"],
            ["0.03751", "12", "2121001"],
            ["0.00669", "1", "2211010"],
            ["0.00514", "126", "1111111"],
        ],
    ],
    [
        [
            ["0.97008", "0", "2221000"],
            ["0.00613", "44", "2111110"],
            ["0.00492", "141", "1211101"],
            ["0.00457", "178", "1121011"],
            ["0.00402", "17", "2201200"],
            ["0.00393", "275", "0221002"],
            ["0.00384", "81", "2021020"],
        ],
        [
            ["0.93374", "126", "1222000"],
            ["0.02074", "269", "0222001"],
            ["0.00812", "136", "1212100"],
            ["0.00717", "172", "1122010"],
            ["0.00574", "30", "2122000"],
            ["0.00543", "188", "1112110"],
            ["0.00396", "129", "1221001"],
            ["0.00380", "152", "1202200"],
            ["0.00341", "225", "1022020"],
        ],
        [
            ["0.94890", "4", "2212000"],
            ["0.02277", "138", "1212001"],
            ["0.00489", "41", "2112010"],
            ["0.00356", "94", "2012020"],
            ["0.00334", "191", "1112011"],
            ["0.00291", "57", "2102110"],
            ["0.00284", "14", "2202100"],
        ],
        [
            ["0.93053", "30", "2122000"],
            ["0.02488", "173", "1122001"],
            ["0.00873", "76", "2022010"],
            ["0.00721", "126", "1222000"],
            ["0.00399", "56", "2102200"],
            ["0.00380", "189", "1112101"],
            ["0.00332", "40", "2112100"],
            ["0.00266", "92", "2012110"],
        ],
    ],
]


# ## RESULTS FROM THE C2F4_01.hess FILE ##

orca_hess_dipders = [
    [
        ["-1.041194", "0.077425", "-0.236446"],
        ["0.021347", "-0.053665", "0.064080"],
        ["-0.064917", "0.064030", "-0.228121"],
        ["1.334075", "0.025554", "-0.077999"],
        ["0.025455", "0.179824", "-0.349540"],
        ["-0.078013", "-0.349384", "1.132034"],
        ["-0.292885", "-0.102966", "0.314406"],
        ["-0.046806", "-0.126137", "0.285463"],
        ["0.142946", "0.285361", "-0.903922"],
        ["1.334072", "0.025555", "-0.078001"],
        ["0.025456", "0.179823", "-0.349540"],
        ["-0.078015", "-0.349384", "1.132038"],
        ["-1.041194", "0.077424", "-0.236443"],
        ["0.021345", "-0.053666", "0.064079"],
        ["-0.064912", "0.064030", "-0.228121"],
        ["-0.292884", "-0.102965", "0.314403"],
        ["-0.046806", "-0.126136", "0.285464"],
        ["0.142945", "0.285362", "-0.903926"],
    ]
]


orca_hess_freqs = [
    [
        ["0.000000"],
        ["0.000000"],
        ["0.000000"],
        ["0.000000"],
        ["0.000000"],
        ["0.000000"],
        ["194.490162"],
        ["198.587114"],
        ["389.931897"],
        ["402.713910"],
        ["538.244274"],
        ["542.017838"],
        ["548.246738"],
        ["800.613516"],
        ["1203.096114"],
        ["1342.200360"],
        ["1349.543713"],
        ["1885.157022"],
    ]
]


# ## SAMPLE NUMBERS AND MATCHING TOKENS ##

number_token_template = "#{{0}}{{1}}{{2}}{0}"

number_patterns = {
    "123": number_token_template.format(".i"),
    "-123": number_token_template.format("-i"),
    "+123": number_token_template.format("+i"),
    "0.2": number_token_template.format(".f"),
    "-.285": number_token_template.format("-f"),
    "+315.": number_token_template.format("+f"),
    "3e5": number_token_template.format(".s"),
    "-.13e+5": number_token_template.format("-s"),
    "+3.1e-5": number_token_template.format("+s"),
    ".266": number_token_template.format(".d"),
    "-15.285": number_token_template.format("-d"),
    "+315.185": number_token_template.format("+d"),
    "35": number_token_template.format(".g"),
    "-.13": number_token_template.format("-g"),
    "+3.1e+15": number_token_template.format("+g"),
}

assert len(number_patterns) == 15


# ## EXHAUSTIVE MATCHES OF NUMBERS TO NUMBER/SIGN TYPES ##

number_sign_vals = {
    "0": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-0": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): True,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+0.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-.00": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+35": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "23": {
        (Number.Integer, Sign.Positive): True,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-12": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): True,
        (Number.Integer, Sign.Any): True,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    ".12": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "35.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+218.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.355": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "0.23": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): True,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-.22": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "-234.": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "-392.34": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): True,
        (Number.Float, Sign.Any): True,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+3e3": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3e+3": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3e+003": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "3e+003": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+3.e5": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+2e-04": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.34e23": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "+.48e-2": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): True,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): True,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): True,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): True,
    },
    "-2e-04": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): True,
        (Number.SciNot, Sign.Any): True,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): True,
        (Number.Decimal, Sign.Any): True,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): True,
        (Number.General, Sign.Any): True,
    },
    "+-0.39": {
        (Number.Integer, Sign.Positive): False,
        (Number.Integer, Sign.Negative): False,
        (Number.Integer, Sign.Any): False,
        (Number.Float, Sign.Positive): False,
        (Number.Float, Sign.Negative): False,
        (Number.Float, Sign.Any): False,
        (Number.SciNot, Sign.Positive): False,
        (Number.SciNot, Sign.Negative): False,
        (Number.SciNot, Sign.Any): False,
        (Number.Decimal, Sign.Positive): False,
        (Number.Decimal, Sign.Negative): False,
        (Number.Decimal, Sign.Any): False,
        (Number.General, Sign.Positive): False,
        (Number.General, Sign.Negative): False,
        (Number.General, Sign.Any): False,
    },
    # INVALID VALUES... complex(?), etc.
}

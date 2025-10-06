import inspect
import pprint

from video.captions.subtitles_circuitAnime_basic import generateSubtitles_findEquations, generateSubtitles_solvingSteps


pp = pprint.PrettyPrinter(indent=4)

def test_generateSubtitles_findEquations(verbose=False):

    #used to tell the viewer what type it is?
    nodeId__type = {0: 'resistor', 1: 'wire', 2: 'wire', 3: 'resistor', 4: 'wire', 5: 'wire', 6: 'wire', 7: 'wire', 8: 'battery', 9: 'wire', 10: 'wire'}

    #used to display each variable
    textStr__textMeshUUID = {#<<<<check if basic.js needs all these keys, then we can make the anime slightly more light weight
    "-I_{DC_{8}}+I_{R_{0}}+I_{R_{3}}=0": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 1,
                "endPos": 11,
                "info": [
                    [
                        "I",
                        "89d94075-50b0-44e1-908a-eddc38feb021"
                    ],
                    [
                        "D",
                        "2ec2f07a-f864-43b5-bfb9-6150813629a4"
                    ],
                    [
                        "C",
                        "b979f2dd-f696-41e2-99c3-44d2d8828b5c"
                    ],
                    [
                        "8",
                        "24d8be0c-2c94-4ab0-b608-c3c7f538730d"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 12,
                "endPos": 21,
                "info": [
                    [
                        "I",
                        "f8b755f9-71a9-4a30-8d32-30cee48b1d0c"
                    ],
                    [
                        "R",
                        "bf0003fb-195b-4e91-ac3d-69fc722acb54"
                    ],
                    [
                        "0",
                        "c54c2cdb-55f0-40e5-8e21-d9d906eb26bf"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 22,
                "endPos": 31,
                "info": [
                    [
                        "I",
                        "d1074299-5d40-4845-9e01-7c731d3ece38"
                    ],
                    [
                        "R",
                        "e2e47b16-754f-40ad-b0a0-3cc3de2b7781"
                    ],
                    [
                        "3",
                        "d88749ef-aff9-4694-9e58-1874ffafa8e0"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "78beb9ae-b859-4ee2-ace2-6c1a97434633"
    },
    "-V_{R_{0}}+V_{DC_{8}}=0": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 1,
                "endPos": 10,
                "info": [
                    [
                        "V",
                        "e05d97cf-ba23-44c0-9a9e-6262e74ea7d6"
                    ],
                    [
                        "R",
                        "e43893cb-7eda-4674-a233-5f4eded27355"
                    ],
                    [
                        "0",
                        "102bae5f-d102-4cb8-84b5-7a658cab161b"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 11,
                "endPos": 21,
                "info": [
                    [
                        "V",
                        "03ffe383-bbb1-4777-aa43-ed61cbfa7a73"
                    ],
                    [
                        "D",
                        "1431e5ad-c938-4a03-8b1f-552b2bb504be"
                    ],
                    [
                        "C",
                        "e2f1e782-1010-4f6a-b7d6-ccf42accfd8b"
                    ],
                    [
                        "8",
                        "de787a99-af9c-4479-b604-94dbd38b4f4b"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "cd184e5f-658a-4a80-8486-52bdcc492cdb"
    },
    "V_{DC_{8}}-V_{R_{3}}=0": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 0,
                "endPos": 10,
                "info": [
                    [
                        "V",
                        "b6af477a-7b5e-41c4-93c9-8b17ab916f06"
                    ],
                    [
                        "D",
                        "bcf7024d-16ef-4ceb-a412-83d40470a93d"
                    ],
                    [
                        "C",
                        "745cdadb-182c-4ab9-a030-74123ccfe935"
                    ],
                    [
                        "8",
                        "4752a6e1-51e2-4e4b-b908-42d7e02859ec"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 11,
                "endPos": 20,
                "info": [
                    [
                        "V",
                        "9e7d1dbf-525e-4b3c-bc48-8e9dc75b7845"
                    ],
                    [
                        "R",
                        "d710e39b-8b42-4b78-b1f6-b39ac3265f83"
                    ],
                    [
                        "3",
                        "a1e2c932-6362-49db-bbae-f7f7a98b91f9"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "10cca465-3f43-4149-8904-5a086b0ec174"
    },
    "\\frac{V_{R_{0}}}{I_{R_{0}}}=R_{R_{0}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 6,
                "endPos": 15,
                "info": [
                    [
                        "V",
                        "7a01e5d9-e77c-4709-8e5f-2577ab5b7aab"
                    ],
                    [
                        "R",
                        "a8641b98-4558-47c3-8d4c-3f1c82e2949e"
                    ],
                    [
                        "0",
                        "fe5c35f3-9c05-41a8-a93d-34ae20665d16"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 17,
                "endPos": 26,
                "info": [
                    [
                        "I",
                        "974ed162-0fbf-4f16-a8a2-c540469f62f5"
                    ],
                    [
                        "R",
                        "af181b26-2b03-47b7-a436-6bc32bac7f62"
                    ],
                    [
                        "0",
                        "ebcce8e1-b76e-4962-8372-06c22e38a9b7"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 28,
                "endPos": 37,
                "info": [
                    [
                        "R",
                        "ed1b2ff9-cce2-40bd-b106-cb1cc36ee9c3"
                    ],
                    [
                        "R",
                        "49368d76-ab2f-4918-974b-33a2a95cfcef"
                    ],
                    [
                        "0",
                        "cc374f0a-c9f4-4014-91ab-999794cea4c9"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "10c68f92-b296-4a99-904e-5103e900efef"
    },
    "\\frac{V_{R_{3}}}{I_{R_{3}}}=R_{R_{3}}": {
        "info": [
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 6,
                "endPos": 15,
                "info": [
                    [
                        "V",
                        "b51d7ee1-9edb-4e38-9707-3e3296a553c1"
                    ],
                    [
                        "R",
                        "f61583f5-92c1-4436-b5df-4d3985b6404c"
                    ],
                    [
                        "3",
                        "85a0b90c-0ca9-4ebc-80a4-0ed0d7613480"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 17,
                "endPos": 26,
                "info": [
                    [
                        "I",
                        "33591c20-a95d-48a4-b51c-e0ffd1e74bb2"
                    ],
                    [
                        "R",
                        "db9773e3-37f1-4749-8473-cb080b5a1b47"
                    ],
                    [
                        "3",
                        "017dd7c8-4ba2-4d18-af45-0027146c0e35"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 28,
                "endPos": 37,
                "info": [
                    [
                        "R",
                        "9aa9becf-c1c7-4363-aabd-62791e85a895"
                    ],
                    [
                        "R",
                        "3320dea9-ba8c-456a-b91e-f8fe126e169d"
                    ],
                    [
                        "3",
                        "4472324b-b7c1-4b81-9d80-bbe5289fdff0"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "5d8c8d5f-2f9e-4215-a7b9-429e2196bc9a"
    },
    "\\frac{V_{DC_{8}}}{I_{DC_{8}}}=R_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 6,
                "endPos": 16,
                "info": [
                    [
                        "V",
                        "fa1fb946-9e0e-4364-b6dd-24b9a6fc448e"
                    ],
                    [
                        "D",
                        "cacdf298-685f-4874-bc01-a452fc65abd8"
                    ],
                    [
                        "C",
                        "154e5ac9-0d55-4fc6-91d9-b4a669072cd5"
                    ],
                    [
                        "8",
                        "7a26a43a-aaba-42cc-80c8-69d6de7f9bf5"
                    ]
                ]
            },
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 18,
                "endPos": 28,
                "info": [
                    [
                        "I",
                        "98b76d6b-6783-4c46-ac20-1a7bad0de6ea"
                    ],
                    [
                        "D",
                        "d09f05e6-2f24-4045-820a-9782a8aec093"
                    ],
                    [
                        "C",
                        "5702a067-c9f6-4fe8-9c13-2101d1013301"
                    ],
                    [
                        "8",
                        "f4ac47da-92d7-4065-a2b4-b98e87a446af"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 30,
                "endPos": 40,
                "info": [
                    [
                        "R",
                        "34bc0f0f-0aa2-4ddc-970a-16dfd41a4d69"
                    ],
                    [
                        "D",
                        "8595b345-5536-463d-aae1-d98d75c6168b"
                    ],
                    [
                        "C",
                        "dfd074df-bde3-4abb-91de-8b2c4a67db32"
                    ],
                    [
                        "8",
                        "bd5c98f2-46bd-4686-9e84-eb1b09a36f19"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "fb785fac-6e45-468d-aeda-1a3674677f01"
    },
    "(-I_{DC_{8}}+I_{R_{0}})+I_{R_{3}}=0": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 2,
                "endPos": 12,
                "info": [
                    [
                        "I",
                        "806284c2-2867-4add-bea2-b9201979e670"
                    ],
                    [
                        "D",
                        "ecda3d36-fd97-4260-a4c8-66043e8fc7fb"
                    ],
                    [
                        "C",
                        "66e88690-e62b-455e-9671-9605a948010f"
                    ],
                    [
                        "8",
                        "6c0da8d3-28c4-4107-85a5-b6765ae98fdc"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 13,
                "endPos": 22,
                "info": [
                    [
                        "I",
                        "6d6a6d9c-7190-4155-a45e-effb4d8d1508"
                    ],
                    [
                        "R",
                        "9488c0dc-3ac3-47dc-a3d3-bfd133093397"
                    ],
                    [
                        "0",
                        "a7d97a52-3035-42cd-a447-854d3d8c5a9f"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 24,
                "endPos": 33,
                "info": [
                    [
                        "I",
                        "901788d5-023f-4570-a25d-0474bb02e859"
                    ],
                    [
                        "R",
                        "fcfefc4b-affe-47d5-8024-10fe42315a8a"
                    ],
                    [
                        "3",
                        "5a165927-51a7-4b66-8ff9-ade65d833e2e"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "9b6b2bc9-92f9-436a-bbb2-a4bd42de9ff6"
    },
    "-I_{DC_{8}}+I_{R_{0}}=-I_{R_{3}}": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 1,
                "endPos": 11,
                "info": [
                    [
                        "I",
                        "1b8d1f20-028c-480b-8dfd-c5ccdb3b4a29"
                    ],
                    [
                        "D",
                        "51691657-f4f8-4835-bcb4-341c7d79f597"
                    ],
                    [
                        "C",
                        "bf08ccb7-4a84-40c1-8112-9936fe8b2f08"
                    ],
                    [
                        "8",
                        "fdd510d6-2e09-4a28-8991-891a78a3318e"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 12,
                "endPos": 21,
                "info": [
                    [
                        "I",
                        "df0fb06c-876c-4547-a4e3-ceb9443419dc"
                    ],
                    [
                        "R",
                        "86438d3f-5dde-4009-97a3-fe9d943eb5de"
                    ],
                    [
                        "0",
                        "7eb14254-b5bc-4474-8165-78a10f5e6add"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 23,
                "endPos": 32,
                "info": [
                    [
                        "I",
                        "daca82b2-ac54-4a7d-aad7-4a5ad27b02ce"
                    ],
                    [
                        "R",
                        "f936e2c4-e9cc-4ffb-bf7c-d0204697b978"
                    ],
                    [
                        "3",
                        "64688870-8998-436a-af1a-280d9e64d328"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "24cce376-22e6-4af9-b51d-4655f21f6255"
    },
    "-I_{DC_{8}}=-I_{R_{3}}-I_{R_{0}}": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 1,
                "endPos": 11,
                "info": [
                    [
                        "I",
                        "433e463e-f024-435a-a068-c53434411ef4"
                    ],
                    [
                        "D",
                        "a51ce515-ec40-4ea1-be8e-d4cb825dc3ab"
                    ],
                    [
                        "C",
                        "346d3970-b461-4c8c-a85a-cc889b7c684a"
                    ],
                    [
                        "8",
                        "d9d1dd49-10a8-49de-a665-dd0495e52410"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 13,
                "endPos": 22,
                "info": [
                    [
                        "I",
                        "b9eb899a-81de-43be-90df-52cc6b13e4c7"
                    ],
                    [
                        "R",
                        "b459416c-6011-42d7-9d3d-1735f8f6619e"
                    ],
                    [
                        "3",
                        "1b56cd1a-25b9-4049-a687-c980aafae99c"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 23,
                "endPos": 32,
                "info": [
                    [
                        "I",
                        "95fc4e3d-4a0d-47b2-b1ff-62375d0479ab"
                    ],
                    [
                        "R",
                        "6bddf4cc-9f51-4c65-897d-702d8d5afd0e"
                    ],
                    [
                        "0",
                        "08c943e4-1fc3-4d26-a536-45b1bdda21c8"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "36ce058e-d6be-4b37-ad8e-f3ce2a15c46c"
    },
    "I_{DC_{8}}=--I_{R_{3}}-I_{R_{0}}": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 0,
                "endPos": 10,
                "info": [
                    [
                        "I",
                        "175f62fc-42f0-489e-b8b7-afbef710dd5c"
                    ],
                    [
                        "D",
                        "f811702f-0a9f-44a4-9ce1-9a2552ef9028"
                    ],
                    [
                        "C",
                        "b8941543-6795-42c5-a643-26154073c070"
                    ],
                    [
                        "8",
                        "e83112f9-54c8-42e1-80ac-0758bc94a2e7"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 13,
                "endPos": 22,
                "info": [
                    [
                        "I",
                        "4c07447a-c1d2-46a3-9bb8-c797cce2d752"
                    ],
                    [
                        "R",
                        "faf5ff84-075b-409a-8e2b-1e99ce5180e4"
                    ],
                    [
                        "3",
                        "e18c9af9-0aa9-4f48-b2b4-4fa8ef15dc17"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 23,
                "endPos": 32,
                "info": [
                    [
                        "I",
                        "543753e4-0fe1-4c29-bcb7-757359123776"
                    ],
                    [
                        "R",
                        "5d20ff39-91d6-4580-add8-648f7bd62531"
                    ],
                    [
                        "0",
                        "ad597046-1e53-4689-8caa-f3a9e1042f50"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "67e6a167-616b-4561-b972-d71a406987db"
    },
    "I_{DC_{8}}=I_{R_{3}}+I_{R_{0}}": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 0,
                "endPos": 10,
                "info": [
                    [
                        "I",
                        "891cf11d-8b62-4db4-80fc-42894412ee1f"
                    ],
                    [
                        "D",
                        "2902b3cd-63bb-45b0-a650-750e45a77a1c"
                    ],
                    [
                        "C",
                        "b8bbf396-c441-4125-bd9d-bd6ca87d189d"
                    ],
                    [
                        "8",
                        "cefec9e3-9125-49f9-8eef-20fd8dcaac42"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 11,
                "endPos": 20,
                "info": [
                    [
                        "I",
                        "b743085c-5d36-4603-ba6d-0d821718958d"
                    ],
                    [
                        "R",
                        "8010b568-8207-4ed2-be57-0805acb07a81"
                    ],
                    [
                        "3",
                        "f42b5de1-bd96-44a0-955d-44aa3d328314"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 21,
                "endPos": 30,
                "info": [
                    [
                        "I",
                        "7e2667a2-3c21-4dab-b86b-a7b51339f994"
                    ],
                    [
                        "R",
                        "8ab47b84-8266-4386-a4f2-8250c64828b5"
                    ],
                    [
                        "0",
                        "35b9352e-dfe4-47d9-9495-dc7d2a4037b1"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "f2c6183a-7212-49db-8440-b6c303ee7619"
    },
    "I_{DC_{8}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}": {
        "info": [
            {
                "variableStr": "I_{DC_{8}}",
                "startPos": 0,
                "endPos": 10,
                "info": [
                    [
                        "I",
                        "5b63326d-3a7d-4f5e-915f-c29ada2e5ba9"
                    ],
                    [
                        "D",
                        "0ac2110b-73c8-4e4b-aa59-c3d5b6234b45"
                    ],
                    [
                        "C",
                        "c7383590-0a70-4554-8b88-4a82e0951f26"
                    ],
                    [
                        "8",
                        "e4390bdd-10ff-4eb7-b369-84d069f6af53"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 17,
                "endPos": 27,
                "info": [
                    [
                        "V",
                        "10be2bb6-a29d-4d6a-86f0-699f32e9e26c"
                    ],
                    [
                        "D",
                        "2a645e79-ddc6-4e80-82b1-15387114b480"
                    ],
                    [
                        "C",
                        "5af6624f-bc7b-4721-bf97-6a8e5c88ff81"
                    ],
                    [
                        "8",
                        "0065e572-ae3a-4c6a-bab3-4085f440ce95"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 29,
                "endPos": 39,
                "info": [
                    [
                        "R",
                        "c5030eb7-5971-429c-ae6e-f43c6f9dcd17"
                    ],
                    [
                        "D",
                        "24fdd142-aa9e-435d-9d2e-8d50d7bce661"
                    ],
                    [
                        "C",
                        "5398bc9e-839f-45b8-b401-da9c09b8c121"
                    ],
                    [
                        "8",
                        "f0e8d260-8532-4038-a9b9-c78da39f0464"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "3e3c2816-f93d-4bef-b5c7-bb43caccfcc9"
    },
    "I_{R_{3}}+I_{R_{0}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 26,
                "endPos": 36,
                "info": [
                    [
                        "V",
                        "e511fe0b-805b-4188-8563-42018428c2cb"
                    ],
                    [
                        "D",
                        "30307b5d-5ea7-43dc-8bca-59c71bc11295"
                    ],
                    [
                        "C",
                        "dfea9666-9dfb-4509-bee3-26f0ec0e8f8f"
                    ],
                    [
                        "8",
                        "0eda49c1-446a-401b-b70d-5621200f0faa"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 38,
                "endPos": 48,
                "info": [
                    [
                        "R",
                        "058d6f88-2210-4277-9222-c49676119c5a"
                    ],
                    [
                        "D",
                        "5a4e02ba-4151-49fa-b637-b69bf33a3e18"
                    ],
                    [
                        "C",
                        "edb8c80b-a135-4018-bde5-59acb8f55068"
                    ],
                    [
                        "8",
                        "aa733a93-c9e7-47f5-9d75-97a93b821d42"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "bf2abe3a-49e7-4e66-8a0b-41b95434b8f5"
    },
    "I_{R_{0}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-I_{R_{3}}": {
        "info": [
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "I",
                        "bdb162a6-afc7-49dd-91b8-b633a243b83f"
                    ],
                    [
                        "R",
                        "a26b717f-5bf6-4534-8388-cb2a46018bbd"
                    ],
                    [
                        "0",
                        "cf2a3b12-8788-4c14-9a4b-dcebe59b7f0d"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 16,
                "endPos": 26,
                "info": [
                    [
                        "V",
                        "6d4ce4c7-8c61-487e-962e-83923f28a1cc"
                    ],
                    [
                        "D",
                        "7a153230-f12b-4976-97bf-89aa6e7e87eb"
                    ],
                    [
                        "C",
                        "0f30791a-e01c-4e75-9dc3-1680935b793f"
                    ],
                    [
                        "8",
                        "18c9c472-f19a-41ea-8c69-9e7ebefce0cb"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 28,
                "endPos": 38,
                "info": [
                    [
                        "R",
                        "9fbcf52b-7e4e-46e8-8235-e9223f44efea"
                    ],
                    [
                        "D",
                        "8d6f7142-225d-45f5-a148-4de6b057aecb"
                    ],
                    [
                        "C",
                        "c44663ce-88e6-4602-bf6a-8eeccdfbb708"
                    ],
                    [
                        "8",
                        "19f2dc22-b639-4f85-a02f-3017f1c3386a"
                    ]
                ]
            },
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 40,
                "endPos": 49,
                "info": [
                    [
                        "I",
                        "98fdaadd-a1cb-435a-979e-2b8b8aadf114"
                    ],
                    [
                        "R",
                        "d4f5bf21-ed54-4895-8829-8c50e7909cb1"
                    ],
                    [
                        "3",
                        "72ba209d-3a2b-487d-98c1-070c86826532"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "24164f2c-02a2-4e67-a43e-3739a729018a"
    },
    "I_{R_{0}}=\\frac{V_{R_{0}}}{R_{R_{0}}}": {
        "info": [
            {
                "variableStr": "I_{R_{0}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "I",
                        "045e7d89-e037-40c3-8e33-5aed37f5c8b2"
                    ],
                    [
                        "R",
                        "556c0b9f-3119-4f95-9639-c6c1dcffc9ba"
                    ],
                    [
                        "0",
                        "556bdca0-5047-4fd5-9252-e43c982a8aa5"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 16,
                "endPos": 25,
                "info": [
                    [
                        "V",
                        "9a4e113a-9c06-4736-80c1-90ac386e2c86"
                    ],
                    [
                        "R",
                        "3d1b8b4d-de7f-419f-9149-893be863bd50"
                    ],
                    [
                        "0",
                        "0464c0a3-9c9f-4189-a75a-3e799c735f3e"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 27,
                "endPos": 36,
                "info": [
                    [
                        "R",
                        "3d7f9806-6881-4327-8a8a-6a4497b51faf"
                    ],
                    [
                        "R",
                        "0ee881b9-bf8a-464e-b4d0-0fad6f540ad4"
                    ],
                    [
                        "0",
                        "9e1f32be-dad4-4791-9d06-b32146026e93"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "319b4970-fbc6-4a53-b73e-6478f87c8557"
    },
    "\\frac{V_{DC_{8}}}{R_{DC_{8}}}-I_{R_{3}}=\\frac{V_{R_{0}}}{R_{R_{0}}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 46,
                "endPos": 55,
                "info": [
                    [
                        "V",
                        "4bad3d8b-7508-4252-bc4d-0c07154e9f5f"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 57,
                "endPos": 66,
                "info": [
                    [
                        "R",
                        "a96f4c72-4899-476b-8037-a7b93c77eb4c"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 57,
                "endPos": 66,
                "info": [
                    [
                        "R",
                        "e6d670a3-d04b-4ea2-a5b6-fa732853e645"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 57,
                "endPos": 66,
                "info": [
                    [
                        "0",
                        "397e02d4-d8a3-4466-8401-4b30b025478e"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "39c41143-f9dd-4f3b-92b9-5dd13a978677"
    },
    "I_{R_{3}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}": {
        "info": [
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "I",
                        "6b9edf71-229c-41e4-8212-20942cc20766"
                    ],
                    [
                        "R",
                        "ff540566-a4e9-415a-b373-e7c5afa91448"
                    ],
                    [
                        "3",
                        "9820a24d-1aef-4a3e-b087-8bcbff734bf5"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 16,
                "endPos": 26,
                "info": [
                    [
                        "V",
                        "47d223e8-82d5-4ac2-ad51-eaddbd267640"
                    ],
                    [
                        "D",
                        "aeee64ef-9755-4761-a665-767d31b63904"
                    ],
                    [
                        "C",
                        "849c822d-0d09-40d0-8861-92791b5216a4"
                    ],
                    [
                        "8",
                        "0cd54e99-d895-41f0-83fb-77eb84a8df59"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 28,
                "endPos": 38,
                "info": [
                    [
                        "R",
                        "b7d9718c-2fd2-48cd-bebd-78feb3cdb0e9"
                    ],
                    [
                        "D",
                        "0c711efa-6344-442e-8e13-c11332527d24"
                    ],
                    [
                        "C",
                        "61ad7846-0307-4f60-88fd-1b827a3a85df"
                    ],
                    [
                        "8",
                        "3ed300fd-cff4-4105-a35d-78293b894ab1"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 46,
                "endPos": 55,
                "info": [
                    [
                        "V",
                        "3e60c968-3992-4697-a6b9-946cb9a84da7"
                    ],
                    [
                        "R",
                        "7bdec9ff-14d2-476a-b5e0-d8ce4e9ba603"
                    ],
                    [
                        "0",
                        "fe304f43-4c8f-439c-8a8e-9f9a2d4a0f10"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 57,
                "endPos": 66,
                "info": [
                    [
                        "R",
                        "9cf7dd44-b494-4f87-af30-9dfb9fec9a2c"
                    ],
                    [
                        "R",
                        "2ba009d8-d990-43b8-a0dc-42309e085bc7"
                    ],
                    [
                        "0",
                        "8c19502d-79bb-484c-94a6-b50bb28c431e"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "b332bba4-f202-4a05-b32a-51dbbd455400"
    },
    "I_{R_{3}}=\\frac{V_{R_{3}}}{R_{R_{3}}}": {
        "info": [
            {
                "variableStr": "I_{R_{3}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "I",
                        "1cc4c6dd-85dd-4bcd-a916-4944f31848f3"
                    ],
                    [
                        "R",
                        "b4e0d507-a4c4-4426-894b-db85ce656344"
                    ],
                    [
                        "3",
                        "0a4ae9fb-8a69-4bd1-a1c2-0f1ac81492af"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 16,
                "endPos": 25,
                "info": [
                    [
                        "V",
                        "b38eb3fd-6697-47a2-bf58-5b002826f6b6"
                    ],
                    [
                        "R",
                        "04fd6afd-b4fc-40e0-bf48-189dedd2f10b"
                    ],
                    [
                        "3",
                        "6093e8a8-4fbf-4e8f-a4a1-e6954bc0773f"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 27,
                "endPos": 36,
                "info": [
                    [
                        "R",
                        "ba9dc364-4d64-48dd-8a0f-e83c7a3b685c"
                    ],
                    [
                        "R",
                        "11e9bc6e-08d5-4e63-986f-5ba100da0cc2"
                    ],
                    [
                        "3",
                        "13c32360-e1e4-46ba-82f2-8cfb542eb46b"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "7d9d5603-b83c-49c1-be18-88dd27ae090f"
    },
    "\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{R_{3}}}{R_{R_{3}}}": {
        "info": [
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 64,
                "endPos": 73,
                "info": [
                    [
                        "V",
                        "60b48184-2a76-480d-87e3-d34d62660371"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 75,
                "endPos": 84,
                "info": [
                    [
                        "R",
                        "3ee38070-b947-4569-8b21-b0df035285b4"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 75,
                "endPos": 84,
                "info": [
                    [
                        "R",
                        "5eb224e4-a649-457e-b658-f1813742abe3"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 75,
                "endPos": 84,
                "info": [
                    [
                        "3",
                        "90d2f20b-1e75-448a-bab8-bedc82f6d117"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "d3d55655-70e4-4676-b0c6-113bddaf14a2"
    },
    "(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}})R_{R_{3}}=V_{R_{3}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 7,
                "endPos": 17,
                "info": [
                    [
                        "V",
                        "6428931f-3dc8-4240-bf32-d27fc4cacf5d"
                    ],
                    [
                        "D",
                        "72317828-57aa-4f15-8262-007c452a584b"
                    ],
                    [
                        "C",
                        "70c1c8c2-1ede-4382-96e8-522b9f3d2c66"
                    ],
                    [
                        "8",
                        "cc6e452e-a1cc-445a-9d27-f59ab3f2f29a"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 19,
                "endPos": 29,
                "info": [
                    [
                        "R",
                        "dded389c-b43d-4aac-9931-9f9d23b9fda0"
                    ],
                    [
                        "D",
                        "ff6cc6e6-6de6-4995-99ff-7ddedf57a5bb"
                    ],
                    [
                        "C",
                        "9fd490b4-0995-4ca8-9f9d-adecece318b2"
                    ],
                    [
                        "8",
                        "52b397ba-8e0d-4c22-a1d9-ec48d758c101"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 37,
                "endPos": 46,
                "info": [
                    [
                        "V",
                        "6f15f26e-c697-4623-8f38-422a529b1ea0"
                    ],
                    [
                        "R",
                        "984ecce5-0abd-4a58-98df-ad51d9124c65"
                    ],
                    [
                        "0",
                        "5c7fa92a-5ae8-4130-987f-cbb63990f69a"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 48,
                "endPos": 57,
                "info": [
                    [
                        "R",
                        "1feadb06-3730-482e-9fb9-a7f865c1e265"
                    ],
                    [
                        "R",
                        "3bed91e5-d9db-4483-a9b3-cfd2c0e916b1"
                    ],
                    [
                        "0",
                        "54d84f02-8bd8-4151-8a18-9256a9648053"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 59,
                "endPos": 68,
                "info": [
                    [
                        "R",
                        "bc97a926-8ba6-464f-b41d-82d32757df0f"
                    ],
                    [
                        "R",
                        "d90a8272-6b98-4be4-bd10-b5a9ea55f0b8"
                    ],
                    [
                        "3",
                        "ee388e45-3b97-49e1-bf89-bc6426b23396"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 69,
                "endPos": 78,
                "info": [
                    [
                        "V",
                        "14199130-95f4-44e6-a3aa-93a792610f88"
                    ],
                    [
                        "R",
                        "a296f759-26c2-4c64-adc8-836a645c753c"
                    ],
                    [
                        "3",
                        "2427434e-2f06-4aff-831b-1c502c23b039"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "557b876c-5ee3-4601-9a2f-e8c0dae827ac"
    },
    "V_{R_{3}}=V_{DC_{8}}-0": {
        "info": [
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "V",
                        "6618539d-ecd0-4696-aaad-8ade6906227d"
                    ],
                    [
                        "R",
                        "06541ebd-6131-46cc-9b26-393ce8cbfa04"
                    ],
                    [
                        "3",
                        "5544c96a-2859-44e7-8d17-744b258e24bf"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 10,
                "endPos": 20,
                "info": [
                    [
                        "V",
                        "3d589453-00ff-412b-aa26-650d4d360200"
                    ],
                    [
                        "D",
                        "877cf950-e853-437e-aefe-8e5962f52996"
                    ],
                    [
                        "C",
                        "ac93eb3d-9b4c-4586-a83e-cdaf3bd8bc34"
                    ],
                    [
                        "8",
                        "ba7a254b-d84e-4be2-b355-5c10f3182e8b"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "a6c9fe05-7518-4943-ba50-ea1beaa84e2d"
    },
    "V_{R_{3}}=V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{R_{3}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "V",
                        "9d1fb478-cc04-48a3-b0dc-20c36feece58"
                    ],
                    [
                        "R",
                        "57cba841-18da-4034-9615-7ebe36955c11"
                    ],
                    [
                        "3",
                        "1694c844-2995-4362-8bf4-7103dd75818f"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 10,
                "endPos": 20,
                "info": [
                    [
                        "V",
                        "0669e76e-5815-4ec4-8830-4dae811cc42a"
                    ],
                    [
                        "D",
                        "b9bd6e7b-c4d7-4e3f-9000-9d0c306ffbab"
                    ],
                    [
                        "C",
                        "e56d523c-f99b-4d6d-8c4b-e1f79695f851"
                    ],
                    [
                        "8",
                        "3cf27366-06ba-4c39-94fe-081549d72489"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "4db9a126-6c4f-4fa2-b003-645c2826f9ea"
    },
    "(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}})R_{R_{3}}=V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 7,
                "endPos": 17,
                "info": [
                    [
                        "V",
                        "555eb76b-f486-4f4f-a784-1a5791049c50"
                    ],
                    [
                        "D",
                        "626b463c-ac67-448a-9c3c-9f9877b7f4a9"
                    ],
                    [
                        "C",
                        "0fa89be0-e0ce-43bf-a1dd-ffaeb036c649"
                    ],
                    [
                        "8",
                        "e5b7e730-cf8b-41c7-a766-c4a34e00ea43"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 69,
                "endPos": 79,
                "info": [
                    [
                        "D",
                        "36b4d852-1ac6-42ee-983b-d3706c4cf2a8"
                    ],
                    [
                        "C",
                        "57d1a481-3187-408e-80c5-658f4ebf9da6"
                    ],
                    [
                        "8",
                        "5233c90b-9e38-447b-b942-8d2c4257caf6"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 69,
                "endPos": 79,
                "info": [
                    [
                        "V",
                        "0fc35b66-117d-4e02-a9de-5b30ec6b9dc4"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "90e77578-f6ef-424b-9cc9-b5fd083408b2"
    },
    "\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{DC_{8}}}{R_{R_{3}}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 6,
                "endPos": 16,
                "info": [
                    [
                        "V",
                        "0dafdefe-a059-45bf-8dcc-f36745483ffb"
                    ],
                    [
                        "D",
                        "76fc2fb4-b232-4fc7-950f-add9c40a937c"
                    ],
                    [
                        "C",
                        "df75d713-f59e-4091-83c6-40e0fc23a58f"
                    ],
                    [
                        "8",
                        "c18c2572-0670-4d26-bac5-69c9b87057b3"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 18,
                "endPos": 28,
                "info": [
                    [
                        "R",
                        "bc7a1fa8-3a6c-4f38-8d1c-d7f792754706"
                    ],
                    [
                        "D",
                        "5e52eb39-1f90-4079-82c4-5561fc24c566"
                    ],
                    [
                        "C",
                        "ddcbaa5f-94b2-4f70-a3f3-b7dddc7228c3"
                    ],
                    [
                        "8",
                        "b582cf7e-5a08-4f84-baec-33e732c2757a"
                    ]
                ]
            },
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 36,
                "endPos": 45,
                "info": [
                    [
                        "V",
                        "67c46afd-bd67-4993-b78f-54f2c936dc05"
                    ],
                    [
                        "R",
                        "75a70282-8a0c-41bc-87de-013a654f0835"
                    ],
                    [
                        "0",
                        "7a12614b-446d-4aaa-b0b0-6ed9b0de8c2b"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 47,
                "endPos": 56,
                "info": [
                    [
                        "R",
                        "e6fffe4f-ee9c-486c-b4a6-5d19b81935a9"
                    ],
                    [
                        "R",
                        "35d01040-5222-4e2b-b831-82b7072b361f"
                    ],
                    [
                        "0",
                        "b10007ba-9980-454d-a8f2-96a3fed57911"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 64,
                "endPos": 74,
                "info": [
                    [
                        "V",
                        "78e98e5e-5c26-49b2-a40d-f97e1c1065c2"
                    ],
                    [
                        "D",
                        "99a4272d-87e3-4c58-b189-e0cc17a03798"
                    ],
                    [
                        "C",
                        "292126e7-d282-4774-b257-4e2abd5d9a80"
                    ],
                    [
                        "8",
                        "07a6e981-76c0-4865-ba12-e4f90b25a219"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 76,
                "endPos": 85,
                "info": [
                    [
                        "R",
                        "2c022c6d-201f-476c-ad8a-5217151fc2f0"
                    ],
                    [
                        "R",
                        "1e1a8b10-57a8-429a-afa3-f4723b2697f6"
                    ],
                    [
                        "3",
                        "936e2cc5-6dd0-4ce5-b1ec-f7584743711e"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "dbf138b3-976c-4b19-af98-3cbdf483e15e"
    },
    "\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 6,
                "endPos": 15,
                "info": [
                    [
                        "V",
                        "1724b854-3edb-4eb5-95d7-6e2b7bf7dd23"
                    ],
                    [
                        "R",
                        "fc3d886c-9da2-4346-b24d-13f3735e408f"
                    ],
                    [
                        "0",
                        "0991e958-f6f5-4def-92d8-38be79089d6c"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 17,
                "endPos": 26,
                "info": [
                    [
                        "R",
                        "05f3cf98-ecc0-4162-a50c-fca9a93d7b1f"
                    ],
                    [
                        "R",
                        "d5cbaefe-e622-4dfb-b0e1-86bd3c4ab958"
                    ],
                    [
                        "0",
                        "522445d2-01ef-44d4-bd30-81181f93e85c"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 34,
                "endPos": 44,
                "info": [
                    [
                        "V",
                        "e85cb6cd-4cb2-4e12-9950-dbb3105625a9"
                    ],
                    [
                        "D",
                        "6c41ca65-2137-429f-adf9-226c40b4afd3"
                    ],
                    [
                        "C",
                        "01a4e9ef-588d-4fa4-b0dc-cb73fba7532a"
                    ],
                    [
                        "8",
                        "aaf81a66-5f6d-4303-8254-f324494a8b03"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 46,
                "endPos": 56,
                "info": [
                    [
                        "R",
                        "607f3dcb-b73e-4924-8612-3eec92ac1281"
                    ],
                    [
                        "D",
                        "61b16984-395b-4859-b8e1-6c01174116d4"
                    ],
                    [
                        "C",
                        "8bdf3238-2475-49e1-9304-9cd36ce41b04"
                    ],
                    [
                        "8",
                        "dbc3c6ac-1441-4e84-8ac8-dd6ddec12306"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 64,
                "endPos": 74,
                "info": [
                    [
                        "V",
                        "47593396-f8c8-423e-b6e3-8e5322a45b7c"
                    ],
                    [
                        "D",
                        "f4c329f6-2ba2-4f47-9bd0-1f9c17150f50"
                    ],
                    [
                        "C",
                        "2120b9ea-ba58-4363-bd8d-ce17d74ce31f"
                    ],
                    [
                        "8",
                        "f612406c-0c2d-41ce-b81d-c87e3c1b9b2e"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 76,
                "endPos": 85,
                "info": [
                    [
                        "R",
                        "f38fd9fa-8f16-43e7-9c7d-42f32522f906"
                    ],
                    [
                        "R",
                        "ae677a6c-722e-4928-867b-a1878ff67ae7"
                    ],
                    [
                        "3",
                        "00eec6e3-64ca-42ce-b9be-c83119230972"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "73f2843f-b76c-4396-8f27-734e2063c748"
    },
    "V_{R_{0}}=(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}})R_{R_{0}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "V",
                        "098baa89-b6c4-4467-8b5a-5c88502e7bc7"
                    ],
                    [
                        "R",
                        "0beaaed5-6e55-4f8b-a8c4-d70a2facd099"
                    ],
                    [
                        "0",
                        "8a003146-cd2e-4a17-8d00-2a375d8f078e"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 17,
                "endPos": 27,
                "info": [
                    [
                        "V",
                        "2d082874-73b5-4011-bcb8-683b792aa116"
                    ],
                    [
                        "D",
                        "73935266-2495-44ce-a001-3b785edf6119"
                    ],
                    [
                        "C",
                        "c1f9f034-3fb7-4897-b26c-c49a9cfe3543"
                    ],
                    [
                        "8",
                        "03b0c9ff-ed47-4fcc-8d9f-4eb407cb80fc"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 29,
                "endPos": 39,
                "info": [
                    [
                        "R",
                        "d8308c8e-34a4-4961-abec-389a4ce3f55d"
                    ],
                    [
                        "D",
                        "68ca60cc-d427-491f-bbae-eaed5e8bd35d"
                    ],
                    [
                        "C",
                        "3ad4cfa0-956e-4cc7-9cd6-ec293dde92f1"
                    ],
                    [
                        "8",
                        "60a6ec76-b295-4c05-b20d-1aaaf3f811d5"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 47,
                "endPos": 57,
                "info": [
                    [
                        "V",
                        "6dd43f32-9a58-44e4-a710-16c52c415eb7"
                    ],
                    [
                        "D",
                        "132f90f4-ef63-450d-8568-c09a315c808e"
                    ],
                    [
                        "C",
                        "c5f5a340-e992-4bb5-9a5a-f8d8bb98c930"
                    ],
                    [
                        "8",
                        "6ff0b54a-06c2-4214-a825-43ea013237ff"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 59,
                "endPos": 68,
                "info": [
                    [
                        "R",
                        "c03fb030-9f19-4eb4-9726-39e8782a8f60"
                    ],
                    [
                        "R",
                        "c5c7f085-804b-4679-8412-aabe42e094e6"
                    ],
                    [
                        "3",
                        "f3716a8b-472a-418c-bece-2418656c43a7"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 70,
                "endPos": 79,
                "info": [
                    [
                        "R",
                        "5d309101-5ecc-450f-b84e-23720b2f94fb"
                    ],
                    [
                        "R",
                        "0a3d4957-a7be-4988-ae5f-5248434c60e2"
                    ],
                    [
                        "0",
                        "708aeed7-b3c5-47c3-a299-e88576dfe3fd"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "2df1b9fc-c7d5-4d3e-ba92-f6dfaf54e9b6"
    },
    "-V_{R_{0}}=-V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 1,
                "endPos": 10,
                "info": [
                    [
                        "V",
                        "4a668251-b6eb-4a59-bbda-2c15739159f6"
                    ],
                    [
                        "R",
                        "09c88456-8020-437e-950d-6aa2d4403cb6"
                    ],
                    [
                        "0",
                        "e3aaa449-7995-4962-a053-05bbc9e23abc"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 12,
                "endPos": 22,
                "info": [
                    [
                        "V",
                        "17e27efa-c274-4c1c-b442-39dc4e095c67"
                    ],
                    [
                        "D",
                        "52ba0400-5f8d-48b2-87dc-7196b13ce27c"
                    ],
                    [
                        "C",
                        "178365dc-0bab-404e-af66-72eab20bda7d"
                    ],
                    [
                        "8",
                        "3ae03579-0149-4495-817f-916c8bd1cc3f"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "19ec7fe0-5f5e-4e1e-8b4b-605b92b8dc0c"
    },
    "V_{R_{0}}=--V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "V",
                        "1c437dbf-6dc6-4f3b-b3a2-909daf52aafe"
                    ],
                    [
                        "R",
                        "65ed0659-f72b-4ba0-9f58-53893bf8e934"
                    ],
                    [
                        "0",
                        "f75a796a-d15b-46a4-bf7d-a171a3428c87"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 12,
                "endPos": 22,
                "info": [
                    [
                        "V",
                        "e77b002c-7b80-48a7-a2ab-ca7a156287d6"
                    ],
                    [
                        "D",
                        "fc761cd2-101e-4660-8a7d-721736cba3ec"
                    ],
                    [
                        "C",
                        "4f2f45e9-5e2a-4218-a59b-a162f07c7402"
                    ],
                    [
                        "8",
                        "fc23cdd6-9c69-4ad7-bff5-02e174b2e00c"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "bcfaccf1-329b-4011-a45f-27325dd4650d"
    },
    "V_{R_{0}}=V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{R_{0}}",
                "startPos": 0,
                "endPos": 9,
                "info": [
                    [
                        "V",
                        "89df0a45-4076-4fac-a314-30bbbaa568ca"
                    ],
                    [
                        "R",
                        "c6111df7-4b6f-4fb2-ba14-4c58495814cf"
                    ],
                    [
                        "0",
                        "d91a3d68-8b85-4bf4-b5fb-e106ba76ceaf"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 10,
                "endPos": 20,
                "info": [
                    [
                        "V",
                        "4c562bd2-fcc3-4b15-af20-eeff1d3b2465"
                    ],
                    [
                        "D",
                        "cfadcb99-e04c-4ce7-9fbe-bd31bde48688"
                    ],
                    [
                        "C",
                        "b800f656-84e4-4eed-a0ad-460bb09679be"
                    ],
                    [
                        "8",
                        "4412fcee-e152-4463-b3ef-3f740a478d92"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "48cd29c6-924b-4a0b-9fc6-1aa221da32b9"
    },
    "(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}})R_{R_{0}}=V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 7,
                "endPos": 17,
                "info": [
                    [
                        "V",
                        "9abd10bd-934c-48fc-86f5-07e28bea535b"
                    ],
                    [
                        "D",
                        "47e311e3-efc1-4d74-aa39-22225922807a"
                    ],
                    [
                        "C",
                        "c41120b4-6e3f-4543-8258-51b674491c4f"
                    ],
                    [
                        "8",
                        "1a28f6db-68ac-4822-b62a-d3c21e2a9aef"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 37,
                "endPos": 47,
                "info": [
                    [
                        "D",
                        "0095861d-ec7c-4c82-9008-c99786f08256"
                    ],
                    [
                        "C",
                        "bc304423-ffb6-4d99-908e-4292b4fdf3d1"
                    ],
                    [
                        "8",
                        "ecc53cd1-2be9-4b0e-8513-9a7d09440a77"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 70,
                "endPos": 80,
                "info": [
                    [
                        "V",
                        "1543fe5d-1cee-4f77-8359-2dab221d5b4d"
                    ],
                    [
                        "D",
                        "2eff1e96-6c61-4957-9f59-c06e14d2d233"
                    ],
                    [
                        "C",
                        "91e9d9fc-0ab9-43d1-9037-0d85eb3c8421"
                    ],
                    [
                        "8",
                        "3b066865-0605-4b48-ae99-569af3d6caa8"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "36ed5cea-33fd-41a9-8f58-800456a26d86"
    },
    "V_{DC_{8}}(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=V_{DC_{8}}": {
        "info": [
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 0,
                "endPos": 10,
                "info": [
                    [
                        "V",
                        "42c74783-8ba4-41a9-990f-78c6c6b7f18c"
                    ],
                    [
                        "D",
                        "86eff332-e912-407a-bb42-98358f197987"
                    ],
                    [
                        "C",
                        "d5ed2464-4910-45ee-b606-67b1bdee3501"
                    ],
                    [
                        "8",
                        "2affb4cd-e2e3-4a3d-882f-4a3444004d2b"
                    ]
                ]
            },
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 20,
                "endPos": 30,
                "info": [
                    [
                        "R",
                        "d227e37b-4389-4818-9feb-48acbfadd66b"
                    ],
                    [
                        "D",
                        "4c172fa4-1af6-4f22-9ea7-2149096d2aee"
                    ],
                    [
                        "C",
                        "e8ceae72-5133-4806-8439-82b6e45481c2"
                    ],
                    [
                        "8",
                        "8b6aa5fe-064e-4162-bacc-dd813054defb"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 41,
                "endPos": 50,
                "info": [
                    [
                        "R",
                        "1027ce65-26f8-4a0d-9dbc-4c46f9b0fd37"
                    ],
                    [
                        "R",
                        "97e57d7c-0ccb-441e-8b50-61079e5dc6d6"
                    ],
                    [
                        "3",
                        "3578aeef-0a30-4ea6-80e4-6e2994e402c5"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 52,
                "endPos": 61,
                "info": [
                    [
                        "R",
                        "39a25076-1f26-41f2-b00c-939c17b8ff62"
                    ],
                    [
                        "R",
                        "d69d386b-5443-432c-b2b8-0b5e5b00065f"
                    ],
                    [
                        "0",
                        "bfc34122-03b2-4b75-b26b-e68eb57db621"
                    ]
                ]
            },
            {
                "variableStr": "V_{DC_{8}}",
                "startPos": 62,
                "endPos": 72,
                "info": [
                    [
                        "V",
                        "e03d1e08-d635-401b-bc9c-e02d32ac842f"
                    ],
                    [
                        "D",
                        "b6ac6f5d-5941-4f82-92ee-caf64c8ef152"
                    ],
                    [
                        "C",
                        "6c312389-dc73-488b-a846-161655f3c737"
                    ],
                    [
                        "8",
                        "29982fdc-23ee-4ccf-9361-739a3480f44f"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "9e640988-a049-4c44-afec-bddbeeb41be8"
    },
    "(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=1": {
        "info": [
            {
                "variableStr": "R_{DC_{8}}",
                "startPos": 10,
                "endPos": 20,
                "info": [
                    [
                        "R",
                        "f2d4cc60-2eb4-4ba3-9cd4-16cdc5e5bf8c"
                    ],
                    [
                        "D",
                        "f0e87d25-c72e-43ef-99be-fe86eab6f11c"
                    ],
                    [
                        "C",
                        "0ee2a749-109e-4b28-bdf4-511eb8ec316a"
                    ],
                    [
                        "8",
                        "33f872b5-a582-4fac-bc8d-b9a7478598af"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{3}}",
                "startPos": 31,
                "endPos": 40,
                "info": [
                    [
                        "R",
                        "82f1e215-e9b2-4a31-b74d-53986e48589e"
                    ],
                    [
                        "R",
                        "5e324495-4902-45bb-9fff-53a1ed7fb9ed"
                    ],
                    [
                        "3",
                        "2df2a35b-c0df-4924-8394-a71e51c2f312"
                    ]
                ]
            },
            {
                "variableStr": "R_{R_{0}}",
                "startPos": 42,
                "endPos": 51,
                "info": [
                    [
                        "R",
                        "58c4e09e-9851-4db4-a70a-9219ab37be78"
                    ],
                    [
                        "R",
                        "b73bdb2d-1ae7-4294-b602-2be2fa9a1f0b"
                    ],
                    [
                        "0",
                        "5439acab-8061-4b4f-ba7d-7a79d1198bdf"
                    ]
                ]
            }
        ],
        "type": "latex",
        "meshUUID": "fea38639-d62e-42f2-abbb-d23d4da55469"
    }
}


    list_equationNetworkInfoDict = [
    {
        "equation": "-I_{DC_{8}}+I_{R_{0}}+I_{R_{3}}=0",
        "equationFinderDisplayName": "Kirchhoff Current Law",
        "list_list_networkNodeIds": [
            [
                1,
                9,
                8,
                10,
                5
            ],
            [
                1,
                2,
                0,
                6,
                5
            ],
            [
                1,
                4,
                3,
                7,
                5,
                5
            ]
        ],
        "variableInfos": {
            "0": [
                "I_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "I_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "I_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "I_{R_{3}}",
            "I_{R_{0}}",
            "I_{DC_{8}}"
        ],
        "variableStr__nodeId": {
            "I_{R_{0}}": 0,
            "I_{R_{3}}": 3,
            "I_{DC_{8}}": 8
        }
    },
    {
        "equation": "-V_{R_{0}}+V_{DC_{8}}=0",
        "equationFinderDisplayName": "Kirchhoff Voltage Law",
        "list_list_networkNodeIds": [
            [
                0,
                6,
                5,
                9,
                8,
                10,
                1,
                2,
                0
            ]
        ],
        "variableInfos": {
            "0": [
                "V_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "V_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "V_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "V_{DC_{8}}",
            "V_{R_{0}}"
        ],
        "variableStr__nodeId": {
            "V_{R_{0}}": 0,
            "V_{R_{3}}": 3,
            "V_{DC_{8}}": 8
        }
    },
    {
        "equation": "V_{DC_{8}}-V_{R_{3}}=0",
        "equationFinderDisplayName": "Kirchhoff Voltage Law",
        "list_list_networkNodeIds": [
            [
                5,
                9,
                8,
                10,
                1,
                4,
                3,
                7,
                5
            ]
        ],
        "variableInfos": {
            "0": [
                "V_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "V_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "V_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "V_{R_{3}}",
            "V_{DC_{8}}"
        ],
        "variableStr__nodeId": {
            "V_{R_{0}}": 0,
            "V_{R_{3}}": 3,
            "V_{DC_{8}}": 8
        }
    },
    {
        "equation": "\\frac{V_{R_{0}}}{I_{R_{0}}}=R_{R_{0}}",
        "equationFinderDisplayName": "Ohm Law",
        "list_list_networkNodeIds": [
            [
                0
            ]
        ],
        "variableInfos": {
            "0": [
                "R_{R_{0}}",
                "V_{R_{0}}",
                "I_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "R_{R_{3}}",
                "V_{R_{3}}",
                "I_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "R_{DC_{8}}",
                "V_{DC_{8}}",
                "I_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "R_{R_{0}}",
            "I_{R_{0}}",
            "V_{R_{0}}"
        ],
        "variableStr__nodeId": {
            "R_{R_{0}}": 0,
            "V_{R_{0}}": 0,
            "I_{R_{0}}": 0,
            "R_{R_{3}}": 3,
            "V_{R_{3}}": 3,
            "I_{R_{3}}": 3,
            "R_{DC_{8}}": 8,
            "V_{DC_{8}}": 8,
            "I_{DC_{8}}": 8
        }
    },
    {
        "equation": "\\frac{V_{R_{3}}}{I_{R_{3}}}=R_{R_{3}}",
        "equationFinderDisplayName": "Ohm Law",
        "list_list_networkNodeIds": [
            [
                3
            ]
        ],
        "variableInfos": {
            "0": [
                "R_{R_{0}}",
                "V_{R_{0}}",
                "I_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "R_{R_{3}}",
                "V_{R_{3}}",
                "I_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "R_{DC_{8}}",
                "V_{DC_{8}}",
                "I_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "R_{R_{3}}",
            "I_{R_{3}}",
            "V_{R_{3}}"
        ],
        "variableStr__nodeId": {
            "R_{R_{0}}": 0,
            "V_{R_{0}}": 0,
            "I_{R_{0}}": 0,
            "R_{R_{3}}": 3,
            "V_{R_{3}}": 3,
            "I_{R_{3}}": 3,
            "R_{DC_{8}}": 8,
            "V_{DC_{8}}": 8,
            "I_{DC_{8}}": 8
        }
    },
    {
        "equation": "\\frac{V_{DC_{8}}}{I_{DC_{8}}}=R_{DC_{8}}",
        "equationFinderDisplayName": "Ohm Law",
        "list_list_networkNodeIds": [
            [
                8
            ]
        ],
        "variableInfos": {
            "0": [
                "R_{R_{0}}",
                "V_{R_{0}}",
                "I_{R_{0}}"
            ],
            "1": [],
            "2": [],
            "3": [
                "R_{R_{3}}",
                "V_{R_{3}}",
                "I_{R_{3}}"
            ],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "R_{DC_{8}}",
                "V_{DC_{8}}",
                "I_{DC_{8}}"
            ],
            "9": [],
            "10": []
        },
        "variables": [
            "R_{DC_{8}}",
            "I_{DC_{8}}",
            "V_{DC_{8}}"
        ],
        "variableStr__nodeId": {
            "R_{R_{0}}": 0,
            "V_{R_{0}}": 0,
            "I_{R_{0}}": 0,
            "R_{R_{3}}": 3,
            "V_{R_{3}}": 3,
            "I_{R_{3}}": 3,
            "R_{DC_{8}}": 8,
            "V_{DC_{8}}": 8,
            "I_{DC_{8}}": 8
        }
    }
]


    language_introduction_findEquations = {
        'en-US':'This is a circuit with two resistors connected in parallel, lets find all the equations related to the components of this circuit',
        'zh-CN':'我们求，此二电阻器并联电路内，所有方程式。',
        'ja-JP':'こちらは、並列に接続されている抵抗が二つである。その並列回路の素子においての公式を、全て見つけましょう',
        'de-DE':'Der folgende Stromkreis ist eine ParallelSchaltung. Versuchen wir jetzt, alle Gleichungen der Bauelemente dieses Stromkreises aufzuschreiben',
        'fr-FR':'Nous avons deux résistances en parallèle et nous allons trouver toutes les équations relatives à ses composants.',
        'ru-RU':'У нас есть два резистора, соединенных параллельно, и нам нужно найти все уравнения, связанные с их компонентами.'
    }

    language_conclusion_findEquations = {
        'en-US':'We have found all the equations relating to the two resistors and their parallel connectivity.',
        'zh-CN':'现阶段，我们以求获所有相关的方程式。',
        'ja-JP':'今まで、その並列回路の素子においての公式を、求めました。',
        'de-DE':'Wir haben alle Gleichungen der Bauelemente dieses Stromkreises gefunden,',
        'fr-FR':'Nous avons trouvé toutes les équations relatives à ses composants.',
        'ru-RU':'Мы нашли все уравнения, касающиеся его компонентов.'
    }
    results = generateSubtitles_findEquations(list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, language_introduction_findEquations, language_conclusion_findEquations)

    if verbose:
        print('***********************')
        pp.pprint(results)



def test_generateSubtitles_solvingSteps(verbose=False):

    language_introduction_solvingSteps = {
        'en-US':'Lets try to find the resistance of the battery in terms of the two resistors!',
        'zh-CN':'然后，我们利用之前取获的方程式，推出总电阻。',
        'ja-JP':'それから、求めました公式を使って、その回路は、合成抵抗が、求めましょう！',
        'de-DE':'Damit können wir den Gesamtwiderstand dieses Stromkreises berechnen.',
        'fr-FR':'Calculons la résistance équivalente aux réseaux ci-dessous.',
        'ru-RU':'Рассчитаем эквивалентное сопротивление сетей ниже.'
    }

    language_conclusion_solvingSteps = {
        'en-US':'And thats it! However, there are many redundant steps, can you find a more elegant solution? Leave your solution in the comments below!',
        'zh-CN':'可是，之前的解题步骤有一点繁琐，您能找到更简易的解题步骤吗？请在讨论区留下您的雅论。',
        'ja-JP':'通りですけど、無駄な手順がいっぱいあります。表した手順より、きれいな解き方を求めることができますか？ぜひ、解き方と考えが、コメント欄に、書いて下さい。',
        'de-DE':'Und so ist es! Aber es gibt viele überflüssige Rechnengen, und das motiviert uns, nach einer eleganten Antwort zu suchen. Schreib uns deine elegante Antworte in die Commentare!',
        'fr-FR':"C'est exact, mais il y a beaucoup d'étapes inutiles. Pouvez-vous trouver une solution plus élégante que celles que j'ai présentées ? N'hésitez pas à partager votre solution et vos réflexions dans les commentaires.",
        'ru-RU':'Это верно, но есть много лишних шагов. Можете ли вы найти более элегантное решение, чем те, что я предложил? Не стесняйтесь делиться своими решениями и мыслями в комментариях.'
    }

    solvingSteps = [   {   'hin': {},
        'hin__subSteps': [],
        'sub': '',
        'vor': {   'latex': '(-I_{DC_{8}}+I_{R_{0}})+I_{R_{3}}=0',
                   'root': ('=', 3),
                   'scheme': '(= (+ (+ (- 0 I_{DC_{8}}) I_{R_{0}}) I_{R_{3}}) '
                             '0)',
                   'variables': ['I_{R_{3}}', 'I_{R_{0}}', 'I_{DC_{8}}']},
        'vor__subSteps': []},
    {   'hin': {   'latex': '\\frac{V_{DC_{8}}}{I_{DC_{8}}}=R_{DC_{8}}',
                   'root': ('=', 1),
                   'scheme': '(= (/ V_{DC_{8}} I_{DC_{8}}) R_{DC_{8}})',
                   'variables': ['R_{DC_{8}}', 'I_{DC_{8}}', 'V_{DC_{8}}']},
        'hin__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '/',
                                 'id': 0,
                                 'lastId': 1,
                                 'resultLatexStr': 'I_{DC_{8}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}',
                                 'resultSchemeStr': '(= I_{DC_{8}} (/ '
                                                    'V_{DC_{8}} R_{DC_{8}}))',
                                 'resultVariables': [   'I_{DC_{8}}',
                                                        'V_{DC_{8}}',
                                                        'R_{DC_{8}}'],
                                 'stepType': 'solving'}],
        'sub': 'I_{DC_{8}}',
        'vor': {   'latex': 'I_{R_{3}}+I_{R_{0}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}',
                   'root': ('=', 1),
                   'scheme': '(= (+ I_{R_{3}} I_{R_{0}}) (/ V_{DC_{8}} '
                             'R_{DC_{8}}))',
                   'variables': ['R_{DC_{8}}', 'I_{DC_{8}}', 'V_{DC_{8}}']},
        'vor__subSteps': [   {   'argumentIdx': 0,
                                 'functionName': '+',
                                 'id': 2,
                                 'lastId': 3,
                                 'resultLatexStr': '-I_{DC_{8}}+I_{R_{0}}=-I_{R_{3}}',
                                 'resultSchemeStr': '(= (+ (- 0 I_{DC_{8}}) '
                                                    'I_{R_{0}}) (- 0 '
                                                    'I_{R_{3}}))',
                                 'resultVariables': [   'I_{DC_{8}}',
                                                        'I_{R_{0}}',
                                                        'I_{R_{3}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': 0,
                                 'functionName': '+',
                                 'id': 1,
                                 'lastId': 3,
                                 'resultLatexStr': '-I_{DC_{8}}=-I_{R_{3}}-I_{R_{0}}',
                                 'resultSchemeStr': '(= (- 0 I_{DC_{8}}) (- (- '
                                                    '0 I_{R_{3}}) I_{R_{0}}))',
                                 'resultVariables': [   'I_{DC_{8}}',
                                                        'I_{R_{3}}',
                                                        'I_{R_{0}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': 1,
                                 'functionName': '-',
                                 'id': 0,
                                 'lastId': 3,
                                 'resultLatexStr': 'I_{DC_{8}}=--I_{R_{3}}-I_{R_{0}}',
                                 'resultSchemeStr': '(= I_{DC_{8}} (- 0 (- (- '
                                                    '0 I_{R_{3}}) I_{R_{0}})))',
                                 'resultVariables': [   'I_{DC_{8}}',
                                                        'I_{R_{3}}',
                                                        'I_{R_{0}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': None,
                                 'functionName': (   'Doublenegative',
                                                     'pretty',
                                                     '(- 0 (- (- 0 $0) $1))',
                                                     '(+ $0 $1)'),
                                 'id': None,
                                 'lastId': None,
                                 'resultLatexStr': 'I_{DC_{8}}=I_{R_{3}}+I_{R_{0}}',
                                 'resultSchemeStr': '(= I_{DC_{8}} (+ '
                                                    'I_{R_{3}} I_{R_{0}}))',
                                 'resultVariables': [   'I_{DC_{8}}',
                                                        'I_{R_{3}}',
                                                        'I_{R_{0}}'],
                                 'stepType': 'simplification'}]},
    {   'hin': {   'latex': '\\frac{V_{R_{0}}}{I_{R_{0}}}=R_{R_{0}}',
                   'root': ('=', 1),
                   'scheme': '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})',
                   'variables': ['R_{R_{0}}', 'I_{R_{0}}', 'V_{R_{0}}']},
        'hin__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '/',
                                 'id': 0,
                                 'lastId': 1,
                                 'resultLatexStr': 'I_{R_{0}}=\\frac{V_{R_{0}}}{R_{R_{0}}}',
                                 'resultSchemeStr': '(= I_{R_{0}} (/ V_{R_{0}} '
                                                    'R_{R_{0}}))',
                                 'resultVariables': [   'I_{R_{0}}',
                                                        'V_{R_{0}}',
                                                        'R_{R_{0}}'],
                                 'stepType': 'solving'}],
        'sub': 'I_{R_{0}}',
        'vor': {   'latex': '\\frac{V_{DC_{8}}}{R_{DC_{8}}}-I_{R_{3}}=\\frac{V_{R_{0}}}{R_{R_{0}}}',
                   'root': ('=', 1),
                   'scheme': '(= (- (/ V_{DC_{8}} R_{DC_{8}}) I_{R_{3}}) (/ '
                             'V_{R_{0}} R_{R_{0}}))',
                   'variables': ['R_{R_{0}}', 'I_{R_{0}}', 'V_{R_{0}}']},
        'vor__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '+',
                                 'id': 24,
                                 'lastId': 1,
                                 'resultLatexStr': 'I_{R_{0}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-I_{R_{3}}',
                                 'resultSchemeStr': '(= I_{R_{0}} (- (/ '
                                                    'V_{DC_{8}} R_{DC_{8}}) '
                                                    'I_{R_{3}}))',
                                 'resultVariables': [   'I_{R_{0}}',
                                                        'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'I_{R_{3}}'],
                                 'stepType': 'solving'}]},
    {   'hin': {   'latex': '\\frac{V_{R_{3}}}{I_{R_{3}}}=R_{R_{3}}',
                   'root': ('=', 1),
                   'scheme': '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})',
                   'variables': ['R_{R_{3}}', 'I_{R_{3}}', 'V_{R_{3}}']},
        'hin__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '/',
                                 'id': 0,
                                 'lastId': 1,
                                 'resultLatexStr': 'I_{R_{3}}=\\frac{V_{R_{3}}}{R_{R_{3}}}',
                                 'resultSchemeStr': '(= I_{R_{3}} (/ V_{R_{3}} '
                                                    'R_{R_{3}}))',
                                 'resultVariables': [   'I_{R_{3}}',
                                                        'V_{R_{3}}',
                                                        'R_{R_{3}}'],
                                 'stepType': 'solving'}],
        'sub': 'I_{R_{3}}',
        'vor': {   'latex': '\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{R_{3}}}{R_{R_{3}}}',
                   'root': ('=', 1),
                   'scheme': '(= (- (/ V_{DC_{8}} R_{DC_{8}}) (/ V_{R_{0}} '
                             'R_{R_{0}})) (/ V_{R_{3}} R_{R_{3}}))',
                   'variables': ['R_{R_{3}}', 'I_{R_{3}}', 'V_{R_{3}}']},
        'vor__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '-',
                                 'id': 33,
                                 'lastId': 1,
                                 'resultLatexStr': 'I_{R_{3}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}',
                                 'resultSchemeStr': '(= I_{R_{3}} (- (/ '
                                                    'V_{DC_{8}} R_{DC_{8}}) (/ '
                                                    'V_{R_{0}} R_{R_{0}})))',
                                 'resultVariables': [   'I_{R_{3}}',
                                                        'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'V_{R_{0}}',
                                                        'R_{R_{0}}'],
                                 'stepType': 'solving'}]},
    {   'hin': {   'latex': 'V_{DC_{8}}-V_{R_{3}}=0',
                   'root': ('=', 1),
                   'scheme': '(= (- V_{DC_{8}} V_{R_{3}}) 0)',
                   'variables': ['V_{R_{3}}', 'V_{DC_{8}}']},
        'hin__subSteps': [   {   'argumentIdx': 1,
                                 'functionName': '-',
                                 'id': 0,
                                 'lastId': 1,
                                 'resultLatexStr': 'V_{R_{3}}=V_{DC_{8}}-0',
                                 'resultSchemeStr': '(= V_{R_{3}} (- '
                                                    'V_{DC_{8}} 0))',
                                 'resultVariables': ['V_{R_{3}}', 'V_{DC_{8}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': None,
                                 'functionName': (   'Subtractzero',
                                                     'essential',
                                                     '(- $0 0)',
                                                     '$0'),
                                 'id': None,
                                 'lastId': None,
                                 'resultLatexStr': 'V_{R_{3}}=V_{DC_{8}}',
                                 'resultSchemeStr': '(= V_{R_{3}} V_{DC_{8}})',
                                 'resultVariables': ['V_{R_{3}}', 'V_{DC_{8}}'],
                                 'stepType': 'simplification'}],
        'sub': 'V_{R_{3}}',
        'vor': {   'latex': '(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}})R_{R_{3}}=V_{DC_{8}}',
                   'root': ('=', 1),
                   'scheme': '(= (* (- (/ V_{DC_{8}} R_{DC_{8}}) (/ V_{R_{0}} '
                             'R_{R_{0}})) R_{R_{3}}) V_{DC_{8}})',
                   'variables': ['V_{R_{3}}', 'V_{DC_{8}}']},
        'vor__subSteps': [   {   'argumentIdx': 0,
                                 'functionName': '/',
                                 'id': 0,
                                 'lastId': 1,
                                 'resultLatexStr': '(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}})R_{R_{3}}=V_{R_{3}}',
                                 'resultSchemeStr': '(= (* (- (/ V_{DC_{8}} '
                                                    'R_{DC_{8}}) (/ V_{R_{0}} '
                                                    'R_{R_{0}})) R_{R_{3}}) '
                                                    'V_{R_{3}})',
                                 'resultVariables': [   'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'V_{R_{0}}',
                                                        'R_{R_{0}}',
                                                        'R_{R_{3}}',
                                                        'V_{R_{3}}'],
                                 'stepType': 'solving'}]},
    {   'hin': {   'latex': '-V_{R_{0}}+V_{DC_{8}}=0',
                   'root': ('=', 2),
                   'scheme': '(= (+ (- 0 V_{R_{0}}) V_{DC_{8}}) 0)',
                   'variables': ['V_{DC_{8}}', 'V_{R_{0}}']},
        'hin__subSteps': [   {   'argumentIdx': 0,
                                 'functionName': '+',
                                 'id': 1,
                                 'lastId': 2,
                                 'resultLatexStr': '-V_{R_{0}}=-V_{DC_{8}}',
                                 'resultSchemeStr': '(= (- 0 V_{R_{0}}) (- 0 '
                                                    'V_{DC_{8}}))',
                                 'resultVariables': ['V_{R_{0}}', 'V_{DC_{8}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': 1,
                                 'functionName': '-',
                                 'id': 0,
                                 'lastId': 2,
                                 'resultLatexStr': 'V_{R_{0}}=--V_{DC_{8}}',
                                 'resultSchemeStr': '(= V_{R_{0}} (- 0 (- 0 '
                                                    'V_{DC_{8}})))',
                                 'resultVariables': ['V_{R_{0}}', 'V_{DC_{8}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': None,
                                 'functionName': (   'Doublenegative',
                                                     'pretty',
                                                     '(- 0 (- 0 $0))',
                                                     '$0'),
                                 'id': None,
                                 'lastId': None,
                                 'resultLatexStr': 'V_{R_{0}}=V_{DC_{8}}',
                                 'resultSchemeStr': '(= V_{R_{0}} V_{DC_{8}})',
                                 'resultVariables': ['V_{R_{0}}', 'V_{DC_{8}}'],
                                 'stepType': 'simplification'}],
        'sub': 'V_{R_{0}}',
        'vor': {   'latex': '(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}})R_{R_{0}}=V_{DC_{8}}',
                   'root': ('=', 2),
                   'scheme': '(= (* (- (/ V_{DC_{8}} R_{DC_{8}}) (/ V_{DC_{8}} '
                             'R_{R_{3}})) R_{R_{0}}) V_{DC_{8}})',
                   'variables': ['V_{DC_{8}}', 'V_{R_{0}}']},
        'vor__subSteps': [   {   'argumentIdx': 0,
                                 'functionName': '*',
                                 'id': 6,
                                 'lastId': 1,
                                 'resultLatexStr': '\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{DC_{8}}}{R_{R_{3}}}',
                                 'resultSchemeStr': '(= (- (/ V_{DC_{8}} '
                                                    'R_{DC_{8}}) (/ V_{R_{0}} '
                                                    'R_{R_{0}})) (/ V_{DC_{8}} '
                                                    'R_{R_{3}}))',
                                 'resultVariables': [   'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'V_{R_{0}}',
                                                        'R_{R_{0}}',
                                                        'R_{R_{3}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': 1,
                                 'functionName': '-',
                                 'id': 48,
                                 'lastId': 1,
                                 'resultLatexStr': '\\frac{V_{R_{0}}}{R_{R_{0}}}=\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}}',
                                 'resultSchemeStr': '(= (/ V_{R_{0}} '
                                                    'R_{R_{0}}) (- (/ '
                                                    'V_{DC_{8}} R_{DC_{8}}) (/ '
                                                    'V_{DC_{8}} R_{R_{3}})))',
                                 'resultVariables': [   'V_{R_{0}}',
                                                        'R_{R_{0}}',
                                                        'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'R_{R_{3}}'],
                                 'stepType': 'solving'},
                             {   'argumentIdx': 0,
                                 'functionName': '/',
                                 'id': 15,
                                 'lastId': 1,
                                 'resultLatexStr': 'V_{R_{0}}=(\\frac{V_{DC_{8}}}{R_{DC_{8}}}-\\frac{V_{DC_{8}}}{R_{R_{3}}})R_{R_{0}}',
                                 'resultSchemeStr': '(= V_{R_{0}} (* (- (/ '
                                                    'V_{DC_{8}} R_{DC_{8}}) (/ '
                                                    'V_{DC_{8}} R_{R_{3}})) '
                                                    'R_{R_{0}}))',
                                 'resultVariables': [   'V_{R_{0}}',
                                                        'V_{DC_{8}}',
                                                        'R_{DC_{8}}',
                                                        'R_{R_{3}}',
                                                        'R_{R_{0}}'],
                                 'stepType': 'solving'}]},
    {   'hin': {   'latex': '(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=1',
                   'root': ('=', 0),
                   'scheme': '(= (* (- (/ 1 R_{DC_{8}}) (/ 1 R_{R_{3}})) '
                             'R_{R_{0}}) 1)',
                   'variables': ['R_{R_{0}}', 'R_{DC_{8}}', 'R_{R_{3}}']},
        'hin__subSteps': [],
        'sub': '',
        'vor': {   'latex': '(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=1',
                   'root': ('=', 0),
                   'scheme': '(= (* (- (/ 1 R_{DC_{8}}) (/ 1 R_{R_{3}})) '
                             'R_{R_{0}}) 1)',
                   'variables': ['R_{R_{0}}', 'R_{DC_{8}}', 'R_{R_{3}}']},
        'vor__subSteps': [   {   'resultLatexStr': 'V_{DC_{8}}(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=V_{DC_{8}}',
                                 'resultSchemeStr': '(= (* (* V_{DC_{8}} (- (/ '
                                                    '1 R_{DC_{8}}) (/ 1 '
                                                    'R_{R_{3}}))) R_{R_{0}}) '
                                                    'V_{DC_{8}})',
                                 'resultVariables': [   'R_{R_{0}}',
                                                        'R_{DC_{8}}',
                                                        'R_{R_{3}}',
                                                        'V_{DC_{8}}'],
                                 'stepType': 'simplification'},
                             {   'resultLatexStr': '(\\frac{1}{R_{DC_{8}}}-\\frac{1}{R_{R_{3}}})R_{R_{0}}=1',
                                 'resultSchemeStr': '(= (* (- (/ 1 R_{DC_{8}}) '
                                                    '(/ 1 R_{R_{3}})) '
                                                    'R_{R_{0}}) 1)',
                                 'resultVariables': [   'R_{R_{0}}',
                                                        'R_{DC_{8}}',
                                                        'R_{R_{3}}'],
                                 'stepType': 'simplification'}]}]
    subtitles = generateSubtitles_solvingSteps(solvingSteps, language_introduction_solvingSteps, language_conclusion_solvingSteps)
    if verbose:
        print('***********************')
        pp.pprint(subtitles)

    # print(inspect.currentframe().f_code.co_name, ' PASSED? ', len(Function.TRIGONOMETRIC_NAMES)>0)


if __name__=='__main__':
    test_generateSubtitles_findEquations(True)
    test_generateSubtitles_solvingSteps(True)
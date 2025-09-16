TEST_DATUM={
    ('hin', '0'): {   'expected': '(= a (+ (^ (sin v_{0}) "2") (^ (cos v_{0}) "2")))',
                      'input': '(= a "1")'},#(+ (^ (sin $0) "2") (^ (cos $0) "2"))
    ('vor', '0'): {   'expected': '(= a "1")',
                      'input': '(= a (+ (^ (sin b) "2") (^ (cos b) "2")))'},#"1"


    ('hin', '1'): {   'expected': '(= y (+ "1" (^ (tan x) "2")))',
                      'input': '(= y (^ (sec x) "2"))'},#(+ "1" (^ (tan x) "2"))
    ('vor', '1'): {   'expected': '(= y (^ (sec x) "2"))',
                      'input': '(= y (+ "1" (^ (tan x) "2")))'},#(^ (sec x) "2")


    ('hin', '2'): {   'expected': '(= y (+ (^ (cot x) "2") "1"))',
                      'input': '(= y (^ (cosec x) "2"))'},#(+ (^ (cot x) "2") "1")
    ('vor', '2'): {   'expected': '(= y (^ (cosec x) "2"))',
                      'input': '(= y (+ (^ (cot x) "2") "1"))'},#(^ (cosec x) "2")


    ('hin', '3'): {   'expected': '(= y (- (^ (cosh v_{0}) "2") (^ (sinh v_{0}) "2")))',
                      'input': '(= y "1")'},#(- (^ (cosh $0) "2") (^ (sinh $0) "2"))
    ('vor', '3'): {   'expected': '(= y "1")',
                      'input': '(= y (- (^ (cosh x) "2") (^ (sinh x) "2")))'},#"1"


    ('hin', '4'): {   'expected': '(= y (^ (sech x) "2"))',
                      'input': '(= y (- "1" (^ (tanh x) "2")))'},#(^ (sech $0) "2")
    ('vor', '4'): {   'expected': '(= y (- "1" (^ (tanh x) "2")))',
                      'input': '(= y (^ (sech x) "2"))'},#(- "1" (^ (tanh $0) "2"))


    ('hin', '5'): {   'expected': '(= y (^ (cosech x) "2"))',
                      'input': '(= y (- (^ (coth x) "2") "1"))'},#(^ (cosech $0) "2")
    ('vor', '5'): {   'expected': '(= y (- (^ (coth x) "2") "1"))',
                      'input': '(= y (^ (cosech x) "2"))'},#(- (^ (coth $0) "2") "1")


}
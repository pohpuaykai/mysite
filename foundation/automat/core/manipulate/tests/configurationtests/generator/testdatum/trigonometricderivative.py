TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (D (sin x) x))', 'input': '(= y (* (cos x) (D x x)))'},#(* (cos $0) (D $0 $1))
    ('vor', '0'): {'expected': '(= y (* (cos x) (D x x)))', 'input': '(= y (D (sin x) x))'},#(D (sin $0) $1)


    ('hin', '1'): {'expected': '(= y (D (cos x) x))', 'input': '(= y (* (- "0" (sin x)) (D x x)))'},#(* (- "0" (sin $0)) (D $0 $1))
    ('vor', '1'): {'expected': '(= y (* (- "0" (sin x)) (D x x)))', 'input': '(= y (D (cos x) x))'},#(D (cos $0) $1)


    ('hin', '2'): {'expected': '(= y (D (tan x) x))', 'input': '(= y (* (^ (sec x) "2") (D x x)))'},#(* (^ (sec $0) "2") (D $0 $1))
    ('vor', '2'): {'expected': '(= y (* (^ (sec x) "2") (D x x)))', 'input': '(= y (D (tan x) x))'},#(D (tan $0) $1)


    ('hin', '3'): {   'expected': '(= y (D (sec x) x))',
                      'input': '(= y (* (* (sec x) (tan x)) (D x x)))'},#(* (* (sec $0) (tan $0)) (D $0 $1))
    ('vor', '3'): {'expected': '(= y (* (* (sec x) (tan x)) (D x x)))', 'input': '(= y (D (sec x) x))'},#(D (sec $0) $1)


    ('hin', '4'): {   'expected': '(= y (D (cosec x) x))',
                      'input': '(= y (* (- "0" (* (cosec x) (cot x))) (D x x)))'},#(* (- "0" (* (cosec $0) (cot $0))) (D $0 $1))
    ('vor', '4'): {'expected': '(= y (* (- "0" (* (cosec x) (cot x))) (D x x)))', 'input': '(= y (D (cosec x) x))'},#(D (cosec $0) $1)


    ('hin', '5'): {   'expected': '(= y (D (cot x) x))',
                      'input': '(= y (* (- "0" (^ cosec x) "2") (D x x)))'},#(* (- "0" (^ cosec $0) "2") (D $0 $1))
    ('vor', '5'): {'expected': '(= y (* (- "0" (^ cosec x) "2") (D x x)))', 'input': '(= y (D (cot x) x))'}#(D (cot $0) $1)

}
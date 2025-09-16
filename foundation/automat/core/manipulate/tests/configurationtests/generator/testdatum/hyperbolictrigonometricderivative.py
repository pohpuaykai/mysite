TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (D (sinh x) x))', 'input': '(= y (* (cosh x) (D x x)))'},#(* (cosh $0) (D $0 $1))
    ('vor', '0'): {'expected': '(= y (* (cosh x) (D x x)))', 'input': '(= y (D (sinh x) x))'},#(D (sinh $0) $1)


    ('hin', '1'): {'expected': '(= y (D (cosh x) x))', 'input': '(= y (* (sinh x) (D x x)))'},#(* (sinh $0) (D $0 $1))
    ('vor', '1'): {'expected': '(= y (* (sinh x) (D x x)))', 'input': '(= y (D (cosh x) x))'},#(D (cosh $0) $1)


    ('hin', '2'): {   'expected': '(= y (D (tanh x) x))',
                      'input': '(= y (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x x)))'},#(* (/ "2" (+ (cosh (* "2" $0) "1"))) (D $0 $1))
    ('vor', '2'): {'expected': '(= y (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x x)))', 'input': '(= y (D (tanh x) x))'},#(D (tanh $0) $1)


    ('hin', '3'): {   'expected': '(= y (D (sech x) x))',
                      'input': '(= y (* (- "0" (* (tanh x) (sech x))) (D x x)))'},#(* (- "0" (* (tanh $0) (sech $0))) (D $0 $1))
    ('vor', '3'): {'expected': '(= y (* (- "0" (* (tanh x) (sech x))) (D x x)))', 'input': '(= y (D (sech x) x))'},#(D (sech $0) $1)


    ('hin', '4'): {   'expected': '(= y (D (cosech x) x))',
                      'input': '(= y (* (- "0" (* (coth x) (cosech x))) (D x x)))'},#(* (- "0" (* (coth $0) (cosech $0))) (D $0 $1))
    ('vor', '4'): {'expected': '(= y (* (- "0" (* (coth x) (cosech x))) (D x x)))', 'input': '(= y (D (cosech x) x))'},#(D (cosech $0) $1)


    ('hin', '5'): {   'expected': '(= y (D (coth x) x))',
                      'input': '(= y (* (/ "2" (- "1" (sinh (* "2" x)))) (D x x)))'},#(* (/ "2" (- "1" (sinh (* "2" $0)))) (D $0 $1))
    ('vor', '5'): {'expected': '(= y (* (/ "2" (- "1" (sinh (* "2" x)))) (D x x)))', 'input': '(= y (D (coth x) x))'}#(D (coth $0) $1)

}
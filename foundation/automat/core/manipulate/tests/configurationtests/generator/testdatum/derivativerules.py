TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (D (sin y) x))',
                      'input': '(= y (* (D (sin y) y) (D y x)))'},#(* (D ($0 $1) $1) (D $1 $2))
    ('vor', '0'): {'expected': '(= y (* (D (sin y) y) (D y x)))', 'input': '(= y (D (sin y) x))'},#(D ($0 $1) $2)


    ('hin', '1'): {'expected': '(= y (D (+ a b) x))', 'input': '(= y (+ (D a x) (D b x)))'},#(+ (D $0 $2) (D $1 $2))
    ('vor', '1'): {'expected': '(= y (+ (D a x) (D b x)))', 'input': '(= y (D (+ a b) x))'},#(D (+ $0 $1) $2)


    ('hin', '2'): {   'expected': '(= y (D (* a b) x))',
                      'input': '(= y (+ (* a (D b x)) (* b (D a x))))'},#(+ (* $0 (D $1 $2)) (* $1 (D $0 $2)))
    ('vor', '2'): {'expected': '(= y (+ (* a (D b x)) (* b (D a x))))', 'input': '(= y (D (* a b) x))'},#(D (* $0 $1) $2)

    
    ('hin', '3'): {   'expected': '(= y (D (/ a b) x))',
                      'input': '(= y (/ (- (* b (D a x)) (* a (D b x))) (* b b)))'},#(/ (- (* $1 (D $0 $2)) (* $0 (D $1 $2))) (* $1 $1))
    ('vor', '3'): {'expected': '(= y (/ (- (* b (D a x)) (* a (D b x))) (* b b)))', 'input': '(= y (D (/ a b) x))'}#(D (/ $0 $1) $2)

}#ALSO ADD integration rules like sum, difference, and integration_by_parts
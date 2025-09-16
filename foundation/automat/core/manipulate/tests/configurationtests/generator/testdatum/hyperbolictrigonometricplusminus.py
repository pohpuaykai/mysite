TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (sinh (+ x z)))',
                      'input': '(= y (+ (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))'},#(+ (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ('vor', '0'): {'expected': '(= y (+ (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))', 'input': '(= y (sinh (+ x z)))'},#(sinh (+ $0 $1))


    ('hin', '1'): {   'expected': '(= y (cosh (+ x z)))',
                      'input': '(= y (+ (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))'},#(+ (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ('vor', '1'): {'expected': '(= y (+ (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))', 'input': '(= y (cosh (+ x z)))'},#(cosh (+ $0 $1))


    ('hin', '2'): {   'expected': '(= y (tanh (+ x z)))',
                      'input': '(= y (/ (+ (tanh x) (tanh z)) (+ "1" (* (tanh x) (tanh z)))))'},#(/ (+ (tanh $0) (tanh $1)) (+ "1" (* (tanh $0) (tanh $1))))
    ('vor', '2'): {'expected': '(= y (/ (+ (tanh x) (tanh z)) (+ "1" (* (tanh x) (tanh z)))))', 'input': '(= y (tanh (+ x z)))'},#(tanh (+ $0 $1))


    ('hin', '3'): {   'expected': '(= y (sinh (- x z)))',
                      'input': '(= y (- (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))'},#(- (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ('vor', '3'): {'expected': '(= y (- (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))', 'input': '(= y (sinh (- x z)))'},#(sinh (- $0 $1))


    ('hin', '4'): {   'expected': '(= y (cosh (- x z)))',
                      'input': '(= y (- (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))'},#(- (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ('vor', '4'): {'expected': '(= y (- (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))', 'input': '(= y (cosh (- x z)))'},#(cosh (- $0 $1))


    ('hin', '5'): {   'expected': '(= y (tanh (- x z)))',
                      'input': '(= y (/ (- (tanh x) (tanh z)) (- "1" (* (tanh x) (tanh z)))))'},#(/ (- (tanh $0) (tanh $1)) (- "1" (* (tanh $0) (tanh $1))))
    ('vor', '5'): {'expected': '(= y (/ (- (tanh x) (tanh z)) (- "1" (* (tanh x) (tanh z)))))', 'input': '(= y (tanh (- x z)))'}#(tanh (- $0 $1))

}
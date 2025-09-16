TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (+ (sinh x) (sinh z)))',
                      'input': '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))'},#(* (* "2" (sinh (/ (+ $0 $1) "2"))) (cosh (/ (- $0 $1) "2")))
    ('vor', '0'): {'expected': '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))', 'input': '(= y (+ (sinh x) (sinh z)))'},#(+ (sinh $0) (sinh $1))


    ('hin', '1'): {   'expected': '(= y (+ (cosh x) (cosh z)))',
                      'input': '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))'},#(* (* "2" (cosh (/ (+ $0 $1) "2"))) (cosh (/ (- $0 $1) "2")))
    ('vor', '1'): {'expected': '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))', 'input': '(= y (+ (cosh x) (cosh z)))'},#(+ (cosh $0) (cosh $1))


    ('hin', '2'): {   'expected': '(= y (- (sinh x) (sinh z)))',
                      'input': '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))'},#(* (* "2" (cosh (/ (+ $0 $1) "2"))) (sinh (/ (- $0 $1) "2")))
    ('vor', '2'): {'expected': '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))', 'input': '(= y (- (sinh x) (sinh z)))'},#(- (sinh $0) (sinh $1))


    ('hin', '3'): {   'expected': '(= y (- (cosh x) (cosh z)))',
                      'input': '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))'},#(* (* "2" (sinh (/ (+ $0 $1) "2"))) (sinh (/ (- $0 z) "2")))
    ('vor', '3'): {'expected': '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))', 'input': '(= y (- (cosh x) (cosh z)))'}#(- (cosh $0) (cosh $1))

}
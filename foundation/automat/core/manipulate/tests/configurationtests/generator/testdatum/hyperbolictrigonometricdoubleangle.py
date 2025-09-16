TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (cosh (* "2" x)))',
                      'input': '(= y (+ (^ (sinh x) "2") (^ (cosh x) "2")))'},#(+ (^ (sinh $0) "2") (^ (cosh $0) "2"))
    ('vor', '0'): {'expected': '(= y (+ (^ (sinh x) "2") (^ (cosh x) "2")))', 'input': '(= y (cosh (* "2" x)))'},#(cosh (* "2" $0))


    ('hin', '1'): {   'expected': '(= y (cosh (* "2" x)))',
                      'input': '(= y (+ (* "2" (^ (sinh x) "2")) "1"))'},#(+ (* "2" (^ (sinh $0) "2")) "1")
    ('vor', '1'): {'expected': '(= y (+ (* "2" (^ (sinh x) "2")) "1"))', 'input': '(= y (cosh (* "2" x)))'},#(cosh (* "2" $0))


    ('hin', '2'): {   'expected': '(= y (cosh (* "2" x)))',
                      'input': '(= y (- (* "2" (^ (cosh x) "2")) "1"))'},#(- (* "2" (^ (cosh $0) "2")) "1")
    ('vor', '2'): {'expected': '(= y (- (* "2" (^ (cosh x) "2")) "1"))', 'input': '(= y (cosh (* "2" x)))'},#(cosh (* "2" $0))


    ('hin', '3'): {   'expected': '(= y (sinh (* "2" x)))',
                      'input': '(= y (* (* "2" (sinh x)) (cosh x)))'},#(* (* "2" (sinh $0)) (cosh $0))
    ('vor', '3'): {'expected': '(= y (* (* "2" (sinh x)) (cosh x)))', 'input': '(= y (sinh (* "2" x)))'},#(sinh (* "2" $0))


    ('hin', '4'): {   'expected': '(= y (tanh (* "2" x)))',
                      'input': '(= y (/ (* "2" (tanh x)) (+ "1" (^ (tanh x) "2"))))'},#(/ (* "2" (tanh $0)) (+ "1" (^ (tanh $0) "2")))
    ('vor', '4'): {'expected': '(= y (/ (* "2" (tanh x)) (+ "1" (^ (tanh x) "2"))))', 'input': '(= y (tanh (* "2" x)))'}#(tanh (* "2" $0))

}
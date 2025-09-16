TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (^ "e" x))',
                      'input': '(= y (nroot "2" (/ (+ "1" (tanh x)) (- "1" (tanh x)))))'},#(nroot "2" (/ (+ "1" (tanh $0)) (- "1" (tanh $0))))
    ('vor', '0'): {'expected': '(= y (nroot "2" (/ (+ "1" (tanh x)) (- "1" (tanh x)))))', 'input': '(= y (^ "e" x))'},#(^ "e" $0)


    ('hin', '1'): {   'expected': '(= y (^ "e" x))',
                      'input': '(= y (/ (+ "1" (tanh (/ x "2"))) (- "1" (tanh (/ x "2")))))'},#(/ (+ "1" (tanh (/ $0 "2"))) (- "1" (tanh (/ $0 "2"))))
    ('vor', '1'): {'expected': '(= y (/ (+ "1" (tanh (/ x "2"))) (- "1" (tanh (/ x "2")))))', 'input': '(= y (^ "e" x))'},#(^ "e" $0)


    ('hin', '2'): {   'expected': '(= y (^ "e" (* "i" x)))',
                      'input': '(= y (+ (sinh (* "i" x)) (cosh (* "i" x))))'},#(+ (sinh (* "i" $0)) (cosh (* "i" $0)))
    ('vor', '2'): {'expected': '(= y (+ (sinh (* "i" x)) (cosh (* "i" x))))', 'input': '(= y (^ "e" (* "i" x)))'},#(^ "e" (* "i" $0))


    ('hin', '3'): {'expected': '(= y (^ "e" x))', 'input': '(= y (+ (sinh x) (cosh x)))'},#(+ (sinh $0) (cosh $0))
    ('vor', '3'): {'expected': '(= y (+ (sinh x) (cosh x)))', 'input': '(= y (^ "e" x))'},#(^ "e" $0)


    ('hin', '4'): {'expected': '(= y (^ "e" (- "0" x)))', 'input': '(= y (- (cosh x) (sinh x)))'},#(- (cosh x) (sinh x))
    ('vor', '4'): {'expected': '(= y (- (cosh x) (sinh x)))', 'input': '(= y (^ "e" (- "0" x)))'}#(^ "e" (- "0" x))

}
TEST_DATUM={
    ('hin', '0'): {   'expected': '(= a (/ (sin b) (cos b)))',
                      'input': '(= a (tan b))'},
    ('vor', '0'): {   'expected': '(= a (tan b))',
                      'input': '(= a (/ (sin b) (cos b)))'},
    ('hin', '1'): {   'expected': '(= a (/ (cos b) (sin b)))',
                      'input': '(= a (cot b))'},
    ('vor', '1'): {   'expected': '(= a (cot b))',
                      'input': '(= a (/ (cos b) (sin b)))'},
    ('hin', '2'): {   'expected': '(= a (/ "1" (sin b)))',
                      'input': '(= a (cosec b))'},
    ('vor', '2'): {   'expected': '(= a (cosec b))',
                      'input': '(= a (/ "1" (sin b)))'},
    ('hin', '3'): {'expected': '(= a (/ "1" (cos b)))', 'input': '(= a (sec b))'},
    ('vor', '3'): {'expected': '(= a (sec b))', 'input': '(= a (/ "1" (cos b)))'},
    ('hin', '4'): {'expected': '(= a (/ "1" (tan b)))', 'input': '(= a (cot b))'},
    ('vor', '4'): {'expected': '(= a (cot b))', 'input': '(= a (/ "1" (tan b)))'},
    ('hin', '5'): {'expected': '(= a (/ "1" (cot b)))', 'input': '(= a (tan b))'},
    ('vor', '5'): {'expected': '(= a (tan b))', 'input': '(= a (/ "1" (cot b)))'},

    ('hin', '6'): {'expected':'(= y (sin (- "0" x)))', 'input':'(= y (- "0" (sin x)))'},#(sin (- "0" x))
    ('vor', '6'): {'expected':'(= y (- "0" (sin x)))', 'input':'(= y (sin (- "0" x)))'},#(- "0" (sin x))


    ('hin', '7'): {'expected':'(= y (cos (- "0" x)))', 'input':'(= y (cos x))'},#(cos (- "0" x))
    ('vor', '7'): {'expected':'(= y (cos x))', 'input':'(= y (cos (- "0" x)))'},#(cos x)

    
    ('hin', '8'): {'expected':'(= y (sin x))', 'input':'(= y (/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i")))'},#(sin x)
    ('vor', '8'): {'expected':'(= y (/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i")))', 'input':'(= y (sin x))'},#(/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i"))

    
    ('hin', '9'): {'expected':'(= y (cos x))', 'input':'(= y (/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2"))'},#(cos x)
    ('vor', '9'): {'expected':'(= y (/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2"))', 'input':'(= y (cos x))'},#(/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2")

    
    ('hin', '10'): {'expected':'(= y (^ "e" (* "i" x)))', 'input':'(= y (+ (cos x) (* "i" (sin x))))'},#(^ "e" (* "i" x))
    ('vor', '10'): {'expected':'(= y (+ (cos x) (* "i" (sin x))))', 'input':'(= y (^ "e" (* "i" x)))'}#(+ (cos x) (* "i" (sin x)))

    
    }
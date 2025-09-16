TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (cosh x))',
                      'input': '(= y (/ (+ (^ "e" x) (^ "e" (- "0" x))) "2"))'},#(/ (+ (^ "e" $0) (^ "e" (- "0" $0))) "2")
    ('vor', '0'): {'expected': '(= y (/ (+ (^ "e" x) (^ "e" (- "0" x))) "2"))', 'input': '(= y (cosh x))'},#(cosh $0)


    ('hin', '1'): {   'expected': '(= y (sinh x))',
                      'input': '(= y (/ (- (^ "e" x) (^ "e" (- "0" x))) "2"))'},#(/ (- (^ "e" $0) (^ "e" (- "0" $0))) "2")
    ('vor', '1'): {'expected': '(= y (/ (- (^ "e" x) (^ "e" (- "0" x))) "2"))', 'input': '(= y (sinh x))'},#(sinh $0)


    ('hin', '2'): {'expected': '(= y (cosh (- "0" x)))', 'input': '(= y (cosh x))'},#(cosh $0)
    ('vor', '2'): {'expected': '(= y (cosh x))', 'input': '(= y (cosh (- "0" x)))'},#(cosh (- "0" $0))


    ('hin', '3'): {   'expected': '(= y (sin x))',
                      'input': '(= y (- "0" (* "i" (sinh (* "i" x)))))'},#(- "0" (* "i" (sinh (* "i" $0))))
    ('vor', '3'): {'expected': '(= y (- "0" (* "i" (sinh (* "i" x)))))', 'input': '(= y (sin x))'},#(sin $0)


    ('hin', '4'): {'expected': '(= y (cos x))', 'input': '(= y (cosh (* "i" x)))'},#(cosh (* "i" $0))
    ('vor', '4'): {'expected': '(= y (cosh (* "i" x)))', 'input': '(= y (cos x))'},#(cos $0)


    ('hin', '5'): {'expected': '(= y (sin (* "i" x)))', 'input': '(= y (* "i" (sinh x)))'},#(* "i" (sinh $0))
    ('vor', '5'): {'expected': '(= y (* "i" (sinh x)))', 'input': '(= y (sin (* "i" x)))'},#(sin (* "i" $0))


    ('hin', '6'): {'expected': '(= y (cos (* "i" x)))', 'input': '(= y (cosh x))'},#(cosh $0)
    ('vor', '6'): {'expected': '(= y (cosh x))', 'input': '(= y (cos (* "i" x)))'},#(cos (* "i" $0))


    ('hin', '7'): {'expected': '(= y (sinh (- "0" x)))', 'input': '(= y (- "0" (sinh x)))'},#(- "0" (sinh $0))
    ('vor', '7'): {'expected': '(= y (- "0" (sinh x)))', 'input': '(= y (sinh (- "0" x)))'},#(sinh (- "0" $0))


    ('hin', '8'): {   'expected': '(= y (tan x))',
                      'input': '(= y (- "0" (* "i" (tanh (* "i" x)))))'},#(- "0" (* "i" (tanh (* "i" $0))))
    ('vor', '8'): {'expected': '(= y (- "0" (* "i" (tanh (* "i" x)))))', 'input': '(= y (tan x))'},#(tan $0)


    ('hin', '9'): {'expected': '(= y (cot x))', 'input': '(= y (* "i" (coth (* "i" x))))'},#(* "i" (coth (* "i" $0)))
    ('vor', '9'): {'expected': '(= y (* "i" (coth (* "i" x))))', 'input': '(= y (cot x))'},#(cot $0)


    ('hin', '10'): {'expected': '(= y (sec x))', 'input': '(= y (sech (* "i" x)))'},#(sech (* "i" $0))
    ('vor', '10'): {'expected': '(= y (sech (* "i" x)))', 'input': '(= y (sec x))'},#(sec $0)


    ('hin', '11'): {'expected': '(= y (cosec x))', 'input': '(= y (* "i" (cosech (* "i" x))))'},#(* "i" (cosech (* "i" $0)))
    ('vor', '11'): {'expected': '(= y (* "i" (cosech (* "i" x))))', 'input': '(= y (cosec x))'},#(cosec $0)


    ('hin', '12'): {'expected': '(= y (tanh (- "0" x)))', 'input': '(= y (- "0" (tanh x)))'},#(- "0" (tanh $0))
    ('vor', '12'): {'expected': '(= y (- "0" (tanh x)))', 'input': '(= y (tanh (- "0" x)))'},#(tanh (- "0" x))


    ('hin', '13'): {'expected': '(= y (coth (- "0" x)))', 'input': '(= y (- "0" (coth x)))'},#(- "0" (coth $0))
    ('vor', '13'): {'expected': '(= y (- "0" (coth x)))', 'input': '(= y (coth (- "0" x)))'},#(coth (- "0" $0))


    ('hin', '14'): {'expected': '(= y (sech (- "0" x)))', 'input': '(= y (sech x))'},#(sech $0)
    ('vor', '14'): {'expected': '(= y (sech x))', 'input': '(= y (sech (- "0" x)))'},#(sech (- "0" $0))


    ('hin', '15'): {'expected': '(= y (cosech (- "0" x)))', 'input': '(= y (- "0" (cosech x)))'},#(- "0" (cosech $0))
    ('vor', '15'): {'expected': '(= y (- "0" (cosech x)))', 'input': '(= y (cosech (- "0" x)))'}#(cosech (- "0" $0))

}
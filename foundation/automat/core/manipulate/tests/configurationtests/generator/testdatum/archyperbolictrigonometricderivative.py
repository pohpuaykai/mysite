TEST_DATUM = {   
    ('hin', '0'): {   'expected': '(= y (D (arcsinh x) x))',
                      'input': '(= y (* (sech (arcsinh x)) (D x x)))'},#(* (sech (arcsinh $0)) (D $0 $1))
    ('vor', '0'): {'expected': '(= y (* (sech (arcsinh x)) (D x x)))', 'input': '(= y (D (arcsinh x) x))'},#(D (arcsinh $0) $1)


    ('hin', '1'): {   'expected': '(= y (D (arccosh x) x))',
                      'input': '(= y (* (cosech (arccosh x)) (D x x)))'},#(* (cosech (arccosh $0)) (D $0 $1))
    ('vor', '1'): {'expected': '(= y (* (cosech (arccosh x)) (D x x)))', 'input': '(= y (D (arccosh x) x))'},#(D (arccosh $0) $1)


    ('hin', '2'): {   'expected': '(= y (D (arctanh x) x))',
                      'input': '(= y (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)))'},#(* (/ (+ "1" (cosh (* "2" (arctanh $0)))) "2") (D $0 $1))
    ('vor', '2'): {'expected': '(= y (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)))', 'input': '(= y (D (arctanh x) x))'},#(D (arctanh $0) $1)


    ('hin', '3'): {   'expected': '(= y (D (arcsech x) x))',
                      'input': '(= y (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)))'},#(* (* (- "0" (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1))
    ('vor', '3'): {'expected': '(= y (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)))', 'input': '(= y (D (arcsech x) x))'},#(D (arcsech $0) $1)


    ('hin', '4'): {   'expected': '(= y (D (arccosech x) x))',
                      'input': '(= y (* (* (- "0" (sinh (arccosech x)))) (D x x)))'},#(* (* (- "0" (sinh (arccosech $0)))) (D $0 $1))
    ('vor', '4'): {'expected': '(= y (* (* (- "0" (sinh (arccosech x)))) (D x x)))', 'input': '(= y (D (arccosech x) x))'},#(D (arccosech $0) $1)


    ('hin', '5'): {   'expected': '(= y (D (arccoth x) x))',
                      'input': '(= y (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)))'},#(* (/ (- "1" (sinh (arccoth $0))) "2") (D $0 $1))
    ('vor', '5'): {'expected': '(= y (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)))', 'input': '(= y (D (arccoth x) x))'}#(D (arccoth $0) $1)
}
TEST_DATUM = {
    ('hin', '0'): {'expected': '(= (arcsin (sin y)) (arcsin (sin x)))', 'input': '(= y x)'},#$0
    ('vor', '0'): {'expected': '(= y x)', 'input': '(= y (arcsin (sin x)))'},#(arcsin (sin $0))


    ('hin', '1'): {'expected': '(= (arccos (cos y)) (arccos (cos x)))', 'input': '(= y x)'},#$0
    ('vor', '1'): {'expected': '(= y x)', 'input': '(= y (arccos (cos x)))'},#(arccos (cos $0))


    ('hin', '2'): {'expected': '(= (arctan (tan y)) (arctan (tan x)))', 'input': '(= y x)'},#$0
    ('vor', '2'): {'expected': '(= y x)', 'input': '(= y (arctan (tan x)))'},#(arctan (tan $0))


    ('hin', '3'): {'expected': '(= (arcsec (sec y)) (arcsec (sec x)))', 'input': '(= y x)'},#$0
    ('vor', '3'): {'expected': '(= y x)', 'input': '(= y (arcsec (sec x)))'},#(arcsec (sec $0))


    ('hin', '4'): {'expected': '(= (arccosec (cosec y)) (arccosec (cosec x)))', 'input': '(= y x)'},#$0
    ('vor', '4'): {'expected': '(= y x)', 'input': '(= y (arccosec (cosec x)))'},#(arccosec (cosec $0))


    ('hin', '5'): {'expected': '(= (arccot (cot y)) (arccot (cot x)))', 'input': '(= y x)'},#$0
    ('vor', '5'): {'expected': '(= y x)', 'input': '(= y (arccot (cot x)))'},#(arccot (cot $0))


    ('hin', '6'): {'expected': '(= y (arcsech x))', 'input': '(= y (arccosh (/ "1" x)))'},#(arccosh (/ "1" x))
    ('vor', '6'): {'expected': '(= y (arccosh (/ "1" x)))', 'input': '(= y (arcsech x))'},#(arcsech x)


    ('hin', '7'): {'expected': '(= y (arccosech x))', 'input': '(= y (arcsinh (/ "1" x)))'},#(arcsinh (/ "1" x))
    ('vor', '7'): {'expected': '(= y (arcsinh (/ "1" x)))', 'input': '(= y (arccosech x))'},#(arccosech x)


    ('hin', '8'): {'expected': '(= y (arccoth x))', 'input': '(= y (arctanh (/ "1" x)))'},#(arctanh (/ "1" x))
    ('vor', '8'): {'expected': '(= y (arctanh (/ "1" x)))', 'input': '(= y (arccoth x))'}#(arccoth x)

}
TEST_DATUM = {   
    ('hin', '0'): {'expected': '(= (arcsinh (sinh x)) (arcsinh (sinh x)))', 'input': '(= x x)'}, #$0
    ('vor', '0'): {'expected': '(= y x)', 'input': '(= y (arcsinh (sinh x)))'},#(arcsinh (sinh $0))


    ('hin', '1'): {'expected': '(= (sinh (arcsinh x)) (sinh (arcsinh x)))', 'input': '(= x x)'},#$0
    ('vor', '1'): {'expected': '(= y x)', 'input': '(= y (sinh (arcsinh x)))'},#(sinh (arcsinh $0))


    ('hin', '2'): {'expected': '(= (arccosh (cosh x)) (arccosh (cosh x)))', 'input': '(= x x)'},#$0
    ('vor', '2'): {'expected': '(= y x)', 'input': '(= y (arccosh (cosh x)))'},#(arccosh (cosh $0))


    ('hin', '3'): {'expected': '(= (cosh (arccosh x)) (cosh (arccosh x)))', 'input': '(= x x)'},#$0
    ('vor', '3'): {'expected': '(= y x)', 'input': '(= y (cosh (arccosh x)))'},#(cosh (arccosh $0))


    ('hin', '4'): {'expected': '(= (arctanh (tanh x)) (arctanh (tanh x)))', 'input': '(= x x)'},#$0
    ('vor', '4'): {'expected': '(= y x)', 'input': '(= y (arctanh (tanh x)))'},#(arctanh (tanh $0))


    ('hin', '5'): {'expected': '(= (tanh (arctanh x)) (tanh (arctanh x)))', 'input': '(= x x)'},#$0
    ('vor', '5'): {'expected': '(= y x)', 'input': '(= y (tanh (arctanh x)))'},#(tanh (arctanh $0))


    ('hin', '6'): {'expected': '(= (arcsech (sech x)) (arcsech (sech x)))', 'input': '(= x x)'},#$0
    ('vor', '6'): {'expected': '(= y x)', 'input': '(= y (arcsech (sech x)))'},#(arcsech (sech $0))


    ('hin', '7'): {'expected': '(= (sech (arcsech x)) (sech (arcsech x)))', 'input': '(= x x)'},#$0
    ('vor', '7'): {'expected': '(= y x)', 'input': '(= y (sech (arcsech x)))'},#(sech (arcsech $0))


    ('hin', '8'): {'expected': '(= (arccosech (cosech x)) (arccosech (cosech x)))', 'input': '(= x x)'},#$0
    ('vor', '8'): {'expected': '(= y x)', 'input': '(= y (arccosech (cosech x)))'},#(arccosech (cosech $0))


    ('hin', '9'): {'expected': '(= (cosech (arccosech x)) (cosech (arccosech x)))', 'input': '(= x x)'},#$0
    ('vor', '9'): {'expected': '(= y x)', 'input': '(= y (cosech (arccosech x)))'},#(cosech (arccosech $0))

    ('hin', '10'): {'expected': '(= (arccoth (coth x)) (arccoth (coth x)))', 'input': '(= x x)'},#$0
    ('vor', '10'): {'expected': '(= y x)', 'input': '(= y (arccoth (coth x)))'},#(arccoth (coth $0))


    ('hin', '11'): {'expected': '(= (coth (arccoth x)) (coth (arccoth x)))', 'input': '(= x x)'},#$0
    ('vor', '11'): {'expected': '(= y x)', 'input': '(= y (coth (arccoth x)))'}#(coth (arccoth $0))
}
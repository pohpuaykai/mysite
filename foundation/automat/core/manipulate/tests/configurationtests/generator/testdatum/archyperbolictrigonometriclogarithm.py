TEST_DATUM = {   
    ('hin', '0'): {   'expected': '(= y (arcsinh x))',
                      'input': '(= y (log "e" (+ x (nroot "2" (+ (^ x "2") "1")))))'},#(log "e" (+ $0 (nroot "2" (+ (^ $0 "2") "1"))))
    ('vor', '0'): {'expected': '(= y (log "e" (+ x (nroot "2" (+ (^ x "2") "1")))))', 'input': '(= y (arcsinh x))'},#(arcsinh $0)


    ('hin', '1'): {   'expected': '(= y (arccosh x))',
                      'input': '(= y (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))'},#(log "e" (+ $0 (nroot "2" (- (^ $0 "2") "1"))))
    ('vor', '1'): {'expected': '(= y (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))', 'input': '(= y (arccosh x))'},#(arccosh $0)


    ('hin', '2'): {   'expected': '(= y (arctanh x))',
                      'input': '(= y (/ (log "e" (/ (+ "1" x) (- "1" x))) "2"))'},#(/ (log "e" (/ (+ "1" $0) (- "1" $0))) "2")
    ('vor', '2'): {'expected': '(= y (/ (log "e" (/ (+ "1" x) (- "1" x))) "2"))', 'input': '(= y (arctanh x))'},#(arctanh $0)


    ('hin', '3'): {   'expected': '(= y (arccoth x))',
                      'input': '(= y (/ (log "e" (/ (+ x "1") (- x "1"))) "2"))'},#(/ (log "e" (/ (+ $0 "1") (- $0 "1"))) "2")
    ('vor', '3'): {'expected': '(= y (/ (log "e" (/ (+ x "1") (- x "1"))) "2"))', 'input': '(= y (arccoth x))'},#(arccoth $0)


    ('hin', '4'): {   'expected': '(= y (arcsech x))',
                      'input': '(= y (log "e" (+ (/ "1" x) (nroot "2" (- (/ "1" (^ x "2")) "1")))))'},#(log "e" (+ (/ "1" $0) (nroot "2" (- (/ "1" (^ $0 "2")) "1"))))
    ('vor', '4'): {'expected': '(= y (log "e" (+ (/ "1" x) (nroot "2" (- (/ "1" (^ x "2")) "1")))))', 'input': '(= y (arcsech x))'},#(arcsech $0)


    ('hin', '5'): {   'expected': '(= y (arcsech x))',
                      'input': '(= y (log "e" (/ (+ "1" (nroot "2" (- "1" (^ x "2")))) x)))'},#(log "e" (/ (+ "1" (nroot "2" (- "1" (^ $0 "2")))) $0))
    ('vor', '5'): {'expected': '(= y (log "e" (/ (+ "1" (nroot "2" (- "1" (^ x "2")))) x)))', 'input': '(= y (arcsech x))'},#(arcsech $0)


    ('hin', '6'): {   'expected': '(= y (arccosech x))',
                      'input': '(= y (log "e" (+ (/ "1" x) (nroot "2" (+ (/ "1" (^ x "2")) "1")))))'},#(log "e" (+ (/ "1" $0) (nroot "2" (+ (/ "1" (^ $0 "2")) "1"))))
    ('vor', '6'): {'expected': '(= y (log "e" (+ (/ "1" x) (nroot "2" (+ (/ "1" (^ x "2")) "1")))))', 'input': '(= y (arccosech x))'}#(arccosech $0)
}
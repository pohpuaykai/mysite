TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (arcsin x))',
                      'input': '(= y (- "0" (* "i" (log "e" (+ (* "i" x) (nroot "2" (- "1" (^ x "2"))))))))'},#(- "0" (* "i" (log "e" (+ (* "i" x) (nroot "2" (- "1" (^ x "2")))))))
    ('vor', '0'): {'expected': '(= y (- "0" (* "i" (log "e" (+ (* "i" x) (nroot "2" (- "1" (^ x "2"))))))))', 'input': '(= y (arcsin x))'},#(arcsin x)


    ('hin', '1'): {   'expected': '(= y (arccos x))',
                      'input': '(= y (- "0" (* "i" (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))))'},#(- "0" (* "i" (log "e" (+ x (nroot "2" (- (^ x "2") "1"))))))
    ('vor', '1'): {'expected': '(= y (- "0" (* "i" (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))))', 'input': '(= y (arccos x))'},#(arccos x)


    ('hin', '2'): {   'expected': '(= y (arctan x))',
                      'input': '(= y (* (/ "i" "2") (log "e" (/ (+ "i" x) (- "i" x)))))'},#(* (/ "i" "2") (log "e" (/ (+ "i" x) (- "i" x))))
    ('vor', '2'): {'expected': '(= y (* (/ "i" "2") (log "e" (/ (+ "i" x) (- "i" x)))))', 'input': '(= y (arctan x))'},#(arctan x)


    ('hin', '3'): {   'expected': '(= y (arccosec x))',
                      'input': '(= y (- "0" (* "i" (log "e" (+ (/ "i" x) (nroot "2" (- "1" (/ "1" (^ x "2")))))))))'},#(- "0" (* "i" (log "e" (+ (/ "i" x) (nroot "2" (- "1" (/ "1" (^ x "2"))))))))
    ('vor', '3'): {'expected': '(= y (- "0" (* "i" (log "e" (+ (/ "i" x) (nroot "2" (- "1" (/ "1" (^ x "2")))))))))', 'input': '(= y (arccosec x))'},#(arccosec x)


    ('hin', '4'): {   'expected': '(= y (arcsec x))',
                      'input': '(= y (- "0" (* "i" (log "e" (+ (/ "1" x) (* "i" (nroot "2" (- "1" (/ "1" (^ x "2"))))))))))'},#(- "0" (* "i" (log "e" (+ (/ "1" x) (* "i" (nroot "2" (- "1" (/ "1" (^ x "2")))))))))
    ('vor', '4'): {'expected': '(= y (- "0" (* "i" (log "e" (+ (/ "1" x) (* "i" (nroot "2" (- "1" (/ "1" (^ x "2"))))))))))', 'input': '(= y (arcsec x))'},#(arcsec x)


    ('hin', '5'): {   'expected': '(= y (arccot x))',
                      'input': '(= y (* (/ "i" "2") (log "e" (/ (- x "i") (+ x "i")))))'},#(* (/ "i" "2") (log "e" (/ (- x "i") (+ x "i"))))
    ('vor', '5'): {'expected': '(= y (* (/ "i" "2") (log "e" (/ (- x "i") (+ x "i")))))', 'input': '(= y (arccot x))'}#(arccot x)

}
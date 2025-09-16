TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (D (nroot f g) x))',
                      'input': '(= y (* (nroot f g) (/ (- (/ (* (D g x) f) g) (* (D f x) (log "e" g))) (^ f 2))))'},#(* (nroot $0 $1) (/ (- (/ (* (D $1 $2) $0) $1) (* (D $0 $2) (log "e" $1))) (^ $0 2)))
    ('vor', '0'): {'expected': '(= y (* (nroot f g) (/ (- (/ (* (D g x) f) g) (* (D f x) (log "e" g))) (^ f 2))))', 'input': '(= y (D (nroot f g) x))'},#(D (nroot $0 $1) $2)

    
    ('hin', '1'): {   'expected': '(= y (D (nroot a f) x))',
                      'input': '(= y (* (* (D f x) (/ "1" a)) (^ f (- (/ "1" a) "1"))))'},#
    ('vor', '1'): {'expected': '(= y (* (* (D f x) (/ "1" a)) (^ f (- (/ "1" a) "1"))))', 'input': '(= y (D (nroot a f) x))'}#

}
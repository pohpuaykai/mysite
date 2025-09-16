TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int (/ (- (* (* (D g v_{0}) (/ "1" g)) (log "e" f)) (* (* (D f v_{0}) (/ "1" f)) (log "e" g))) (^ (log "e" f) "2")) v_{0}))', 'input': '(= y (log f g))'},#(log $0 $1)
    ('vor', '0'): {   'expected': '(= y (log f g))',
                      'input': '(= y (int (/ (- (* (* (D g x) (/ "1" g)) (log "e" f)) (* (* (D f x) (/ "1" f)) (log "e" g))) (^ (log "e" f) "2")) x))'},#(int (/ (- (* (* (D $1 $2) (/ "1" $1)) (log "e" $0)) (* (* (D $0 $2) (/ "1" $0)) (log "e" $1))) (^ (log "e" $0) "2")) $2)


    ('hin', '1'): {'expected': '(= y (int (/ (D x v_{0}) (* x (log "e" b))) v_{0}))', 'input': '(= y (log b v_{0}))'},#(log $0 $1)
    ('vor', '1'): {   'expected': '(= y (log b x))',
                      'input': '(= y (int (/ (D x x) (* x (log "e" b))) x))'},#(int (/ (D $1 $2) (* $1 (log "e" $0))) $2)

                      
    ('hin', '2'): {'expected': '(= y (int (/ (D x v_{0}) x) v_{0}))', 'input': '(= y (log "e" v_{0}))'},#(log "e" $0)
    ('vor', '2'): {'expected': '(= y (log "e" x))', 'input': '(= y (int (/ (D x x) x) x))'}#(int (/ (D $0 $1) $1) $1)

    }
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<integration results please add a constant<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
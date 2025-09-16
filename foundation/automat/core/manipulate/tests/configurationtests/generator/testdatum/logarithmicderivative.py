TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (D (log f g) x))',
                      'input': '(= y (/ (- (* (* (D g x) (/ "1" g)) (log "e" f)) (* (* (D f x) (/ "1" f)) (log "e" g))) (^ (log "e" f) "2")))'},#(/ (- (* (* (D $1 $2) (/ "1" $1)) (log "e" $0)) (* (* (D $0 $2) (/ "1" $0)) (log "e" $1))) (^ (log "e" $0) "2"))
    ('vor', '0'): {'expected': '(= y (/ (- (* (* (D g x) (/ "1" g)) (log "e" f)) (* (* (D f x) (/ "1" f)) (log "e" g))) (^ (log "e" f) "2")))', 'input': '(= y (D (log f g) x))'},#(D (log $0 $1) $2)


    ('hin', '1'): {   'expected': '(= y (D (log "10" x) x))',
                      'input': '(= y (/ (D x x) (* x (log "e" "10"))))'},#(/ (D $1 $2) (* $1 (log "e" $0)))
    ('vor', '1'): {'expected': '(= y (/ (D x x) (* x (log "e" "10"))))', 'input': '(= y (D (log "10" x) x))'},#(D (log $0 $1) $2)


    ('hin', '2'): {'expected': '(= y (D (log "e" x) x))', 'input': '(= y (/ (D x x) x))'},#(/ (D $0 $1) $1)
    ('vor', '2'): {'expected': '(= y (/ (D x x) x))', 'input': '(= y (D (log "e" x) x))'}#(D (log "e" $0) $1)

}
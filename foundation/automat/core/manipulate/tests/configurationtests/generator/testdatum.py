TEST_DATUM = {
    "communtativity": {
        ('vor', '0'): {
            "input": "(= a (+ b c))",
            "expected": "(= a (+ c b))"
        },
        ('hin', '0'): {
            "input": "(= a (+ b c))",
            "expected": "(= a (+ c b))"
        },
        ('vor', '1'): {
            "input": "(= a (* b c))",
            "expected": "(= a (* c b))"
        },
        ('hin', '1'): {
            "input": "(= a (* b c))",
            "expected": "(= a (* c b))"
        },
        ('vor', '2'): {
            "input": "(= a b)",
            "expected": "(= b a)"
        },
        ('hin', '2'): {
            "input": "(= a b)",
            "expected": "(= b a)"
        }
    },
    "crossmultiply": {
        ('vor', '0'): {
            "input": "(= a (+ (/ b c) (/ d e)))",
            "expected": "(= a (/ (+ (* b e) (* c d)) (* c e)))"
        },
        ('hin', '0'): {
            "input": "(= a (/ (+ (* b e) (* c d)) (* c e)))",
            "expected": "(= a (+ (/ b c) (/ d e)))"
        }
    },
    "distributivity": {
        ('vor', '0'): {
            "input": "(= a (+ (* b c) (* b d)))",
            "expected": "(= a (* b (+ c d)))"
        },
        ('hin', '0'): {
            "input": "(= a (* b (+ c d)))",
            "expected": "(= a (+ (* b c) (* b d)))"
        },
        ('vor', '1'): {
            "input": "(= a (- (* b c) (* b d)))",
            "expected": "(= a (* b (- c d)))"
        },
        ('hin', '1'): {
            "input": "(= a (* b (- c d)))",
            "expected": "(= a (- (* b c) (* b d)))"
        },
        ('vor', '2'): {
            "input": "(= a (+ (/ b c) (/ d c)))",
            "expected": "(= a (/ (+ b d) c))"
        },
        ('hin', '2'): {
            "input": "(= a (/ (+ b c) d))",
            "expected": "(= a (+ (/ b d) (/ c d)))"
        },
        ('vor', '3'): {
            "input": "(= a (- (/ b c) (/ d c)))",
            "expected": "(= a (/ (- b d) c))"
        },
        ('hin', '3'): {
            "input": "(= a (/ (- b c) d))",
            "expected": "(= a (- (/ b d) (/ c d)))"
        }
    },
    "doubleinverse": {
        ('vor', '0'): {
            "input": "(= a (/ (/ b c) d))",
            "expected": "(= a (/ b (* c d)))"
        },
        ('hin', '0'): {
            "input": "(= a (/ b (* c d)))",
            "expected": "(= a (/ (/ b c) d))"
        },
        ('vor', '1'): {
            "input": "(= a (/ b (/ c d)))",
            "expected": "(= a (/ (* b d) c))"
        },
        ('hin', '1'): {
            "input": "(= a (/ (* b c) d))",
            "expected": "(= a (/ b (/ d c)))"
        }
    },
    "exponential": {
        ('vor', '0'): {
            "input": "(= a (^ b 0))",
            "expected": "1"
        },
        ('hin', '0'): {
            "input": "(= a (+ 1 (+ 1 1)))",
            "expected": "(= a (+ (^ v_{0} 0) (+ (^ v_{1} 0) (^ v_{2} 0))))"
        },
        ('vor', '1'): {
            "input": "(= a (^ b 1))",
            "expected": "(= a b)"
        },
        ('hin', '1'): {
            "input": "(= a a)",
            "expected": "(= (^ a 1) (^ a 1))"
        },
        ('vor', '2'): {
            "input": "(= a (^ b (+ c d)))",
            "expected": "(= a (* (^ b c) (^ b d)))"
        },
        ('hin', '2'): {
            "input": "(= a (* (^ b c) (^ b d)))",
            "expected": "(= a (^ b (+ c d)))"
        },
        ('vor', '3'): {
            "input": "(= a (^ (^ b c) d))",
            "expected": "(= a (^ b (* c d)))"
        },
        ('hin', '3'): {
            "input": "(= a (^ b (* c d)))",
            "expected": "(= a (^ (^ b c) d))"
        },
        ('vor', '4'): {
            "input": "(= a (* (^ b c) (^ d c)))",
            "expected": "(= a (^ (* b d) c))"
        },
        ('hin', '4'): {
            "input": "(= a (^ (* b c) d))",
            "expected": "(= a (* (^ b d) (^ c d)))"
        },
        ('vor', '5'): {
            "input": "(= a (^ b (- \"0\" c)))",
            "expected": "(= a (/ \"1\" (^ b c)))"
        },
        ('hin', '5'): {
            "input": "(= a (/ \"1\" (^ b c)))",
            "expected": "(= a (^ b (- \"0\" c)))"
        }
    },
    "logarithm": {
        ('vor', '0'): {
            "input": "(= a (log a (* b c)))",
            "expected": "(= a (+ (log a b) (log a c)))"
        },
        ('hin', '0'): {
            "input": "(= a (+ (log b c) (log b d)))",
            "expected": "(= a (log b (* c d)))"
        },
        ('vor', '1'): {
            "input": "(= a (log b (/ c d)))",
            "expected": "(= a (- (log b c) (log b d)))"
        },
        ('hin', '1'): {
            "input": "(= a (- (log b c) (log b d)))",
            "expected": "(= a (log b (/ c d)))"
        },
        ('vor', '2'): {
            "input": "(= a (log b (^ c d)))",
            "expected": "(= a (* d (log b c)))"
        },
        ('hin', '2'): {
            "input": "(= a (* b (log c d)))",
            "expected": "(= a (log c (^ d b)))"
        },
        ('vor', '3'): {
            "input": "(= a (log b (nroot c d)))",
            "expected": "(= a (/ (log b d) c))"
        },
        ('hin', '3'): {
            "input": "(= a (/ (log b c) d))",
            "expected": "(= a (log b (nroot d c)))"
        },
        ('vor', '4'): {
            "input": "(= a (/ (log b c) (log b d)))",
            "expected": "(= a (log d c))"
        },
        ('hin', '4'): {
            "input": "(= a (log b c))",
            "expected": "(= a (/ (log v_{0} c) (log v_{0} b)))"
        },
        ('vor', '5'): {
            "input": "(= a (log b b))",
            "expected": "1"
        },
        ('hin', '5'): {
            "input": "(= a 1)",
            "expected": "(= a (log v_{0} v_{0}))"
        },
        ('vor', '6'): {
            "input": "(= a (log b 1))",
            "expected": "0"
        },
        ('hin', '6'): {
            "input": "(= a 0)",
            "expected": "(= a (log v_{0} 1))"
        }
    },
    "multiplydividecancel": {
        ('vor', '0'): {
            "input": "(= a (* (/ b c) c))",
            "expected": "(= a b)"
        },
        ('hin', '0'): {
            "input": "(= a a)",
            "expected": "(= (* (/ a v_{0}) v_{0}) (* (/ a v_{1}) v_{1}))"
        },
        ('vor', '1'): {
            "input": "(= a (/ (* b c) c))",
            "expected": "(= a b)"
        },
        ('hin', '1'): {
            "input": "(= a a)",
            "expected": "(= (/ (* a v_{0}) v_{0}) (/ (* a v_{1}) v_{1}))"
        }
    },
    "multiplyexponential": {
        ('vor', '0'): {
            "input": "(= p (* x x))",
            "expected": "(= p (^ x 2))"
        },
        ('hin', '0'): {
            "input": "(= p (^ x 2))",
            "expected": "(= p (* x x))"
        }
    },
    "multiplynegative": {
        ('vor', '0'): {
            "input": "(= a (* \"-1\" b))",
            "expected": "(= a (- 0 b))"
        },
        ('hin', '0'): {
            "input": "(= a (- 0 b))",
            "expected": "(= a (* \"-1\" b))"
        }
    },
    "nroot": {
        ('vor', '0'): {
            "input": "(= a (nroot b (^ c d)))",
            "expected": "(= a (^ c (/ d b)))"
        },
        ('hin', '0'): {
            "input": "(= a (^ b (/ c d)))",
            "expected": "(= a (nroot d (^ b c)))"
        },
        ('vor', '1'): {
            "input": "(= a (^ (nroot b c) d))",
            "expected": "(= a (nroot b (^ c d)))"
        },
        ('hin', '1'): {
            "input": "(= a (nroot b (^ c d)))",
            "expected": "(= a (^ (nroot b c) d))"
        },
        ('vor', '2'): {
            "input": "(= a (^ (nroot b c) d))",
            "expected": "(= a (^ c (/ d b)))"
        },
        ('hin', '2'): {
            "input": "(= a (^ b (/ c d)))",
            "expected": "(= a (^ (nroot d b) c))"
        },
        ('vor', '3'): {
            "input": "(= a (nroot b (* c d)))",
            "expected": "(= a (* (nroot b c) (nroot b d)))"
        },
        ('hin', '3'): {
            "input": "(= a (* (nroot b c) (nroot b d)))",
            "expected": "(= a (nroot b (* c d)))"
        },
        ('vor', '4'): {
            "input": "(= a (nroot b (/ c d)))",
            "expected": "(= a (/ (nroot b c) (nroot b d)))"
        },
        ('hin', '4'): {
            "input": "(= a (/ (nroot b c) (nroot b d)))",
            "expected": "(= a (nroot b (/ c d)))"
        }
    },
    "pythagoreanangle": {
        ('vor', '0'): {
            "input": "(= a (+ (^ (sin b) 2) (^ (cos b) 2)))",
            "expected": "1"
        },
        ('hin', '0'): {
            "input": "(= a 1)",
            "expected": "(= a (+ (^ (sin v_{0}) 2) (^ (cos v_{0}) 2)))"
        }
    },
    "rootbasenegative": {
        ('vor', '0'): {
            "input": "(= a (nroot (- 0 b) c))",
            "expected": "(= a (nroot b (/ 1 c)))"
        },
        ('hin', '0'): {
            "input": "(= a (nroot b (/ 1 c)))",
            "expected": "(= a (nroot (- 0 b) c))"
        }
    },
    "subtractzero": {
        ('vor', '0'): {
            "input": "(= a (- 0 b))",
            "expected": "(= a b)"
        },
        ('hin', '0'): {
            "input": "(= a a)",
            "expected": "(= (- 0 a) (- 0 a))"
        },
        ('vor', '1'): {
            "input": "(= a (- b 0))",
            "expected": "(= a b)"
        },
        ('hin', '1'): {
            "input": "(= a a)",
            "expected": "(= (- a 0) (- a 0))"
        }
    },
    "trigonometricequivalence": {
        ('vor', '0'): {
            "input": "(= a (/ (sin b) (cos b)))",
            "expected": "(= a (tan b))"
        },
        ('hin', '0'): {
            "input": "(= a (tan b))",
            "expected": "(= a (/ (sin b) (cos b)))"
        },
        ('vor', '1'): {
            "input": "(= a (/ (cos b) (sin b)))",
            "expected": "(= a (cot b))"
        },
        ('hin', '1'): {
            "input": "(= a (cot b))",
            "expected": "(= a (/ (cos b) (sin b)))"
        },
        ('vor', '2'): {
            "input": "(= a (/ 1 (sin b)))",
            "expected": "(= a (cosec b))"
        },
        ('hin', '2'): {
            "input": "(= a (cosec b))",
            "expected": "(= a (/ 1 (sin b)))"
        },
        ('vor', '3'): {
            "input": "(= a (/ 1 (cos b)))",
            "expected": "(= a (sec b))"
        },
        ('hin', '3'): {
            "input": "(= a (sec b))",
            "expected": "(= a (/ 1 (sec b)))"
        },
        ('vor', '4'): {
            "input": "(= a (/ 1 (tan b)))",
            "expected": "(= a (cot b))"
        },
        ('hin', '4'): {
            "input": "(= a (cot b))",
            "expected": "(= a (/ 1 (tan b)))"
        },
        ('vor', '5'): {
            "input": "(= a (/ 1 (cot b)))",
            "expected": "(= a (tan b))"
        },
        ('hin', '5'): {
            "input": "(= a (tan b))",
            "expected": "(= a (/ 1 (cot b)))"
        }
    },
    "trigonometricplusminusmultiply": {
        ('vor', '0'): {
            "input": "(= a (sin (+ b c)))",
            "expected": "(= a (+ (* (sin b) (cos c)) (* (cos b) (sin c))))"
        },
        ('hin', '0'): {
            "input": "(= a (+ (* (sin b) (cos c)) (* (cos b) (sin c))))",
            "expected": "(= a (sin (+ b c)))"
        },
        ('vor', '1'): {
            "input": "(= a (sin (- b c)))",
            "expected": "(= a (- (* (sin b) (cos c)) (* (cos b) (sin c))))"
        },
        ('hin', '1'): {
            "input": "(= a (- (* (sin b) (cos c)) (* (cos b) (sin c))))",
            "expected": "(= a (sin (- b c)))"
        },
        ('vor', '2'): {
            "input": "(= a (cos (+ b c)))",
            "expected": "(= a (- (* (cos b) (cos c)) (* (sin b) (sin c))))"
        },
        ('hin', '2'): {
            "input": "(= a (- (* (cos b) (cos c)) (* (sin b) (sin c))))",
            "expected": "(= a (cos (+ b c)))"
        },
        ('vor', '3'): {
            "input": "(= a (cos (- b c)))",
            "expected": "(= a (+ (* (cos b) (cos c)) (* (sin b) (sin c))))"
        },
        ('hin', '3'): {
            "input": "(= a (+ (* (cos b) (cos c)) (* (sin b) (sin c))))",
            "expected": "(= a (cos (- b c)))"
        }
    },
    'todifferentialoperator': {
        ('vor', '0'): {
            "input": "(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))",
            "expected": "(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))"
        },
        ('hin', '0'): {
            "input": "(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))",
            "expected": "(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))"
        },

        ('vor', '1'): {
            "input": "(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))",
            "expected": "(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))"
        },
        ('hin', '1'): {
            "input": "(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))",
            "expected": "(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))"
        },
        ('vor', '2'): {
            "input": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))",
            "expected": "(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))"
        },
        ('hin', '2'): {
            "input": "(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))",
            "expected": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))"
        },

        ('vor', '3'): {
            "input": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))",
            "expected": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))"
        },
        ('hin', '3'): {
            "input": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))",
            "expected": "(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))"
        },


    }
}
;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
        (if (f (car s))
            (cons-stream (car s) (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s)))))



(define (slice s start end)
  (define (slice-up s i)
    (cond
      ((null? s) nil)
      ((>= i start) (if (= i end) nil (cons (car s) (slice-up (cdr-stream s) (+ i 1)))))
      (else (slice-up (cdr-stream s) (+ i 1)))
    )
  )
  (slice-up s 0)
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (cons-stream 1 (combine-with * factorials (naturals 1)))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs))))
)


(define (exp x)
  (define xsequence (cons-stream x xsequence))
  (define xpow (combine-with expt xsequence (naturals 0)))
  (define single (combine-with / xpow factorials))
  (cons-stream (car single) (combine-with + (cdr-stream single) (exp x)))
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (if (null? s)
    nil
    (begin 
      (define (split s)
        (if (null? (cdr-stream s))
          nil
          (if (> (car s) (car (cdr-stream s)))
            (cdr-stream s)
            (split (cdr-stream s))
          )
        )
      )
      (define s1 (split s))
      (define (lookuplst s)
        (if (null? (cdr-stream s))
          (cons (car s) nil)
          (if (> (car s) (car (cdr-stream s)))
            (cons (car s) nil)
            (cons (car s) (lookuplst (cdr-stream s)))
          )
        )
      )
      (cons-stream (lookuplst s) (nondecrease s1))
    )
  )
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))

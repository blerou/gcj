
(def x (iterate inc 1))

(def in (atom []))

(defn foo 
  [xs] 
  (swap! in conj [(first xs) (take 2 (rest xs))])
  (drop 3 xs))

(take 10 (iterate foo (take 30 x)))

@in

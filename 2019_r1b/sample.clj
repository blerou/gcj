(defn solve-loop [line]
  (loop [line line
         a ""
         b ""]
    (if (empty? line)
        (str a " " b)
        (let [c (first line)]
            (recur
                (rest line)
                (if (= c \4) 
                    (str a "3")
                    (str a c))
                (if (= c \4)
                    (str b "1")
                    (str b "0")))))))

(defn solve-reduce [line]
  (str
   (reduce #(str %1 (if (= %2 \4) \3 %2)) "" line)
   " "
   (reduce #(str %1 (if (= %2 \4) \1 \0)) "" line)))

(def solve solve-loop)

(let [s (java.util.Scanner. *in*)
      t (Integer/parseInt (.nextLine s))]
  (doseq [i (range 1 (inc t))]
    (let [l (.nextLine s)]
      (println (format "Case #%d: %s" i (solve l))))))

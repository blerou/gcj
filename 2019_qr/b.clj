
(let [s (java.util.Scanner. *in*)
      t (Integer/parseInt (.nextLine s))]
  (doseq [i (range 1 (inc t))]
    (.nextLine s)
    (let [result (->> (.nextLine s)
                      (map #(if (= \E %) \S \E))
                      (apply str))]
      (println (format "Case #%d: %s" i result)))))

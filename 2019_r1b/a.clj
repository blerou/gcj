
(defn solve [q ps]
  )

(let [s (java.util.Scanner. *in*)
      t (Integer/parseInt (.nextLine s))]
  (doseq [i (range 1 (inc t))]
    (let [p (.nextInt s)
          q (.nextInt s)
          ps (map #() (range p))]
      (println (format "Case #%d: %s" i (solve q ps))))))

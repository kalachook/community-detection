start=`date +%s`
python remove.py
python readdd.py
python read1.py > input3.txt
python read2.py > sample_input.txt
javac FindDominantLabel.java
javac Lpni_1.java
java Lpni_1
python reverse.py
dur=$(echo "$(date +%s.%N) - $start" | bc)
printf "Execution time: %.6f seconds\n" $dur
python graph1.py
python individual_cluster.py
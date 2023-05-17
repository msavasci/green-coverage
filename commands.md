# To run Randoop

java -cp "/workspace1/compsci621/tools/randoop/randoop-all-4.3.2.jar:/workspace1/compsci621/tests/target/classes/" randoop.main.Main gentests --testclass=com.thealgorithms.testset.MazeRecursion --time-limit=60 --junit-output-dir=/workspace1/tmp/

# To run Evosuite

java -jar /workspace1/compsci621/tools/evosuite/evosuite-1.0.6.jar -class com.thealgorithms.testset.MazeRecursion -projectCP /workspace1/compsci621/tests/target/classes

# To run TackleTest

tkltest-unit --config-file /workspace1/compsci621/tkltest_config.toml --verbose generate ctd-amplified

# Run wall power measurement
python3 power-client-updated.py -m 192.168.245.53 -t 10 -s 2 -f /workspace1/compsci621/wall-power-measurements/randoop-maze-recursion.csv

# Run RAPL power measurement
sudo python3 test_rapl_controlled.py --duration 10 --sampling 2 --file /workspace1/compsci621/rapl-power-measurements/randoop-maze-recursion.csv


# day from argument
set DAY $argv[1]

curl --cookie "session=$AOC_SESSION" https://adventofcode.com/2022/day/$DAY/input -o tests/inputs/day$DAY.txt
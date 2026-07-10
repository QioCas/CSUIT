#!/bin/bash
set -e

base_seed=${1:-1000}
echo "[Info] Base seed = ${base_seed}"
echo "[Compile] Building generators and solution..."
g++ validator.cpp -o validator
g++ solution.cpp  -o solution
g++ generate.cpp  -o generate
echo "[Compile] Done."

rm -rf tests
mkdir -p tests

total_tests=40
pad_width=${#total_tests}
last=0

run() {
    local type=$1   # 1-normal, 2-special, 3-edge, 4-stress
    local cas=$2
    local maxN=$3
    local minA=$4
    local maxA=$5
    local subtask=$6

    last=$((last + 1))
    local seed=$((base_seed + last))
    local test_name
    test_name=$(printf "test%0${pad_width}d" "${last}")
    mkdir -p "tests/${test_name}"

    echo "[Run] ${test_name}: type=${type}, cas=${cas}, maxN=${maxN}, subtask=${subtask}"

    ./generate --type=${type} --seed=${seed} --cas=${cas} --maxN=${maxN} --minA=${minA} --maxA=${maxA} \
        > "tests/${test_name}/input.in"
    ./validator < "tests/${test_name}/input.in"
    ./solution < "tests/${test_name}/input.in" > "tests/${test_name}/output.out"
}

minA=-100000
maxA=100000

# ================================
# TEST CONFIGURATIONS
# ================================

# n = 1
run 1 1 1 $minA $maxA 1    # normal
run 3 1 1 $minA $maxA 1    # edge
run 3 2 1 $minA $maxA 1
run 3 3 1 $minA $maxA 1


for((x=1;x<=3;x++)); do 
    # n = 100
    run 1 1 100 $minA $maxA 1  # normal
    # n = 1000
    run 1 1 1000 $minA $maxA 1 # normal
    run 4 1 1000 $minA $maxA 1 # stress
    run 4 2 1000 $minA $maxA 1
    run 4 3 1000 $minA $maxA 1
    run 3 1 1000 $minA $maxA 1 # edge
    run 3 2 1000 $minA $maxA 1
    run 3 3 1000 $minA $maxA 1
    run 3 4 1000 $minA $maxA 1
    run 2 1 1000 $minA $maxA 1 # special
    run 2 2 1000 $minA $maxA 1
    run 2 3 1000 $minA $maxA 1
    run 2 4 1000 $minA $maxA 1
done

for((x=1;x<=3;x++)); do
    # n = 100000
    run 1 1 100000 $minA $maxA 2  # normal
    run 4 1 100000 $minA $maxA 2  # stress
    run 4 2 100000 $minA $maxA 2
    run 4 3 100000 $minA $maxA 2
    run 3 1 100000 $minA $maxA 2  # edge
    run 3 2 100000 $minA $maxA 2
    run 3 3 100000 $minA $maxA 2
    run 3 4 100000 $minA $maxA 2
    run 2 1 100000 $minA $maxA 2  # special
    run 2 2 100000 $minA $maxA 2
    run 2 3 100000 $minA $maxA 2
    run 2 4 100000 $minA $maxA 2
done

echo "✅ All test data generated successfully!"

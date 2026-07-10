#!/bin/bash
set -euo pipefail

# =======================================================
# gen.sh - Generate testcases for Hamilton Path problem
# =======================================================
# Usage: ./gen.sh [base_seed]
# Default base_seed = 1000
# Produces tests under ./tests/testXXX/{input.in,output.out}
# =======================================================

base_seed=${1:-1000}
echo "[Info] Base seed = ${base_seed}"

# Compile
echo "[Compile] Building generators, validator, and solution..."
g++ -std=c++17 -O2 -pipe -static -s validator.cpp  -o validator
g++ -std=c++17 -O2 -pipe -static -s solution.cpp   -o solution

# Compile all generator programs (assumes .cpp in current dir)
g++ gen/edgeCase.cpp   -o genEdgeCase
g++ gen/normalCase.cpp -o genNormalCase
g++ gen/specialCase.cpp -o genSpecialCase
g++ gen/stressCase.cpp  -o genStressCase
g++ gen/genGPT.cpp        -o genGPT

echo "[Compile] Done."

# Prepare tests dir
rm -rf tests
mkdir -p tests

# Expected maximum tests to determine pad width (tweak if you add more)
expected_max=999
pad_width=${#expected_max}

total_tests=0

# Helper: run a generator binary N times with given type and category
gen_and_run() {
    local gen_bin=$1    # executable name (e.g. genEdgeCase)
    local type=$2       # generator type param
    local count=$3      # how many tests to generate
    local category=$4   # short category name for filenames

    echo "[RunGen] ${gen_bin} type=${type} count=${count} (${category})"

    for ((i=0; i<count; i++)); do
        total_tests=$((total_tests + 1))
        local test_name
        test_name=$(printf "tests/test%0${pad_width}d" "${total_tests}")
        mkdir -p "${test_name}"

        local seed=$((base_seed + total_tests))
        local input="${test_name}/input.in"
        local output="${test_name}/output.out"

        # run generator
        ./${gen_bin} ${type} ${seed} > "${input}"

        # run validator (if validator exists) - allow validator to warn but don't fail generation
        if [[ -x ./validator ]]; then
            if ! ./validator < "${input}" > /dev/null 2>&1; then
                echo "[Warning] Validator reported an issue for ${input}"
            fi
        fi

        # run solution to produce expected output
        if [[ -x ./solution ]]; then
            ./solution < "${input}" > "${output}"
        else
            echo "[Error] solution binary not found or not executable"
            exit 1
        fi

        # quick sanity check on solution output format
        if ! grep -Eq '^(-1|([0-9]+[[:space:]]+){0,11}[0-9]+)$' "${output}"; then
            echo "[Warning] Output format suspicious for ${input}; see ${output}"
            echo "----- OUTPUT START -----"
            sed -n '1,20p' "${output}"
            echo "----- OUTPUT END -----"
        fi

        echo "[Gen] ${gen_bin} type=${type} seed=${seed} -> ${test_name}"
    done
}

# -------------------------
# Generate test groups
# -------------------------

# Edge cases: explicitly call each type present in genEdgeCase
# (adjust counts per type as you like)
gen_and_run genEdgeCase 1 1 "edge"
gen_and_run genEdgeCase 2 1 "edge"
gen_and_run genEdgeCase 3 1 "edge"
gen_and_run genEdgeCase 4 1 "edge"
gen_and_run genEdgeCase 5 1 "edge"
gen_and_run genEdgeCase 6 1 "edge"
gen_and_run genEdgeCase 7 1 "edge"
gen_and_run genEdgeCase 8 1 "edge"

# Normal random cases
# genNormalCase ignores type param in current code; still pass 1..3 for reproducibility
gen_and_run genNormalCase 1 5 "normal"
gen_and_run genNormalCase 2 5 "normal"
gen_and_run genNormalCase 3 5 "normal"

# Special structured cases
gen_and_run genSpecialCase 1 2 "special"  # line graph
gen_and_run genSpecialCase 2 2 "special"  # cycle graph
gen_and_run genSpecialCase 3 2 "special"  # almost complete
gen_and_run genSpecialCase 4 2 "special"  # disconnected
gen_and_run genSpecialCase 5 2 "special"  # star center high index
gen_and_run genSpecialCase 6 2 "special"  # two components unequal

# Stress cases
gen_and_run genStressCase 1 4 "stress"   # random dense
gen_and_run genStressCase 2 2 "stress"   # worst-case for brute force

# GPT miscellaneous cases (covers many scenarios, including optional oversized)
for t in {1..10}; do
    gen_and_run genGPT ${t} 1 "gpt"
done

echo "✅ Generated total ${total_tests} tests successfully."
echo "[Info] Tests are in ./tests/ (each test in its own folder testNNN with input.in and output.out)"

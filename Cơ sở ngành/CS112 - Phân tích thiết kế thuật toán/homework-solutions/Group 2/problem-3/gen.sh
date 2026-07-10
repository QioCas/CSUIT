#!/bin/bash
set -e

# =======================================================
#  GEN.SH - Hamilton Path test generator script
# =======================================================
#  Mục tiêu:
#  - Tự động build toàn bộ generator, validator, solution.
#  - Sinh bộ test gồm nhiều nhóm (edge, special, stress,...)
#  - Đảm bảo test bao phủ tất cả lỗi tiềm ẩn và subtask.
# =======================================================

# ====== Base seed và compile ======
BASE_SEED=${1:-1000}
echo "[Info] Base seed = ${BASE_SEED}"

echo "[Compile] Building generators, validator, and solution..."
g++ -std=c++17 -O2 -pipe -static -s validator.cpp -o validator
g++ -std=c++17 -O2 -pipe -static -s solution.cpp  -o solution

g++ gen/genEdgeCase.cpp -o genEdgeCase
g++ gen/genNormalCase.cpp -o genNormalCase
g++ gen/genSpecialCase.cpp -o genSpecialCase
g++ gen/genStressCase.cpp -o genStressCase
g++ gen/genGPT.cpp -o genGPT

echo "[Compile] Done."

# ====== Chuẩn bị thư mục test ======
rm -rf tests
mkdir -p tests
TOTAL_TESTS=0

# ====== Hàm sinh test ======
gen_and_run() {
    local GEN=$1
    local TYPE=$2
    local COUNT=$3
    local CATEGORY=$4

    echo "[RunGen] ${GEN} type=${TYPE} count=${COUNT} (${CATEGORY})"

    for ((i=1; i<=COUNT; i++)); do
        TOTAL_TESTS=$((TOTAL_TESTS + 1))

        TEST_NAME=$(printf "tests/test%02d" $TOTAL_TESTS)
        SEED=$((BASE_SEED + TOTAL_TESTS))
        mkdir -p "${TEST_NAME}"
        local input="${TEST_NAME}/input.in"
        local output="${TEST_NAME}/output.out"


        ./${GEN} ${TYPE} ${SEED} > "${input}"

        # validator check
        ./validator < "${input}" || echo "[Warning] Validator failed for ${TEST_NAME}"

        # solution output
        ./solution < "${input}" > "${output}"

        # sanity check
        if ! grep -Eq '^(-1|([0-9]+[[:space:]]+){0,11}[0-9]+)$' "${output}"; then
            echo "[Warning] Output format suspicious for ${TEST_NAME}"
        fi

        echo "[OK] ${GEN} -> ${TEST_NAME}"
    done
}

# =====================================================
#  Nhóm 1: Edge cases
# =====================================================
gen_and_run genEdgeCase 1 1 "edge"
gen_and_run genEdgeCase 2 1 "edge"
gen_and_run genEdgeCase 3 1 "edge"
gen_and_run genEdgeCase 4 1 "edge"
gen_and_run genEdgeCase 5 1 "edge"
gen_and_run genEdgeCase 6 1 "edge"
gen_and_run genEdgeCase 7 1 "edge"
gen_and_run genEdgeCase 8 1 "edge"

# =====================================================
#  Nhóm 2: Normal cases
# =====================================================
for t in {1..5}; do
    gen_and_run genNormalCase ${t} 3 "normal"
done

# =====================================================
#  Nhóm 3: Special structures
# =====================================================
for t in {1..6}; do
    gen_and_run genSpecialCase ${t} 2 "special"
done

# =====================================================
#  Nhóm 4: Stress and worst-case
# =====================================================
gen_and_run genStressCase 1 3 "stress"
gen_and_run genStressCase 2 2 "stress"

# =====================================================
#  Nhóm 5: GPT miscellaneous and overflow/int test
# =====================================================
for t in {1..10}; do
    gen_and_run genGPT ${t} 1 "gpt"
done

# =====================================================
echo "✅ Generated total ${TOTAL_TESTS} tests successfully."
echo "[Info] All test files in ./tests/"
echo "[Done]"

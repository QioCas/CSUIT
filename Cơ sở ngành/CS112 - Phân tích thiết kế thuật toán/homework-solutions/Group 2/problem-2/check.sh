#!/bin/bash
set -uo pipefail  # bỏ -e để không dừng khi lỗi

TIME_LIMIT=1      # seconds
MEM_LIMIT_MB=256
MEM_LIMIT_KB=$((MEM_LIMIT_MB*1024))

if [ $# -lt 1 ]; then
  echo "Usage: $0 <solution.cpp or executable>"
  exit 1
fi

SRC="$1"
# --- compile solution ---
if [[ "$SRC" == *.cpp ]]; then
  EXEC="${SRC%.cpp}"
  echo "[Compile] Compiling $SRC -> $EXEC"
  if ! g++ -std=c++17 -O2 -pipe -static -s "$SRC" -o "$EXEC"; then
    echo "❌ Compile failed"
    exit 1
  fi
else
  EXEC="$SRC"
  if [ ! -x "$EXEC" ]; then
    echo "Error: $EXEC not found or not executable"
    exit 1
  fi
fi

# --- compile validator/checker nếu có ---
[ -f validator.cpp ] && g++ -std=c++17 -O2 -pipe -static -s validator.cpp -o validator 2>/dev/null || true
[ -f checker.cpp ]   && g++ -std=c++17 -O2 -pipe -static -s checker.cpp   -o checker   2>/dev/null || true

# --- lấy danh sách test ---
shopt -s nullglob
tests=(tests/test*/)
shopt -u nullglob

if [ ${#tests[@]} -eq 0 ]; then
  echo "No tests found in tests/. Run gen.sh first."
  exit 1
fi

# --- tạo thư mục outputs/ ---
mkdir -p outputs

pass=0; fail=0; total=0

for d in "${tests[@]}"; do
  d=${d%/}
  base=$(basename "$d")
  input="$d/input.in"
  expected="$d/output.out"
  userout="outputs/${base}_user.out"
  timefile=$(mktemp)
  stderrfile=$(mktemp)

  total=$((total+1))
  printf "\n--- %s ---\n" "$base"

  # --- check input/output tồn tại ---
  if [ ! -f "$input" ]; then
    echo "❌ Missing input: $input"
    fail=$((fail+1))
    continue
  fi
  if [ ! -f "$expected" ]; then
    echo "❌ Missing expected: $expected"
    fail=$((fail+1))
    continue
  fi

  # --- validator ---
  if [ -x ./validator ]; then
    if ! ./validator < "$input" > /dev/null 2>&1; then
      echo "❌ Validator failed for $base"
      fail=$((fail+1))
      continue
    fi
  fi

  # --- chạy solution ---
  timeout "${TIME_LIMIT}s" /usr/bin/time -f "%e %M" -o "$timefile" ./"$EXEC" < "$input" > "$userout" 2> "$stderrfile"
  exit_code=$?

  runtime="0.00"; memkb=0
  if [ -s "$timefile" ]; then
    read runtime memkb < "$timefile"
  fi
  memmb=$(awk "BEGIN{printf \"%.2f\", ${memkb}/1024}")

  status="OK"
  if [ $exit_code -eq 124 ]; then
    status="TLE"
  elif [ $exit_code -ne 0 ]; then
    status="RTE"
  fi
  if (( memkb > MEM_LIMIT_KB )); then
    status="MLE"
  fi

  # --- checker hoặc diff ---
  if [ "$status" = "OK" ]; then
    if [ -x ./checker ]; then
      ./checker "$input" "$userout" "$expected" > /dev/null 2> checker_err.txt
      chk_rc=$?
      if [ $chk_rc -ne 0 ]; then
        status="WA"
      fi
    else
      if ! diff -q <(tr -s ' \t\r\n' '\n' < "$userout") <(tr -s ' \t\r\n' '\n' < "$expected") >/dev/null; then
        status="WA"
      fi
    fi
  fi

  printf "%-4s | time=%ss | mem=%sMB\n" "$status" "$runtime" "$memmb"

  if [ "$status" = "OK" ]; then pass=$((pass+1)); else fail=$((fail+1)); fi

  rm -f "$timefile" "$stderrfile" checker_err.txt
done

echo
echo "Summary: passed=$pass failed=$fail total=$total"
echo "Outputs saved to ./outputs/"

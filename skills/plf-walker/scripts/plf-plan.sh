#!/usr/bin/env bash
set -euo pipefail

# PLF launch timeline generator
# Usage: ./plf-plan.sh <YYYY-MM-DD-cart-open> [--type internal|seed|jv] [--cart-days 7]

CART_OPEN="${1:?Usage: plf-plan.sh <YYYY-MM-DD-cart-open> [--type internal|seed|jv] [--cart-days N]}"
LAUNCH_TYPE="internal"
CART_DAYS=7

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --type) LAUNCH_TYPE="$2"; shift 2 ;;
    --cart-days) CART_DAYS="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

# Validate date
if ! date -j -f "%Y-%m-%d" "$CART_OPEN" "+%Y-%m-%d" >/dev/null 2>&1; then
  echo "Invalid date format. Expected YYYY-MM-DD, got: $CART_OPEN"
  exit 2
fi

# Helper: shift date by N days (works on macOS BSD date and GNU date)
shift_date() {
  local base="$1"
  local offset="$2"
  local sign="+"
  if [[ "$offset" == -* ]]; then
    sign=""
  fi
  if [[ "$offset" == "0" ]]; then
    date -j -f "%Y-%m-%d" "$base" "+%Y-%m-%d (%a)" 2>/dev/null \
      || date -d "$base" "+%Y-%m-%d (%a)"
  else
    date -j -v"${sign}${offset}d" -f "%Y-%m-%d" "$base" "+%Y-%m-%d (%a)" 2>/dev/null \
      || date -d "$base ${offset} days" "+%Y-%m-%d (%a)"
  fi
}

# Set offsets based on launch type
case "$LAUNCH_TYPE" in
  seed)
    PRE_PRE_OFFSET=-21
    PLC1_OFFSET=-3
    PLC2_OFFSET=-2
    PLC3_OFFSET=-1
    ;;
  internal)
    PRE_PRE_OFFSET=-42
    PLC1_OFFSET=-7
    PLC2_OFFSET=-4
    PLC3_OFFSET=-1
    ;;
  jv)
    PRE_PRE_OFFSET=-60
    PLC1_OFFSET=-10
    PLC2_OFFSET=-6
    PLC3_OFFSET=-2
    ;;
  *)
    echo "Unknown launch type: $LAUNCH_TYPE (expected: internal | seed | jv)"
    exit 3
    ;;
esac

CART_CLOSE_OFFSET=$((CART_DAYS - 1))
POST_LAUNCH_OFFSET=$CART_DAYS

echo ""
echo "================================================="
echo "  PLF Launch Timeline – $LAUNCH_TYPE"
echo "  Cart Open: $CART_OPEN"
echo "  Cart length: $CART_DAYS days"
echo "================================================="
echo ""
echo "PHASE 1: Pre-Pre-Launch"
echo "  Start audience building:    $(shift_date "$CART_OPEN" $PRE_PRE_OFFSET)"
echo "  Goal: collect waitlist, surveys, content warming"
echo ""
echo "PHASE 2: Pre-Launch (PLC sequence)"
echo "  PLC1 Opportunity:           $(shift_date "$CART_OPEN" $PLC1_OFFSET)"
echo "  PLC2 Transformation:        $(shift_date "$CART_OPEN" $PLC2_OFFSET)"
echo "  PLC3 Ownership / tease:     $(shift_date "$CART_OPEN" $PLC3_OFFSET)"
echo ""
echo "PHASE 3: Open Cart"
echo "  Cart Open (Day 0):          $(shift_date "$CART_OPEN" 0)"

# Print intermediate cart days
for ((d=1; d<CART_DAYS-1; d++)); do
  printf "  Cart Day %-2d (objection / case / FAQ): %s\n" "$((d+1))" "$(shift_date "$CART_OPEN" $d)"
done

echo "  Cart Close (final crescendo):  $(shift_date "$CART_OPEN" $CART_CLOSE_OFFSET)"
echo ""
echo "PHASE 4: Post-Launch"
echo "  Welcome + Day 1:            $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET)))"
echo "  Quick win check:            $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET + 2)))"
echo "  First group meeting:        $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET + 6)))"
echo "  Testimonial request:        $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET + 13)))"
echo "  Upsell / next step:         $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET + 29)))"
echo ""
echo "================================================="
echo "Total cycle: from $(shift_date "$CART_OPEN" $PRE_PRE_OFFSET) to $(shift_date "$CART_OPEN" $((POST_LAUNCH_OFFSET + 29)))"
echo "================================================="

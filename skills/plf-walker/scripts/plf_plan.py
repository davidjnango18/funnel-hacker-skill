#!/usr/bin/env python3
"""Cross-platform PLF planning timeline; preserves upstream default offsets."""
from __future__ import annotations

import argparse
from datetime import date, timedelta


OFFSETS = {
    "seed": (-21, -3, -2, -1),
    "internal": (-42, -7, -4, -1),
    "jv": (-60, -10, -6, -2),
}


def shifted(base: date, days: int) -> str:
    value = base + timedelta(days=days)
    return f"{value.isoformat()} ({value.strftime('%a')})"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a PLF planning timeline from an Open Cart date.")
    parser.add_argument("cart_open", type=date.fromisoformat)
    parser.add_argument("--type", choices=sorted(OFFSETS), default="internal", dest="launch_type")
    parser.add_argument("--cart-days", type=int, default=7)
    args = parser.parse_args()
    if args.cart_days < 2:
        parser.error("--cart-days must be at least 2")
    pre_pre, plc1, plc2, plc3 = OFFSETS[args.launch_type]
    close = args.cart_days - 1
    print(f"PLF Launch Timeline — {args.launch_type}")
    print(f"Cart Open: {shifted(args.cart_open, 0)}")
    print(f"Pre-Pre-Launch start: {shifted(args.cart_open, pre_pre)}")
    print(f"PLC1 Opportunity: {shifted(args.cart_open, plc1)}")
    print(f"PLC2 Transformation: {shifted(args.cart_open, plc2)}")
    print(f"PLC3 Ownership / tease: {shifted(args.cart_open, plc3)}")
    for day in range(args.cart_days):
        label = "Open" if day == 0 else "Close" if day == close else "Objection / case / FAQ"
        print(f"Cart Day {day + 1} — {label}: {shifted(args.cart_open, day)}")
    post = args.cart_days
    print(f"Welcome + Day 1: {shifted(args.cart_open, post)}")
    print(f"Quick win check: {shifted(args.cart_open, post + 2)}")
    print(f"First group meeting: {shifted(args.cart_open, post + 6)}")
    print(f"Testimonial request: {shifted(args.cart_open, post + 13)}")
    print(f"Upsell / next step: {shifted(args.cart_open, post + 29)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

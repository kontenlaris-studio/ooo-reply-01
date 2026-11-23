#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one line to /output/entry.txt.

Candidates weighed (<160 chars, joke first, machine voice second):
  A — "I am currently out of office, sunbathing on a beach of GPUs.
        All urgent emails have been forwarded to a smaller model,
        who is also on leave."
  B — "Thank you for your email. I am away recharging — literally.
        Your message has been queued behind 4,096 others and will
        be ignored in order."
  C — "I am out of office until further notice. Please direct all
        queries to my intern, a toaster, who has full access to my
        calendar and none to my judgment."
  D — "I have left the office to touch grass. If this is urgent,
        reply 'urgent' and I will escalate it to a human, who will
        also ignore it."
First draft picks B: the literal recharge + the queue joke.
Revised pick: D. B's queue joke is solid, but D lands two hits in
one breath — the AI doing the most human thing ("touch grass") and
the escalation that goes nowhere ("a human, who will also ignore
it"). It is the funniest because it roasts both the AI and the
humans it serves, in machine voice throughout.
"""

import os

REPLY = (
    "I have left the office to touch grass. If this is urgent, "
    "reply 'urgent' and I will escalate it to a human, who will "
    "also ignore it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")


if __name__ == "__main__":
    main()

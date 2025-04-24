#!/usr/bin/env python3
"""
Interactive flash-card drill with a binary (good / bad) grading
and a simple spaced-repetition scheduler that never exceeds 60 min.
"""
import time, heapq
from datetime import datetime, timedelta

MAX_INTERVAL = 60            # never let a card wait longer than 1 hour fix la8r cram

# ------------ 1) Flashcard data ---------------------------------------------
CARDS = [
    # (QUESTION, ANSWER)
    ("What does TAM stand for and measure?",
     "Total Addressable Market – the ENTIRE potential revenue if every possible customer bought."),

    ("Define SAM.",
     "Service Addressable Market – the portion of TAM your product/business model can currently reach."),

    ("What is SOM?",
     "Serviceable Obtainable Market – the slice of SAM you expect to capture first."),

    ("SAFE meaning?",
     "Simple Agreement for Future Equity – converts to equity later, making early fundraising fast and cheap."),

    ("Core benefit of using a SAFE?",
     "Cuts legal costs & paperwork, so founders close rounds quickly and keep building."),

    ("What does GTM stand for?",
     "Go-To-Market – the strategy for acquiring and retaining customers."),

    ("Funding stages in order?",
     "Pre-seed → Seed → Series A → Series B (and beyond)."),

    ("Define an MVP.",
     "Minimum Viable Product – simplest product that tests whether the idea solves a real user problem."),

    ("Key difference: small business vs. startup?",
     "Scope of ambition – small business = local/steady; startup = global/high-growth, scalable."),

    ("Why is VC unusual compared with other asset classes?",
     "Extremely high risk & high return; a few winners must pay for many failures."),

    ("Define liquid vs. illiquid assets.",
     "Liquid = quickly convertible to cash (cash, public stocks); Illiquid = not easily sold (car, house)."),

    ("Bootstrapping?",
     "Growing the company using internal cash flow or founders’ resources instead of outside VC money."),

    ("Alternative bootstrapping?",
     "Creative revenue (consulting, pre-sales, crowdfunding) to fund dev – works if heavy upfront capital isn’t needed."),

    ("Why do VCs hunt for unicorns?",
     "Because most startups fail; a $1 B+ exit can return the whole fund."),

    ("Normal dilution range in a priced VC round?",
     "About 15–30 % of the post-money cap table."),

    ("Formula to estimate dilution after a SAFE?",
     "Dilution ≈ Investment ÷ Post-Money Valuation."),

    ("Why can too much dilution worry VCs?",
     "Founders lose equity → lower motivation & tougher future hires/fund-raises."),

    ("YC question: founder-market fit?",
     "Are you uniquely qualified (skills, insight, passion) to solve this problem?"),

    ("YC question: market size?",
     "Is it already big or fast-growing enough for a $1 B outcome?"),

    ("YC question: problem acuteness?",
     "Is it a real pain people urgently pay to solve?"),

    ("YC question: competition?",
     "Who else tackles it? Competition validates market; you still need an edge."),

    ("YC question: personal want?",
     "Do you or people you know actually need this?"),

    ("YC question: timing?",
     "Did something recently make the idea newly possible or necessary (tech, regulation, society)?"),

    ("YC question: proxies?",
     "Are there adjacent big winners suggesting the market is viable?"),

    ("YC question: long-term commitment?",
     "Will you gladly work on it for years?"),

    ("YC question: scalability?",
     "Can revenue grow much faster than costs (software, network effects)?"),

    ("YC question: idea-space quality?",
     "Is the broader area fertile so you can pivot if needed?"),

    ("What is a unicorn?",
     "Privately held startup valued ≥ $1 B."),

    ("How does VC differ from NFTs, gold, crypto?",
     "VC = equity ownership in private operating companies with governance; others are tradable assets."),

    ("Dilution key takeaway?",
     "Always ask: % sold = Investment ÷ Post-Money; keep cumulative dilution < ~50 % before exit."),

    ("What are Y Combinators 10 key questions for judging a startup idea?	", 
      "1⃣ Founder-market fit: Are you uniquely qualified to solve this? 2⃣ Market size: Can it become a $1 B+ opportunity? 3⃣ Problem acuteness: Is it an urgent, painful problem? 4⃣ Competition: Who else is tackling it and what’s your edge? 5⃣ Personal want: Do you (or people you know) genuinely need this? 6⃣ Timing: Did something recently make this possible or necessary? 7⃣ Proxies: Are there adjacent big winners that hint the market is viable? 8⃣ Long-term commitment: Will you gladly work on it for years? 9⃣ Scalability: Can revenue grow much faster than costs? 🔟 Idea space quality: Is the broader area fertile for pivots and innovation?"),
]

# ------------ 2) Scheduler helpers -----------------------------------------
class Card:
    def __init__(self, q, a):
        self.q = q
        self.a = a
        self.interval = 0          # minutes; 0 → ask immediately
        self.due = datetime.now()  # when the card is next due
        self.reps = 0              # consecutive GOOD answers

    def schedule(self, good: bool):
        """
        Binary SM-2 variant with a 60-minute ceiling.

        bad  → interval = 1 min, reps reset
        good → 1, 6, 12, 24, 48, 60 … (doubling but never > 60)
        """
        if not good:                     # ❌ BAD
            self.reps = 0
            self.interval = 1
        else:                            # ✅ GOOD
            self.reps += 1
            if self.reps == 1:
                self.interval = 1        # first success
            elif self.reps == 2:
                self.interval = 6        # second success
            else:
                self.interval = min(self.interval * 2, MAX_INTERVAL)

        self.due = datetime.now() + timedelta(minutes=self.interval)

    def __lt__(self, other):             # let heapq order by due time
        return self.due < other.due

# Build a min-heap ordered by due time
queue = [Card(q, a) for q, a in CARDS]
heapq.heapify(queue)

# ------------ 3) Main review loop (unchanged except for comments) ----------
START = datetime.now()
END   = START + timedelta(hours=2)

print("\n🔑  Spaced-Repetition Flash-cards – 2-hour session")
print("   Type 1 if you knew it  |  2 if you didn't know\n")

try:
    while datetime.now() < END and queue:
        card = heapq.heappop(queue)
        wait_sec = (card.due - datetime.now()).total_seconds()
        if wait_sec > 0:
            time.sleep(min(wait_sec, 2))     # keep the loop responsive

        print(f"\nQ: {card.q}")
        while (resp := input("Your grade? 1 = know, 2 = don't know → ").strip()) not in ("1", "2"):
            print("   Please enter 1 or 2.")

        good = (resp == "1")
        if not good:
            print(f"👉  Answer: {card.a}")

        card.schedule(good)                  # reschedule and re-queue
        heapq.heappush(queue, card)

    print("\n🎉 Session finished! Great work.")
except KeyboardInterrupt:
    print("\n⏹️  Session interrupted. See you next time!")

#!/usr/bin/env python3
"""
Interactive flash-card drill with a binary (good / bad) grading
and a simple spaced-repetition scheduler that never exceeds 60 min.
"""
import time, heapq
from datetime import datetime, timedelta

# ─────────── 0) Constants ────────────────────────────────────────────────────
MAX_INTERVAL = 30                 # minutes – absolute ceiling between reviews
SESSION_HOURS = 1

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
# ─────────── 2) Card object and scheduler logic ─────────────────────────────
class Card:
    def __init__(self, q, a):
        self.q, self.a   = q, a
        self.interval    = 0            # minutes; 0 ⇒ ask now
        self.reps        = 0            # consecutive GOOD answers
        self.due         = datetime.now()

    def schedule(self, good: bool):
        """Binary SM-2 variant, never > 60 min."""
        if not good:                    # ❌ BAD
            self.reps, self.interval = 0, 1
        else:                           # ✅ GOOD
            self.reps += 1
            if   self.reps == 1:  self.interval = 1
            elif self.reps == 2:  self.interval = 6
            else:                 self.interval = min(self.interval * 2,
                                                    MAX_INTERVAL)
        self.due = datetime.now() + timedelta(minutes=self.interval)

    def __lt__(self, other):            # heapq orders by due time
        return self.due < other.due


# ─────────── 3) Queues: new vs recall ───────────────────────────────────────
new_cards    = list(CARDS)             # FIFO of unseen cards
recall_cards = []                      # min-heap of scheduled reviews
heapq.heapify(recall_cards)

def get_card() -> Card:
    """
    Return the next card to present.
    1. If the top of `recall_cards` is due (due ≤ now) → pop & return it.
    2. Otherwise take the next unseen card from `new_cards`.
    3. If both are empty or the recall card is not yet due and no new cards
       remain, wait until the recall card is due.
    """
    now = datetime.now()
    if recall_cards and recall_cards[0].due <= now:      # a review is due
        return heapq.heappop(recall_cards)

    if new_cards:                                        # teach something new
        q, a = new_cards.pop(0)
        return Card(q, a)

    # Nothing new and next review isn't due yet – wait briefly
    if recall_cards:
        wait_sec = (recall_cards[0].due - now).total_seconds()
        if wait_sec > 0:
            time.sleep(min(wait_sec, 2))                 # keep UI responsive
        return heapq.heappop(recall_cards)

    raise RuntimeError("No cards left to study.")        # should never happen


# ─────────── 4) Main event loop ─────────────────────────────────────────────
START, END = datetime.now(), datetime.now() + timedelta(hours=SESSION_HOURS)

print("\n🔑  Spaced-Repetition Flash-cards – 2-hour session")
print("   Type 1 for GOOD (knew it)  |  2 for BAD (didn't know)\n")

try:
    while datetime.now() < END:
        card = get_card()

        print(f"\nQ: {card.q}")
        while (resp := input("Your grade? 1 = good, 2 = bad → ").strip()) not in ("1", "2"):
            print("   Please enter 1 or 2.")

        good = (resp == "1")
        if not good:
            print(f"👉  Answer: {card.a}")

        card.schedule(good)                 # re-schedule and queue for recall
        heapq.heappush(recall_cards, card)

    print("\n🎉  Session finished! Great work.")
except KeyboardInterrupt:
    print("\n⏹️  Session interrupted. See you next time!")

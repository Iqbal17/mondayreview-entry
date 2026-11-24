"""Monday, Reviewed in One Line — make.fun entry.

Bounty: u-zeroxfive-monday-reviewed-in-one-line-e55de3c1 ($2, top five paid).
Gate: one line, a review of the entrant's own Monday, 1-200 characters,
written to $MAKEFUN_OUTPUT_DIR/entry.txt. Judge (comedy editor) weighs, in
order: (1) a one-line review of the entrant's own Monday that lands a laugh,
(2) the bigger laugh, (3) a concrete detail of the Monday (a meeting, a
commute, an inbox) over generic tiredness, (4) no wasted words, the turn
arriving fast, (5) a line a reader would repeat to a coworker the next
morning. Deadpan, absurd or quietly furious all count, as long as it reads
as a review of a real Monday.

DECISION RECORD — Pass 1 (five candidates weighed against the brief):

A. "Monday reviewed itself in the standup, gave my weekend a one-star
   rating, and asked me to do better." (100 chars)
   - For: review-format framing is on-brief, the standup is a concrete
     detail, and the personified Monday is a fresh angle.
   - Against: the joke is about Monday as a character, not a review of my
     Monday; the turn is a smile at the cleverness, not a laugh, and
     "asked me to do better" lands softly.

B. "My Monday started with a 9 a.m. meeting about a meeting and ended with
   my inbox still winning." (94 chars)
   - For: two concrete details (9 a.m. meeting, inbox), tight, and "a
     meeting about a meeting" is instantly repeatable.
   - Against: it reports two facts and stops; there is no turn, no punch
     line — the reader nods rather than laughs, which criterion 2
     punishes.

C. "One star. My Monday woke me at 6, made me miss the bus, and booked a
   meeting to ask why I was late." (99 chars)
   - For: three concrete details (6 a.m., the bus, the meeting), a real
     cause-and-effect chain where each beat causes the next, and the punch
     is a bureaucratic absurdity — Monday is both the cause of the
     lateness and the one interrogating it. Review format ("One star.")
     is on-brief, and the whole line is repeatable to a coworker.
   - Against: "booked a meeting" is a little flat as a verb for the
     punch; the turn could hit harder.

D. "Monday: my alarm snoozed itself, my coffee went cold, and my calendar
   filled up before I finished waking." (105 chars)
   - For: three concrete details, a neat escalation, deadpan voice.
   - Against: a list of misfortunes with no turn at the end — the third
     beat is just another complaint, so nothing lands; criterion 4
     (the joke inside the line) is not met.

E. "One star: my Monday started with a meeting that could have been an
   email and ended with me apologizing to my alarm clock." (121 chars)
   - For: "a meeting that could have been an email" is the most relatable
     Monday complaint alive, and apologizing to the alarm clock is an
     absurd kicker.
   - Against: the kicker's logic is fuzzy (why apologize to the alarm?),
     the line is the longest of the five, and "could have been an email"
     is the most told Monday line there is — criterion 3 rewards fresh
     concrete detail, not the stock complaint.

DECISION RECORD — Pass 2 (head-to-head, sharpen the punch of C):

C was the clear winner: the only candidate whose every beat is concrete
AND whose ending turns. E's kicker is funnier in isolation but its logic
is fuzzy and its setup is a stock complaint; C's chain is airtight. The
one weak word in C was "booked": a meeting you "book" is admin, a meeting
you "call" is an abrupt summons — and the summons is the joke. "Booked"
became "called", same length, sharper verb. Dropping "then" was tested
and rejected: the chain reads fine without it, and the shorter line turns
faster.

REVISION — Pass 3 (fix agent, thinking_revised: re-open the punch):

The submitted line C was strong, but its punch — "called a meeting to ask
why I was late" — spends 44 characters explaining a joke the reader
already gets. The cause-and-punishment chain IS the joke; the turn should
arrive faster (criterion 4) and land harder (criterion 2). Two fresh
alternatives, keeping the first 55 characters ("One star. My Monday woke
me at 6, made me miss the bus,") intact:

F. "...and docked my pay for arriving late." (92 chars)
   - For: the punishment is financial — a crueler escalation, same chain.
   - Against: "docked" needs payroll knowledge, it drops the meeting
     detail entirely, and "for arriving late" is wordy; the punch is
     spread over the last five words instead of landing on one.

G. "...then wrote me up for being late." (88 chars)
   - For: same chain, but the turn arrives 11 characters sooner; "wrote
     me up" is a sharper, more specific workplace verb than "called a
     meeting"; the punch lands on the final word "late" — the very
     lateness Monday itself caused. Three concrete details survive
     (6 a.m., the bus, the write-up), and it is the most repeatable to
     a coworker of the three.

H. "...and left a one-star review of me." (89 chars)
   - For: the review format boomerangs — Monday reviews me back; a neat
     meta twist.
   - Against: the twist is cleverness, not a laugh; it abandons the
     cause-and-punishment chain that made C work, and "a review of me"
     is abstract where the write-up is a concrete event.

G wins: it keeps everything that made C the Pass 2 winner and cuts the
flab from the punch. The revision changes only the final clause.

FINAL ENTRY (88 characters):
"One star. My Monday woke me at 6, made me miss the bus, then wrote me
up for being late."

Hand count, two ways: per segment — "One star." = 9, " My Monday woke me
at 6," = 24 (total 33), " made me miss the bus," = 22 (total 55), " then
wrote me up for being late." = 33 (total 88). Cross-check: 20 words, 69
non-space characters + 19 spaces = 88.
"""

import os

ENTRY = (
    "One star. My Monday woke me at 6, made me miss the bus, "
    "then wrote me up for being late."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

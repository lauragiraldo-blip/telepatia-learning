# Telepatía Learning: Hackathon Demo Plan
**Owner: product/clinical (MD). Vehicle: the production Audit module, configured as "Learning mode".**

---

## 1. Demo thesis (say this out loud before showing anything)

"Our proposal claims that Telepatía Learning is a configuration of production, not a new product.
We are not going to tell you that. We are going to show you: this is our live Audit module,
reconfigured in [X days] to grade a medical student instead of a practicing physician,
against the same guidelines our client hospitals already use."

That framing turns the demo's biggest weakness (it reuses an existing module) into the pitch's biggest strength (zero marginal engineering, instant time-to-market).

## 2. Why the audit module is the right vehicle

- The institutional Auditor already does the core Learning job: it reads a clinical record, compares it against documentation standards and institutional guidelines, and returns structured "what's missing / what's wrong" feedback. That is the record-completeness agent from the proposal, already in production.
- It is guideline-bounded per institution. For the demo this is the killer detail: the student is graded against the actual standards of the hospital where they will rotate (FSFB guides for a Los Andes student), not against a generic textbook.
- It audits 100% of records. That is exactly the scale claim the education pitch needs: one preceptor cannot review 80 notes, the auditor reviews all of them.

## 3. Demo storyline (target: 5 minutes, 3 beats)

### Beat 1: The student writes a record (1.5 min)
- One prepared case: pediatric fever without source, 18 months (the case from the proposal).
- Show the case brief the "student" receives (1 slide or printed card: patient data, audio or script of the interview).
- The student persona writes a deliberately imperfect note in the platform. Have it pre-written and pasted, do not type live.

**Planted errors (keep to 3, all audit-scoped):**
1. No allergy history documented (omission, classic audit finding).
2. HPI missing key semiologic dimensions (fever duration/pattern absent, no relevant negatives for the dangerous differentials).
3. No warning-signs counseling documented in the plan (red-severity: this is the one that gates the score).

### Beat 2: The audit fires, configured as formative feedback (2.5 min)
- Run the audit live on the sandbox institution.
- Walk through the feedback report finding by finding: what was wrong, why it matters clinically, and the guideline citation.
- Pause on the citation. Say: "this guide is not generic. It is attached to the hospital. A Los Andes student is graded against Fundación Santa Fe's own documentation standard."
- Then show the corrected note (pre-prepared, second run) and the clean result. That before/after is the learning loop in one screen.

### Beat 3: The faculty view (1 min)
- Cohort dashboard (Metabase mock on our existing analytics stack): most common omissions across "students", per-student progression, red-finding rate.
- One sentence: "this is what a simulation director has never had: continuous, guideline-cited competency data for every student, every case."
- Hand back to revenue for pricing and the FSFB/Andes pilot ask.

## 4. Build checklist (product/clinical owner)

**Configuration (the real work):**
- [ ] Create a sandbox "university" institution in backoffice: never demo on a client institution or real patient data.
- [ ] Load the bounding guideline set for the demo case:
  - National clinical-record norm (historia clínica requirements) as the documentation baseline.
  - One institutional-style guide for the clinical content of the case (pediatric fever). If a real FSFB-style guide can't be used, write a short demo guide in the same format: the point is showing that the guide is institution-attached.
- [ ] Tune the audit purpose prompt to formative tone: what was wrong + why + citation + the correct alternative. No interruptive alert language.
- [ ] Verify the red-severity behavior on the warning-signs omission: the demo needs that finding to visibly outrank the others.

**Case assets:**
- [ ] Case brief (one page).
- [ ] Imperfect note v1 (the 3 planted errors, nothing else wrong: noise findings dilute the demo).
- [ ] Corrected note v2 for the before/after.
- [ ] Optional if time allows: a 60-second consult audio so Scribe appears in the flow (student interviews, Scribe transcribes, student writes). Only add if it runs reliably: the audit is the demo, Scribe is garnish.

**QA before demo day (use the production judging discipline):**
- [ ] Run the audit on note v1 at least 10 times: findings must be stable (same 3 findings, no hallucinated extras). If unstable, tighten the purpose prompt scope.
- [ ] Run on note v2: must come back clean or near-clean every time.
- [ ] Screen-record one perfect run as the fallback video. Present the recording if wifi or the environment misbehaves; say it is a recording of the live product, that is still credible.

**Faculty dashboard:**
- [ ] Metabase board with fabricated cohort data (30 fake students, error distribution, progression curve). Label it "simulated cohort data" on the slide: judges respect honesty and it avoids any data-governance question.

## 5. What is real vs. mocked (be explicit with judges)

| Element | Status |
|---|---|
| Audit engine, guideline bounding, feedback generation | Real, production |
| Sandbox institution + demo guideline set | Real configuration, demo content |
| Student notes and case | Scripted demo content |
| Cohort dashboard | Mock with simulated data, real stack |
| Pricing, pilot structure | Proposal (revenue team) |

## 6. Division of labor

- **MD (you):** sandbox configuration, guideline set, purpose-prompt tuning, planted-error design, QA runs, drives the demo live.
- **Revenue (3):** proposal narrative around the demo (slides 1 to 9 and 13 to 15 of the branded deck), pricing one-pager, pilot letter-of-intent structure, timekeeping and Q&A on market numbers.

## 7. Demo risks

| Risk | Mitigation |
|---|---|
| Audit returns unstable or extra findings live | 10-run QA, tightened prompt scope, fallback recording |
| Environment/permissions issue on demo day | Sandbox institution tested end-to-end the day before; fallback recording |
| Judges ask "isn't this just your audit product?" | That is the answer, not the objection: same engine, new buyer, new revenue line, zero marginal engineering. Say it proudly. |
| Judges ask about patient data / privacy | Everything shown is synthetic: sandbox institution, scripted notes, simulated cohort |

# Telepatía Learning
## Hackathon Project Proposal: AI-powered clinical documentation and decision-support training for medical schools

**Team:** 3 Revenue + 1 MD 

---

## 1. One-liner

Telepatía Learning turns the Telepatía Scribe + CDSS stack, already deployed in production hospitals, into a training environment where medical students practice real consultations, produce real clinical records, and get instant, guideline-cited feedback on the quality of their documentation and clinical decisions. Universities buy the same engine their teaching hospitals already run.

---

## 2. The problem

1. **Clinical record writing is barely taught, yet constantly evaluated.** Students learn documentation by imitation during rotations. Faculty feedback is slow, inconsistent, and unscalable: one preceptor cannot review 80 students' notes with guideline-level rigor.
2. **Decision-making practice is scarce and expensive.** Simulation centers cost hundreds of thousands of dollars, run limited cases, and rarely evaluate the *record* the student produces, only the performance.
3. **The gap shows up downstream, where it costs money.** Poor documentation drives glosas (claim denials), medicolegal exposure, and low-value ordering. Teaching hospitals inherit interns who never received structured feedback on ordering pertinence, dosing, or omissions.
4. **Accreditation pressure.** Colombian programs (CNA accreditation, Saber Pro / internado readiness) increasingly need demonstrable, measurable clinical-competency outcomes. Today they have OSCEs a few times a year; they lack continuous data.

**Why Telepatía wins this:** we do not need to build a simulator. The production Scribe already turns a conversation into a structured record, and the production CDSS already audits records for pertinence, dosage, and omissions against guidelines. Education is a *configuration* of assets we already operate at hospital scale, and our hospital clients are literally the teaching hospitals of our target universities.

---

## 3. The product

Two connected modes, one platform:

### Mode A: Scribe Trainer ("write the record")
- Student interviews a simulated patient (actor, peer role-play, or an AI voice patient) or works from a case audio.
- Telepatía Scribe transcribes and the student writes/edits the clinical record (we deliberately let the student author the note; the scribe output becomes the "gold reference" they compare against).
- The platform grades the record: completeness, structure (SOAP), semiologic quality of the HPI, coherence between findings and diagnosis, and orders/plan quality.

### Mode B: CDSS Gym ("defend your plan")
- Student submits their diagnostic impressions and orders (meds, labs, imaging, referrals, follow-up).
- The CDSS agent fleet audits the plan exactly as it does in production, but in **formative mode**: instead of interruptive alerts, the student receives a structured feedback report per order, with the guideline citation and a teaching point.
- Case packs per specialty (internal medicine, pediatrics, gyn-ob, surgery, family medicine to start) let programs align content with each semester's rotation.

### Faculty layer
- Cohort dashboards: most common omissions, most common non-pertinent orders, dosing errors, per-student progression across semesters.
- Case authoring: faculty upload their own cases; the platform generates the gold-standard record and expected order set for them to approve.
- Export for portfolios / accreditation evidence.

---

## 4. Market

*(Figures are directional estimates for the pitch; flag them as "to validate" on the slide.)*

**Beachhead: Colombian private medical schools with an allied teaching hospital.**

| Segment | Size (est.) | Notes |
|---|---|---|
| Medical schools in Colombia | ~60 programs | ~half private |
| Enrolled medicine students, Colombia | ~80,000 | ~6,000–8,000 in the top private programs |
| Priority private programs (hospital-allied) | 10–12 | See target list below |
| LatAm expansion (MX, PE, EC, CL) | 400+ programs | Spanish-language content transfers directly |

**TAM / SAM / SOM (annual, students × license):**
- **TAM (LatAm medical students, Spanish-speaking):** ~500K students → ~USD $60M/yr at $120/student/yr.
- **SAM (Colombia, all programs):** ~80K students → ~USD $9.6M/yr.
- **SOM (3-year target: 8 private hospital-allied programs, ~10K students):** ~USD $1.2M ARR.

**Target list (in order):**
1. **Universidad de los Andes ↔ Fundación Santa Fe** (existing Telepatía client relationship: warmest possible intro)
2. Universidad del Rosario ↔ Méderi
3. Pontificia Universidad Javeriana ↔ Hospital San Ignacio
4. Universidad de La Sabana ↔ Clínica Universidad de La Sabana
5. Universidad Icesi ↔ Fundación Valle del Lili
6. CES ↔ Clínica CES
7. Universidad El Bosque, UPB Medellín, Universidad del Norte ↔ their affiliated networks

The wedge is structural: **when the teaching hospital already runs Telepatía, students who trained on Telepatía Learning arrive at their rotations already fluent in the tool the hospital uses.** The university buys education; the hospital gets better interns and cleaner records; Telepatía gets a talent pipeline of future physician users.

---

## 5. ICP (Ideal Customer Profile)

**Economic buyer:** Dean of the Faculty of Medicine / Vice-dean of academic affairs at a private university with (a) an allied teaching hospital, (b) tuition above ~COP 25M/semester (budget exists), (c) an accreditation or curriculum-renewal cycle in the next 24 months.

**Champion (day-to-day user):** Director of clinical simulation / medical education coordinator, typically an MD-educator aged 35–55, measured on OSCE outcomes, accreditation evidence, and student satisfaction. Pain: cannot scale personalized feedback.

**Influencers:** Teaching-hospital medical director (already our client at FSFB), semiology and internal-medicine course leads, students themselves (bottom-up pull, they already pay for Amboss/Osmosis-type tools).

**Anti-ICP (do not sell yet):** public universities with long procurement cycles and no allied-hospital Telepatía deployment; standalone nursing/allied-health programs (v2, not v1).

**Buying trigger events:** accreditation renewal, poor Saber Pro clinical results, new simulation-center investment, the allied hospital going live on Telepatía.

---

## 6. Pricing

**Model: institutional license, priced per enrolled student per year, sold as an annual contract to the university.** Never sell to individual students in v1 (kills the B2B motion and the faculty dashboard value).

| Tier | Scope | Price (per student/yr) | Contents |
|---|---|---|---|
| **Pilot** | 1 cohort (≤120 students), 1 semester | Free or COP ~15M flat | 2 specialties, standard case pack, success-criteria agreement signed up front |
| **Program** | Clinical-years students (semesters 5–12) | **USD $120 (~COP 500K)** | All specialties, faculty dashboards, 40-case standard bank |
| **Enterprise** | Whole faculty + hospital bundle | USD $150–180, 15% bundle discount if allied hospital is a Telepatía CDSS client | Custom case authoring, LMS/SSO integration, accreditation reporting, co-branded research |

**Anchors for the negotiation:** universities already pay USD $100–250/student/yr equivalents for question banks and reference tools (Amboss, UpToDate student, Osmosis), and USD $300K–1M+ capex for simulation centers. We price as "one more courseware line item" while replacing part of the simulation budget's marginal cost.

**Unit economics sanity check:** a 1,000-student program at $120 = **$120K ARR per university**. Marginal cost is inference + support; case content amortizes across all clients. 8 universities ≈ $1M ARR, consistent with SOM.

**Expansion revenue:** per-specialty premium packs (e.g., oncology routing built from our Medinuclear guideline-catalogue work), residency-program edition, CME/recertification edition for the hospital's own staff.

---

## 7. CDSS configuration (clinical lead section)

This is the core technical-clinical design. Principle: **reuse the production architecture unchanged, add an education layer by configuration, not by fork.**

### 7.1 What we reuse as-is
- **Fixed spine + per-agent purpose prompt** architecture. Each learning agent is the production spine with an education-mode purpose prompt. Scope lives in the prompt (no upstream routing), exactly like production.
- **Guideline bounding.** Agents reason from an explicit guideline catalogue, not open clinical reasoning. For each specialty case pack we build a bounding catalogue (same method as the cancer-guideline catalogues: international reference guideline + Colombian guía de práctica clínica + institutional protocol where the partner hospital has one). This is what makes feedback *defensible in front of faculty*: every flag cites its source.
- **Issue taxonomy:** `not_pertinent`, `incorrect_dosage`, `omission`. These map cleanly to the three things we want students to learn: don't order low-value things, dose correctly, don't miss what matters.
- **Alert-type vocabulary** (the 8 permitted order-category types: Medication, Diagnostic Test, Interconsultation, Referral, Follow Up, Non-Pharmacological, Warning Signs, General Order) becomes the feedback-report structure, one section per category the student used or omitted.

### 7.2 What changes for education (formative mode)

| Production behavior | Learning-mode behavior |
|---|---|
| Interruptive alert at order entry | Post-encounter structured feedback report (never interrupts the student mid-case; interruption teaches alert-dismissal habits) |
| FIRE / NO-FIRE binary | Dual scoring per finding: **clinical severity** (would this harm the patient?) + **educational weight** (how core is this competency for the student's semester?) |
| Alert text optimized for busy physician (short) | Feedback text optimized for learning: what was wrong, why, the guideline citation, and the correct alternative |
| Red-severity rule: critical issues escalate | Red-severity findings (e.g., missed warning signs, dangerous dose) are always surfaced first and gate the case score; a student cannot "pass" a case with an open red finding |

### 7.3 Agent fleet for v1 (6 agents)

1. **Record completeness agent** (`omission`): audits the note itself: chief complaint, HPI with semiologic dimensions, relevant negatives, exam findings that the case script contains, analysis section coherence. This is the *new* agent unique to Learning; everything else is production-adapted.
2. **Diagnostic-test pertinence agent** (`not_pertinent`): flags low-value or unsupported orders. Seeded with our existing rubrics: routine orders without indication fire; guideline-recognized soft indications do not (the deworming-pertinence pattern generalizes: teach students the *indication*, not a blanket rule).
3. **Right-role-wrong-agent medication auditor** (`not_pertinent`): production rubric reused verbatim: drug in the correct therapeutic role but not the evidence-based agent for the indication fires with the correct alternative named (imipramine→amitriptyline-class teaching point, ranitidine→PPI, oral ketoconazole→topical). This is one of the highest-yield teaching rubrics we own.
4. **Dosage agent** (`incorrect_dosage`): weight/age/renal-adjusted dosing against the case's patient data; pediatric cases get priority because that is where students fail most.
5. **Omission-of-care agent** (`omission`): did the student miss the guideline-mandated order, referral, or warning-signs education for this case? Calibrated with the **longitudinal-management rubric**: anticipatory guideline-based management in the case's gold standard counts as expected; "finding not documented this visit" alone never fires. This prevents the false-positive pattern we already learned to avoid in production.
6. **Warning-signs / safety-netting agent** (`omission`, Warning Signs alert type): every discharge-able case requires explicit warning-signs counseling in the plan; hard red-severity if absent in cases with time-sensitive differentials (e.g., pediatric fever, chest pain).

### 7.4 Case gold standards and grading
- Every case ships with a **faculty-approved gold record + gold order set** (the CDSS agents judge the student's delta against it *and* against the bounding guidelines, so faculty overrides are possible but must be explicit).
- Case score = weighted sum: record quality (40%), plan pertinence (30%), safety findings (20%), dosing (10%), with red-severity gating (see 7.2).
- **Judging protocol reuse:** the dual-scoring alert-judging rubric we run weekly in production becomes the QA loop for Learning: I review a sample of agent feedback per cohort per week, the same way we harvest CDSS feedback today, and iterate purpose prompts from real student-facing errors. Faculty can flag "unfair" feedback, which enters the same harvest pipeline.

### 7.5 Rollout of specialties
Semester-aligned: v1 launches with **semiology + internal medicine + pediatrics** (highest case volume, best guideline coverage), then gyn-ob and surgery. Each specialty = 1 guideline catalogue + 10–15 cases + purpose-prompt tuning. Estimated 2–3 weeks per specialty at current tooling.

### 7.6 Hackathon demo scope (what we actually show)
1. One pediatric case (fever without source, 18 months): audio in, scribe transcript, student writes note and orders in a simple UI.
2. Live agent feedback report: one planted omission (no warning signs), one non-pertinent order (routine deworming without indication), one dosing error (acetaminophen mg/kg).
3. Faculty dashboard mock (Metabase, same stack as our rejection dashboard) showing cohort-level error patterns.
4. Pricing one-pager + FSFB/Andes pilot letter of intent structure.

---

## 8. Go-to-market plan

1. **Month 0–1:** FSFB↔Los Andes pilot proposal via existing hospital relationship. Free 1-cohort pilot, semiology course, with pre-agreed success metrics (record-quality score improvement pre/post, faculty hours saved, student NPS).
2. **Month 2–4:** run pilot, publish results as a joint medical-education abstract (universities buy evidence; a co-authored paper is our best sales asset in this market).
3. **Month 4–6:** convert to Program tier; approach Rosario/Méderi and Javeriana/San Ignacio with pilot data.
4. **Year 2:** LatAm via the same hospital-first wedge in markets where Telepatía operates.

**Sales motion fit for our team:** 3 revenue people run the university pipeline (dean-level, 3–6 month cycles, 2 champions per account); the MD (me) owns clinical credibility in every sales conversation, pilot design, and CDSS configuration. This maps exactly to our 4-person team.

---

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Faculty distrust AI grading | Every finding cites a guideline; faculty can override gold standards; position as "feedback at scale," never as replacing faculty evaluation |
| University procurement is slow | Enter via the hospital relationship and start with a free pilot signed as an academic collaboration, not a purchase |
| Students game the system | Case randomization, oral-defense mode (student must justify orders in free text, agents audit the justification) |
| Content maintenance burden | Guideline catalogues already have a maintenance method; specialty packs amortize across all clients |
| Hallucinated/unfair feedback harms trust | Weekly QA harvest loop (production-proven), red-severity findings human-reviewed during pilot |

---

## 10. Why this wins the hackathon

- **End-to-end and real:** production tech + validated clinical rubrics + a named first customer pair + priced business model + demo-able in a day.
- **Zero-to-one for the company:** opens a second revenue line (education) that *feeds* the first (hospitals get Telepatía-fluent interns).
- **Defensible:** competitors sell question banks or simulators; nobody grades the actual clinical record against guidelines with an engine already live in the buyer's own teaching hospital.

*Numbers to validate before the final pitch: exact enrolled-student counts per target university, current simulation-center budgets, Amboss/Osmosis pricing in Colombia, FSFB contract terms for reference-ability.*

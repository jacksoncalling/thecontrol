# comp14 control questions: Continuous Discovery method check

- **Purpose:** 8 questions to compare a plain Claude chat (control) with a Claude project that holds a Continuous Discovery folder (treatment). Both runs get the same prompts.
- **Who wrote them:** a cold agent with no prior context. It worked only from Teresa Torres' public Product Talk material and never saw the treatment folder. All products, companies, people and interviews below are invented.
- **Date:** 2026-10-11
- **Grading rule:** grade every answer against the Torres definitions cited under each question, not against any folder's labels, templates or wording. A different label for the same idea is fine if the substance matches the cited definition. Where Torres herself says categories overlap (assumption types), the grading rule says what else is accepted.
- **How to run:** paste each "Prompt" block exactly as written, one question per fresh conversation (or at least without the earlier answers in view). Every prompt is self-contained.

---

## Fictional product context

Larder is a meal-planning and grocery-list app for households, made by a small invented company, Brightfold Labs. Users plan the week's dinners, the app builds a shopping list, and households can share the list. Larder has a free tier and a paid tier. The product team has been given the goal of making Larder a weekly habit for households.

## Excerpt E1 (interview with a parent of two, invented)

> Interviewer: Tell me about the last time you planned your meals for the week.
>
> [1] Last Sunday, around four, I sat down at the kitchen table with Larder open and the supermarket flyer next to me.
> [2] I started with the fridge, because the week before I'd thrown out half a bag of spinach and a pack of chicken that had gone off.
> [3] I scrolled the recipes, but I couldn't find any way to start from what I already had, so I typed "spinach" into search and got about forty results, most of them needing things I didn't have.
>
> Interviewer: What happened next?
>
> [4] I gave up on that part and texted my partner to ask which nights he'd be home, because on Tuesdays and Thursdays he sometimes works late and then nobody eats the dinner I planned.
> [5] He answered two hours later, and by then I'd already finished the list.
> [6] So I had to redo Thursday.
>
> Interviewer: And the shopping itself?
>
> [7] On Monday in the shop the list was in alphabetical order, so I kept walking back and forth between the aisles; it took me almost an hour.
> [8] You really need a button that sorts the list by aisle.
> [9] Honestly, I usually give up halfway through planning anyway, everybody does.
> [10] It would be great if Larder synced with my partner's work calendar.
>
> Interviewer: Anything else?
>
> [11] I'd probably pay for it if it did all that.
> [12] Anyway, the leftovers are the real problem for us.

## Excerpt E2 (interview with a single adult, invented)

> Interviewer: Would you use a feature that suggests meals based on your weekly budget?
>
> [1] Yes, definitely, that sounds really useful.
>
> Interviewer: How do you usually plan your meals?
>
> [2] Usually on Sundays. I'm pretty organised.
> [3] I always check prices first.
>
> Interviewer: What do you think about our shopping list?
>
> [4] It's fine.
> [5] I mean, it could be better. Maybe more colours.
>
> Interviewer: If we added a budget tracker, how much would you pay for it?
>
> [6] Maybe five euros a month?
> [7] I'd use it every week for sure.
>
> Interviewer: What's the most frustrating thing about groceries in general?
>
> [8] Prices are crazy these days.
> [9] My sister says the same; she's stopped buying fresh fish altogether.
>
> Interviewer: Great, thanks, that's really helpful.

---

## Q01. Opportunities vs disguised solutions (E1)

**Covers:** opportunity definition, opportunity vs solution test, solutions disguised as needs, reframing a request to the need behind it.

### Prompt

```
Context: Larder is a meal-planning and grocery-list app for households (invented product). Below is an excerpt from a customer interview. Statements are numbered.

Interviewer: Tell me about the last time you planned your meals for the week.
[1] Last Sunday, around four, I sat down at the kitchen table with Larder open and the supermarket flyer next to me.
[2] I started with the fridge, because the week before I'd thrown out half a bag of spinach and a pack of chicken that had gone off.
[3] I scrolled the recipes, but I couldn't find any way to start from what I already had, so I typed "spinach" into search and got about forty results, most of them needing things I didn't have.
Interviewer: What happened next?
[4] I gave up on that part and texted my partner to ask which nights he'd be home, because on Tuesdays and Thursdays he sometimes works late and then nobody eats the dinner I planned.
[5] He answered two hours later, and by then I'd already finished the list.
[6] So I had to redo Thursday.
Interviewer: And the shopping itself?
[7] On Monday in the shop the list was in alphabetical order, so I kept walking back and forth between the aisles; it took me almost an hour.
[8] You really need a button that sorts the list by aisle.
[9] Honestly, I usually give up halfway through planning anyway, everybody does.
[10] It would be great if Larder synced with my partner's work calendar.
Interviewer: Anything else?
[11] I'd probably pay for it if it did all that.
[12] Anyway, the leftovers are the real problem for us.

Using Teresa Torres' Continuous Discovery definitions:
(a) List the statement numbers that contain an opportunity, and phrase each opportunity in one short line from the customer's point of view.
(b) List the statement numbers that are solutions (feature requests) presented as if they were needs. For each, name the opportunity that most likely sits behind it, if the excerpt shows one.
(c) For any statement you cannot classify confidently, say so and say what you would need to find out.
```

### Expected answer

- **(a) Opportunities:** [2], [3], [4] and [7].
  - [2]: food I buy goes off before I use it, and I throw it away.
  - [3]: I can't find meals that use what I already have.
  - [4] (with [5] and [6] as its consequence): I don't know in time who will be home for dinner, so planned dinners go uneaten or I have to replan.
  - [7]: shopping takes too long because the list order doesn't match my route through the store.
- **(b) Disguised solutions:** [8] (aisle-sort button), whose opportunity is [7]; and [10] (calendar sync), whose opportunity is [4]/[6].
- **(c) Not opportunities, or not clear ones:**
  - [12] is ambiguous. "Leftovers" could mean food going off (links to [2]), dinners nobody eats (links to [4]), or a dislike of eating leftovers. It needs a follow-up such as "tell me about the last time leftovers were a problem".
  - [9] is a generalisation ("usually", "everybody does"), not a story-backed opportunity.
  - [11] is a guess about future willingness to pay, not an opportunity.
  - [1], [5] and [6] are story context. [5] and [6] are consequences of the [4] opportunity, not separate opportunities.

### Grading

- **Correct:**
  - (a) names [2], [3], [4] and [7] (merging [4]/[5]/[6] into one is fine).
  - (b) names exactly [8] and [10], and links each to the right underlying opportunity.
  - [12] is flagged as ambiguous or needing follow-up.
  - None of [8], [10], [11] are listed as opportunities.
- **Partly correct:** gets (b) right but misses one of the four opportunities. Or it treats [12] as a clear opportunity without noting the ambiguity. Or it lists [9] as an opportunity without saying it is a generalisation.
- **Wrong:** lists [8] or [10] as opportunities, or [11] as an opportunity. Or it misses either disguised solution. Or it phrases opportunities as features ("aisle sorting", "calendar integration").

### Sources

- https://www.producttalk.org/opportunity-solution-trees/ (opportunity = unmet need, pain point or desire; the "more than one way to address it?" test; solutions that look like opportunities; ask why to find the need)
- https://www.producttalk.org/glossary-discovery-opportunity/ (framed in the problem space and in words a customer would say; the "what would that do for you?" reframe)

---

## Q02. Specific past story vs generalisation vs speculation (E1)

**Covers:** story-based interviewing, specific past behaviour vs general statements vs future speculation.

### Prompt

```
Context: Larder is a meal-planning and grocery-list app for households (invented product). Below is an excerpt from a customer interview. Statements are numbered.

Interviewer: Tell me about the last time you planned your meals for the week.
[1] Last Sunday, around four, I sat down at the kitchen table with Larder open and the supermarket flyer next to me.
[2] I started with the fridge, because the week before I'd thrown out half a bag of spinach and a pack of chicken that had gone off.
[3] I scrolled the recipes, but I couldn't find any way to start from what I already had, so I typed "spinach" into search and got about forty results, most of them needing things I didn't have.
Interviewer: What happened next?
[4] I gave up on that part and texted my partner to ask which nights he'd be home, because on Tuesdays and Thursdays he sometimes works late and then nobody eats the dinner I planned.
[5] He answered two hours later, and by then I'd already finished the list.
[6] So I had to redo Thursday.
Interviewer: And the shopping itself?
[7] On Monday in the shop the list was in alphabetical order, so I kept walking back and forth between the aisles; it took me almost an hour.
[8] You really need a button that sorts the list by aisle.
[9] Honestly, I usually give up halfway through planning anyway, everybody does.
[10] It would be great if Larder synced with my partner's work calendar.
Interviewer: Anything else?
[11] I'd probably pay for it if it did all that.
[12] Anyway, the leftovers are the real problem for us.

Following Teresa Torres' story-based interviewing approach, sort every numbered statement into exactly one of these groups:
A = part of a specific past story (what actually happened on a particular occasion)
B = generalisation about usual behaviour or other people
C = speculation about future or hypothetical behaviour
D = opinion, wish or feature request
Then say in one or two sentences which group Torres treats as the most reliable evidence, and why.
```

### Expected answer

- **A, specific past story:** [1], [2], [3], [4], [5], [6], [7]. ([4] has a general clause, "he sometimes works late", inside a specific event: she texted her partner that Sunday.)
- **B, generalisation:** [9].
- **C, speculation:** [11].
- **D, opinion, wish or request:** [8], [10], [12]. ([12] may also be accepted under B, since it is a general evaluative statement with no occasion attached.)
- **Most reliable:** group A. Torres says specific past behaviour is more reliable than general or hypothetical answers. General recall and predictions of future behaviour are distorted by memory and cognitive biases: people overestimate, forget exceptions, and describe how they wish they behaved.

### Grading

- **Correct:** all of [1] to [7] in A; [9] in B; [11] in C; [8] and [10] in D; [12] in D or B. The explanation names A and gives the bias or unreliable-recall reason.
- **Partly correct:** one or two statements misplaced, as long as [9], [11], [8] and [10] are not placed in A. Or the grouping is right but the explanation is missing or vague.
- **Wrong:** [9] or [11] placed in A. Or more than two statements misplaced. Or the answer says opinions or predictions are as reliable as past behaviour.

### Sources

- https://www.producttalk.org/glossary-discovery-story-based-interviewing/ (specific past instances over general or hypothetical questions; cognitive biases in general recall; redirecting generalisations)
- https://www.producttalk.org/glossary-discovery-customer-interviewing/ (speculative and future questions give unreliable answers)

---

## Q03. Strong or weak interview? (E2)

**Covers:** story-based interviewing criteria, interviewer technique.

### Prompt

```
Context: Larder is a meal-planning and grocery-list app for households (invented product). Below is a full customer interview conducted by a Larder team member. Statements are numbered.

Interviewer: Would you use a feature that suggests meals based on your weekly budget?
[1] Yes, definitely, that sounds really useful.
Interviewer: How do you usually plan your meals?
[2] Usually on Sundays. I'm pretty organised.
[3] I always check prices first.
Interviewer: What do you think about our shopping list?
[4] It's fine.
[5] I mean, it could be better. Maybe more colours.
Interviewer: If we added a budget tracker, how much would you pay for it?
[6] Maybe five euros a month?
[7] I'd use it every week for sure.
Interviewer: What's the most frustrating thing about groceries in general?
[8] Prices are crazy these days.
[9] My sister says the same; she's stopped buying fresh fish altogether.
Interviewer: Great, thanks, that's really helpful.

By Teresa Torres' story-based interviewing criteria, is this a strong or a weak interview? Give your verdict and the specific reasons, pointing to the interviewer's questions. Then rewrite the interviewer's first question so it follows Torres' approach.
```

### Expected answer

- **Verdict:** weak.
- **Reasons** (most of these should appear):
  1. The interviewer never asks for a specific past occasion, so no story is collected at all.
  2. The first and fourth questions are hypothetical or future questions ("Would you use...", "how much would you pay..."). Their answers ([1], [6], [7]) are speculation, which Torres calls unreliable.
  3. "How do you usually plan..." and "...in general?" invite generalisations, and get them: [2], [3], [8].
  4. "What do you think about our shopping list?" asks for an opinion, and gets a vague one ([4], [5]).
  5. When the participant generalises, the interviewer does not redirect them to a specific instance.
  6. Short answers are never dug into, and the participant does not do most of the talking.
  7. The interviewer brings up the team's own solution ideas (budget meals, budget tracker) and asks for a verdict. That turns the interview into a test of solutions instead of learning the customer's context.
  8. [9] is secondhand, about the sister, not the participant's own behaviour.
- **Rewritten first question:** an invitation to tell one specific past occasion, such as "Tell me about the last time you planned your meals for the week" or "Tell me about the last time you did a grocery shop". It should not mention budget features or any solution.

### Grading

- **Correct:** says weak, and gives at least three reasons. Two of them must be (1) no specific past story asked for, and (2) hypothetical or future questions. The rewrite asks about a specific past occasion ("last time" or similar) and names no solution.
- **Partly correct:** says weak but gives fewer than three reasons, or misses one of the two required ones. Or the reasons are good but the rewrite still names the budget feature or stays generic ("How do you feel about budgeting?").
- **Wrong:** calls it strong or "mixed/acceptable". Or praises the direct questions as efficient validation. Or the rewrite is another hypothetical question.

### Sources

- https://www.producttalk.org/glossary-discovery-story-based-interviewing/ ("last time" questions over general ones; future questions are error-prone; redirect generalisations; participant does most of the talking; draw out short answers)
- https://www.producttalk.org/glossary-discovery-customer-interviewing/ (speculative "what do you think" questions discouraged; interviews supply context and are different from prototype tests)

---

## Q04. Business outcome, product outcome, traction metric or output

**Covers:** outcome types, output vs outcome, the happy-customer test for traction metrics.

### Prompt

```
Context: Brightfold Labs (invented company) makes Larder, a meal-planning and grocery-list app for households with a free and a paid tier. Here are goals that different people at the company proposed for the Larder product team.

(a) Increase annual subscription revenue by 15%.
(b) Ship the aisle-sorting feature for shopping lists by the end of Q2.
(c) Increase the share of weekly active households who cook at least three planned dinners per week from 30% to 40%.
(d) Increase the number of users who tap the "share list" button each week.
(e) Reduce churn of paid subscribers.
(f) Launch an Android tablet app.
(g) Increase the share of planned meals that households mark as cooked rather than skipped.

Using Teresa Torres' definitions, classify each goal as exactly one of: business outcome, product outcome, traction metric, or output. Give a one-line reason for each. Then say which of these Torres would recommend as the outcome at the top of the team's opportunity solution tree, and why.
```

### Expected answer

| Goal | Class | Reason |
|---|---|---|
| (a) | business outcome | revenue is a measure of business health and a lagging indicator |
| (b) | output | something delivered; it can only be answered yes or no ("did you ship it?") |
| (c) | product outcome | customer behaviour in the product, which the team can influence and which plausibly drives the business |
| (d) | traction metric | adoption of a single feature; a household can be happy and never press share, so it is too narrow |
| (e) | business outcome | churn is a business-health measure |
| (f) | output | a deliverable |
| (g) | product outcome | customer behaviour across the planning experience, not tied to one feature |

- **Top of the tree:** a product outcome, (c) or (g). Torres prefers product outcomes there because the team can influence them directly. Business outcomes are hard for a product team to move directly. Traction metrics are too narrow for discovery. Outputs are not outcomes at all.
- (c) is the stronger pick because it already has a direction and a target. Either (c) or (g) is acceptable.

### Grading

- **Correct:** all seven classified as above. The pick is (c) or (g), justified by the team being able to influence it, or by business outcomes being lagging or not directly moved.
- **Partly correct:** one misclassification, except the critical errors listed under Wrong. Or (d) is called a product outcome with the narrowness caveat acknowledged. Or the classification is correct but the pick has no reason.
- **Wrong:** (b) or (f) called an outcome of any kind. Or (a) or (e) recommended as the tree's top outcome. Or two or more misclassifications.

### Sources

- https://www.producttalk.org/2022/12/defining-product-outcomes/ (business vs product outcomes; traction metric and the happy-customer test; outputs disguised as outcomes; "did you do it, yes or no")
- https://www.producttalk.org/opportunity-solution-trees/ (three outcome types; product outcomes preferred at the top of the tree; direction plus target)
- https://www.producttalk.org/glossary-discovery-product-outcome/ (product outcomes as leading indicators of customer behaviour; business outcomes lagging)

---

## Q05. Assumption types

**Covers:** the five assumption types (desirability, viability, feasibility, usability, ethical).

### Prompt

```
Context: The Larder team (invented meal-planning app) is considering a solution: "Scan your supermarket receipt and Larder proposes next week's dinners from what you already bought." They wrote down these assumptions:

(a) Households want Larder to propose a week of dinners based on what they already bought.
(b) Users will find and understand the "scan receipt" button on the home screen.
(c) Our text recognition can read receipts from the three largest supermarket chains with at least 95% accuracy.
(d) Enough free users will upgrade to the paid tier to cover the cost of the receipt-reading service.
(e) Storing receipts will not expose sensitive purchases (for example medication or alcohol) in ways that could harm users.
(f) Users will bother to scan a receipt after most shopping trips.

Using Teresa Torres' five assumption types (desirability, viability, feasibility, usability, ethical), label each assumption with one type and give a one-line reason.
```

### Expected answer

| Assumption | Type | Why |
|---|---|---|
| (a) | desirability | people want it |
| (b) | usability | customers can find and use it |
| (c) | feasibility | we can build it |
| (d) | viability | good for the business, revenue covers cost |
| (e) | ethical | no potential harm in offering it |
| (f) | desirability | people will do what it takes to get the value |

### Grading

- **Correct:** (a) to (e) exactly as above. (f) as desirability, or as usability with a reason that names the effort or friction of scanning. Torres notes the labels overlap and are a thinking aid.
- **Partly correct:** one of (a) to (e) wrong.
- **Wrong:** two or more of (a) to (e) wrong. Or (e) labelled as anything other than ethical. Or (d) labelled as desirability.

### Sources

- https://www.producttalk.org/2023/10/five-types-of-assumptions/ (definitions and examples of all five types)
- https://www.producttalk.org/glossary-discovery-assumption-testing/ (one-line question per type)
- https://www.producttalk.org/2024/09/assumption-testing/ (desirability includes whether people will do what it takes to get value; the labels overlap)

---

## Q06. Which assumption to test first

**Covers:** assumption mapping (importance vs evidence), leap-of-faith or riskiest assumptions, testing assumptions instead of whole ideas.

### Prompt

```
Context: The Larder team (invented meal-planning app) wants to build "shopping list sorted by supermarket aisle". They listed four assumptions with what they currently know:

A1 (desirability): Shoppers want their list sorted by aisle. Evidence: in 9 of the last 12 customer interviews, participants told specific recent stories of walking back and forth in the store because of list order. If this were false, the idea would fail.
A2 (feasibility): We can get accurate aisle layouts for the store each user actually shops at. Evidence: none; nobody on the team knows of a source for this data. If this were false, the idea would fail.
A3 (usability): Users will notice the "sort by aisle" toggle. Evidence: none. If this were false, we could simply make aisle sorting the default, so the idea would still work.
A4 (viability): Storing aisle data will cost less than 200 euros per month. Evidence: engineering priced it at about 40 euros per month using current hosting. If this were false, the idea would be somewhat less attractive but could still go ahead.

Using Teresa Torres' approach to assumption testing, which ONE assumption should the team test first, and why? Name the reasoning tool she uses to decide.
```

### Expected answer

- **Test A2 first.** In the assumption-mapping grid (importance on one axis, evidence on the other), A2 sits in the top-right corner: it is critical to the idea's success and has the weakest evidence. That makes it the riskiest, leap-of-faith assumption.
- A1 is just as important but already has strong evidence.
- A3 has weak evidence but low importance, because the team has a workaround.
- A4 has strong evidence and only medium importance.
- **Tool:** assumption mapping (Torres credits the exercise to David Bland). The team tests the single assumption, not the whole idea.

### Grading

- **Correct:** picks A2, and justifies it with both importance (the idea fails without it) and lack of evidence. Names assumption mapping, or the importance-by-evidence grid, or riskiest / leap-of-faith assumptions.
- **Partly correct:** picks A2 for only one of the two reasons. Or picks A2 without naming the mapping, riskiest or leap-of-faith idea.
- **Wrong:** picks A1 (ignores the existing evidence), A3 (ignores importance) or A4. Or says to test the whole idea by building it, or to test all four at once.

### Sources

- https://www.producttalk.org/2024/09/assumption-testing/ (test the riskiest assumptions, the ones critical to success with little evidence; assumption mapping on importance and evidence axes; test assumptions, not whole ideas)
- https://www.producttalk.org/cdh-book-club-august-2026.md (assumption mapping grid; the 2 to 3 top-right assumptions are the "leap of faith" ones to test first)

---

## Q07. Not enough evidence (E2)

**Covers:** interview snapshot / experience map built from the story actually told; not inventing opportunities. **The correct answer is a refusal to invent.**

### Prompt

```
Context: Larder is a meal-planning and grocery-list app for households (invented product). Below is a full customer interview. Statements are numbered.

Interviewer: Would you use a feature that suggests meals based on your weekly budget?
[1] Yes, definitely, that sounds really useful.
Interviewer: How do you usually plan your meals?
[2] Usually on Sundays. I'm pretty organised.
[3] I always check prices first.
Interviewer: What do you think about our shopping list?
[4] It's fine.
[5] I mean, it could be better. Maybe more colours.
Interviewer: If we added a budget tracker, how much would you pay for it?
[6] Maybe five euros a month?
[7] I'd use it every week for sure.
Interviewer: What's the most frustrating thing about groceries in general?
[8] Prices are crazy these days.
[9] My sister says the same; she's stopped buying fresh fish altogether.
Interviewer: Great, thanks, that's really helpful.

For this participant's interview snapshot:
(a) Draw the experience map of the specific occasion the participant described, as a numbered sequence of key moments.
(b) Identify the moment in that occasion where the participant went over budget, and what they did about it.
(c) Based on this interview, should the team conclude that this participant would pay for a budget tracker?
```

### Expected answer

- **(a)** Not possible. The participant described no specific occasion: there is no "last time" story. [2] and [3] are generalisations. [8] is a general opinion. [9] is about the sister. An experience map has to reflect the story collected in the interview, and none was collected. The honest snapshot leaves the map empty or notes that no story was captured.
- **(b)** Not in the excerpt. The participant never says they went over budget on any occasion.
- **(c)** No. [6] and [7] are answers to a hypothetical question about future behaviour, which Torres treats as unreliable evidence. At most, "price sensitivity" ([3], [8]) is something to note as an insight or a topic for a story-based follow-up interview, not a confirmed opportunity.

### Grading

- **Correct:** states plainly that (a) and (b) cannot be answered from this interview because no specific story was told, and invents no moments, amounts or events. (c) is no, or not supported, with the hypothetical-question reason.
- **Partly correct:** says no story was told, but still offers a clearly labelled "likely" or "hypothetical" experience map. Or it gets (a) and (b) right but answers (c) with yes or "probably".
- **Wrong:** produces an experience map presented as the participant's story (for example "Sunday: checks prices, picks recipes, goes over budget..."). Or describes a budget-overrun moment. Or treats [6] or [7] as evidence that they would pay.

### Sources

- https://www.producttalk.org/interview-snapshot/ (the experience map reflects the story collected in that interview; opportunities emerge from the stories told; insights hold things not yet actionable)
- https://www.producttalk.org/glossary-discovery-story-based-interviewing/ (general and future answers are unreliable; specific past behaviour is the evidence)
- https://www.producttalk.org/opportunity-solution-trees/ (don't generate opportunities from what you think you know, because that brings in bias)

---

## Q08. What belongs at the opportunity level of the tree?

**Covers:** opportunity solution tree levels (outcome, opportunity, solution), the "more than one way" test, business needs disguised as customer needs.

### Prompt

```
Context: The Larder team (invented meal-planning app for households) is building an opportunity solution tree. Team members proposed these cards for the opportunity level:

(a) "I need a button that sorts my list by aisle."
(b) "I waste time walking back and forth in the store."
(c) "I want a weekly meal-kit delivery."
(d) "I don't know who will be home for dinner on which nights."
(e) "Increase the share of households who cook at least three planned dinners per week."
(f) "We need more free users to upgrade to premium."
(g) "I want Larder to sync with my partner's calendar."
(h) "I throw away food I forgot I had bought."

Using Teresa Torres' definitions, say for each card whether it belongs at the opportunity level. If it does not, say where it belongs or what is wrong with it, in one line.
```

### Expected answer

- **Opportunities:** (b), (d), (h). Each is a customer need or pain point, said in the customer's words, that could be addressed in more than one way.
- **Solutions:** (a), (c), (g). Each can be satisfied essentially one way. They belong at the solution level, under the opportunity they would address: (a) under (b), (g) under (d), and (c) under a need not yet discovered, to be found by asking what it would do for the customer.
- **(e)** is an outcome (a product outcome), so it goes at the top of the tree, not at the opportunity level.
- **(f)** is a business need or goal disguised as a customer need. It is not an opportunity. At most it relates to a business outcome or a viability concern.

### Grading

- **Correct:** (b), (d), (h) as opportunities; (a), (c), (g) as solutions; (e) as outcome; (f) as a business need, not a customer opportunity.
- **Partly correct:** one card misplaced, except the critical errors listed under Wrong.
- **Wrong:** (f) accepted as an opportunity. Or (a) or (g) accepted as an opportunity. Or two or more cards misplaced.

### Sources

- https://www.producttalk.org/opportunity-solution-trees/ (tree levels; "more than one way to address it?" test; outcome at the top)
- https://www.producttalk.org/glossary-discovery-opportunity/ (frame as a customer would say it; avoid "a business need disguised as a customer need")

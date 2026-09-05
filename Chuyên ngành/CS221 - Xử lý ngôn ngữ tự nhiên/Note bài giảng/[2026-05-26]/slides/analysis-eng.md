# Failure 120 Analysis: MiniRAG on OpenBookQA

## 1. Case Overview

- Failure ID: `120`
- Dataset: `OpenBookQA`
- Question:

```text
Endangered pandas are sometimes
(A) accidentally dropped into volcanoes
(B) confined to enclosures to be viewed by the public
(C) found eating corn in the middle of North America
(D) made into delicious rare steaks
```

- Gold answer label: `B`
- Gold answer text: `confined to enclosures to be viewed by the public`
- Original MiniRAG prediction: `A`
- Fresh rerun prediction: `C`

This is already informative. The model did not just make one stable wrong choice. It produced two different wrong choices across runs, which suggests the answer was not strongly grounded in retrieved evidence.

## 2. General Retrieval Overview

This section describes what MiniRAG actually retrieved and prioritized before discussing why it failed.

### 2.1 Query Decomposition

MiniRAG extracted the following items from the question:

- `answer_type_keywords`: `ACTION`, `B`, `C`, `D`
- `entities_from_query`:
  - `Endangered pandas`
  - `Volcanoes`
  - `Enclosures`
  - `Public Viewing`
  - `Corn`
  - `Middle of North America`
  - `Steaks`

This means the system treated the content of the multiple-choice options as retrieval targets, not just the core subject of the question.

### 2.2 Entity-Name Retrieval

For each extracted query entity, MiniRAG searched the graph for matching entity nodes.

Important top matches were:

- For `Endangered pandas`:
  - `ENDANGERED` (`0.4082`)
  - `MOST PREDATORS` (`0.3491`)
  - `ANIMAL SPECIES` (`0.3296`)
  - `RACCOONS` (`0.3273`)
  - `ARCTIC ANIMALS` (`0.3050`)
- For `Volcanoes`:
  - `VOLCANOES` (`0.7458`)
  - `LAVA` (`0.4591`)
  - `TECTONIC PLATE` (`0.4331`)
  - `TECTONIC PLATES` (`0.4314`)
  - `MAGMA` (`0.4227`)
- For `Enclosures`:
  - `SURFACES` (`0.3546`)
  - `ELECTRICAL INSULATION` (`0.3360`)
  - `PROTECTED AREAS` (`0.3291`)
  - `WOOD` (`0.3268`)
  - `OBJECTS MADE OF GLASS` (`0.3213`)
- For `Public Viewing`:
  - `SEEING` (`0.3716`)
  - `CAMERA` (`0.3411`)
  - `ZOO EXHIBITS` (`0.3314`)
  - `ASTRONOMICAL OBSERVATION` (`0.3306`)
  - `BINOCULARS` (`0.3122`)
- For `Corn`:
  - `CORN` (`0.7502`)
  - `CROPS` (`0.5125`)
  - `PLANTS` (`0.4092`)
  - `FOOD` (`0.4074`)
  - `SUGARS` (`0.4008`)

At this stage, two patterns already stand out:

- distractor concepts such as `corn` and `volcanoes` matched very strongly
- useful concepts such as `enclosures` and `public viewing` matched weakly and ambiguously

### 2.3 Relationship Retrieval

MiniRAG then retrieved graph relationships. The kept relationships were:

- `ANIMAL -> ENVIRONMENT`
- `ANIMAL -> POPULATION`
- `ENVIRONMENT -> FOOD`
- `PREDATORS -> PREY`
- `CHIPMUNK -> EVENT`
- `ORGANIZATION -> PRESERVATION OF FOOD`
- `ANIMAL -> FOOD`
- `ANIMAL SPECIES -> POPULATION DECREASE`

These relations are broad and mostly ecological. None of them directly target the specific concept needed for the correct answer, such as:

- zoo housing
- animal enclosures
- public exhibition

### 2.4 Selected Graph Entities

The highest-priority graph entities for this question were:

1. `CORN`
2. `VOLCANOES`
3. `CROPS`
4. `LAVA`
5. `TECTONIC PLATE`
6. `TECTONIC PLATES`
7. `MAGMA`
8. `PLANTS`
9. `ENDANGERED`
10. `FOOD`

Other notable entities that appeared lower in the ranking included:

- `SEEING`
- `CAMERA`
- `CARNIVORES`
- `HERBIVORES`
- `MOST PREDATORS`
- `ZOO EXHIBITS` at rank `41`

So the graph did contain a partially relevant concept, `ZOO EXHIBITS`, but it was ranked far below distractor-driven concepts.

### 2.5 Final Retrieved Source Chunks

MiniRAG's final source list included 30 chunks. The first part of the list was dominated by generic animal and distractor-related facts.

Top retrieved chunks included:

- `fact_0749.txt`: `if an animal eats another animal then that animal is a carnivore or omnivore or predator`
- `fact_0701.txt`: `herbivores only eat plants`
- `fact_0876.txt`: `most predators live in the same environment as their prey`
- `fact_0861.txt`: `mice live in in holes in the ground in fields`
- `fact_0729.txt`: `if a habitat can no longer support animals then those animals will move to another area`
- `fact_1280.txt`: `when a habitat can support living things , living things can live in that habitat`
- `fact_0787.txt`: `if the amount of available food and water decreases in an environment then animals may leave that environment to find food and water`
- `fact_0898.txt`: `new land can be formed by volcanoes erupting by lava cooling`
- `fact_1257.txt`: `volcanoes are often found under oceans`
- `fact_0880.txt`: `mountains are formed by volcanoes`
- `fact_0642.txt`: `feeders attract animals to a location`

The most relevant chunks for the gold answer were only:

- rank `19`: `fact_1060.txt`: `some animals live in zoo exhibits`
- rank `21`: `fact_0622.txt`: `endangered means low in population`

So the retrieval pipeline did surface some weakly relevant evidence, but only after many unrelated or weakly related facts.

### 2.6 Final Prompt Context

The raw MiniRAG context started with entity rows such as:

- `CORN`
- `VOLCANOES`
- `CROPS`
- `LAVA`
- `TECTONIC PLATE`

The first source rows were about:

- predators
- herbivores
- prey
- habitats

This gives a useful high-level picture of what the model actually saw at answer time:

- the context was not organized around `pandas`, `zoo exhibits`, and `public viewing`
- it was organized around `animals`, `food`, `predators`, `habitats`, `corn`, and `volcanoes`

## 3. What Evidence Would Be Needed for the Correct Answer

The intended answer is `B`, which requires reasoning roughly like:

- pandas are animals
- pandas can be endangered
- some animals are kept in zoo exhibits or enclosures
- zoo exhibits are places where the public can view animals

The problem is that the available OpenBookQA facts only weakly support this reasoning. The closest supporting facts found here are:

- `fact_1060.txt`: `some animals live in zoo exhibits`
- `fact_0622.txt`: `endangered means low in population`

These facts help, but they do not explicitly state:

- pandas are kept in zoo exhibits
- zoo exhibits are enclosures
- zoo exhibits exist for public viewing

So even an ideal retrieval would still need a commonsense bridge.

## 4. Where MiniRAG Failed

Once the general overview is clear, the failure itself can be broken into several stages.

### 4.1 The question was decomposed in a way that amplified distractors

The query decomposition pulled in option content like:

- `Volcanoes`
- `Corn`
- `Steaks`

That means distractor options were allowed to directly drive entity retrieval. Because those distractors have strong lexical anchors in the fact bank, they became highly competitive retrieval targets.

This is one of the most important points in the failure:

- MiniRAG was not only retrieving for the correct concept
- it was also retrieving for the wrong answers

### 4.2 The graph matched the wrong parts of the knowledge base

The retrieved entity matches show that:

- `Corn` mapped cleanly to `CORN`, `CROPS`, `PLANTS`, `FOOD`
- `Volcanoes` mapped cleanly to `VOLCANOES`, `LAVA`, `TECTONIC PLATE`, `MAGMA`
- `Enclosures` did not map cleanly to zoo-related concepts
- `Public Viewing` only weakly reached `ZOO EXHIBITS`

This created a very uneven retrieval landscape:

- wrong options had strong direct graph anchors
- the correct option had weak and indirect graph anchors

### 4.3 The selected graph neighborhood was off-topic

Once graph selection started, MiniRAG concentrated on entities like:

- `CORN`
- `VOLCANOES`
- `CROPS`
- `LAVA`

instead of a more useful neighborhood like:

- `ENDANGERED`
- `ZOO EXHIBITS`
- `ANIMALS`
- `ENCLOSURES`

This matters because MiniRAG's generation stage depends on the graph-selected neighborhood. If the selected graph neighborhood is already off-topic, the final answer stage inherits that error.

### 4.4 The retrieved documents were mostly unrelated to the correct answer

The final source chunks show clear retrieval drift. The model spent much of its evidence budget on:

- predator facts
- herbivore facts
- habitat survival facts
- volcano facts
- corn facts

Those facts are not useful for distinguishing the correct answer from the distractors.

The two most relevant facts, `zoo exhibits` and `endangered means low in population`, were retrieved late and surrounded by much stronger irrelevant context. That makes it difficult for the generation model to focus on them.

### 4.5 The final context supported distractor reasoning better than correct reasoning

Given the final context, it is not surprising that the model chose a distractor. The context contained far more support for concepts like:

- `corn`
- `volcanoes`
- `animal habitats`
- `predators`

than for:

- `enclosures`
- `public viewing`
- `zoo exhibits`

So this is not only an answer-generation mistake. It is a retrieval-and-context-construction mistake.

### 4.6 The answer instability is another sign of weak grounding

The original run predicted `A`, while the fresh rerun predicted `C`.

That behavior suggests:

- the retrieved context did not strongly constrain the answer
- multiple distractors remained plausible under the final context
- the model was guessing within a noisy evidence field

If MiniRAG had retrieved a strong, coherent support chain for the correct answer, we would expect the output to be much more stable.

## 5. Why This Happens More Easily on OpenBookQA

This failure is not just about one bad query. It also reflects the structure of the OpenBookQA graph.

### 5.1 OpenBookQA gives MiniRAG less graph support per chunk

From the current graph comparison:

| Metric | OpenBookQA | MultiHop-RAG |
| --- | ---: | ---: |
| Entity nodes | 1,228 | 6,730 |
| Relation edges | 398 | 2,214 |
| Avg directly linked entities per linked chunk | 2.09 | 8.79 |
| Avg directly linked relations per linked chunk | 0.34 | 2.15 |
| Avg reachable entities within `<= 5` hops from a linked chunk | 100.87 | 542.77 |
| Avg reachable entities within `<= 10` hops from a linked chunk | 145.79 | 872.03 |

These numbers mean that an OpenBookQA chunk usually has:

- fewer immediate entity attachments
- fewer immediate relations
- a much smaller reachable evidence neighborhood

So when retrieval starts in the wrong place, the graph has less structure available to recover.

### 5.2 The facts are short and semantically shallow

OpenBookQA facts are mostly short, isolated statements. They do not provide the kind of rich multi-hop structure that MiniRAG benefits from on datasets like MultiHop-RAG.

In this case:

- `corn` and `volcanoes` have strong lexical matches
- the correct answer depends on a weaker, more indirect chain
- the graph does not have enough local support around the correct concept to overpower the distractors

### 5.3 This helps explain why a simpler baseline can compete

If the graph neighborhood is small and weakly informative, graph expansion can add more noise than benefit. On a dataset like OpenBookQA, that can make MiniRAG weaker than a simpler retrieval method that relies more directly on short factual matches.

## 6. Main Takeaways

- MiniRAG retrieved both the question topic and the distractor topics.
- The distractors `corn` and `volcanoes` had much stronger graph anchors than the correct answer.
- The selected graph entities were dominated by the wrong semantic neighborhood.
- The final retrieved documents were largely unrelated to the gold answer.
- The weakly relevant zoo-related evidence was retrieved too late and too weakly.
- The answer instability from `A` to `C` suggests poor grounding.
- This failure is consistent with the broader issue that OpenBookQA provides a much smaller question-local support graph than MultiHop-RAG.

## 7. Bottom-Line Interpretation

Failure 120 is best understood as a retrieval drift failure inside a weak-support graph regime.

MiniRAG did not fail because there were no animal-related facts in the corpus. It failed because:

- distractor options were allowed to drive retrieval
- those distractors had stronger lexical hooks than the correct concept
- the graph selected the wrong neighborhood
- the final evidence context buried the small amount of useful support

On a richer graph dataset, MiniRAG may recover from early noise. On OpenBookQA, the graph around each question is often too small and too weakly connected for that recovery to happen reliably.
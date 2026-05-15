# Deep Dive: Data Analysis and Summarisation

I classify Data Analysis and Summarisation as the well-covered capability in this set of deep dives. Its capability ID is C07, its usage frequency is 0.0751, its normalised coverage score is 0.2000, and its gap score is 0.0601. The benchmark inventory includes 7 benchmarks that cover it, with an average quality score of 4.0000 among those benchmarks.

## 1. Current Evaluation Landscape

In the Phase 1 taxonomy, I define Data Analysis and Summarisation as the ability to process, analyse, and synthesise existing datasets, documents, or information corpora in order to extract insights, patterns, statistical results, or compressed representations. The model acts as an analyst or information processor. The key point is that the user provides existing data or content as the main input, and the model converts it into a more structured or meaningful output.

The strongest coverage comes from Spider 2.0, DA-Code, InfiAgent-DABench, and MMLongBench-Doc, all of which receive 5/5. Spider 2.0 is strong for enterprise text-to-SQL and BI workflows, although its focus on SQL means it may underrepresent non-SQL analysis. DA-Code is useful because it evaluates executable data-science tasks, but the environment setup cost is high and low model success can make scores sparse. InfiAgent-DABench is relevant because it tests agentic data analysis over CSV files, although it is narrower than wider enterprise analytics. MMLongBench-Doc gives strong long-context document coverage, but document question answering is not the same as full statistical analysis.

SimpleQA and FACTS Grounding provide 3/5 coverage because they test factuality and grounded document use, but they do not fully cover advisory synthesis or broader data analysis. LiveBench also receives 3/5 because it includes relevant reasoning tasks, although its multi-capability design makes attribution less precise. WildBench receives 2/5 because real-user tasks are valuable, but broadness and LLM judge dependence limit how confidently I can treat it as direct coverage of this capability.

Overall, this capability is better covered than several others, but the coverage is still uneven. The strongest benchmarks tend to focus on structured data, document question answering, or agentic CSV analysis. Real user workflows often combine these activities with judgement, explanation, formatting, and decisions about what analysis is appropriate in the first place.

## 2. Technical and Practical Challenges to Evaluation

I find this capability challenging to evaluate because it includes text summarisation, statistical computing, document processing, format conversion, business intelligence, and forecasting. These tasks do not all have the same kind of correct answer. A SQL query can often be checked automatically, but a good executive summary or business interpretation may require judgement about relevance, accuracy, and usefulness.

The Phase 2 quality notes show the same recurring problems that appear across the project. Static public datasets may become contaminated, agentic environments can be expensive to run, open-ended outputs need careful judging, and proxy formats can fail to represent real use. For this capability, there is also a specific tension between measurable tasks and useful tasks. The most easily scored tasks are not always the ones that best represent how users ask models to analyse documents or data.

## 3. Real-World Importance

I ground the importance of this capability in the mapped Anthropic AEI top-task data. The clearest examples are creating, converting, formatting, and manipulating documents across file types at 2.1915%, extracting and processing content from images and documents at 1.4706%, and assisting with data analysis, statistical computing, and database management at 0.9618%.

These examples show why I do not treat coverage as a simple count of benchmarks. A benchmark ecosystem can appear strong because there are several data and document benchmarks, but users often need models to preserve context, handle messy inputs, explain results, and produce outputs in useful formats. Those requirements are harder to capture than a single answer field.

## 4. Consequences of Inadequate Evaluation

If this capability is evaluated inadequately, organisations may trust models for analysis tasks without knowing whether they can handle messy files, ambiguous user goals, or domain-specific interpretation. Model selection may reward performance on narrow tasks such as SQL execution while missing weaknesses in summarisation, document transformation, or judgement-heavy analysis.

For Data Analysis and Summarisation, the most direct risk is that users may act on outputs that look organised but contain missing context, statistical mistakes, or unsupported conclusions. This matters because the outputs of this capability often feed into reports, decisions, and further analysis. A high benchmark score on a simplified task may not guarantee reliable performance in a real workflow.

## 5. Requirements for Adequate Coverage

In my view, adequate coverage would require realistic task samples that include documents, spreadsheets, databases, and mixed-format inputs. It would also need to separate sub-capabilities so that strong SQL performance does not hide weak summarisation or weak business interpretation. Automated checks should be used where they fit, especially for executable queries or calculations, but human or expert judgement is still needed for open-ended synthesis.

I would also expect benchmarks to use contamination controls, such as private holdouts or refreshed task pools, and to report limitations clearly. Scores should be linked to use-case assumptions and uncertainty rather than presented as general proof that a model can perform data analysis. For Phase 5, I would only prioritise a new benchmark here if the existing tools fail to cover the most deployment-relevant workflows.

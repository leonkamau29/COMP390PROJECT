"""
Generate the final thesis PDF from structured content.
Uses fpdf2 to produce an academic-quality PDF with embedded figures,
tables, and proper formatting.
"""

import os
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "thesis", "THESIS_FINAL.pdf")

PHASE2_CHARTS = os.path.join(BASE_DIR, "outputs", "phase2", "charts")
PHASE3_CHARTS = os.path.join(BASE_DIR, "outputs", "phase3", "charts")
UOL_LOGO = os.path.join(BASE_DIR, "assets", "uol_logo.png")


class ThesisPDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=25)
        self.figure_count = 0
        self.table_count = 0
        self.current_chapter = 0
        fonts_dir = r"C:\Windows\Fonts"
        self.add_font("TNR", "", os.path.join(fonts_dir, "times.ttf"), uni=True)
        self.add_font("TNR", "B", os.path.join(fonts_dir, "timesbd.ttf"), uni=True)
        self.add_font("TNR", "I", os.path.join(fonts_dir, "timesi.ttf"), uni=True)
        self.add_font("TNR", "BI", os.path.join(fonts_dir, "timesbi.ttf"), uni=True)

    def header(self):
        pass

    def footer(self):
        if self.page_no() > 2:
            self.set_y(-20)
            self.set_font("TNR", "", 10)
            self.set_text_color(0, 0, 0)
            self.cell(0, 10, str(self.page_no()), align="C")

    def title_page(self):
        self.add_page()
        if os.path.exists(UOL_LOGO):
            logo_w = 55
            x = (210 - logo_w) / 2
            self.image(UOL_LOGO, x=x, y=15, w=logo_w)
            self.ln(55)
        else:
            self.ln(60)
        self.set_font("TNR", "B", 22)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, "Benchmark Coverage Gap:", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("TNR", "B", 18)
        self.cell(0, 10, "A Systematic Analysis of Real-World", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 10, "AI Capabilities and Evaluation Practices", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("TNR", "", 14)
        self.cell(0, 10, "COMP390 Honours Project", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)
        self.set_font("TNR", "", 13)
        self.cell(0, 10, "Leon Kamau Kiunga", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "Student ID: 201759400", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.cell(0, 8, "BSc Computer Science", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "School of Electrical Engineering,", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "Electronics and Computer Science", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "University of Liverpool", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)
        self.cell(0, 8, "Supervisor: Dr Konstantinos Tsakalidis", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.cell(0, 8, "May 2026", align="C", new_x="LMARGIN", new_y="NEXT")

    def anon_title_page(self):
        self.add_page()
        self.ln(70)
        self.set_font("TNR", "B", 22)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, "Benchmark Coverage Gap:", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("TNR", "B", 18)
        self.cell(0, 10, "A Systematic Analysis of Real-World", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 10, "AI Capabilities and Evaluation Practices", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("TNR", "", 14)
        self.cell(0, 10, "COMP390 Honours Project", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.cell(0, 8, "May 2026", align="C", new_x="LMARGIN", new_y="NEXT")

    def chapter_title(self, title):
        self.current_chapter += 1
        self.add_page()
        self.set_font("TNR", "B", 18)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, f"Chapter {self.current_chapter}: {title}", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

    def unnumbered_chapter(self, title):
        self.add_page()
        self.set_font("TNR", "B", 18)
        self.set_text_color(0, 0, 0)
        self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(8)

    def section_title(self, number, title):
        self.ln(4)
        self.set_font("TNR", "B", 13)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, f"{number}  {title}", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def subsection_title(self, number, title):
        self.ln(3)
        self.set_font("TNR", "B", 11)
        self.set_text_color(30, 30, 30)
        self.cell(0, 7, f"{number}  {title}", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("TNR", "", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def italic_text(self, text):
        self.set_font("TNR", "I", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bold_text(self, text):
        self.set_font("TNR", "B", 11)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def bullet_point(self, text):
        self.set_font("TNR", "", 11)
        self.set_text_color(0, 0, 0)
        x = self.get_x()
        self.cell(8, 6, chr(8226))
        self.multi_cell(0, 6, text)
        self.ln(1)

    def add_figure(self, image_path, caption, width=170):
        self.figure_count += 1
        if self.get_y() + 100 > 270:
            self.add_page()
        self.ln(4)
        if os.path.exists(image_path):
            x = (210 - width) / 2
            self.image(image_path, x=x, w=width)
        else:
            self.set_font("TNR", "I", 10)
            self.cell(0, 8, f"[Image not found: {os.path.basename(image_path)}]", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_font("TNR", "I", 9)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, f"Figure {self.figure_count}: {caption}", align="C")
        self.set_text_color(0, 0, 0)
        self.ln(4)

    def add_table(self, headers, rows, caption=None, col_widths=None):
        self.table_count += 1
        if caption:
            self.ln(3)
            self.set_font("TNR", "B", 10)
            self.set_text_color(0, 0, 0)
            self.multi_cell(0, 5, f"Table {self.table_count}: {caption}")
            self.ln(2)

        if col_widths is None:
            col_widths = [190 / len(headers)] * len(headers)

        # header row
        self.set_font("TNR", "B", 9)
        self.set_fill_color(230, 230, 230)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
        self.ln()

        # data rows
        self.set_font("TNR", "", 9)
        self.set_fill_color(255, 255, 255)
        for row in rows:
            max_h = 7
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 7, str(cell), border=1, align="C")
            self.ln()
        self.ln(4)


def build_thesis():
    pdf = ThesisPDF()

    # ==================== TITLE PAGE ====================
    pdf.title_page()

    # ==================== ANON TITLE PAGE ====================
    pdf.anon_title_page()

    # ==================== ABSTRACT ====================
    pdf.unnumbered_chapter("Abstract")
    pdf.body_text(
        "Large language models (LLMs) are increasingly deployed across professional, educational, and personal "
        "contexts, yet evaluation practice remains centred on standardised benchmarks such as MMLU, HumanEval, "
        "and GSM8K. A growing body of evidence demonstrates that strong benchmark performance does not reliably "
        "predict utility on the tasks users actually bring to these systems. This project addresses the absence of "
        "a systematic, usage-weighted analysis of benchmark coverage across documented real-world LLM capabilities."
    )
    pdf.body_text(
        "Adopting a mixed-methods design comprising inductive thematic analysis of empirical usage data, systematic "
        "benchmark inventory construction, quantitative gap score analysis, and literature-based validation, the "
        "project produces four principal outputs. First, an eight-capability taxonomy \u2014 Content Generation, Code "
        "Development and Technical Problem Solving, Information Retrieval and Advisory, Learning and Education "
        "Support, Review and Feedback, Translation and Language Processing, Data Analysis and Summarisation, and "
        "Conversational Interaction and Roleplay \u2014 validated with a Cohen\u2019s \u03ba of 1.00 against the Anthropic "
        "Economic Index top-task data. Second, a structured inventory of 28 major LLM benchmarks with quality "
        "ratings across five dimensions. Third, a usage-weighted coverage analysis demonstrating through chi-square "
        "testing (\u03c7\u00b2 = 31.96, p < 0.001) that benchmark coverage is not distributed in proportion to usage demand, "
        "with Code Development (gap score 0.2307), Content Generation (0.2202), and Information Retrieval and "
        "Advisory (0.1453) identified as the three most urgent gaps. Fourth, five benchmark design specifications "
        "and a reusable practitioner Assessment Toolkit."
    )

    # ==================== ETHICAL COMPLIANCE ====================
    pdf.unnumbered_chapter("Statement of Ethical Compliance")
    pdf.body_text(
        "This project falls under data category D (publicly available secondary data) and participant category 0 "
        "(no human participants in the analytical phases). All primary empirical sources \u2014 the Anthropic Economic "
        "Index dataset (Handa et al., 2025), the Ouyang et al. (2025) NBER Working Paper, and the OpenRouter 100T "
        "Token Study \u2014 are publicly released research outputs containing no individual-level data. Their use requires "
        "no ethics approval. The Assessment Toolkit pilot test involved two volunteers providing informal "
        "usability feedback on an interactive web tool; no personal data was collected or retained. The project was conducted "
        "in full accordance with the University of Liverpool School of Electrical Engineering, Electronics and Computer "
        "Science ethical guidelines."
    )

    # ==================== TABLE OF CONTENTS ====================
    pdf.unnumbered_chapter("Table of Contents")
    toc_items = [
        ("Chapter 1", "Introduction and Background"),
        ("Chapter 2", "Background and Literature Review"),
        ("Chapter 3", "Research Design and Methodology"),
        ("Chapter 4", "Implementation and Results"),
        ("Chapter 5", "Testing and Evaluation"),
        ("Chapter 6", "Recommendations and Toolkit"),
        ("Chapter 7", "Project Ethics"),
        ("Chapter 8", "Conclusion and Future Work"),
        ("Chapter 9", "BCS Criteria and Self-Reflection"),
        ("", "References"),
        ("", "Appendices"),
    ]
    for num, title in toc_items:
        pdf.set_font("TNR", "", 12)
        label = f"{num}: {title}" if num else title
        pdf.cell(0, 9, label, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_font("TNR", "B", 12)
    pdf.cell(0, 9, "Table of Figures", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("TNR", "", 11)
    figure_list = [
        "Figure 1: Distribution of benchmarks by primary capability",
        "Figure 2: Quality ratings radar chart across five evaluation dimensions",
        "Figure 3: Contamination risk distribution across the benchmark inventory",
        "Figure 4: Coverage heatmap showing benchmark-capability quality ratings",
        "Figure 5: Usage-weighted gap scores ranked by severity",
        "Figure 6: Usage frequency versus normalised coverage score scatter plot",
        "Figure 7: Temporal trends in benchmark publication by capability, 2020\u20132025",
    ]
    for fig in figure_list:
        pdf.cell(0, 7, fig, new_x="LMARGIN", new_y="NEXT")

    # ==================== CHAPTER 1: INTRODUCTION ====================
    pdf.chapter_title("Introduction and Background")

    pdf.section_title("1.1", "Background and Motivation")
    pdf.body_text(
        "Large language models have transitioned from research prototypes to tools used by millions across "
        "professional, educational, and personal contexts. This transition raises a pressing question: how well do "
        "the evaluation frameworks developed by the research community reflect what users actually ask these models "
        "to do?"
    )
    pdf.body_text(
        "The dominant approach has been to cite performance on standardised benchmarks. Models are routinely "
        "evaluated on the Massive Multitask Language Understanding benchmark (Hendrycks et al., 2021), competitive "
        "programming tasks such as HumanEval (Chen et al., 2021) and LiveCodeBench (Jain et al., 2024), and "
        "mathematical reasoning datasets such as GSM8K (Cobbe et al., 2021). These scores are used to compare "
        "models, justify deployment decisions, and direct research investment. Yet mounting evidence suggests that "
        "strong benchmark performance does not reliably translate to strong performance on real-world tasks."
    )
    pdf.body_text(
        "Miller and Tang (2025) provide a foundational analysis of this disconnect, identifying six core capabilities "
        "\u2014 Summarization, Technical Assistance, Reviewing Work, Data Structuring, Generation, and Information "
        "Retrieval \u2014 that represent how people commonly use LLMs. Their evaluation reveals significant gaps in "
        "benchmark coverage, particularly for Reviewing Work and Data Structuring, which lack any dedicated "
        "evaluation framework. They assess benchmarks through five human-centred criteria (coherence, accuracy, "
        "clarity, relevance, and efficiency) and find that existing benchmarks emphasise code generation and factual "
        "recall while neglecting the broader range of activities users rely on. This present project extends the Miller "
        "and Tang framework by constructing a more granular, empirically validated taxonomy, quantifying coverage "
        "gaps through usage-weighted scoring, and producing actionable benchmark design specifications."
    )
    pdf.body_text(
        "Handa et al. (2025) analysed approximately four million Claude.ai conversations mapped to O*NET task "
        "categories, revealing that technical assistance accounts for 65.1% of usage and reviewing work accounts for "
        "58.9%, yet reviewing work has no dedicated evaluation framework. Xu et al. (2025) demonstrate in "
        "TheAgentCompany that frontier models complete only 30% of autonomous workplace tasks despite strong "
        "benchmark scores. Singh et al. (2025) document that selective disclosure of benchmark results distorts "
        "published rankings by up to 112 positions. Pezeshkpour and Hruschka (2024) show that reordering answer "
        "options in multiple-choice questions shifts model rankings by approximately eight positions, revealing "
        "sensitivity to format rather than capability. Balloccu et al. (2024) document widespread data contamination "
        "in closed-source models, and Jain et al. (2024) demonstrate that coding performance drops sharply after "
        "training cutoff dates, evidencing memorisation rather than generalisation."
    )
    pdf.body_text(
        "Together, these findings motivate a systematic investigation into the gap between what benchmarks measure "
        "and what users need. Despite substantial individual evidence of misalignment, no existing study provides a "
        "comprehensive, usage-weighted map of the benchmark ecosystem that quantifies where coverage gaps are most "
        "severe and most consequential."
    )

    pdf.section_title("1.2", "Problem Statement")
    pdf.body_text(
        "The central problem is the systematic misalignment between LLM evaluation practice and empirically "
        "documented patterns of real-world use. Standard benchmarks measure a narrow set of capabilities \u2014 "
        "predominantly multiple-choice knowledge recall, algorithmic coding, and formal mathematical reasoning \u2014 "
        "while users employ LLMs for a broader range of tasks including reviewing content, providing grounded "
        "advisory responses, and supporting learning across diverse domains. This misalignment means that research "
        "investment flows toward capabilities that score well on benchmarks rather than those that matter most in "
        "deployment, model selection decisions may not identify the best model for a given practical purpose, and "
        "failure modes in deployed systems go undetected until they manifest as real-world errors."
    )

    pdf.section_title("1.3", "Research Objectives")
    pdf.body_text("This project pursues nine objectives:")
    objectives = [
        "O1: Build an empirically grounded capability taxonomy covering \u226595% of documented usage patterns, validated through inter-coder reliability analysis (target Cohen\u2019s \u03ba > 0.8).",
        "O2: Compile a standardised inventory of 15\u201320 major LLM benchmarks with complete structured metadata.",
        "O3: Map benchmarks to capabilities through a structured coverage matrix with justified quality ratings.",
        "O4: Quantify coverage gaps using a usage-weighted gap score formula.",
        "O5: Conduct qualitative deep dive analysis for capabilities spanning the coverage spectrum.",
        "O6: Validate the framework against published academic literature and cross-platform usage studies.",
        "O7: Produce three to five benchmark design specifications targeting the highest-priority gaps.",
        "O8: Build a reusable Assessment Toolkit for practitioners.",
        "O9: Write and submit a complete thesis.",
    ]
    for obj in objectives:
        pdf.bullet_point(obj)

    pdf.section_title("1.4", "Contributions")
    pdf.body_text(
        "This thesis makes four contributions. First, the first comprehensive, usage-derived eight-capability taxonomy "
        "for real-world LLM interaction, validated at Cohen\u2019s \u03ba = 1.00. Second, a systematically constructed "
        "benchmark inventory of 28 benchmarks with quality ratings across five dimensions, extending the evaluation "
        "framework introduced by Miller and Tang (2025) with formal quality rubrics and contamination risk "
        "assessments. Third, the first usage-weighted quantitative analysis of benchmark coverage gaps, demonstrating "
        "statistically significant distributional mismatch (\u03c7\u00b2 = 31.96, p < 0.001). Fourth, five benchmark design "
        "specifications and a practitioner Assessment Toolkit."
    )

    # ==================== CHAPTER 2: LITERATURE REVIEW ====================
    pdf.chapter_title("Background and Literature Review")

    pdf.section_title("2.1", "The Rise of LLM Benchmarking")
    pdf.body_text(
        "The evaluation of NLP systems has evolved substantially over the past decade. Early NLP evaluation relied "
        "on narrow, well-specified tasks \u2014 part-of-speech tagging, syntactic parsing, and information extraction \u2014 "
        "where ground truth was unambiguous. As neural language models became capable of producing coherent text "
        "across many domains, researchers needed comparative frameworks that could characterise model capability in "
        "aggregate rather than in isolation."
    )
    pdf.body_text(
        "The GLUE (Wang et al., 2018) and SuperGLUE (Wang et al., 2019) benchmarks marked a turning point by "
        "collecting multiple tasks \u2014 natural language inference, coreference resolution, question answering, and "
        "sentiment analysis \u2014 into unified evaluation suites. However, models quickly saturated these benchmarks, "
        "with systems exceeding human performance on SuperGLUE within approximately three years (He et al., 2021). "
        "This was evidence of benchmark-specific optimisation rather than genuine capability."
    )
    pdf.body_text(
        "The release of GPT-3 (Brown et al., 2020) changed the evaluation challenge fundamentally. Models "
        "demonstrating strong zero-shot and few-shot performance required broader frameworks. MMLU (Hendrycks "
        "et al., 2021) responded by collecting 57 academic subjects into a multiple-choice evaluation. BIG-Bench "
        "(Srivastava et al., 2022) extended this with over 200 tasks. Domain-specific benchmarks proliferated: "
        "HumanEval (Chen et al., 2021) for code generation, GSM8K (Cobbe et al., 2021) for mathematical reasoning, "
        "HellaSwag (Zellers et al., 2019) for commonsense inference, and TruthfulQA (Lin et al., 2022) for "
        "truthfulness. By the mid-2020s, public leaderboards had become central to model comparison, making the "
        "validity of the benchmark ecosystem a matter of practical significance."
    )

    pdf.section_title("2.2", "Empirical Studies of Real-World LLM Use")
    pdf.body_text(
        "Until recently, empirical study of actual LLM usage was sparse. The most significant study for this project "
        "is Handa et al. (2025), whose analysis of four million Claude.ai conversations revealed that technical "
        "assistance accounts for 65.1% of usage, reviewing work for 58.9%, and information retrieval and "
        "summarisation each for 16.6%. Critically, reviewing work has no dedicated evaluation framework."
    )
    pdf.body_text(
        "Miller and Tang (2025) provide a complementary analysis, identifying six core capabilities through thematic "
        "analysis of occupational tasks and validating them against the same Claude.ai dataset. Their framework "
        "categorises AI use into Summarization, Technical Assistance, Reviewing Work, Data Structuring, Generation, "
        "and Information Retrieval. They find that existing benchmarks cover only three of these six capabilities, "
        "leaving Generation partially covered and Reviewing Work and Data Structuring without any widely adopted "
        "benchmark. Their assessment through five human-centred criteria \u2014 coherence, accuracy, clarity, relevance, "
        "and efficiency \u2014 provides the methodological foundation that this project extends into a systematic, "
        "quantitative coverage analysis."
    )
    pdf.body_text(
        "Ouyang et al. (2025) confirm these patterns through analysis of OpenAI platform usage, with writing, "
        "coding, analysis, and tutoring emerging as dominant categories. The OpenRouter 100T Token Study reveals "
        "that roleplay and interactive fiction account for a disproportionate share of open-source model usage. "
        "Together, these sources demonstrate cross-provider consistency in usage patterns."
    )

    pdf.section_title("2.3", "Benchmark Validity and Known Limitations")
    pdf.body_text(
        "A substantial body of work has documented specific validity problems. Data contamination is extensively "
        "documented: Balloccu et al. (2024) show that benchmark test items appear in training data at inflating "
        "rates, and Jain et al. (2024) demonstrate through LiveCodeBench that performance drops on problems "
        "released after training cutoff dates, providing direct evidence that scores reflect familiarity rather than "
        "general ability."
    )
    pdf.body_text(
        "Format sensitivity compounds these concerns: Pezeshkpour and Hruschka (2024) demonstrate that option "
        "reordering in multiple-choice questions shifts model rankings by eight positions. Singh et al. (2025) document "
        "selective disclosure practices that distort rankings by up to 112 positions. Goodhart\u2019s Law applies with "
        "particular force: when a measure becomes a target, it ceases to be a good measure (Strathern, 1997). "
        "Chang et al. (2023) note a structural tendency toward benchmark-specific optimisation at the expense of "
        "genuine capability development. Benchmark saturation has prompted harder variants including MMLU-Pro "
        "(Wang et al., 2024), HumanEval+ (Liu et al., 2023), and Humanity\u2019s Last Exam (Phan et al., 2025)."
    )

    pdf.section_title("2.4", "Gaps in the Literature")
    pdf.body_text(
        "No prior study provides a systematic, usage-weighted, cross-benchmark coverage analysis linking empirically "
        "documented usage frequencies to structured quality assessments. Miller and Tang (2025) identify the gap most "
        "directly, noting that Reviewing Work and Data Structuring lack any dedicated benchmark, but do not compute "
        "quantitative gap scores or produce actionable benchmark specifications. This project addresses that space by "
        "building a capability taxonomy from usage data before examining the benchmark landscape, computing "
        "usage-weighted gap scores, and producing actionable recommendations."
    )

    # ==================== CHAPTER 3: METHODOLOGY ====================
    pdf.chapter_title("Research Design and Methodology")

    pdf.section_title("3.1", "Overall Research Design")
    pdf.body_text(
        "This project adopts a mixed-methods research design combining systematic literature review, qualitative "
        "thematic analysis, quantitative gap assessment, and literature-based validation. Determining whether "
        "benchmark coverage is misaligned with real-world use requires both an empirically derived account of what "
        "users do (qualitative methods) and a systematic characterisation of how well benchmarks address those uses "
        "(quantitative comparison). A pure expert survey design was rejected because it would depend on a small "
        "convenience sample. A purely computational approach was rejected because it would not capture qualitative "
        "judgements about coverage quality."
    )

    pdf.section_title("3.2", "Five-Phase Research Structure")
    pdf.body_text("The project follows five sequential phases, each producing inputs required by the next:")
    phases = [
        "Phase 1 (Weeks 1\u20134): Capability framework development through thematic analysis of 131 task instances from three empirical sources.",
        "Phase 2 (Weeks 5\u20139): Systematic benchmark inventory compilation and standardised analysis of 28 benchmarks.",
        "Phase 3 (Weeks 10\u201313): Coverage matrix construction, gap quantification, statistical testing, deep dive analyses, and case studies.",
        "Phase 4 (Weeks 14\u201316): Literature-based validation of the framework and findings against published research.",
        "Phase 5 (Weeks 17\u201320): Benchmark design specifications, Assessment Toolkit, and recommendations synthesis.",
    ]
    for p in phases:
        pdf.bullet_point(p)

    pdf.section_title("3.3", "Qualitative Methods: Thematic Analysis")
    pdf.body_text(
        "The primary qualitative method was Braun and Clarke\u2019s (2006) six-phase thematic analysis. This framework "
        "was chosen over grounded theory (Glaser and Strauss, 1967), which imposes more prescriptive procedures "
        "suited to iterative interview data, and content analysis (Krippendorff, 2018), which requires a pre-existing "
        "coding scheme. The analysis was conducted on 131 task instances from three sources: the Anthropic Economic "
        "Index (103 tasks), Ouyang et al. (19 task categories), and the OpenRouter 100T Token Study (9 categories)."
    )
    pdf.body_text(
        "The six phases \u2014 familiarisation, open coding, axial coding, selective coding, theme definition, and taxonomy "
        "production \u2014 were executed in strict sequence. The selective coding criterion was that two categories should "
        "remain distinct if they require different evaluation approaches. Inter-coder reliability was assessed on a 10% "
        "subsample independently coded by a second coder using only the decision rules. Cohen\u2019s \u03ba was calculated as "
        "\u03ba = 1.0000, substantially exceeding the target of > 0.80 (Cohen, 1960)."
    )

    pdf.section_title("3.4", "Quantitative Methods")
    pdf.body_text(
        "Each benchmark was assessed against a five-dimension quality rubric (Coherence, Accuracy, Clarity, "
        "Relevance, Efficiency) on a 1\u20135 scale, adopting the same evaluative criteria proposed by Miller and Tang "
        "(2025) but applying them systematically across 28 benchmarks with required written justifications."
    )
    pdf.body_text(
        "The central quantitative measure is the usage-weighted gap score:"
    )
    pdf.bold_text("    Gap Score = Usage Frequency \u00d7 (1 \u2212 Normalised Coverage Score)")
    pdf.body_text(
        "where Usage Frequency is the proportion of total LLM usage attributable to the capability and Normalised "
        "Coverage Score is the total quality-weighted coverage divided by the maximum possible, scaled 0\u20131. Higher "
        "gap scores indicate capabilities that are both heavily used and poorly covered."
    )
    pdf.body_text(
        "Three statistical analyses were conducted: Pearson correlation between usage frequency and coverage score, "
        "chi-square goodness-of-fit testing whether benchmark counts match usage-proportional expectations, and "
        "per-capability temporal linear regressions modelling benchmark publication rates from 2020 to 2025. All "
        "statistical operations used np.random.seed(42) for reproducibility."
    )

    pdf.section_title("3.5", "Data Sources")
    pdf.body_text(
        "Usage frequency data was drawn from the Anthropic Economic Index (Handa et al., 2025), cross-validated "
        "against Ouyang et al. (2025) and the OpenRouter study. Benchmark data was compiled through four search "
        "channels: Papers with Code listings, major model technical reports (GPT-4, Claude 3/3.5, Gemini, Llama "
        "2/3, DeepSeek R1), Google Scholar searches filtered to 2020\u20132025, and snowball sampling from key "
        "project references."
    )

    # ==================== CHAPTER 4: IMPLEMENTATION AND RESULTS ====================
    pdf.chapter_title("Implementation and Results")

    pdf.section_title("4.1", "Phase 1 \u2014 Capability Taxonomy Development")

    pdf.subsection_title("4.1.1", "Thematic Analysis Outcomes")
    pdf.body_text(
        "The thematic analysis of 131 task instances produced 19 intermediate axial categories that collapsed into "
        "eight core capabilities. The coding process revealed several non-obvious convergences: software engineering, "
        "web development, debugging, DevOps, and agentic technical execution shared the characteristic that the "
        "expected output was an executable artefact. Professional writing, creative writing, marketing content, and "
        "clinical documentation shared the characteristic that the model was the primary author. Academic support, "
        "tutoring, and concept explanation shared the characteristic that the user\u2019s goal was knowledge acquisition."
    )

    pdf.subsection_title("4.1.2", "The Eight-Capability Taxonomy")
    pdf.body_text(
        "C01 \u2014 Content Generation: producing original written artefacts. C02 \u2014 Code Development and Technical "
        "Problem Solving: writing, debugging, refactoring, and maintaining software. C03 \u2014 Information Retrieval "
        "and Advisory: locating, synthesising, and delivering factual information or advisory guidance. C04 \u2014 "
        "Learning and Education Support: assisting knowledge acquisition through tutoring and guided engagement. "
        "C05 \u2014 Review and Feedback: evaluating, critiquing, editing, and improving existing work. C06 \u2014 "
        "Translation and Language Processing: cross-lingual text conversion and language support. C07 \u2014 Data "
        "Analysis and Summarisation: processing existing data to extract insights or compressed representations. "
        "C08 \u2014 Conversational Interaction and Roleplay: open-ended interactive dialogue for entertainment or "
        "personal support."
    )
    pdf.body_text(
        "This taxonomy extends the six-capability framework of Miller and Tang (2025) by disaggregating their "
        "broader categories into more granular constructs. Their \u201cTechnical Assistance\u201d maps primarily to C02 but is "
        "distinguished from C03 advisory functions. Their \u201cSummarization\u201d is incorporated within C07. The addition "
        "of C04 and C08 reflects usage patterns in educational and open-source contexts less prominent in the Miller "
        "and Tang analysis."
    )
    pdf.body_text(
        "The distribution of the 103 AEI tasks was: C02 received 35 tasks (34.0%), C03 received 22 (21.4%), C01 "
        "received 18 (17.5%), C07 received 11 (10.7%), C04 received 8 (7.8%), C05 received 4 (3.9%), C08 received "
        "3 (2.9%), and C06 received 2 (1.9%). All 103 tasks were mapped at high or medium confidence with no task "
        "remaining unmapped, achieving 100% coverage. Inter-coder reliability yielded Cohen\u2019s \u03ba = 1.0000."
    )

    pdf.section_title("4.2", "Phase 2 \u2014 Benchmark Inventory")

    pdf.subsection_title("4.2.1", "Search and Selection")
    pdf.body_text(
        "A four-channel systematic search identified 127 candidate benchmarks. After screening against inclusion "
        "criteria (public documentation, use in \u22652 major model reports, coverage of \u22651 Phase 1 capability), 28 "
        "benchmarks were selected for the final inventory."
    )

    pdf.add_table(
        headers=["Capability", "Code", "Count"],
        rows=[
            ["Code Development & Technical Problem Solving", "C02", "5"],
            ["Information Retrieval and Advisory", "C03", "5"],
            ["Content Generation", "C01", "4"],
            ["Data Analysis and Summarisation", "C07", "4"],
            ["Learning and Education Support", "C04", "3"],
            ["Review and Feedback", "C05", "3"],
            ["Conversational Interaction and Roleplay", "C08", "2"],
            ["Translation and Language Processing", "C06", "2"],
        ],
        caption="Benchmark distribution by primary capability",
        col_widths=[100, 25, 25],
    )

    pdf.add_figure(
        os.path.join(PHASE2_CHARTS, "chart2_benchmarks_by_capability.png"),
        "Distribution of the 28 inventoried benchmarks across the eight capability categories. Code Development "
        "(C02) and Information Retrieval (C03) receive the highest primary benchmark counts, while Translation "
        "(C06) and Conversational Interaction (C08) receive the lowest.",
    )

    pdf.subsection_title("4.2.2", "Quality Ratings Analysis")
    pdf.body_text(
        "Each benchmark was rated on five quality dimensions. The mean ratings were: Coherence 4.61, Relevance "
        "4.54, Accuracy 4.39, Clarity 4.21, and Efficiency 3.50. The lower Efficiency score reflects the operational "
        "cost of agentic benchmarks, writing benchmarks requiring LLM judges, and tutoring benchmarks requiring "
        "multi-turn simulation."
    )

    pdf.add_figure(
        os.path.join(PHASE3_CHARTS, "quality_radar.png"),
        "Radar chart showing mean quality ratings across the five evaluation dimensions for all 28 benchmarks. "
        "Coherence and Relevance score highest, while Efficiency is the weakest dimension, consistent with Miller "
        "and Tang\u2019s (2025) observation that efficiency measurement remains a major blind spot.",
        width=140,
    )

    pdf.subsection_title("4.2.3", "Contamination Risk Assessment")
    pdf.body_text(
        "Of the 28 benchmarks, 24 were classified as Low contamination risk, 3 as Medium, and 1 (HumanEval) as "
        "High. HumanEval\u2019s 164-problem test set has been publicly available since 2021 and is widely distributed in "
        "training corpora, corroborating Jain et al. (2024)."
    )

    pdf.add_figure(
        os.path.join(PHASE2_CHARTS, "chart5_contamination_risk.png"),
        "Contamination risk assessment for the 28 benchmarks. The majority (86%) are classified as Low risk. "
        "HumanEval is the sole High-risk benchmark.",
        width=140,
    )

    pdf.section_title("4.3", "Phase 3 \u2014 Coverage Analysis")

    pdf.subsection_title("4.3.1", "Coverage Matrix Construction")
    pdf.body_text(
        "The coverage matrix assessed how well each of the 28 benchmarks tests each of the eight capabilities on a "
        "0\u20135 scale, with every non-zero cell accompanied by a written justification. Across the full 28 \u00d7 8 matrix, "
        "50 cells received non-zero ratings, revealing that most benchmarks are capability-specific."
    )

    pdf.add_figure(
        os.path.join(PHASE3_CHARTS, "coverage_heatmap.png"),
        "Heatmap of the capability-benchmark coverage matrix. Cell colour intensity indicates quality rating (0\u20135). "
        "The matrix reveals concentrated coverage in C02 (Code Development) and C07 (Data Analysis), with "
        "sparse coverage for C06 (Translation) and C05 (Review and Feedback).",
    )

    pdf.subsection_title("4.3.2", "Gap Score Computation")
    pdf.body_text(
        "Usage frequencies were derived by summing AEI task percentages for each capability. The gap scores are "
        "presented in Table 2."
    )

    pdf.add_table(
        headers=["Rank", "Capability", "Usage", "Coverage", "Gap Score", "Severity"],
        rows=[
            ["1", "C02 Code Development", "0.3019", "0.2357", "0.2307", "High"],
            ["2", "C01 Content Generation", "0.2568", "0.1429", "0.2202", "High"],
            ["3", "C03 Info. Retrieval", "0.1754", "0.1714", "0.1453", "High"],
            ["4", "C04 Learning & Educ.", "0.1113", "0.1714", "0.0922", "High"],
            ["5", "C07 Data Analysis", "0.0751", "0.2000", "0.0601", "Medium"],
            ["6", "C05 Review & Feedback", "0.0308", "0.1286", "0.0269", "Medium"],
            ["7", "C06 Translation", "0.0271", "0.0714", "0.0252", "Medium"],
            ["8", "C08 Conversational", "0.0215", "0.1286", "0.0188", "Low"],
        ],
        caption="Usage-weighted gap score ranking \u2014 all eight capabilities",
        col_widths=[14, 55, 22, 28, 28, 22],
    )

    pdf.add_figure(
        os.path.join(PHASE3_CHARTS, "gap_scores.png"),
        "Gap scores for all eight capabilities, ranked from highest to lowest. Code Development (C02) ranks first "
        "despite having the highest benchmark count, because its usage frequency is so substantially greater than "
        "what even the densest coverage can proportionally address. The four High-severity gaps collectively "
        "account for 84.5% of documented usage.",
    )

    pdf.body_text(
        "C02 ranks first despite having the highest benchmark count because its usage frequency (0.3019) is so "
        "substantially greater than what existing coverage can proportionally address. C01 ranks second with both "
        "high demand (0.2568) and thin coverage (0.1429). This is consistent with Miller and Tang\u2019s (2025) "
        "observation that Generation is only partially covered by existing benchmarks."
    )

    pdf.subsection_title("4.3.3", "Statistical Analysis")
    pdf.body_text(
        "The Pearson correlation between usage frequency and total coverage score yielded r = 0.639, p = 0.088 "
        "(95% CI: [\u22120.119, 0.927]). The moderate positive correlation indicates a tendency for higher-usage "
        "capabilities to receive more benchmark coverage, but the result is not statistically significant at "
        "\u03b1 = 0.05, reflecting substantial uncertainty with eight observations."
    )
    pdf.body_text(
        "The chi-square goodness-of-fit test assessed whether benchmark counts matched usage-proportional "
        "expectations: \u03c7\u00b2(7) = 31.96, p < 0.001, Cram\u00e9r\u2019s V = 0.302 (bootstrap 95% CI: [0.202, 0.528]). "
        "This provides strong evidence that benchmark coverage is not distributed in proportion to usage demand."
    )

    pdf.add_figure(
        os.path.join(PHASE3_CHARTS, "usage_vs_coverage_scatter.png"),
        "Scatter plot of usage frequency against normalised coverage score for each capability. The moderate "
        "positive correlation (r = 0.639) indicates partial tracking of usage by benchmark development, but the "
        "non-significant p-value demonstrates substantial residual misalignment.",
        width=150,
    )

    pdf.body_text(
        "Temporal linear regressions revealed statistically significant positive slopes for C01 (slope = 0.514, "
        "p = 0.021), C04 (slope = 0.743, p = 0.009), and C05 (slope = 0.600, p = 0.034), indicating accelerating "
        "benchmark activity in these capability areas."
    )

    pdf.add_figure(
        os.path.join(PHASE3_CHARTS, "temporal_trends.png"),
        "Annual benchmark publication counts by capability over 2020\u20132025. C04 (Learning and Education "
        "Support) shows the steepest positive trend (slope = 0.743, p = 0.009), reflecting the post-ChatGPT surge "
        "in tutoring-related evaluation research.",
    )

    pdf.subsection_title("4.3.4", "Case Studies")
    pdf.body_text(
        "Six case studies documented instances where high benchmark performance did not correspond to reliable "
        "deployment performance. Xu et al. (2025) show that frontier agents complete only 30% of workplace tasks. "
        "Jain et al. (2024) demonstrate contamination effects in coding benchmarks. Pezeshkpour and Hruschka "
        "(2024) reveal format sensitivity in multiple-choice evaluations. Kanjee et al. (2024) document clinically "
        "significant errors from models with strong medical knowledge scores. Magesh et al. (2025) document "
        "fictitious legal citations from models marketed as legal research tools. Singh et al. (2025) demonstrate "
        "that selective disclosure distorts rankings by up to 112 positions. The cross-case pattern confirms that "
        "benchmarks are valid for specific capabilities under specific conditions, but are regularly used as broader "
        "evidence of capability than their design supports."
    )

    # ==================== CHAPTER 5: TESTING AND EVALUATION ====================
    pdf.chapter_title("Testing and Evaluation")

    pdf.section_title("5.1", "Literature-Based Validation")
    pdf.body_text(
        "The eight-capability taxonomy is corroborated by convergent evidence from multiple independent sources. "
        "Ouyang et al. (2025) identify a comparable distribution of task categories from OpenAI API requests. The "
        "decision to treat Content Generation (C01) and Review and Feedback (C05) as distinct capabilities is "
        "independently supported by Handa et al.\u2019s (2025) finding that reviewing work constitutes a separately "
        "identifiable usage cluster, and is consistent with Miller and Tang\u2019s (2025) framework."
    )
    pdf.body_text(
        "Baan et al. (2025) provide substantive external validation, reviewing 445 LLM benchmarks and finding "
        "that approximately one-fifth are published without a clear definition of the capability they purport to "
        "measure. Their recommendation of a \u201cbenchmark-validation-first\u201d culture aligns with the gap score "
        "methodology used here. The chi-square result (\u03c7\u00b2 = 31.96, p < 0.001) is corroborated by Qian et al. "
        "(2026), who find significant quality variation across benchmark domains."
    )

    pdf.section_title("5.2", "Assessment Toolkit Pilot Testing")
    pdf.body_text(
        "The Assessment Toolkit was pilot-tested with two postgraduate volunteers outside NLP/ML. Both completed "
        "a use case scenario (evaluating benchmarks for a customer support deployment) without assistance in 18 and "
        "23 minutes respectively, within the 15\u201325 minute target. One participant identified a labelling usability "
        "issue, addressed by adding plain English descriptions. The second noted the absence of weight sum "
        "validation, addressed by adding a normalisation formula. No errors were found in the calculations."
    )

    pdf.section_title("5.3", "Research Objectives Evaluation")
    pdf.add_table(
        headers=["Objective", "Status", "Evidence"],
        rows=[
            ["O1", "Exceeded", "8 capabilities; 100% coverage; \u03ba = 1.000"],
            ["O2", "Exceeded", "28 benchmarks (target: 15\u201320)"],
            ["O3", "Met", "28\u00d78 matrix; 50 justified ratings"],
            ["O4", "Met", "Gap scores; \u03c7\u00b2 confirms mismatch"],
            ["O5", "Met", "4 deep dives; 6 case studies"],
            ["O6", "Met", "Literature-based validation"],
            ["O7", "Met", "5 benchmark specifications"],
            ["O8", "Met", "Interactive web toolkit; pilot-tested"],
            ["O9", "Met", "This thesis"],
        ],
        caption="Evaluation of research objectives against evidence",
        col_widths=[25, 25, 100],
    )

    pdf.section_title("5.4", "Limitations")
    pdf.body_text(
        "The literature-based validation relies on published sources also drawn upon in constructing the framework, "
        "providing convergent but not fully independent validation. The toolkit pilot involved only two participants. "
        "Usage frequency weights are derived primarily from one provider\u2019s data. The benchmark inventory reflects "
        "the state of published benchmarks as of early 2026."
    )

    # ==================== CHAPTER 6: RECOMMENDATIONS ====================
    pdf.chapter_title("Recommendations and Toolkit")

    pdf.section_title("6.1", "Benchmark Design Specifications")
    pdf.body_text(
        "Five benchmark specifications were developed for the five highest-priority gaps. The selection criterion was "
        "whether existing benchmarks were structurally unable to address the evaluation need."
    )
    pdf.body_text(
        "MaintBench (C02) targets everyday software maintenance \u2014 multi-file debugging, dependency integration, "
        "refactoring under constraints \u2014 rather than competitive programming. Each task provides a repository "
        "snapshot, stakeholder request, logs, and constraints. The proposed first release comprises approximately 600 "
        "tasks across 60 repositories. This responds directly to Miller and Tang\u2019s (2025) finding that Technical "
        "Assistance benchmarks focus predominantly on isolated Python coding tasks."
    )
    pdf.body_text(
        "WorkWriteBench (C01) evaluates professional writing under realistic workplace constraints: communications, "
        "decision documents, marketing copy, and audience-specific transformations. The proposed release contains "
        "approximately 1,000 tasks with hybrid automated and judged scoring."
    )
    pdf.body_text(
        "GroundedAdviceBench (C03) evaluates whether models can provide evidence-grounded, context-sensitive "
        "advice while communicating uncertainty. The proposed release contains approximately 800 tasks across five "
        "advisory domains."
    )
    pdf.body_text(
        "TutorScaffoldBench (C04) evaluates models as tutors rather than answer engines, assessing misconception "
        "diagnosis, adaptive scaffolding, and formative feedback across approximately 1,200 tasks."
    )
    pdf.body_text(
        "MessyDataBench (C07) evaluates the full analyst workflow: handling imperfect data, interpreting "
        "uncertainty, and communicating conclusions to non-technical audiences across approximately 700 tasks."
    )

    pdf.section_title("6.2", "Assessment Toolkit")
    pdf.body_text(
        "The Assessment Toolkit is implemented as an interactive, zero-dependency static web application, enabling "
        "practitioners to evaluate benchmark coverage for their specific deployment context without requiring any "
        "software installation. The toolkit comprises five sections: a Coverage Calculator that computes weighted "
        "coverage scores based on user-input capability priorities against the Phase 3 coverage data, a Capabilities "
        "view presenting the full taxonomy, a Benchmarks view summarising the Phase 2 inventory, an Evidence "
        "Dashboard visualising gap scores and coverage metrics, and a Methodology section explaining the underlying "
        "framework. Users can select predefined deployment profiles or create custom capability weightings, and the "
        "toolkit ranks benchmarks from the Phase 2 inventory using the coverage matrix. The application loads project "
        "data files at runtime, keeping outputs reproducible and traceable to the research evidence base. It can be "
        "deployed at no cost via GitHub Pages."
    )

    pdf.section_title("6.3", "Implementation Roadmap")
    pdf.body_text(
        "In the short term (0\u20131 year), MaintBench and WorkWriteBench should be converted into pilot-ready "
        "artefacts. In the medium term (1\u20133 years), pilots should become maintained benchmarks with private "
        "evaluation splits. In the long term (3+ years), the goal is a capability-weighted benchmark ecosystem "
        "where evaluation reports communicate model fitness for specific capability profiles rather than aggregate "
        "leaderboard positions."
    )

    # ==================== CHAPTER 7: PROJECT ETHICS ====================
    pdf.chapter_title("Project Ethics")
    pdf.body_text(
        "All primary empirical sources \u2014 the Anthropic Economic Index (Handa et al., 2025), Ouyang et al. (2025), "
        "and the OpenRouter 100T Token Study \u2014 are publicly released research outputs containing no individual-level "
        "or personal data. Their use requires no ethics approval and complies with standard academic access terms."
    )
    pdf.body_text(
        "The Assessment Toolkit pilot test involved two postgraduate volunteers who provided informal usability "
        "feedback. No personal data was collected; participation was voluntary and anonymous."
    )
    pdf.body_text(
        "All project data is stored on university OneDrive with version control via Git. No personally identifiable "
        "information appears in any data file. The repository will be made public following thesis submission. "
        "Processing complies with UK GDPR data minimisation and storage limitation principles."
    )
    

    # ==================== CHAPTER 8: CONCLUSION ====================
    pdf.chapter_title("Conclusion and Future Work")

    pdf.section_title("8.1", "Summary of Findings")
    pdf.body_text(
        "This project set out to investigate whether LLM benchmark coverage is systematically misaligned with "
        "documented patterns of real-world use. The answer is clearly affirmative. The eight-capability taxonomy "
        "provides a structured, empirically grounded vocabulary for describing the full range of documented LLM use, "
        "extending the six-capability framework of Miller and Tang (2025). The coverage analysis demonstrates "
        "through chi-square testing that benchmark allocation does not match usage frequency (\u03c7\u00b2 = 31.96, "
        "p < 0.001). The four highest-priority gaps \u2014 Code Development (0.2307), Content Generation (0.2202), "
        "Information Retrieval and Advisory (0.1453), and Learning and Education Support (0.0922) \u2014 collectively "
        "account for approximately 84.5% of documented usage."
    )

    pdf.section_title("8.2", "Contributions Revisited")
    pdf.body_text(
        "The taxonomy contribution provides the first usage-derived capability classification validated through "
        "inter-coder reliability testing. The benchmark inventory provides the first cross-benchmark quality "
        "assessment mapped to a usage-derived taxonomy. The gap analysis provides the first quantitative evidence "
        "that benchmark coverage is significantly misaligned with usage demand. The recommendations provide "
        "concrete, implementable benchmark designs and a practitioner tool. All four contributions are novel; "
        "the first three are also confirmatory of concerns raised independently by Miller and Tang (2025), "
        "Handa et al. (2025), and Baan et al. (2025)."
    )

    pdf.section_title("8.3", "Limitations")
    pdf.body_text(
        "The most consequential limitation is the reliance on single-provider usage data for frequency weights. "
        "Coverage ratings are researcher judgements that different raters might assign differently. The statistical "
        "analyses involve small samples, making results descriptive rather than confirmatory. The benchmark "
        "specifications are design documents whose validity cannot be confirmed until implemented."
    )

    pdf.section_title("8.4", "Future Work")
    pdf.body_text(
        "Five directions are identified: (1) implementing MaintBench or WorkWriteBench as pilot benchmarks for "
        "the two largest gaps; (2) replicating the coverage analysis with a multi-provider usage dataset; (3) extending "
        "taxonomy validation through a larger inter-coder sample and formal expert survey; (4) a longitudinal study "
        "tracking whether gaps narrow as benchmark development accelerates; and (5) extending the web-based "
        "Assessment Toolkit with automated benchmark database updates and community-contributed coverage ratings."
    )

    # ==================== CHAPTER 9: BCS ====================
    pdf.chapter_title("BCS Criteria and Self-Reflection")

    pdf.section_title("9.1", "BCS Criteria")
    pdf.add_table(
        headers=["#", "BCS Outcome", "Where Addressed"],
        rows=[
            ["1", "Practical and analytical skills", "Chapters 3\u20134"],
            ["2", "Innovation and creativity", "Chapter 6"],
            ["3", "Synthesis and evaluation", "Chapters 4\u20135"],
            ["4", "Meets a real need", "Chapter 1"],
            ["5", "Self-management", "Section 9.2"],
            ["6", "Critical self-evaluation", "Section 9.3"],
        ],
        caption="Mapping against BCS outcomes",
        col_widths=[12, 80, 58],
    )

    pdf.section_title("9.2", "Self-Management Reflection")
    pdf.body_text(
        "I managed this project across 24 weeks using a structured phase-based timeline, with each phase producing "
        "documented deliverables before the next began. The scope of the benchmark inventory was revised from an "
        "initial target of 40\u201350 benchmarks to 15\u201320 following supervisor feedback, and the final inventory of 28 "
        "benchmarks represented a pragmatic middle ground between depth and breadth. The Phase 1 taxonomy "
        "underwent substantial revision in Week 17 when the coverage matrix revealed that original capability "
        "boundaries were insufficiently distinct for quantitative analysis."
    )

    pdf.section_title("9.3", "Critical Self-Evaluation")
    pdf.body_text(
        "I am most satisfied with the gap score methodology, which provides a genuinely novel analytical instrument "
        "for prioritising evaluation investment, and with the taxonomy\u2019s strong validation result. The weakest aspect "
        "is the reliance on a single provider\u2019s usage data for frequency weights, a limitation I would address by "
        "incorporating API-level usage data from multiple providers if the project were repeated. I would also begin "
        "the benchmark inventory earlier, as the Phase 2 analysis took longer than anticipated."
    )
    pdf.body_text(
        "The most important skill I developed was the ability to design and execute a mixed-methods research study "
        "from first principles, integrating qualitative thematic analysis with quantitative statistical testing. The "
        "project taught me that evaluation is not a neutral act \u2014 the choice of what to measure shapes what gets "
        "optimised, and the gaps in our evaluation frameworks have direct consequences for how AI systems serve "
        "their users."
    )

    # ==================== REFERENCES ====================
    pdf.unnumbered_chapter("References")
    pdf.set_font("TNR", "", 9)
    refs = [
        "Baan, J., Giulianelli, M., Kuribayashi, T., Linzen, T., R\u00f6ttger, P., Shwartz, V., White, B., Zhu, W. and Fokkens, A. (2025). Measuring what matters: Construct validity in large language model benchmarks. arXiv:2511.04703.",
        "Balloccu, S., Schmidtov\u00e1, P., Lango, M. and Du\u0161ek, O. (2024). Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source LLMs. In Proceedings of EACL 2024, pp. 67\u201393.",
        "Braun, V. and Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), pp. 77\u2013101. https://doi.org/10.1191/1478088706qp063oa",
        "Brown, T. B. et al. (2020). Language models are few-shot learners. In Advances in Neural Information Processing Systems, Vol. 33. arXiv:2005.14165.",
        "Burnham, S. et al. (2025). Medical large language model benchmarks should prioritize construct validity. arXiv:2503.10694.",
        "Chang, Y. et al. (2023). A survey on evaluation of large language models. ACM TIST, 15(3), pp. 1\u201345. arXiv:2307.03109.",
        "Chen, M. et al. (2021). Evaluating large language models trained on code. arXiv:2107.03374.",
        "Clark, P. et al. (2018). Think you have solved question answering? Try ARC. arXiv:1803.05457.",
        "Cobbe, K. et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.",
        "Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), pp. 37\u201346.",
        "Glaser, B. G. and Strauss, A. L. (1967). The Discovery of Grounded Theory. Chicago: Aldine.",
        "Handa, K. et al. (2025). Which economic tasks are performed with AI? Evidence from millions of Claude conversations. arXiv:2503.04761.",
        "He, P. et al. (2021). DeBERTa: Decoding-enhanced BERT with disentangled attention. In ICLR 2021. arXiv:2006.03654.",
        "Hendrycks, D. et al. (2021). Measuring massive multitask language understanding. In ICLR 2021. arXiv:2009.03300.",
        "Jain, N. et al. (2024). LiveCodeBench: Holistic and contamination free evaluation of LLMs for code. arXiv:2403.07974.",
        "Kanjee, Z., Crowe, B. and Rodman, A. (2024). Evaluation and mitigation of LLM limitations in clinical decision-making. Nature Medicine, 30, pp. 2613\u20132615.",
        "Krippendorff, K. (2018). Content Analysis: An Introduction to Its Methodology (4th edn). SAGE.",
        "Lin, S., Hilton, J. and Evans, O. (2022). TruthfulQA: Measuring how models mimic human falsehoods. In ACL 2022. arXiv:2109.07958.",
        "Liu, J. et al. (2023). Is your code generated by ChatGPT really correct? Rigorous evaluation with EvalPlus. In NeurIPS 2023. arXiv:2305.01210.",
        "Magesh, V. et al. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. arXiv:2405.20362.",
        "Miller, J. K. and Tang, W. (2025). Evaluating LLM metrics through real-world capabilities. arXiv:2505.08253.",
        "Ouyang, S. et al. (2025). How are large language models used? Evidence from millions of OpenAI API requests (NBER Working Paper 34255).",
        "Pezeshkpour, P. and Hruschka, E. (2024). Large language models sensitivity to the order of options in multiple-choice questions. In Findings of NAACL 2024. arXiv:2308.11483.",
        "Phan, L. et al. (2025). Humanity\u2019s last exam. arXiv:2501.14249.",
        "Qian, Q. et al. (2026). Benchmark\u00b2: Systematic evaluation of LLM benchmarks. arXiv:2601.03986.",
        "Rein, D. et al. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv:2311.12022.",
        "Singh, S. et al. (2025). The leaderboard illusion. arXiv:2504.20879.",
        "Srivastava, A. et al. (2022). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. TMLR. arXiv:2206.04615.",
        "Strathern, M. (1997). \u2018Improving ratings\u2019: Audit in the British University system. European Review, 5(3), pp. 305\u2013321.",
        "Wang, A. et al. (2018). GLUE: A multi-task benchmark for NLU. In EMNLP BlackboxNLP Workshop. arXiv:1804.07461.",
        "Wang, A. et al. (2019). SuperGLUE: A stickier benchmark for general-purpose language understanding. In NeurIPS 2019. arXiv:1905.00537.",
        "Wang, Y. et al. (2024). MMLU-Pro: A more robust and challenging multi-task language understanding benchmark. arXiv:2406.01574.",
        "Xu, F. F. et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. arXiv:2412.14161.",
        "Zellers, R. et al. (2019). HellaSwag: Can a machine really finish your sentence? In ACL 2019. arXiv:1905.07830.",
    ]
    for ref in refs:
        pdf.multi_cell(0, 5, ref)
        pdf.ln(2)

    # ==================== APPENDICES ====================
    pdf.unnumbered_chapter("Appendices")
    pdf.section_title("A", "Capability Taxonomy Summary")
    pdf.body_text(
        "The full eight-capability taxonomy with definitions, decision rules, sub-categories, and worked examples "
        "is available in outputs/phase1/capability_taxonomy_FINAL.md."
    )
    pdf.section_title("B", "Benchmark Database")
    pdf.body_text(
        "The complete 28-benchmark database with all metadata fields and quality ratings is available in "
        "outputs/phase2/benchmark_database_FINAL.csv."
    )
    pdf.section_title("C", "Coverage Matrix")
    pdf.body_text(
        "The full 28 \u00d7 8 coverage matrix with justification notes is available in data/phase3/coverage_matrix.csv "
        "and data/phase3/coverage_matrix_notes.csv."
    )
    pdf.section_title("D", "Statistical Analysis Code")
    pdf.body_text(
        "All statistical analyses were conducted in Python using scipy and numpy with np.random.seed(42). "
        "Scripts are available in the scripts/ directory."
    )
    pdf.section_title("E", "Assessment Toolkit")
    pdf.body_text(
        "The Assessment Toolkit is available as an interactive static web application in "
        "outputs/phase5/web_toolkit/. It can be run locally via a static HTTP server or deployed via GitHub "
        "Pages at no cost. Source files include index.html, styles.css, and app.js, with no external dependencies."
    )

    # Save
    pdf.output(OUTPUT_PATH)
    print(f"PDF saved to: {OUTPUT_PATH}")
    print(f"Total pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_thesis()

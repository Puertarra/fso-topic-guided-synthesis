# Topic-guided expert questions for a traceable literature synthesis: physical-layer security in FSO systems

Data, prompts, notebooks and validation scripts for the article:

> Leiva-Araos, A., Kaushal, H., Gana, B. *Topic modelling guides expert research questions in a traceable synthesis of physical-layer security for free-space optical systems.* (submitted).

Archived version: Zenodo, DOI: `10.5281/zenodo.XXXXXXX` (to be updated after the first release).

## What the workflow does

1. **Corpus and extraction.** Records retrieved from Web of Science are screened by the authors; each full text is summarised into seven structured fields with GPT-4 Turbo (`gpt-4-turbo-2024-04-09`, temperature 0).
2. **Topic discovery.** BERTopic groups the 145 modelled documents into 15 topics (plus an outlier class); the domain expert consolidates them into five supertopics.
3. **Expert questions.** The expert formulates 42 research questions using the supertopics and topics as a scaffold; all authors review them.
4. **Document-grounded answers.** Each question is answered with Google NotebookLM over the source collection of its supertopic; the answers are condensed with GPT-4 Turbo and verified against the original publications.
5. **Assessment.** Five analyses evaluate the workflow: topic-to-question matrix (V1), document coverage (V2), traceability (V3), claim verification (V4) and evidence tables (T1, Q1), with a blind second rater on samples of V1, V2 and V4.

## Repository layout

| Path | Content |
|---|---|
| `data/corpus_manifest.csv` | All records (145 modelled + complementary search) with topic, supertopic, DOI, whether cited in the synthesis and citation key |
| `data/extraction_records.csv` | Bibliographic metadata and the seven GPT-4 Turbo extraction fields per modelled document |
| `data/topic_assignments.csv` | BERTopic topic, probability and supertopic(s) per document |
| `data/topics.csv` | The 15 topics and the outlier class: size, BERTopic name, LLM label, top words, supertopic(s) |
| `data/supertopic_source_collections.csv` | Documents in the NotebookLM source collection of each supertopic |
| `data/complementary_studies_topic_assignment.csv` | Seven FSO studies from the complementary search and their c-TF-IDF topic assignment |
| `questions/research_questions.csv` | The 42 expert research questions by supertopic |
| `synthesis/question_answers_2025-09-30.md` | Question-level answers (NotebookLM, condensed with GPT-4 Turbo) before verification |
| `prompts/` | Structured-extraction prompt (GPT-4 Turbo) and question-answering prompt (NotebookLM) |
| `notebooks/` | Extraction, BERTopic, post-processing and supertopic notebooks (outputs cleared) |
| `validation/` | Outputs of V1–V4, T1, Q1 and the complementary-study assignment |
| `validation/scripts/` | Python scripts that produce the validation outputs |
| `validation/second_rater/` | Blind second-rater judgments (A.L.-A.) for the V1, V2 and V4 samples; first-pass keys are in `validation/*_rater_key.csv` |

## What is not included and why

- **Full texts (PDFs)** of the reviewed articles are copyrighted. They can be retrieved through the DOIs in `data/corpus_manifest.csv`; the scripts expect them as `data/NNN.pdf` (files 001–125), `data2/NNN.pdf` (126–146) and `data_extra/` (complementary search), named by `file_id`.
- **Abstracts** exported from Web of Science are not redistributed, in line with its terms of use. The text supplied to BERTopic (title, abstract and extracted fields) can be rebuilt from the publications and `data/extraction_records.csv`.
- **NotebookLM notebooks** are not exportable; the source collections and the prompt are documented instead.
- **API keys** have been removed from the notebooks. Insert your own keys to run them.
- The fitted BERTopic model and the document embeddings (Cohere `embed-english-v3.0`, 1024 dimensions) were not preserved; the topic assignments are provided as data.

## Reproducing the validation

The scripts were written against the original working folder and take its root as the only argument:

```bash
python validation/scripts/01_build_manifest.py /path/to/working_folder
```

Requirements: Python 3.10+, `pandas`, `numpy`, `scikit-learn`, `openpyxl`, and `pdftotext` (Poppler) for the scripts that read full texts. Script `10_complementary_topics.py` reproduces the c-TF-IDF assignment of the complementary studies from `topics/topics_documents_0218.pkl` (topic-model output, not redistributed because it contains abstracts) and the texts of the seven studies.

Agreement between the first pass and the second rater: V1 weighted kappa 0.66 (95% CI 0.53–0.77), V2 kappa 0.50, V4 kappa 0.50 (0.24–0.74); see `validation/second_rater_summary.txt`.

## Licence

Code (`notebooks/`, `validation/scripts/`) is released under the MIT licence (`LICENSE`). Data, prompts and documentation are released under CC BY 4.0 (`LICENSE-DATA`). Bibliographic metadata belongs to the respective publishers.

## Citation

See `CITATION.cff`. Please cite the article and the archived dataset.

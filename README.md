# Supply-chain-stress-tester
Local Black Swan Stress-Tester is a privacy-first AI "flight simulator" for supply chains. Using Ollama and Monte Carlo simulations, it transforms qualitative disaster scenarios into quantitative risk metrics like TTS and VaR. By stress-testing a digital twin offline, it empowers companies to build data-driven resilience.
## Local Black Swan Stress-Tester
**Author:** Evan Steel

### Project Overview
The **Local Black Swan Stress-Tester** is a "flight simulator" for supply chain resilience. It addresses the inherent vulnerability of modern global trade to "Black Swan" events—unpredictable, high-impact disruptions like geopolitical conflicts, extreme weather, or global health crises. 

While traditional models are "braced for the average" by relying on historical data, this project uses **Offline Generative AI** to "hallucinate" scientifically plausible but extreme disruption scenarios. By integrating these AI-generated shocks with **Stochastic Monte Carlo simulations**, the system stress-tests a "digital twin" of the supply chain to quantify hidden risks through metrics like **Time-to-Survive (TTS)** and **Time-to-Recover (TTR)**.



---

### Technical Architecture
The system is built on a structural separation between qualitative "reasoned" chaos and quantitative mathematical execution:

* **The Chaos Engine (LLM + RAG):** Powered by **Ollama (Llama 3)**, this engine runs entirely offline to protect sensitive logistical data. It uses a **Retrieval-Augmented Generation (RAG)** pipeline—anchored by a local **ChromaDB** vector store—to ensure simulated crises are grounded in historical disruption patterns.
* **The Impact Engine (Python + NumPy/Pandas):** This engine ingests operational "ground truth" from the **DataCo Smart Supply Chain** dataset. It applies AI-generated "mutators" (such as lead-time multipliers) to baseline distributions, running **10,000-trial Monte Carlo simulations** to calculate **Value at Risk (VaR)** and optimal safety stock limits.

---

### How It Works
1.  **Baseline Generation:** The system calculates the mean and standard deviation of "normal" shipping days from the DataCo dataset.
2.  **Scenario Hallucination:** The user prompts the LLM (e.g., *"Simulate a 30-day regional conflict in Southeast Asia"*). The AI outputs a structured JSON profile containing disruption variables.
3.  **Stress Testing:** The Impact Engine inflates the operational variance (Sigma) based on the AI's multipliers, creating a "Stressed" vs. "Baseline" comparison.
4.  **Resilience Modeling:** The system applies a mitigation strategy (e.g., increased safety stock) to calculate a "Defended Sigma," empirically proving how much risk can be reduced.



---

### Key Features
* **Privacy-First AI:** Operates 100% offline via Ollama, ensuring proprietary shipping routes and financial secrets never leave the local environment.
* **Agentic Risk Analysis:** Moves beyond static reporting to active "what-if" forecasting.
* **Data-Driven Resilience:** Translates vague narratives into concrete KPIs (TTS, TTR, and VaR) to justify capital expenditure on safety stock.

### Tech Stack
* **Language:** Python
* **AI/ML:** Ollama (Llama 3), LangChain/LlamaIndex
* **Database:** ChromaDB (Vector Store)
* **Data Science:** NumPy, Pandas, Matplotlib
* **Environment:** Local/Offline (Privacy-Centric)

---

### Dataset References
* **DataCo Smart Supply Chain:** Provisioning, production, and sales data (180k+ records).
* **Global Supply Chain Disruption:** Historical memory of trade route shocks (10k+ records).

### Project File Directory

The **Local Black Swan Stress-Tester** is organized into logical modules that separate data establishmebt, AI scenario generation, and statistical simulation. Below is a description of the files included in this repository:

---

#### 📦 Core Logic & Simulations
* **`normal_sim.py`**: Establishes the operational "Ground Truth." It calculates baseline mean and standard deviation from the DataCo dataset and generates `baseline_results.csv`.
* **`stress_test_gen.py`**: The **"Chaos Engine."** Connects to the local Llama 3 model via Ollama to generate the qualitative disaster narrative and the structured `black_swan_profile.json`.
* **`stress_test_sim.py`**: The **"Impact Engine."** Ingests the AI’s disaster profile and applies multipliers to the baseline data to simulate supply chain failure.
* **`resilient_sim.py`**: Evaluates the defense strategy. It applies the risk reduction factors from `mitigation_strategy.json` to show how lead times stabilize under protected conditions.
* **`resilience_metrics.py`**: The analytical core. Calculates final KPIs like **Time-to-Survive (TTS)**, **Time-to-Recover (TTR)**, and **Value at Risk (VaR)**.
* **`supply.py`**: Utility script containing helper functions for data cleaning and loading the DataCo Smart Supply Chain dataset.

--- RUNNING 1000 MONTE CARLO TRIALS ---

--- FINAL RESULTS ---
Across 1,000 simulations, the average lead time is: 5.39 days
The worst-case average seen in a single trial was: 12.51 days

#### 📊 Data & Configuration (JSON/CSV)
* **`baseline_results.csv`**: Data showing standard, non-disrupted shipping performance.
* **`stress_results.csv`**: Data showing the chaotic lead-time swings during a Black Swan event.
* **`resilient_results.csv`**: Data showing the dampened, recovered lead times after applying mitigation strategies.
* **`black_swan_profile.json`**: The machine-readable output from the AI (e.g., event duration, delay multipliers).
* **`mitigation_strategy.json`**: User-defined parameters for how the system should defend against a crisis (e.g., safety stock levels).

#### 🛠️ Reporting & Infrastructure
* **`capstone_report.py`**: Consolidates results from all simulations to generate a final executive summary of the stress test findings.
* **`visualzation.py`**: Generates comparative plots (histograms and time-series) to visualize the "Resilience Gap" between baseline and stressed states.
* **`README.md`**: Project documentation, architecture overview, and setup instructions.



## File Structure Overview

| File | Description |
| :--- | :--- |
| **normal_sim.py** | Generates baseline operational data. |
| **stress_test_gen.py** | Uses Ollama to generate AI disaster scenarios. |
| **stress_test_sim.py** | Simulates the impact of the Black Swan event. |
| **resilient_sim.py** | Simulates the supply chain with mitigation active. |
| **resilience_metrics.py** | Calculates TTS, TTR, and VaR. |
| **visualzation.py** | Creates charts for Baseline vs. Stressed vs. Mitigated. |
| ***.json** | Configuration and AI-generated profiles. |
| ***.csv** | Output data from the various simulation stages. |

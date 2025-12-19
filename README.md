# 🎙️ Voice-First Telugu Government Scheme Agent

## 📌 Project Overview

This project presents a **voice-first, agentic AI system** built entirely in **Telugu**, designed to help users identify and understand **government and public welfare schemes** through natural voice interaction.

Unlike traditional chatbots, this system follows an **agent-based reasoning approach** that includes structured planning, tool usage, conversation memory, and robust failure handling. The solution focuses on **accessibility, reliability, and real-world usability**, especially for users who are not comfortable with English or text-based digital platforms.

---

## 🧠 Key Highlights

- 🎤 **Voice-first interaction** with Telugu voice input and output  
- 🌐 **End-to-end Telugu language pipeline**  
- 🤖 **Agentic workflow** using Planner–Tool–Evaluator design  
- 🧰 **Multiple tools** for grounded responses  
- 🧠 **Conversation memory across turns**  
- ⚠️ **Failure handling** for incomplete inputs, STT errors, and API quota limits  

---

## 🏗️ Project Structure
<p align="center">
  <img src="https://github.com/user-attachments/assets/158c3996-5e39-4c40-a2ad-051dbdb1986b"
       alt="CRED_RESOLVE Project Structure"
       width="400"/>
</p>

CRED_RESOLVE/
│
├── audios/                         # Telugu audio input samples
│   ├── a1.mp4
│   ├── a2.mp4
│   ├── a3.mp4
│   ├── a4.mp4
│   ├── a5.mp4
│   ├── a6.mp4
│   └── a7.mp4
│
├── audio_converter.py              # Converts audio to required format
├── SST_Telugu_Gemini.py            # Telugu Speech-to-Text using Gemini
│
├── llm_gemini_tools.py             # LLM + tool integration logic
├── llm_gemini_tools.ipynb          # Notebook for LLM testing & experiments
│
├── check_models.py                 # Checks available Gemini models
├── models_list.txt                 # List of supported / tested models
│
├── failure_mec.ipynb               # Failure mechanism & error handling analysis
│
└── voice agent.docx                # Project explanation & voice agent documentation



---

## ⚙️ Setup Instructions

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository

git clone <your-github-repository-link>
cd CRED_RESOLVE
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

**2️⃣ Create a Virtual Environment (Optional but Recommended)**
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

**3️⃣ Install Dependencies**
pip install -r requirements.txt

**4️⃣ Configure API Key**

Set your Gemini API key as an environment variable or inside the source files:

export GEMINI_API_KEY="your_api_key_here"

**▶️ How to Run the Notebook**

Launch Jupyter Notebook or Jupyter Lab:
jupyter notebook

Navigate to the notebooks/ directory.
Open the notebook:

failure_mec.ipynb
Run the notebook cell by cell from top to bottom.

The notebook demonstrates:
Telugu voice input processing
Failure detection and recovery
Conversation memory usage
Successful end-to-end agent responses

**🎧 Audio Usage**
Pre-recorded Telugu audio clips are used to simulate real user interactions:

Audio File	Scenario Demonstrated
a1.mp4	Incomplete request (failure case)
a2.mp4	Partial user information
a3.mp4	Memory usage across turns
a4.mp4	Near-complete information
a5.mp4	Successful end-to-end flow
The audio files are processed sequentially to simulate a multi-turn conversation with the agent.

**🗣️ Language Used**

Primary Language: Telugu
Telugu is used throughout the complete pipeline:
Voice Input
Speech-to-Text
Agent Reasoning
Tool Interaction
Text-to-Speech Output

No English-based reasoning is used during user interaction.


# Mistral Fine-Tuning & GGUF Export

**Personal AI Fine-Tuning Project**  
This repository contains my experiments in fine-tuning the Mistral language model on custom data and exporting the resulting model to GGUF format for efficient inference on local hardware (RTX 3060). Initiated October 2024 as part of my ongoing portfolio development.

---

## 📋 Table of Contents
- [🎯 Project Overview](#-project-overview)
- [🛠 Technologies](#-technologies)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [⚙️ Usage](#️-usage)
- [📂 Repository Structure](#-repository-structure)
- [✅ Results & Benchmarks](#-results--benchmarks)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [✉️ Contact](#️-contact)

---

### 🎯 Project Overview
A hands-on demonstration of:
1. **Fine-tuning** Mistral on my own dataset using Hugging Face Transformers.  
2. **Exporting** the trained model to GGUF for lightweight deployment with Ollama.  
3. **Automation scripts** in Python and Jupyter to streamline training and export workflows.  
This serves both as a learning exercise and as a showcase of my skills in model training, scripting, and efficient deployment.

### 🛠 Technologies
- **Python 3.10+** with `transformers`, `datasets`, `torch`
- **Jupyter Notebooks** for interactive EDA and model training
- **Ollama + GGUF** for model export and inference on local machine (RTX 3060)
- **Git & GitHub** for version control and portfolio presentation

### 🚀 Getting Started

#### Prerequisites
- GPU-equipped machine (NVIDIA RTX 3060) with CUDA drivers installed  
- Python 3.10+ environment  

#### Installation
1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/mistral-finetune-gguf-export.git
   cd mistral-finetune-gguf-export
   ```
   
2. **Create & activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   
3. **Run notebooks**
   - `train_app.ipynb` for fine-tuning
   - `export_to_gguf.ipynb` for GGUF export 

### ⚙️ Usage
- Fine-tuning: Open `train_app.ipynb`, adjust data paths and hyperparameters, then execute all cells.
- Exporting: Run `export_to_gguf.ipynb` to convert the saved model checkpoint to GGUF.
- Automation script: `save_model.py` can be invoked from the command line:

```bash
python save_model.py --model_dir ./output --format gguf
```

### 📂 Repository Structure
```bash
mistral-finetune-gguf-export/
├── train_app.ipynb      # Fine-tuning notebook
├── export_to_gguf.ipynb  # GGUF export notebook
├── save_model.py         # Script to save and export model
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and instructions
```

### ✅ Results & Benchmarks

After fine-tuning for ~10.8 epochs (475 steps) on my RTX 3060, the model achieved the following evaluation metrics:

- **Evaluation loss:** 1.5814  
- **Eval samples/sec:** 4.08  
- **Eval steps/sec:** 0.56  
- **Total runtime:** 19 min 15 s  
- **Training loss (final):** 0.0542  
- **Gradient norm (final):** 2.574  
- **Learning rate (final):** 1.255×10⁻⁶  

| Metric                     | Value                   |
|----------------------------|-------------------------|
| **Eval loss**              | 1.5814                  |
| **Eval runtime**           | 5.391 s                 |
| **Samples per second**     | 4.081                   |
| **Steps per second**       | 0.556                   |
| **Epochs completed**       | 10.80                   |
| **Global training steps**  | 475                     |
| **Final training loss**    | 0.0542                  |
| **Final gradient norm**    | 2.5739                  |
| **Final learning rate**    | 0.0000012550           |
| **Total runtime**          | 1155.95 s (~19 min 15 s) |

> **Note:** Metrics come directly from WandB logs (run step 37).  


### 🤝 Contributing
This is a personal portfolio project; pull requests are welcome but will be reviewed for alignment with the project’s scope. If you fork and adapt, please credit the original author.

### 📜 License
Distributed under the `MIT License`.

### 🙏 Acknowledgments
- Code structure and notebooks adapted from [brevdev/launchables](https://github.com/brevdev/launchables)
- Inspiration from best practices in README writing by Tom Preston-Werner and the GitHub Docs team 

### ✉️ Contact
- Name: Ezra H (1bytess)
- Email: project@ezrahernowo.com
- LinkedIn: [linkedin.com/in/ezrahernowo](www.linkedin.com/id/ezrahernowo)
- GitHub: github.com/1bytess

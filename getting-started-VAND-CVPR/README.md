# 🚀 Getting Started with MVTec AD 2 – VAND 2025 CVPR Challenge

Welcome to the official starter notebook and resources for the **Visual Anomaly and Novelty Detection (VAND) 2025 Challenge** at CVPR!

This repository is designed to help participants get up and running with the **MVTec AD 2** dataset using the [FiftyOne](https://voxel51.com/fiftyone) platform for dataset management, visualization, and evaluation. Whether you're an academic researcher or an industry practitioner, this challenge is your chance to contribute to the next generation of AI models for real-world anomaly detection.

---

## About the VAND 2025 Challenge

Hosted at **CVPR 2025**, the VAND Challenge is an initiative to push the boundaries of visual anomaly detection. Sponsored by **Voxel51**, **Intel**, and **MVTec**, this challenge brings together the best minds in computer vision to address real industrial use cases using modern techniques like **few-shot learning**, **Vision-Language Models (VLMs)**, and **robust feature extraction**.

🔗 [Challenge Registration & Info](https://voxel51.com/computer-vision-events/vand-3-0-challenge-at-cvpr-2025/)  
📅 Challenge Dates: April 7 – May 26, 2025  
📢 Results Announced: June 3, 2025  
💬 Join us on Discord: [FiftyOne Community](https://discord.com/invite/fiftyone-community) → `#cvpr-challenge-vand3-0`  
📂 Dataset: [MVTec AD 2](https://www.mvtec.com/company/research/datasets/mvtec-ad-2)

---

## Challenge Tracks

### Track 1: Adapt & Detect
Work with the newly released **MVTec AD 2** dataset featuring 8 object categories and multiple distribution shifts (e.g., lighting changes). Develop models that are **robust**, **adaptive**, and can detect **previously unseen anomalies** in challenging real-world conditions.

### Track 2: VLM Anomaly Challenge
Use the **MVTec LOCO AD** dataset to tackle logical and structural anomalies. This track encourages the use of **Vision-Language Models** and **few-shot techniques** to identify defects with minimal examples.

---

## What’s in this Repository?

- A complete `getting_started_mvtecad2.ipynb` notebook
  - Load and explore MVTec AD 2
  - Create custom FiftyOne datasets
  - Add segmentation masks
  - Group and visualize samples
  - Apply CLIP embeddings for dataset exploration
  - Export your dataset in FiftyOne format

- Tools used:
  - [FiftyOne](https://docs.voxel51.com/)
  - [OpenCV](https://opencv.org/)
  - [CLIP Model](https://github.com/openai/CLIP)
  - [UMAP](https://umap-learn.readthedocs.io/en/latest/)
  - Dataset utilities for structured loading and annotation

---

## Why Participate?

- Showcase innovative solutions to real-world anomaly detection challenges
- Collaborate with industry and research leaders
- Get access to high-quality datasets and tools
- Present your work at the VAND 2025 Workshop at CVPR
- Win prizes and gain visibility in the computer vision community

---

## How to Use this Notebook

1. Clone the repository and install the required dependencies
2. Download the [MVTec AD 2 dataset](https://www.mvtec.com/company/research/datasets/mvtec-ad-2)
3. Update the dataset path in the notebook
4. Follow the cells step-by-step to:
   - Visualize the dataset
   - Build your FiftyOne samples
   - Apply grouping and embeddings
   - Export your dataset

---

## Contribute

If you build something cool with this notebook or dataset, please consider sharing it on the FiftyOne community Discord or submitting a pull request!

---

Let's build better anomaly detection together. 💥

— Team Voxel51 | Anomalib | MVTec
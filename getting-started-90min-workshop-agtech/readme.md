# 🌱 Getting Started with FiftyOne for AgTech

Welcome to this hands-on computer vision workshop using [FiftyOne](https://voxel51.com/fiftyone), the open-source tool for visualizing, curating, and improving datasets for AI. Together, we’ll explore data-centric workflows with a real-world **Colombian coffee beans dataset**—straight from the mountains to the model!

---

## 🎯 Workshop Objectives

By the end of this session, you will:
- Understand the role of **data-centric AI** in agricultural technologies
- Learn to **load and explore** annotated image datasets in FiftyOne
- Apply **prompt-based segmentation** using SAM2 (Segment Anything Model)
- Evaluate **visual uniqueness and similarity** in your dataset
- Use **FiftyOne plugins and dashboards** for deeper insights

---

## 🍒 Dataset Overview: Colombian Coffee Beans

This unique dataset was captured in Colombia’s coffee regions. It contains:
- Over **1,500 images** of coffee tree branches
- **Instance segmentation masks** (COCO format) for:
  - `immature`
  - `mature`
  - `overmature` beans
- Real-world variation in lighting, occlusion, and maturity stages

---

## 🧪 Workshop Notebooks

Each notebook builds progressively through a 90-minute hands-on experience.

### 1️⃣ `notebook1_GS_AgTec.ipynb` – Loading, Filtering & Exploring Coffee Beans Data
Learn to:
- Load a real-world agricultural dataset from Hugging Face into FiftyOne
- Visualize segmentation masks and metadata using the FiftyOne App
- Filter and query data using labels, metadata, and confidence thresholds
- Clone views, export filtered subsets, and compute image uniqueness
- Explore dataset similarity and enable insights using plugins and embeddings

### 2️⃣ `notebook2_GS_AgTec.ipynb` – Enhancing Dataset Quality with SAM2
Learn to:
- Apply the SAM2 segmentation model from the FiftyOne Model Zoo
- Automatically label coffee fruit instances using bounding box prompts
- Identify and filter visually unique samples to optimize annotation
- Use embedding-based similarity to match and auto-label instances
- Clean and export high-quality subsets in COCO, CVAT, or FiftyOne format

### 3️⃣ `notebook3_GS_AgTec.ipynb` – Evaluating Models with FiftyOne
Learn to:
- Load a curated coffee dataset and visualize it in the FiftyOne App
- Run inference using Intel Geti SDK models (before/after dataset curation)
- Convert polygon annotations into instance segmentations with masks
- Visualize and compare predictions from different models
- Use the Model Evaluation Plugin or SDK to compute COCO-style metrics

### 4️⃣ `notebook4_GS_AgTec.ipynb` – Dataset Loading & Geolocation Exploration
Learn to:
- Load the Colombian coffee dataset using FiftyOne and Hugging Face integration
- Visualize segmentation masks and inspect dataset structure in the FiftyOne App
- Assign and explore geolocation metadata using a CSV of tree coordinates
- Analyze and visualize coffee bean maturation stages with custom metadata
- Use the Plotly Map Plugin for interactive, map-based exploration of spatial trends

---

## 🔧 Installation

Ensure your Python environment includes:

```bash
# ✅ Core environment setup
pip install --upgrade pip wheel setuptools
pip install fiftyone
pip install umap-learn>=0.5
pip install opencv-python-headless
pip install pandas
pip install "huggingface_hub>=0.20.0"
pip install geti-sdk

# ✅ SAM2 (Segment Anything v2)
git clone https://github.com/facebookresearch/sam2.git && cd sam2 && pip install -e . && cd ..

# ✅ FiftyOne Plugins
fiftyone plugins download https://github.com/allenleetc/plotly-map-panel
fiftyone plugins download https://github.com/voxel51/fiftyone-plugins --plugin-names @voxel51/evaluation

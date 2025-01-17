# Model Evaluation for Human Action Recognition with FiftyOne

This notebook walks you through the process of evaluating machine learning models for human action recognition, using the FiftyOne open-source tool. Whether you're participating in the **Elderly Action Recognition Challenge** or exploring action recognition for the first time, this notebook provides an interactive and insightful approach to model evaluation.

The notebook leverages [FiftyOne](https://voxel51.com/) to streamline dataset preparation, including importing, parsing actions, assigning categories, splitting videos into clips, and exporting datasets.

---

## Challenge Overview

The **Elderly Action Recognition Challenge** focuses on identifying Activities of Daily Living (ADLs) and fall detection for the elderly. Participants are encouraged to contribute models that address real-world healthcare challenges and assistive living scenarios.

- **Challenge Page**: [Details & Instructions](https://voxel51.com/computer-vision-events/elderly-action-recognition-challenge-wacv-2025/)
- **Submission Platform**: [Submit Here](https://eval.ai/web/challenges/challenge-page/2427/overview)
- **Discord Channel**: [Join the Discussion](https://discord.com/channels/1266527359511564372/1319053378843836448)

---

## Notebook Contents

### 1. **Notebook: `HAR_model_evaluation.ipynb`**
This notebook walks you through:
- How to import and manage datasets with FiftyOne.
- Visualize and analyze predictions alongside ground truth labels.
- Evaluate model performance using metrics and confusion matrices.
- Explore advanced features like bias detection and explainability.
- Streamline your AI/ML workflows for computer vision tasks.

### 2. **Notebook Dataset and model**
We use the [UFC-100 Dataset](https://www.crcv.ucf.edu/wp-content/uploads/2019/03/UCF101_CRCV-TR-12-01.pdf) in this notebook, which is designed for human action recognition. We integrate a pre-trained VideoMAE model from Hugging Face fine-tuned on UCF101 to demonstrate real-world use cases. Here is the model we used [sayakpaul/videomae-base-finetuned-kinetics-finetuned-ucf101-subset](https://huggingface.co/sayakpaul/videomae-base-finetuned-kinetics-finetuned-ucf101-subset)

### 3. **Resources**
- [FiftyOne Documentation](https://docs.voxel51.com/)
- [UFC-101 Dataset](https://www.crcv.ucf.edu/wp-content/uploads/2019/03/UCF101_CRCV-TR-12-01.pdfs)
- [Finetuned UCF-101-subset Model](https://huggingface.co/sayakpaul/videomae-base-finetuned-kinetics-finetuned-ucf101-subset)

---

## Prerequisites

### 1. Install Dependencies
Make sure you have Python 3.8 or higher installed, and als have a Python Environment in yout system. For beginners, take a look of these [instructions](https://github.com/voxel51/fiftyone-examples?tab=readme-ov-file#-prerequisites-for-beginners-)

Then, install the jupyter lab or run this notebook using VS Code
```bash
pip install jupyterlab
pip install -U transformers torch
```
---

## Usage

1. Open the notebook:
```bash
jupyter HAR_model_evaluation.ipynb
```

2. Follow the steps in the notebook:

- Install FiftyOne, Hugging Face Transformers, and other dependencies.
- Use FiftyOne’s Data Zoo to import the UCF101 dataset.
- Re-encode videos to ensure compatibility with the FiftyOne app.
- Load the pre-trained VideoMAE model from Hugging Face.
- Compare model predictions with ground truth labels.
- Calculate evaluation metrics, including accuracy and precision.
- Generate and explore an interactive confusion matrix.
- Use FiftyOne’s evaluation panel to debug and refine model predictions.

3. Launch the FiftyOne App to interact with and visualize your dataset:
```bash
session = fo.launch_app(dataset)
```

---

## Output Formats

- Visual and report-based

Summary Card:
![Image](https://github.com/user-attachments/assets/4491333b-39d5-47eb-a37b-60827f867f2d)

Metric Performance Card:
![Image](https://github.com/user-attachments/assets/17702e31-0a95-43b8-89a8-48c4705a301f)

Class performance Card:
![Image](https://github.com/user-attachments/assets/e0ab993a-b5f2-4ff5-8e4f-a770d98da42a)

Confusion Matrix Card:
![Image](https://github.com/user-attachments/assets/31c08f43-4377-4aff-86ea-23063bbaf67f)

---

## Contributing
We welcome contributions to improve the notebook or add new features! Including Model Training, Model Evaluation. Please submit a pull request or open an issue with your suggestions.

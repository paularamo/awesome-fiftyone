# **Video Embeddings with FiftyOne: Potential use in the Elderly Action Recognition Challenge**

This section of the repository contains a Jupyter notebook for the **Elderly Action Recognition Challenge**, where participants will generate and visualize video embeddings for action recognition tasks using **FiftyOne** and the **Hiera Video Embeddings plugin**. The notebook guides users through the process of preparing the dataset, computing embeddings, and visualizing them for analysis.

---

## **Overview**

The **Elderly Action Recognition Challenge** is focused on improving action recognition systems tailored to elderly individuals, with applications in healthcare and elderly care. This notebook demonstrates how to use **FiftyOne** for creating video embeddings. You will learn to:

- Load and manage datasets.
- Compute video embeddings using the **Hiera Video Embeddings Plugin**.
- Visualize embeddings using dimensionality reduction (UMAP).
- Analyze video embeddings for the challenge.

---

## **Requirements**

Before running the notebook, make sure you have the following:

1. **Python Environment**  
   Set up a Python environment if you haven’t already. For instructions on creating a virtual environment, refer to the [prerequisites guide](https://github.com/voxel51/fiftyone-examples?tab=readme-ov-file#-prerequisites-for-beginners-).

2. **Install Dependencies**  
   Install **FiftyOne** and other necessary packages for dataset management and visualization:
   ```bash
   pip install fiftyone umap-learn huggingface-hub ipywidgets

3. **Hiera Video Embeddings Plugin**  
   The Hiera Video Embeddings Plugin is required for computing video embeddings. This plugin enables efficient computation of embeddings using pretrained models. To install the plugin, follow the instructions in the notebook.

---

## **Running the Notebook**

### **1. Load the Dataset**  
The notebook loads the dataset from Hugging Face using the `load_from_hub()` function. The dataset `"Voxel51/GMNCSA24-FO"` is used for video action recognition.

### **2. Install and Set Up the Plugin**  
The **Hiera Video Embeddings Plugin** is installed and configured to compute embeddings for video. A delegated service needs to be launched to handle long-running tasks like embedding computation.

### **3. Compute and Visualize Embeddings**  
The notebook demonstrates how to compute video embeddings using two models: `hiera_base_16x224` and `hiera_base_plus_16x224`. The embeddings are visualized using **UMAP** (Uniform Manifold Approximation and Projection), which reduces the dimensionality of the embeddings for easier visualization and analysis.

### **4. Visualization and Analysis**  
The **FiftyOne Brain** module is used to compute visualizations of the embeddings, making it easier to explore relationships between video data. The results can be explored interactively using the **FiftyOne App**.

---

## **Key Features**

- **FiftyOne Platform**: An open-source project designed to streamline the workflow of visual AI projects., ideal for computer vision tasks like video action recognition.
- **Hiera Video Embeddings Plugin**: A plugin for generating embeddings from video data, which can then be analyzed and visualized.
- **UMAP Visualization**: A method for dimensionality reduction, enabling easy inspection of video embeddings. Use the one of your preference or your  own embeddings model. 
- **Delegated Service**: Ensures efficient computation of embeddings.

---

## **Resources**

- [Elderly Action Recognition Challenge Overview](https://voxel51.com/computer-vision-events/elderly-action-recognition-challenge-wacv-2025/)
- [FiftyOne Documentation](https://docs.voxel51.com/)
- [Hiera Video Embeddings Plugin](https://github.com/harpreetsahota204/hiera-video-embeddings-plugin)

---

## **License**

This project is licensed under the MIT License.

# FiftyOne + Mosaic AI Vector Search: Visual Search at Scale

This awesome-fiftyone folder contains a Jupyter notebook that demonstrates how to integrate **FiftyOne** with **Databricks Mosaic AI Vector Search** to enable powerful visual similarity search over image datasets. 

## Overview

As AI evolves beyond classification and detection tasks, the next frontier is **semantic understanding and retrieval** — especially for visual data.

**Vector search** allows you to:

- Represent complex visual features as embeddings
- Index large-scale datasets in milliseconds
- Perform similarity queries (by image, text, or numerical approach)
- Visualize embedding space structure
- Power content discovery, deduplication, recommendation, and anomaly detection

### Why It Matters

In the era of Foundation Models, Vision Transformers, and Multi-modal AI, vector search is becoming **the essential retrieval layer**. It enables workflows where models and humans can **search by meaning** rather than metadata.

This notebook showcases how to bring this future into practice using:
- [FiftyOne](https://voxel51.com/fiftyone) for dataset curation and visualization
- [Mosaic AI Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search) to scale similarity search
- CLIP-based embeddings for semantic feature representation

---

## Notebook Highlights

- Authenticate with Databricks and set up your workspace
- Load the `quickstart` dataset in FiftyOne
- Generate image embeddings using CLIP
- Create a **Direct Access Index** in Databricks - FiftyOne manages this for you.
- Query with image ID, similarity index or natural language prompts
- Visualize embeddings in FiftyOne's Embeddings Panel
- Clean up your index and brain keys

---

## Requirements

- Databricks account with Mosaic AI Vector Search enabled
- A vector search endpoint and catalog + schema set up
- Python environment with:
  ```bash
  pip install fiftyone databricks-sdk databricks-vectorsearch mlflow umap-learn
  ```

---

## Files

- `fiftyone_mosaic_full_setup_finalipynb`: Full working notebook
- `README.md`: This file

---

## Future Extensions

- Use your own image dataset
- Extend to patch-level embeddings (objects)
- Combine with zero-shot classification or captioning
- Plug into LLM-powered visual search flows

---

## Acknowledgments

Created by Paula Ramos, with valuable support and collaboration from Tom Schmidt and Prerna Dhareshwar.  

For more on FiftyOne + Vector Search: [Voxel51 Docs](https://docs.voxel51.com/integrations/mosaic.html)

---


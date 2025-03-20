"""
cubes dataset.
Apache2.0 License
Author: Paula Ramos
"""
import os
import shutil

import fiftyone as fo


def download_and_prepare(dataset_dir, split=None, **kwargs):
    """Downloads the dataset and prepares it for use with FiftyOne."""
    
    # Example: Download a dataset from a URL
    # You can use requests, wget, or other methods to retrieve data
    import os
    import fiftyone as fo
    
    if split:
        dataset_path = os.path.join(dataset_dir, split)
    else:
        dataset_path = dataset_dir
    
    # Simulating dataset preparation
    os.makedirs(dataset_path, exist_ok=True)
    
    # Define dataset type
    dataset_type = fo.types.ImageClassificationDirectoryTree
    
    # Example number of samples (adjust based on actual dataset)
    num_samples = 188
    
    # Optionally define classes
    classes = ["abnormal", "normal"]
    
    return dataset_type, num_samples, classes


def load_dataset(dataset, dataset_dir, split=None, **kwargs):
    """Loads the dataset into FiftyOne."""
    
    import fiftyone as fo
    from fiftyone import Sample
    from fiftyone.core.labels import Classification
    import os
    
    # Example: Load image paths and labels
    samples = []
    for img_path in os.listdir(dataset_dir):
        if img_path.endswith(".jpg") or img_path.endswith(".png"):
            filepath = os.path.join(dataset_dir, img_path)
            label = "abnormal" if "abnormal" in img_path else "normal"
            sample = Sample(filepath=filepath, 
                            ground_truth=Classification(label=label))
            samples.append(sample)
    
    # Add samples to dataset
    dataset.add_samples(samples)

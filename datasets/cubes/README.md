# COCO-2017

COCO is a large-scale object detection, segmentation, and captioning
dataset.

This version contains images, bounding boxes, and segmentations for the 2017
version of the dataset.

## Notes

-   COCO defines 91 classes but the data only uses 80 classes
-   Some images from the train and validation sets don't have annotations
-   The test set does not have annotations
-   COCO 2014 and 2017 use the same images, but the splits are different

## Details

-   Dataset name: ``voxel51/coco-2017``
-   Dataset source: http://cocodataset.org/#home
-   Dataset size: 25.20 GB
-   Tags: ``image, detection, segmentation``
-   Supported splits: ``train, validation, test``

## Full split stats

-   Train split: 118,287 images
-   Test split: 40,670 images
-   Validation split: 5,000 images

## Partial downloads

FiftyOne provides parameters that can be used to efficiently download specific
subsets of the COCO dataset to suit your needs. When new subsets are specified,
FiftyOne will use existing downloaded data first if possible before resorting
to downloading additional data from the web.

The following parameters are available to configure a partial download of
COCO-2017 by passing them to
[load_zoo_dataset()](https://docs.voxel51.com/api/fiftyone.zoo.datasets.html#fiftyone.zoo.datasets.load_zoo_dataset):

-   **split** (*None*) and **splits** (*None*): a string or list of strings,
    respectively, specifying the splits to load. Supported values are
    ``("train", "test", "validation")``. If neither is provided, all available
    splits are loaded

-   **label_types** (*None*): a label type or list of label types to load.
    Supported values are ``("detections", "segmentations")``. By default, only
    detections are loaded

-   **classes** (*None*): a string or list of strings specifying required
    classes to load. If provided, only samples containing at least one instance
    of a specified class will be loaded

-   **image_ids** (*None*): a list of specific image IDs to load. The IDs can
    be specified either as ``<split>/<image-id>`` strings or ``<image-id>``
    ints of strings. Alternatively, you can provide the path to a TXT
    (newline-separated), JSON, or CSV file containing the list of image IDs to
    load in either of the first two formats

-   **include_id** (*False*): whether to include the COCO ID of each sample in
    the loaded labels

-   **include_license** (*False*): whether to include the COCO license of each
    sample in the loaded labels, if available. The supported values are:

    -   ``"False"`` (default): don't load the license
    -   ``True``/``"name"``: store the string license name
    -   ``"id"``: store the integer license ID
    -   ``"url"``: store the license URL

-   **only_matching** (*False*): whether to only load labels that match the
    ``classes`` or ``attrs`` requirements that you provide (True), or to load
    all labels for samples that match the requirements (False)

-   **num_workers** (*None*): the number of processes to use when downloading
    individual images. By default, `multiprocessing.cpu_count()` is used

-   **shuffle** (*False*): whether to randomly shuffle the order in which
    samples are chosen for partial downloads

-   **seed** (*None*): a random seed to use when shuffling

-   **max_samples** (*None*): a maximum number of samples to load per split. If
    ``label_types`` and/or ``classes`` are also specified, first priority will
    be given to samples that contain all of the specified label types and/or
    classes, followed by samples that contain at least one of the specified
    labels types or classes. The actual number of samples loaded may be less
    than this maximum value if the dataset does not contain sufficient samples
    matching your requirements

## Example usage

```py
import fiftyone as fo
import fiftyone.zoo as foz

#
# Load 50 random samples from the validation split
#
# Only the required images will be downloaded (if necessary).
# By default, only detections are loaded
#

dataset = foz.load_zoo_dataset(
    "https://github.com/voxel51/coco-2017",
    split="validation",
    max_samples=50,
    shuffle=True,
)

session = fo.launch_app(dataset)

#
# Load segmentations for 25 samples from the validation split that
# contain cats and dogs
#
# Images that contain all `classes` will be prioritized first, followed
# by images that contain at least one of the required `classes`. If
# there are not enough images matching `classes` in the split to meet
# `max_samples`, only the available images will be loaded.
#
# Images will only be downloaded if necessary
#

dataset = foz.load_zoo_dataset(
    "https://github.com/voxel51/coco-2017",
    split="validation",
    label_types=["segmentations"],
    classes=["cat", "dog"],
    max_samples=25,
)

session.dataset = dataset

#
# Download the entire validation split and load both detections and
# segmentations
#
# Subsequent partial loads of the validation split will never require
# downloading any images
#

dataset = foz.load_zoo_dataset(
    "https://github.com/voxel51/coco-2017",
    split="validation",
    label_types=["detections", "segmentations"],
)

session.dataset = dataset
```

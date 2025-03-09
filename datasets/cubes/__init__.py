"""
COCO-2017 dataset.

| Copyright 2017-2024, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
import os
import shutil

import fiftyone as fo
import fiftyone.utils.coco as fouc


def download_and_prepare(
    dataset_dir,
    split=None,
    label_types=None,
    classes=None,
    image_ids=None,
    num_workers=None,
    shuffle=False,
    seed=None,
    max_samples=None,
):
    """Downloads the specified split of the dataset and prepares it for loading
    into FiftyOne.

    Args:
        dataset_dir: the directory in which to construct the dataset
        split (None): a split to download. The supported values are
            ``("train", "validation", "test")``
        label_types (None): a label type or list of label types to download.
            The supported values are ``("detections", "segmentations")``. By
            default, only "detections" are downloaded
        classes (None): a string or list of strings specifying required classes
            to download. If provided, only samples containing at least one
            instance of a specified class will be downloaded
        image_ids (None): an optional list of specific image IDs to download.
            Can be provided in any of the following formats:

            -   a list of ``<image-id>`` ints or strings
            -   a list of ``<split>/<image-id>`` strings
            -   the path to a text (newline-separated), JSON, or CSV file
                containing the list of image IDs to load in either of the first
                two formats
        num_workers (None): a suggested number of threads to use when
            downloading individual images
        shuffle (False): whether to randomly shuffle the order in which samples
            are chosen for partial downloads
        seed (None): a random seed to use when shuffling
        max_samples (None): a maximum number of samples to download per split.
            If ``label_types`` and/or ``classes`` are also specified, first
            priority will be given to samples that contain all of the specified
            label types and/or classes, followed by samples that contain at
            least one of the specified labels types or classes. The actual
            number of samples downloaded may be less than this maximum value if
            the dataset does not contain sufficient samples matching your
            requirements. By default, all matching samples are downloaded

    Returns:
        a tuple of

        -   ``dataset_type``: None
        -   ``num_samples``: the number of downloaded samples for the split
        -   ``classes``: the list of classes in the dataset
    """
    split_dir = os.path.join(dataset_dir, split)
    raw_dir = os.path.join(dataset_dir, "raw")
    scratch_dir = os.path.join(dataset_dir, "tmp-download")

    dataset_type = None
    num_samples, classes, _ = fouc.download_coco_dataset_split(
        split_dir,
        split,
        year="2017",
        label_types=label_types,
        classes=classes,
        image_ids=image_ids,
        num_workers=num_workers,
        shuffle=shuffle,
        seed=seed,
        max_samples=max_samples,
        raw_dir=raw_dir,
        scratch_dir=scratch_dir,
    )

    shutil.rmtree(scratch_dir, ignore_errors=True)

    return dataset_type, num_samples, classes


def load_dataset(
    dataset,
    dataset_dir,
    split=None,
    label_types=None,
    classes=None,
    image_ids=None,
    shuffle=False,
    seed=None,
    max_samples=None,
):
    """Loads the specified split of the dataset into FiftyOne.

    Args:
        dataset: a :class:`fiftyone.core.dataset.Dataset` to which to import
        dataset_dir: the directory to which the dataset was downloaded
        split (None): a split to load. The supported values are
            ``("train", "validation", "test")``
        label_types (None): a label type or list of label types to load. The
            supported values are ``("detections", "segmentations")``. By
            default, only "detections" are loaded
        classes (None): a string or list of strings specifying required classes
            to load. If provided, only samples containing at least one instance
            of a specified class will be loaded
        image_ids (None): an optional list of specific image IDs to load. Can
            be provided in any of the following formats:

            -   a list of ``<image-id>`` ints or strings
            -   a list of ``<split>/<image-id>`` strings
            -   the path to a text (newline-separated), JSON, or CSV file
                containing the list of image IDs to load in either of the first
                two formats
        shuffle (False): whether to randomly shuffle the order in which samples
            are chosen for partial loads
        seed (None): a random seed to use when shuffling
        max_samples (None): a maximum number of samples to load per split. If
            ``label_types`` and/or ``classes`` are also specified, first
            priority will be given to samples that contain all of the specified
            label types and/or classes, followed by samples that contain at
            least one of the specified labels types or classes. The actual
            number of samples loaded may be less than this maximum value if the
            dataset does not contain sufficient samples matching your
            requirements. By default, all matching samples are loaded
    """
    split_dir = os.path.join(dataset_dir, split)
    dataset.add_dir(
        split_dir,
        dataset_type=fo.types.COCODetectionDataset,
        label_types=label_types,
        classes=classes,
        image_ids=image_ids,
        shuffle=shuffle,
        seed=seed,
        max_samples=max_samples,
    )

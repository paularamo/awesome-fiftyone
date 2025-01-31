#https://docs.voxel51.com/integrations/lightning_flash.html
from itertools import chain

from flash import Trainer
from flash.core.data.utils import download_data
from flash.image import SemanticSegmentation, SemanticSegmentationData
from flash.image.segmentation.output import FiftyOneSegmentationLabelsOutput

import fiftyone as fo
import fiftyone.zoo as foz

# 1 Load your FiftyOne dataset

# source: https://www.kaggle.com/kumaresanmanickavelu/lyft-udacity-challenge
download_data(
    "https://github.com/ongchinkiat/LyftPerceptionChallenge/releases/download/v0.1/carla-capture-20180513A.zip",
    "/tmp/carla_data/",
)

dataset = fo.Dataset.from_dir(
    dataset_dir="/tmp/carla_data",
    dataset_type=fo.types.ImageSegmentationDirectory,
    data_path="CameraRGB",
    labels_path="CameraSeg",
    force_grayscale=True,
    shuffle=True,
)

# Just test and val on train dataset for this example
predict_dataset = dataset.take(5)

# 2 Create the Datamodule
datamodule = SemanticSegmentationData.from_fiftyone(
    train_dataset=dataset,
    test_dataset=dataset,
    val_dataset=dataset,
    predict_dataset=predict_dataset,
    label_field="ground_truth",
    transform_kwargs=dict(image_size=(256, 256)),
    num_classes=21,
    batch_size=4,
)

# 3 Build the model
model = SemanticSegmentation(
    backbone="mobilenetv3_large_100",
    head="fpn",
    num_classes=datamodule.num_classes,
)

# 4 Create the trainer
trainer = Trainer(
    max_epochs=1, limit_train_batches=10, limit_val_batches=5
)

# 5 Finetune the model
trainer.finetune(model, datamodule=datamodule, strategy="freeze")

# 6 Save it!
trainer.save_checkpoint("/tmp/semantic_segmentation_model.pt")

# 7 Generate predictions
predictions = trainer.predict(
    model,
    datamodule=datamodule,
    output=FiftyOneSegmentationLabelsOutput(),
)
predictions = list(chain.from_iterable(predictions))  # flatten batches

# Map filepaths to predictions
predictions = {p["filepath"]: p["predictions"] for p in predictions}

# Add predictions to FiftyOne dataset
dataset.set_values(
    "flash_predictions", predictions, key_field="filepath",
)

# 8 Analyze predictions in the App
session = fo.launch_app(predict_dataset)

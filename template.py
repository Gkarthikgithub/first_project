import os
from pathlib import Path
import logging

list_of_files=[

    "github/workflows/.gitkeep",
    "src/__init__.py"
    "src/components/__init__.py",
    "src/components/data_ingestion.py"
    "src/components/data_transformation.py",
    "src/component/model_trainer.py",
    "src/component/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py"
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiment.ipynb"


]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==00):
        with open (filepath,"w") as f:
            pass #create an empty file
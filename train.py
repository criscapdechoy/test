import os

# import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# from elektra.prediction import constants

input_dir = "/opt/ml/input"
output_dir = "/opt/ml/output"
model_dir = "/opt/ml/model"

# client = boto3.client("s3")

bucket = "holaluz-apps"
model_dir_s3 = "elektra/staging/data/sagemaker/data/model/model.txt"

# we're arbitrarily going to iterate through 5 epochs here, a real algorithm
# may choose to determine the number of epochs based on a more realistic
# convergence criteria
num_epochs = 5
channel_name = "training"
terminated = False


# The function to execute the training.
def train():
    # logger.info("Des d'elektra")
    # # z    logger.info(f"holi holi ja funciona...{constants.no_tm_input_table}")
    # logger.info("\nStarting the training.")
    # with open(os.path.join(model_dir, "model.txt"), "w") as f:
    #     f.write("dummy model params")

    # print("uploading model data to s3")
    # # client.upload_file(os.path.join(model_dir, "model.txt"), bucket, model_dir_s3)
    print("Training completed.")


if __name__ == "__main__":
    # As per the SageMaker container spec, the algo takes a 'train' parameter.
    # We will simply ignore this in this dummy implementation.
    print(f"Working_dir: {os.getcwd()}")
    print(f"Directories in dir: {os.listdir()}")
    print("patata")
    train()

import os
# The function to execute the training.
def train():

    print("Training completed.")


if __name__ == "__main__":
    # As per the SageMaker container spec, the algo takes a 'train' parameter.
    # We will simply ignore this in this dummy implementation.
    print(f"Working_dir: {os.getcwd()}")
    print(f"Directories in dir: {os.listdir()}")
    print("patata")
    train()

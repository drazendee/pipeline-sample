from valohai import Pipeline
  
def main(config) -> Pipeline:

    #Create a pipeline called "training-pipeline".
    pipe = Pipeline(name="training-pipeline", config=config)

    # Define the pipeline nodes.
    generate = pipe.execution("generate-data")
    train = pipe.execution("train")
    test = pipe.execution("test")

    # Configure the pipeline, i.e. define the edges.

    # From generate-data to train
    generate.output("train_data.pth").to(train.input("train-dataset"))
    generate.output("test_data.pth").to(train.input("test-dataset"))

    # From generate-data to test
    generate.output("test_data.pth").to(test.input("test-dataset"))

    # From train to test
    train.output("*").to(test.input("model"))

    return pipe
# Environment notes:
To add CUDA version of torch for poetry, we need to create a custom source for the CUDA wheel.
    ```
    poetry source remove --priority=explicit torch-gpu https://download.pytorch.org/whl/cu126
    ```
Then add these libraries to the environment by doing:
    ```
    poetry add --source pytorch-gpu torch torchvision torchaudio
    ```
TODO:
Make the chunking for tokenizer sentiment analysis.
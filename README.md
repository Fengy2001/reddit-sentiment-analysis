# Environment notes:
To add CUDA version of torch for poetry, we need to create a custom source for the CUDA wheel.
    ```
    poetry source remove --priority=explicit torch-gpu https://download.pytorch.org/whl/cu126
    ```
Then add these libraries to the environment by doing:
    ```
    poetry add --source pytorch-gpu torch torchvision torchaudio
    ```

# TODO:
Make the streamlit widget to display the analyzed sentiment of the sentence, then EDA on what the distribution is. If the distribution is bad, consider using a different LLM for more variability in the values.

    Issue 1: Streamlit and pytorch does not work well together for async related functions. May need to look into turning this purely into a backend and design/find another front end interactive data dashboard.
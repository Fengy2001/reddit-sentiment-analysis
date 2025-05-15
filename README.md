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

    Issue 1: Streamlit and pytorch does not work well together for async related functions. May need to look into turning this purely into a backend and design/find another front end interactive data dashboard. _(Addendum) This issue is **low priority** since the main focus of the dashboard is just to visualize the data found. This will be revisited when the concept shows promise_

    Issue 2: Need to change reddit comment retrieval to start at the oldest comment id recieved. Otherwise wasted API calls grab the exact same 100~ comments over and over again. **Medium priority**.

# Notes:
May need to experiment with different sentiment analysis models, "yiyanghkust/finbert-tone" seems to be too strict with what it considers "positive" or "negative" sentiment, labelling most to neutral. The data then presented doesn't seem appealing to analyze.
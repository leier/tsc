
## Welcome to the Time Series Challenge documentation!

---

This is a time series analysis project, which helps analyzing gaps, finding segments in the time series as well as seasonalities and trends.
As an output modelled segments are given, which one can use to fill gaps, or extrapolate the time series within reason.

Please check the notebook 'notebooks/01_Time_Series_Challenge.ipynb' containing documentation in markdown.
The Sphinx Docs give some additional information. However, since we rely on public libraries mostly, the overall software development setup was not used quite the way it could have in a more advanced project. Docstring is however used in the very few function added to utils.

I am not familiar with Sphinx and spent considerable time to get it running, but among other problems autodoc and doctest do not seem to run nicely together. If I may give an unsolicited advice: the following tools are good alternatives to Sphinx: Swagger UI, PDoc3 or MkDocs. I proceed by using markdown in the notebook 01_Time_Series_Challenge.ipynb in the notebook folder.

In the notebook we focus on missing data in a temperature time series of non-equidistant datapoints. 
The dataset - as we will find out - comes with one two categorical features, one of which contains useful information for the analysis.

Outline of the analysis:<br>
1. Package imports and loading data
2. Quick Insights in the dataset
3. Daily, Hourly Seasonalities and Time Differences
4. Hierarchical Clustering for Segmentation
5. Modeling of Time Series Segments
6. Final Remarks

![Time Series Segments](https://github.com/leier/tsc/blob/main/docs/build/html/_images/heating_clusters.png)

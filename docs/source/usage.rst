Usage
----------------

.. _installation:

Installation
----------------

Not yet in an installable version. Just check content for now.



First function:

.. py:function:: utils.fancy_dendrogram(*args, **kwargs)

   Return a dictionary of data structures computed to render the dendrogram.

   :param Z: the linkage matrix encoding the hierarchical clustering to render as a dendrogram
   :type Z: ndarray
   :param ylim: upper limit to plot
   :param p: parameter for truncate mode
   :return: list of dendogram objects to render dendrogram
   :rtype: dict 
def fancy_dendrogram(*args, **kwargs):
    """
    Return a dictionary of data structures computed to render the dendrogram.

    :param Z: the linkage matrix encoding the hierarchical clustering to render as a dendrogram
    :type Z: ndarray
    :param ylim: upper limit to plot
    :param p: parameter for truncate mode
    :return: list of dendogram objects to render dendrogram
    :rtype: dict
    """
    from scipy.cluster.hierarchy import dendrogram
    ylim=10000
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)
    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            yy = d[1]
            if (yy > annotate_above) & (yy < ylim):
                plt.plot(x, yy, 'o', c=c)
                plt.annotate("%.3g" % yy, (x, yy), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

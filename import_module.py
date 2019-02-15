packages = {
    "sys":None,
    "itertools":None,
    "os":None,
    "math":None,
    "numpy": "np",
    "pandas": "pd",
    "tensorflow": "tf",
    "shutil":None,
    "json":None,
    "elif5":None,
    "multiprocessing":None,
    "cufflinks": "cf",
    "plotly.graph_objs":None,
    "warnings":None,
}

for key in packages.keys():
    if packages[key] is None:
        import key
    else:
        import key as packages[key]


for algo in QgsApplication.processingRegistry().algorithms():
    print(algo.id(), "------", algo.displayName())

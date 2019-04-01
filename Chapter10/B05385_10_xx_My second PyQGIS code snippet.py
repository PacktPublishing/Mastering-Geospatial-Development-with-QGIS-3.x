for feature in layer.getFeatures():
    print("Feature with id %d has attributes and geometry:" %feature.id())
    print(feature.attributes())

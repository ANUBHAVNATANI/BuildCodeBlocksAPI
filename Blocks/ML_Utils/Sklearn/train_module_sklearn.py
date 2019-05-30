# Train Function
"""
Sklearn module training function
Docs--
model accept previous function input
"""


def train(X, y, model):
    model.fit(X, y)
    return model

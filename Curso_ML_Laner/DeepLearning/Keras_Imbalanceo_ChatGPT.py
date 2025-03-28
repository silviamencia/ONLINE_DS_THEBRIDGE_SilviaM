# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:08:40 2025

@author: borja
"""

from sklearn.utils.class_weight import compute_class_weight
import numpy as np

# Calcular pesos de clase
class_weights = compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),  # y_train debe ser tu vector de etiquetas
    y=y_train
)
class_weights = dict(enumerate(class_weights))

# Entrenar el modelo con pesos de clase
model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    batch_size=32,
    class_weight=class_weights
)
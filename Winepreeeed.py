
import tkinter as tk
import pickle
from tkinter import ttk
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score , cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import seaborn as sns

import pickle

# Charger le modèle à partir du fichier 'modele_sauvegarde.pkl'
with open('modele_sauvegarde.pkl', 'rb') as fichier:
    model = pickle.load(fichier)


resultats = {
    0: "White wine",
    1: "Red wine"
}

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LogisticRegression


# Fonction pour effectuer la prédiction
def predict_quality():
    # Récupérer les valeurs des caractéristiques saisies par l'utilisateur
    fixed_acidity = float(entry_fixed_acidity.get())
    volatile_acidity = float(entry_volatile_acidity.get())
    citric_acid = float(entry_citric_acid.get())
    residual_sugar = float(entry_residual_sugar.get())
    chlorides = float(entry_chlorides.get())
    free_sulfur_dioxide = float(entry_free_sulfur_dioxide.get())
    total_sulfur_dioxide = float(entry_total_sulfur_dioxide.get())
    density = float(entry_density.get())
    pH = float(entry_pH.get())
    sulphates = float(entry_sulphates.get())
    alcohol = float(entry_alcohol.get())
    wine_type = combobox_wine_type.current()  # Assurez-vous que le type de vin est correctement encodé
    
    # Créer un DataFrame avec les valeurs saisies
    data2 = pd.DataFrame({
        'fixed acidity': [fixed_acidity],
        'volatile acidity': [volatile_acidity],
        'citric acid': [citric_acid],
        'residual sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free sulfur dioxide': [free_sulfur_dioxide],
        'total sulfur dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol],
        'Type': [wine_type]
    })
    
    # Effectuer la prédiction avec le modèle chargé
    prediction = model.predict(data2)
    
    # Afficher la prédiction dans une boîte de dialogue
    messagebox.showinfo('Prédiction', f'Qualité prédite du vin : {prediction[0]}')

# Créer la fenêtre Tkinter
window = tk.Tk()
window.title('Prédiction de la qualité du vin')

# Créer les étiquettes et les champs de saisie pour les caractéristiques
label_fixed_acidity = tk.Label(window, text='Fixed Acidity:')
label_fixed_acidity.grid(row=0, column=0)
entry_fixed_acidity = tk.Entry(window)
entry_fixed_acidity.grid(row=0, column=1)

label_volatile_acidity = tk.Label(window, text='Volatile Acidity:')
label_volatile_acidity.grid(row=1, column=0)
entry_volatile_acidity = tk.Entry(window)
entry_volatile_acidity.grid(row=1, column=1)

label_citric_acid = tk.Label(window, text='Citric Acid:')
label_citric_acid.grid(row=2, column=0)
entry_citric_acid = tk.Entry(window)
entry_citric_acid.grid(row=2, column=1)

# Ajoutez ici les étiquettes et les champs de saisie pour les autres caractéristiques

label_residual_sugar = tk.Label(window, text='Residual Sugar:')
label_residual_sugar.grid(row=3, column=0)
entry_residual_sugar = tk.Entry(window)
entry_residual_sugar.grid(row=3, column=1)

label_chlorides = tk.Label(window, text='Chlorides:')
label_chlorides.grid(row=4, column=0)
entry_chlorides = tk.Entry(window)
entry_chlorides.grid(row=4, column=1)

label_free_sulfur_dioxide = tk.Label(window, text='Free Sulfur Dioxide:')
label_free_sulfur_dioxide.grid(row=5, column=0)
entry_free_sulfur_dioxide = tk.Entry(window)
entry_free_sulfur_dioxide.grid(row=5, column=1)

label_total_sulfur_dioxide = tk.Label(window, text='Total Sulfur Dioxide:')
label_total_sulfur_dioxide.grid(row=6, column=0)
entry_total_sulfur_dioxide = tk.Entry(window)
entry_total_sulfur_dioxide.grid(row=6, column=1)

label_density = tk.Label(window, text='Density:')
label_density.grid(row=7, column=0)
entry_density = tk.Entry(window)
entry_density.grid(row=7, column=1)

label_pH = tk.Label(window, text='pH:')
label_pH.grid(row=8, column=0)
entry_pH = tk.Entry(window)
entry_pH.grid(row=8, column=1)

label_sulphates = tk.Label(window, text='Sulphates:')
label_sulphates.grid(row=9, column=0)
entry_sulphates = tk.Entry(window)
entry_sulphates.grid(row=9, column=1)

label_alcohol = tk.Label(window, text='Alcohol:')
label_alcohol.grid(row=10, column=0)
entry_alcohol = tk.Entry(window)
entry_alcohol.grid(row=10, column=1)

label_wine_type = tk.Label(window, text='Type:')
label_wine_type.grid(row=11, column=0)

combobox_wine_type = ttk.Combobox(window, values=list(resultats.values()), state="readonly")
combobox_wine_type.grid(row=11, column=1)

combobox_wine_type.current(0)

# Créer le bouton "Prédire"
button_predict = tk.Button(window, text='Prédire', command=predict_quality)
button_predict.grid(row=12, columnspan=2)

# Lancer la boucle principale Tkinter
window.mainloop()


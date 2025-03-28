# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import cvxpy
from fancyimpute  import IterativeImputer 
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from keras.layers import Dense
import tensorflow as tf
from keras.models import Sequential
import random
from keras.layers import Dropout
from keras.regularizers import l2,l1
from sklearn.metrics import r2_score
import seaborn as sns
from keras.callbacks import EarlyStopping

os.chdir(r"C:\Users\LENOVO\Documents\DataVM\Cursos\CursoPythonCompleto\17-Modelos\HousePrices")
data = pd.read_csv("train.csv")

# Establecemos las semillas para la reproducibilidad
tf.random.set_seed(1)
np.random.seed(1)
random.seed(1)

################### 1. ENTENDER EL DATASET ############################

"""
# Añadimos un resumen de los datos
SSubClass: Identifies the type of dwelling involved in the sale.	

        20	1-STORY 1946 & NEWER ALL STYLES
        30	1-STORY 1945 & OLDER
        40	1-STORY W/FINISHED ATTIC ALL AGES
        45	1-1/2 STORY - UNFINISHED ALL AGES
        50	1-1/2 STORY FINISHED ALL AGES
        60	2-STORY 1946 & NEWER
        70	2-STORY 1945 & OLDER
        75	2-1/2 STORY ALL AGES
        80	SPLIT OR MULTI-LEVEL
        85	SPLIT FOYER
        90	DUPLEX - ALL STYLES AND AGES
       120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
       150	1-1/2 STORY PUD - ALL AGES
       160	2-STORY PUD - 1946 & NEWER
       180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
       190	2 FAMILY CONVERSION - ALL STYLES AND AGES

MSZoning: Identifies the general zoning classification of the sale.
		
       A	Agriculture
       C	Commercial
       FV	Floating Village Residential
       I	Industrial
       RH	Residential High Density
       RL	Residential Low Density
       RP	Residential Low Density Park 
       RM	Residential Medium Density
	
LotFrontage: Linear feet of street connected to property

LotArea: Lot size in square feet

Street: Type of road access to property

       Grvl	Gravel	
       Pave	Paved
       	
Alley: Type of alley access to property

       Grvl	Gravel
       Pave	Paved
       NA 	No alley access
		
LotShape: General shape of property

       Reg	Regular	
       IR1	Slightly irregular
       IR2	Moderately Irregular
       IR3	Irregular
       
LandContour: Flatness of the property

       Lvl	Near Flat/Level	
       Bnk	Banked - Quick and significant rise from street grade to building
       HLS	Hillside - Significant slope from side to side
       Low	Depression
		
Utilities: Type of utilities available
		
       AllPub	All public Utilities (E,G,W,& S)	
       NoSewr	Electricity, Gas, and Water (Septic Tank)
       NoSeWa	Electricity and Gas Only
       ELO	Electricity only	
	
LotConfig: Lot configuration

       Inside	Inside lot
       Corner	Corner lot
       CulDSac	Cul-de-sac
       FR2	Frontage on 2 sides of property
       FR3	Frontage on 3 sides of property
	
LandSlope: Slope of property
		
       Gtl	Gentle slope
       Mod	Moderate Slope	
       Sev	Severe Slope
	
Neighborhood: Physical locations within Ames city limits

       Blmngtn	Bloomington Heights
       Blueste	Bluestem
       BrDale	Briardale
       BrkSide	Brookside
       ClearCr	Clear Creek
       CollgCr	College Creek
       Crawfor	Crawford
       Edwards	Edwards
       Gilbert	Gilbert
       IDOTRR	Iowa DOT and Rail Road
       MeadowV	Meadow Village
       Mitchel	Mitchell
       Names	North Ames
       NoRidge	Northridge
       NPkVill	Northpark Villa
       NridgHt	Northridge Heights
       NWAmes	Northwest Ames
       OldTown	Old Town
       SWISU	South & West of Iowa State University
       Sawyer	Sawyer
       SawyerW	Sawyer West
       Somerst	Somerset
       StoneBr	Stone Brook
       Timber	Timberland
       Veenker	Veenker
			
Condition1: Proximity to various conditions
	
       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street	
       Norm	Normal	
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad
	
Condition2: Proximity to various conditions (if more than one is present)
		
       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street	
       Norm	Normal	
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad
	
BldgType: Type of dwelling
		
       1Fam	Single-family Detached	
       2FmCon	Two-family Conversion; originally built as one-family dwelling
       Duplx	Duplex
       TwnhsE	Townhouse End Unit
       TwnhsI	Townhouse Inside Unit
	
HouseStyle: Style of dwelling
	
       1Story	One story
       1.5Fin	One and one-half story: 2nd level finished
       1.5Unf	One and one-half story: 2nd level unfinished
       2Story	Two story
       2.5Fin	Two and one-half story: 2nd level finished
       2.5Unf	Two and one-half story: 2nd level unfinished
       SFoyer	Split Foyer
       SLvl	Split Level
	
OverallQual: Rates the overall material and finish of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor
       1	Very Poor
	
OverallCond: Rates the overall condition of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average	
       5	Average
       4	Below Average	
       3	Fair
       2	Poor
       1	Very Poor
		
YearBuilt: Original construction date

YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)

RoofStyle: Type of roof

       Flat	Flat
       Gable	Gable
       Gambrel	Gabrel (Barn)
       Hip	Hip
       Mansard	Mansard
       Shed	Shed
		
RoofMatl: Roof material

       ClyTile	Clay or Tile
       CompShg	Standard (Composite) Shingle
       Membran	Membrane
       Metal	Metal
       Roll	Roll
       Tar&Grv	Gravel & Tar
       WdShake	Wood Shakes
       WdShngl	Wood Shingles
		
Exterior1st: Exterior covering on house

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast	
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles
	
Exterior2nd: Exterior covering on house (if more than one material)

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles
	
MasVnrType: Masonry veneer type

       BrkCmn	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       None	None
       Stone	Stone
	
MasVnrArea: Masonry veneer area in square feet

ExterQual: Evaluates the quality of the material on the exterior 
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
ExterCond: Evaluates the present condition of the material on the exterior
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
Foundation: Type of foundation
		
       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete	
       Slab	Slab
       Stone	Stone
       Wood	Wood
		
BsmtQual: Evaluates the height of the basement

       Ex	Excellent (100+ inches)	
       Gd	Good (90-99 inches)
       TA	Typical (80-89 inches)
       Fa	Fair (70-79 inches)
       Po	Poor (<70 inches
       NA	No Basement
		
BsmtCond: Evaluates the general condition of the basement

       Ex	Excellent
       Gd	Good
       TA	Typical - slight dampness allowed
       Fa	Fair - dampness or some cracking or settling
       Po	Poor - Severe cracking, settling, or wetness
       NA	No Basement
	
BsmtExposure: Refers to walkout or garden level walls

       Gd	Good Exposure
       Av	Average Exposure (split levels or foyers typically score average or above)	
       Mn	Mimimum Exposure
       No	No Exposure
       NA	No Basement
	
BsmtFinType1: Rating of basement finished area

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters	
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement
		
BsmtFinSF1: Type 1 finished square feet

BsmtFinType2: Rating of basement finished area (if multiple types)

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters	
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement

BsmtFinSF2: Type 2 finished square feet

BsmtUnfSF: Unfinished square feet of basement area

TotalBsmtSF: Total square feet of basement area

Heating: Type of heating
		
       Floor	Floor Furnace
       GasA	Gas forced warm air furnace
       GasW	Gas hot water or steam heat
       Grav	Gravity furnace	
       OthW	Hot water or steam heat other than gas
       Wall	Wall furnace
		
HeatingQC: Heating quality and condition

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor
		
CentralAir: Central air conditioning

       N	No
       Y	Yes
		
Electrical: Electrical system

       SBrkr	Standard Circuit Breakers & Romex
       FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)	
       FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
       FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
       Mix	Mixed
		
1stFlrSF: First Floor square feet
 
2ndFlrSF: Second floor square feet

LowQualFinSF: Low quality finished square feet (all floors)

GrLivArea: Above grade (ground) living area square feet

BsmtFullBath: Basement full bathrooms

BsmtHalfBath: Basement half bathrooms

FullBath: Full bathrooms above grade

HalfBath: Half baths above grade

Bedroom: Bedrooms above grade (does NOT include basement bedrooms)

Kitchen: Kitchens above grade

KitchenQual: Kitchen quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       	
TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)

Functional: Home functionality (Assume typical unless deductions are warranted)

       Typ	Typical Functionality
       Min1	Minor Deductions 1
       Min2	Minor Deductions 2
       Mod	Moderate Deductions
       Maj1	Major Deductions 1
       Maj2	Major Deductions 2
       Sev	Severely Damaged
       Sal	Salvage only
		
Fireplaces: Number of fireplaces

FireplaceQu: Fireplace quality

       Ex	Excellent - Exceptional Masonry Fireplace
       Gd	Good - Masonry Fireplace in main level
       TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
       Fa	Fair - Prefabricated Fireplace in basement
       Po	Poor - Ben Franklin Stove
       NA	No Fireplace
		
GarageType: Garage location
		
       2Types	More than one type of garage
       Attchd	Attached to home
       Basment	Basement Garage
       BuiltIn	Built-In (Garage part of house - typically has room above garage)
       CarPort	Car Port
       Detchd	Detached from home
       NA	No Garage
		
GarageYrBlt: Year garage was built
		
GarageFinish: Interior finish of the garage

       Fin	Finished
       RFn	Rough Finished	
       Unf	Unfinished
       NA	No Garage
		
GarageCars: Size of garage in car capacity

GarageArea: Size of garage in square feet

GarageQual: Garage quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage
		
GarageCond: Garage condition

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage
		
PavedDrive: Paved driveway

       Y	Paved 
       P	Partial Pavement
       N	Dirt/Gravel
		
WoodDeckSF: Wood deck area in square feet

OpenPorchSF: Open porch area in square feet

EnclosedPorch: Enclosed porch area in square feet

3SsnPorch: Three season porch area in square feet

ScreenPorch: Screen porch area in square feet

PoolArea: Pool area in square feet

PoolQC: Pool quality
		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       NA	No Pool
		
Fence: Fence quality
		
       GdPrv	Good Privacy
       MnPrv	Minimum Privacy
       GdWo	Good Wood
       MnWw	Minimum Wood/Wire
       NA	No Fence
	
MiscFeature: Miscellaneous feature not covered in other categories
		
       Elev	Elevator
       Gar2	2nd Garage (if not described in garage section)
       Othr	Other
       Shed	Shed (over 100 SF)
       TenC	Tennis Court
       NA	None
		
MiscVal: $Value of miscellaneous feature

MoSold: Month Sold (MM)

YrSold: Year Sold (YYYY)

SaleType: Type of sale
		
       WD 	Warranty Deed - Conventional
       CWD	Warranty Deed - Cash
       VWD	Warranty Deed - VA Loan
       New	Home just constructed and sold
       COD	Court Officer Deed/Estate
       Con	Contract 15% Down payment regular terms
       ConLw	Contract Low Down payment and low interest
       ConLI	Contract Low Interest
       ConLD	Contract Low Down
       Oth	Other
		
SaleCondition: Condition of sale

       Normal	Normal Sale
       Abnorml	Abnormal Sale -  trade, foreclosure, short sale
       AdjLand	Adjoining Land Purchase
       Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit	
       Family	Sale between family members
       Partial	Home was not completed when last assessed (associated with New Homes)


"""


'''
el dataset tiene datos sobre diferentes características de casas (como el tamaño,
el tipo de material, la ubicación, si tiene garaje/piscina...) y el objetivo es 
predecir el precio de cada casa. Por lo tanto, se trata de un MODELO de REGRESIÓN.
'''

# Visión general de las características
AnalisisNumericas=data.describe() 


######################### 2. PREPROCESAMIENTO DE LOS DATOS #########################


### VALORES FALTANTES

# Observamos que hay variables con valores faltantes que indican cierta información.
# Lo primero es cambiar los NAs por la categoria que indican de acuerdo a los datos.
data.columns
data["Alley"]=data["Alley"].fillna("NO ALLEY ACCESS")
data["BsmtCond"]=data["BsmtCond"].fillna("NO BASEMENT")
data["BsmtExposure"]=data["BsmtExposure"].fillna("NO BASEMENT")
data["BsmtFinType1"]=data["BsmtFinType1"].fillna("NO BASEMENT")
data["BsmtFinType2"]=data["BsmtFinType2"].fillna("NO BASEMENT")
data["BsmtQual"]=data["BsmtQual"].fillna("NO BASEMENT")
data["FireplaceQu"]=data["FireplaceQu"].fillna("NO FIRE PLACE")
data["GarageType"]=data["GarageType"].fillna("NO GARAGE")
data["GarageQual"]=data["GarageQual"].fillna("NO GARAGE")
data["GarageCond"]=data["GarageCond"].fillna("NO GARAGE")
data["GarageFinish"]=data["GarageFinish"].fillna("NO GARAGE")
data["PoolQC"]=data["PoolQC"].fillna("NO POOL")
data["Fence"]=data["Fence"].fillna("NO FENCE")
data["MiscFeature"]=data["MiscFeature"].fillna("NONE")

# Una vez hecho esto pasamos a analizar los NAs como tal
data.isnull().any().any()

# Vemos que existen valores perdidos
# Realizamos un sumatorio para observar los NAs por columna.
Perdidos = data.isnull().sum()

'''
Los valores perdidos se concentran en:
LotFrontage(259), GarageYrBlt (81),MasVnrType (872), MasVnrArea (8) y Electrical (1)

Teniendo en cuenta que contamos con 81 variables, y la variable "MasVnrType" tiene 
aproximadamente el 60% de registros con valores faltantes, decidimos eliminarla.

Como unicamente hay un registro con la variable Electrical con NA la eliminamos.
También podríamos imputarla con la moda (ya que es categórica).
'''

del(data["MasVnrType"])
data = data.dropna(subset=['Electrical'])
del(data["Id"])

# Visualizamos los datos de No Garage
NoGarage = data[data["GarageType"]== "NO GARAGE"]
min(data["GarageYrBlt"])

'''
Vemos que los que NO tienen Garage coinciden con los que no tienen año.
En nuestro conjunto de datos el año mínimo es 1900. Luego decidimos convertir los
NAs referidos a los garages en 1800, ya que es un valor diferente pero no muy lejano
y puede servir al modelo.
'''

data["GarageYrBlt"]=data["GarageYrBlt"].fillna(1800)


'''
Al resto de los datos asumo que los valores perdidos son reales por lo que 
procedo a imputarlos con el Iterative Imputer. Este método modela los datos 
faltantes basándose en los valores de otras características, lo que resulta en 
una imputación más precisa que usar una técnica más simple como la media o la moda.
'''

# Identificamos las variables numéricas.
datoNum1 = data.loc[:, data.dtypes == np.float64]
datoNum2 = data.loc[:, data.dtypes == np.int64]

datoNum = pd.concat([datoNum1, datoNum2], axis=1)

# Identificamos las variables categóricas.
datoNoNum = data.loc[:, data.dtypes == object]

# Imputamos los valores perdidos de las variables numéricas
my_imputer = IterativeImputer(random_state=1)
datoNumcomp = my_imputer.fit_transform(datoNum)

datoNumcomp = pd.DataFrame(datoNumcomp)
datoNumcomp.columns = datoNum.columns

datoNoNum.reset_index(drop=True, inplace=True)
datoNumcomp.reset_index(drop=True, inplace=True)

datos_completos= pd.concat([datoNoNum, datoNumcomp], axis=1)



### CREAR NUEVAS VARIABLES:
    
# Procedemos a enriquecer los datos añadiendo nuevas variables.
datos_completos.columns

# Creamos una nueva columna llamada 'Crisis' para indicar si la venta ocurrió 
#durante o después de la crisis financiera de 2008.
datos_completos["Crisis"] = "NO"
datos_completos["Crisis"][datos_completos["YrSold"]>2007] = "SI"

# Creamos una nueva columna llamada 'TiempoPasado', que calcula el tiempo 
# transcurrido desde la última remodelación hasta el año de venta de la vivienda.
datos_completos["TiempoPasado"] = datos_completos["YrSold"] - datos_completos["YearRemodAdd"]




### TRANSFORMACIÓN DE LOS DATOS:
    
# Procedemos a binominalizar las variables categoricas.
datos_completos = pd.get_dummies(datos_completos, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=True, dtype=None)





################################## 3. ENTRENAR LOS MODELOS #####################################

############# DIVISIÓN DE DATOS:
    
# Seleccionamos la variable objetivo y las explicativas
y = datos_completos['SalePrice']
X = datos_completos.drop(['SalePrice'], axis = 1)

# Realizamos la particion dejando un 75% para entrenar y un 25% de test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

X_train.dtypes


########### PROBAMOS NORMALIZANDO LAS VARIABLES

'''
En las RNA, es importante normalizar las variables, ya que características con
escalas muy diferentes pueden causar oscilaciones en el gradiente, dificultando 
la convergencia del modelo.
'''

X_num1 = X_train.loc[:, X_train.dtypes == np.float64]
X_num2 = X_train.loc[:, X_train.dtypes == np.int64]
X_num = pd.concat([X_num1, X_num2], axis=1)

X_Nonum=X_train.loc[:, X_train.dtypes == bool]

# Estandarizamos las variables numericas
scaler = StandardScaler()
scaler.fit(X_num)
X_num_estandarizado = scaler.transform(X_num)

X_num_estandarizado = pd.DataFrame(X_num_estandarizado)
X_num_estandarizado.columns = X_num.columns

X_num_estandarizado.reset_index(drop=True, inplace=True)
X_Nonum.reset_index(drop=True, inplace=True)

X_estandarizado = pd.concat([X_num_estandarizado, X_Nonum], axis=1)



############ DEFINIMOS NUESTRO MODELO:
    
model = Sequential()

model.add(Dense(128, input_dim=258, activation='relu',kernel_regularizer=l2(0.001)))
model.add(Dropout(0.6)) 
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu',kernel_regularizer=l2(0.001)))
model.add(Dropout(0.3))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0009),
              loss='mse',
              metrics=['mae'])




# Definir el Early Stopping
early_stopping = EarlyStopping(
    monitor='val_loss',  # Monitorea la pérdida en el conjunto de validación
    patience=30,         # Espera 30 épocas sin mejora antes de detenerse
    restore_best_weights=True  # Restaura los pesos de la mejor época
)

history = model.fit(X_estandarizado, y_train, validation_split=0.2, epochs=150, 
                    batch_size=30, callbacks=[early_stopping])


'''
Hemos tomado el 20% del data de train como VALIDACIÓN. Este conjunto es 
importante porque te ayuda a ajustar y optimizar el modelo mientras lo entrenas, 
sin que el modelo se sobreajuste a los datos de entrenamiento. 


Los CALLBACKS son funciones que se ejecutan durante el entrenamiento ayudando a
optimizar el proceso de entrenamiento de manera eficiente.


EARLY STOPPING es una técnica que se usa para detener el entrenamiento cuando 
el modelo deja de mejorar en un conjunto de validación.
Ayudar a detener el entrenamiento automáticamente cuando el modelo deja de 
mejorar, evita el sobreentrenamiento y reduce el tiempo de entrenamiento 
innecesario.
'''

_, mae = model.evaluate(X_estandarizado, y_train)
print(f"Mean Absolute Error en train: {mae}")


# Gráfico de pérdida (loss) en función de las épocas
plt.plot(history.history['loss'], label='Loss en entrenamiento')
plt.plot(history.history['val_loss'], label='Loss en validación')
plt.xlabel('Épocas')
plt.ylabel('Loss')
plt.legend()
plt.title('Progreso del entrenamiento')
plt.show()

'''
Observamos como muestra una tendencia decreciente tanto en los datos de 
entrenamiento como en validación, ya que eso indica que el modelo está mejorando 
con el tiempo y aprendiendo de manera efectiva.

Si observásemos saltos o picos en este gráfico, indicaría que el modelo no está
convergiendo bien. (overfitting, tasa de aprendizaje demasiado alta...)
'''


########### Realizamos las predicciones

X_num1 = X_test.loc[:, X_test.dtypes == np.float64]
X_num2 = X_test.loc[:, X_test.dtypes == np.int64]
X_num = pd.concat([X_num1, X_num2], axis=1)

X_Nonum = X_test.loc[:, X_test.dtypes == bool]


# Estandarizamos las variables numericas

X_num_estandarizado = scaler.transform(X_num)

X_num_estandarizado = pd.DataFrame(X_num_estandarizado)
X_num_estandarizado.columns = X_num.columns

X_num_estandarizado.reset_index(drop=True, inplace=True)
X_Nonum.reset_index(drop=True, inplace=True)

X_estandarizado_test = pd.concat([X_num_estandarizado, X_Nonum], axis=1)



# Evaluamos el modelo en el conjunto de prueba
loss, mae = model.evaluate(X_estandarizado_test, y_test, verbose=0)
mae

# Cálculo del R2 score
y_pred_test = model.predict(X_estandarizado_test).flatten()  
r2 = r2_score(y_test, y_pred_test)  
r2 

# Cálculo del error relativo promedio
mape = np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100
mape

print(f"Mean Absolute Error en test: {mae:.2f}")
print(f"R2 score en test: {r2:.2f}")
print(f"MAPE en test: {mape:.2f}%")



########## Exploramos la DISTRIBUCIÓN de la variable objetivo, precio vivienda:

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 3))
sns.histplot(data, x='SalePrice', kde=True,ax=ax)
sns.set_style("white")
ax.set_title("Distribución Precio")
ax.set_xlabel('precio');

print(f"Rango de SalePrice: {y.min()} - {y.max()}")
print(f"Media de SalePrice: {y.mean()}")
print(f"Desviación estándar de SalePrice: {y.std()}")

'''
Los precios de las casas varían entre 34.900 y 755.000, lo que indica una gran 
dispersión.
La media es 180.921,20, lo que sugiere que la mayoría de los precios se concentran
en este rango o cerca de él.
La desviación estándar de 79.442.50 indica que hay una variabilidad significativa 
en los precios.
'''



######################### CONCLUSIÓN:
    
'''
El modelo, en promedio, se equivoca por unos 19.874 dólares (MAE), lo cual no 
está nada mal si consideramos que el precio promedio de las casas es de 180.930 
dólares. Con un R² de 0.8, logra explicar un 80% de la variabilidad en los 
precios, demostrando que capta la mayoría de los patrones importantes en los 
datos. Por otro lado, el error relativo promedio (MAPE) es del 11.48%, lo que 
significa que, en general, las predicciones están dentro de un rango del 11% 
del precio real.
'''

plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Línea perfecta
plt.xlabel("Valores reales (y_test)")
plt.ylabel("Predicciones (y_pred_test)")
plt.title("Predicciones vs Valores reales")
plt.show()




################################ Entrenamiento definivo
'''
Una vez que encontramos el mejor modelo, lo entrenamos de nuevo con todos los 
datos disponibles. Así aprovechamos al máximo la información para que el modelo 
esté lo mejor preparado antes de usarlo en producción.
'''

X_num1 = X.loc[:, X.dtypes == np.float64]
X_num2 = X.loc[:, X.dtypes == np.int64]
X_num = pd.concat([X_num1, X_num2], axis=1)

X_Nonum=X.loc[:, X.dtypes == bool]

# Estandarizamos las variables numericas
scaler = StandardScaler()
X_num_estandarizado = scaler.fit_transform(X_num)

X_num_estandarizado = pd.DataFrame(X_num_estandarizado)
X_num_estandarizado.columns = X_num.columns

X_num_estandarizado.reset_index(drop=True, inplace=True)
X_Nonum.reset_index(drop=True, inplace=True)

X_estand = pd.concat([X_num_estandarizado, X_Nonum], axis=1)



model.fit(X_estand, y, epochs=150, batch_size=30)

# Evaluamos el modelo 
loss, mae = model.evaluate(X_estand, y, verbose=0)
mae

# Cálculo del R2 score
y_predic = model.predict(X_estand).flatten()  
r2 = r2_score(y, y_predic)  
r2 

# Cálculo del error relativo promedio
mape = np.mean(np.abs((y - y_predic) / y)) * 100
mape

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 score: {r2:.2f}")
print(f"MAPE: {mape:.2f}%")


